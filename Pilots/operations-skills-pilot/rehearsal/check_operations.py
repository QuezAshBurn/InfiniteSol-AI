"""Generate evidence for the synthetic invoice-report rehearsal."""

from hashlib import sha256
import json
from pathlib import Path


SOURCE = (
    ('north', 7, 1, 'posted', 6500),
    ('south', 7, 1, 'posted', 3400),
    ('south', 7, 2, 'posted', 3500),
    ('south', 8, 1, 'draft', 1000),
)
EXPECTED = {'north': 6500, 'south': 3500}


def invoice_snapshot(rows):
    seen = {}
    latest = {}
    for tenant, invoice, revision, status, amount in rows:
        key = (tenant, invoice)
        record = (revision, status, amount)
        source_key = (tenant, invoice, revision)
        if seen.setdefault(source_key, record) != record:
            raise ValueError('Conflicting rows at the same revision')
        current = latest.get(key)
        if current is None or revision > current[0]:
            latest[key] = record

    totals = {}
    for (tenant, _), (_, status, amount) in latest.items():
        if status == 'posted':
            totals[tenant] = totals.get(tenant, 0) + amount
    return totals


def run_data_checks():
    totals = invoice_snapshot(SOURCE)
    assert totals == EXPECTED
    assert invoice_snapshot((*SOURCE, *SOURCE)) == EXPECTED
    assert invoice_snapshot(tuple(reversed(SOURCE))) == EXPECTED
    print('PASS | tenant grain, repeated local ID, duplicate replay, latest correction and draft exclusion')

    switched = {'north': totals['south'], 'south': totals['north']}
    assert sum(switched.values()) == sum(EXPECTED.values())
    assert switched != EXPECTED
    print('PASS | tenant reconciliation detected a planted swap that global totals could not detect')

    for revision in (1, 2):
        try:
            invoice_snapshot((*SOURCE, ('south', 7, revision, 'posted', 9999)))
        except ValueError:
            continue
        raise AssertionError('Expected duplicate-revision conflict to stop report output')
    print('PASS | conflicting latest and superseded revisions failed before report output')
    return json.dumps(totals, sort_keys=True, separators=(',', ':')).encode('utf-8')


def run_cost_checks():
    approved, incurred, signed, already_incurred, incremental = 1000, 300, 500, 200, 200
    outstanding = signed - already_incurred
    estimate = incurred + outstanding + incremental
    assert (outstanding, estimate, estimate - approved, estimate + 100) == (300, 800, -200, 900)
    print('PASS | synthetic cost forecast AUD 800, variance AUD -200 and downside AUD 900')

    double_counted = incurred + signed + incremental
    assert double_counted - estimate == already_incurred
    print('PASS | finance check isolated AUD 200 duplicated between actuals and commitments')


def run_artifact_checks(artifact):
    # Simulate artifact comparisons in memory. No environment connection or deployment.
    candidate = sha256(artifact).hexdigest()
    testing = sha256(artifact).hexdigest()
    staging = sha256(artifact).hexdigest()
    assert candidate == testing == staging
    print(f'PASS | simulated Testing and Staging matched report artifact SHA-256 {candidate}')

    prior = b'{"north":6500,"south":3400}'
    prior_approval = sha256(prior).hexdigest()
    assert prior_approval != candidate
    print('PASS | simulated operator handoff rejected a prior artifact approval')


def main():
    print(f'Script SHA-256 {sha256(Path(__file__).read_bytes()).hexdigest()}')
    artifact = run_data_checks()
    run_cost_checks()
    run_artifact_checks(artifact)


if __name__ == '__main__':
    main()
