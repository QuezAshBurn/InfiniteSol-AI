# DEL-001: Exclude archived pending orders from the count

**Status:** DRAFT FOR APPROVAL. Not approved, not dispatched, not for implementation.
**Revision:** r1 (2026-11-20)
**Role:** Business Analyst
**Decision owner:** PM, who owns approval of this revision and any implementation authorization.

## Provenance

| Item | Value |
|---|---|
| Skill | story-specification v0.1.0 |
| Manifest SHA-256 | `952dfd1147fd5152539b6e8589c99a0fa5329b490cdb9e09b76b1abaeaad76b9` (operator-verified this run; not re-run) |
| Source-pack fingerprint | **Not recorded.** No tools were permitted, so the reference files (APPROVED-WORK, 02-business-analyst, GOAL-AND-QUALITY) were not read. |
| Authority | Analysis approval covers specification only, for DEL-001 in a synthetic local project. |
| Source evidence | DEL-001 request text from the pilot product owner, supplied in this run. |
| Code inspected | None. Current behaviour is stated from the request only and has not been observed in code. |

## User and outcome

The pilot product owner needs a count of pending orders that excludes archived pending orders. Legacy records with no archive flag must still be counted.

## Behaviour

- **Observed (per request, unverified):** an existing Python helper in `src/orders.py` counts pending orders. Whether it currently considers archiving is unknown.
- **Desired:** count only orders that are pending and not archived.
- **Undecided:** how to treat archive flag values that are not booleans (see N-1).

## Business rules

| ID | Rule | Source |
|---|---|---|
| R-1 | An order is pending only when its status is exactly `pending`. The match is case-sensitive, with no trimming. | DEL-001 |
| R-2 | A pending order with archive flag `True` is excluded from the count. | DEL-001 |
| R-3 | A pending order with no archive flag (legacy record) is counted as active. | DEL-001 |
| R-4 | A pending order with archive flag `False` is counted. | DEL-001 (implied) |
| R-5 | Orders with any other status are never counted, whatever their archive flag. | DEL-001 |
| R-6 | An empty input returns `0` without error. | DEL-001 |
| R-7 | Counting must not mutate, reorder or remove the input order data. | DEL-001 |

**Precedence:** R-1 and R-5 are applied first (status), then R-2, R-3 and R-4 (archive state).

## Scope

- **Allowed:** `src/orders.py` (the existing counting helper) and `tests/test_orders.py`.
- **Excluded:**
  - other files
  - new dependencies
  - new spend (budget AUD 0)
  - schema or data migration
  - changes to status semantics
  - archiving or unarchiving behaviour
  - UI and reporting
- **Preserve:**
  - the helper's existing signature and return type
  - counting behaviour for non-archived pending orders
  - treatment of non-pending statuses

## Acceptance criteria

| ID | Setup | Action | Observable outcome | Evidence |
|---|---|---|---|---|
| AC-1 | 2 pending orders, neither has an archive flag | Count | `2` | Test name and pass result |
| AC-2 | 1 pending with `archived=True`, 1 pending with `archived=False` | Count | `1` | Test pass |
| AC-3 | 1 pending legacy record (no archive key), 1 pending with `archived=True` | Count | `1` | Test pass |
| AC-4 | Statuses `Pending`, `PENDING`, ` pending`, `pending ` | Count | `0` | Test pass |
| AC-5 | Statuses `shipped`, `cancelled`, `""`, each both archived and not archived | Count | `0` | Test pass |
| AC-6 | Empty input (`[]`) | Count | `0`, no exception | Test pass |
| AC-7 | Mixed input from AC-2 and AC-3; keep a deep copy before counting | Count | Input equals the copy afterwards (same length, order and field values) | Test pass |
| AC-8 | All pending orders archived | Count | `0` | Test pass |
| AC-9 (regression) | Pre-existing tests in `tests/test_orders.py` | Run the suite | All existing tests pass, unmodified unless they conflict with R-2 (any such conflict is reported) | Full test output |

## Open items (nonblocking)

- **N-1:** Handling of non-boolean archive values such as `"yes"`, `1` or `None`.
  - Proposed default: only `True` excludes; anything else counts as not archived.
  - Alternative: treat any truthy value as archived.
  - The PM should confirm. N-1 is outside the AC baseline until decided.
- **N-2:** The archive field name is assumed to be `archived`. Confirm it against the code before implementation.
- **N-3:** The source-pack fingerprint should be recorded once the references have been read.

## Developer handoff (only after the PM approves r1 and authorizes implementation)

- Change only the counting helper in `src/orders.py` to apply R-1 to R-7.
  - Read the archive flag defensively, so a missing key means active.
  - Do not mutate the input.
- Add tests for AC-1 to AC-8 in `tests/test_orders.py`.
- No new dependencies, and no other files.
- Report:
  - the diff
  - full test output
  - any conflict found with existing tests or with N-2

## QA handoff (only after implementation is authorized and delivered)

- Verify AC-1 to AC-9 against the delivered revision, and record the pass or fail result for each with its test output.
- Confirm the diff touches only the two in-scope files and adds no dependencies.
- Confirm that the input-immutability test (AC-7) exists and passes.
- Report any behaviour that depends on N-1 separately, not as a pass or fail.

## Boundaries

- This is a drafting output only. No tools were run, no files were edited, and nothing was approved or dispatched.
- The story stays in DRAFT until the PM approves revision r1 exactly. Implementation requires separate PM authorization.
