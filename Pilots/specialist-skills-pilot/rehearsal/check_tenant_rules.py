"""Exercise the synthetic R1 rule contract in an isolated in-memory database."""

from contextlib import closing
from hashlib import sha256
from pathlib import Path
import sqlite3


DEFAULT_RULE = 'manual'
FIXTURE = (('tenant-a', 7, 'priority'), ('tenant-b', 7, 'standard'))


class SimulatedInterruption(Exception):
    """Inject a local failure before the copy transaction completes."""


def baseline(db):
    db.execute('PRAGMA foreign_keys = ON')
    db.executescript(
        """
        CREATE TABLE tenants (id TEXT PRIMARY KEY);
        CREATE TABLE legacy_rules (
            tenant_id TEXT NOT NULL REFERENCES tenants(id),
            local_id INTEGER NOT NULL,
            rule TEXT NOT NULL,
            PRIMARY KEY (tenant_id, local_id)
        );
        """
    )
    with db:
        db.executemany('INSERT INTO tenants VALUES (?)',
                       [('tenant-a',), ('tenant-b',), ('tenant-c',)])
        db.executemany('INSERT INTO legacy_rules VALUES (?, ?, ?)', FIXTURE)


def migrate(db, *, interrupt=False):
    source = db.execute('SELECT * FROM legacy_rules ORDER BY tenant_id, local_id').fetchall()
    with db:
        db.execute('BEGIN')
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS dispatch_rules (
                tenant_id TEXT NOT NULL REFERENCES tenants(id),
                local_id INTEGER NOT NULL,
                rule TEXT NOT NULL,
                PRIMARY KEY (tenant_id, local_id)
            )
            """
        )
        for row in source:
            db.execute(
                'INSERT INTO dispatch_rules VALUES (?, ?, ?) '
                'ON CONFLICT (tenant_id, local_id) DO NOTHING',
                row,
            )
            if interrupt:
                raise SimulatedInterruption()
        migrated = db.execute(
            'SELECT * FROM dispatch_rules ORDER BY tenant_id, local_id'
        ).fetchall()
        if migrated != source:
            raise ValueError('Per-tenant reconciliation failed')


def read_rule(db, authorized_tenant, requested_tenant, local_id):
    if not authorized_tenant or authorized_tenant != requested_tenant:
        raise PermissionError('Tenant context must match')
    row = db.execute(
        'SELECT rule FROM dispatch_rules WHERE tenant_id = ? AND local_id = ?',
        (authorized_tenant, local_id),
    ).fetchone()
    return row[0] if row else DEFAULT_RULE


def verify_rules(db):
    assert read_rule(db, 'tenant-a', 'tenant-a', 7) == 'priority'
    assert read_rule(db, 'tenant-b', 'tenant-b', 7) == 'standard'
    assert read_rule(db, 'tenant-c', 'tenant-c', 7) == DEFAULT_RULE


def verify_authorization(db):
    queries = []
    db.set_trace_callback(queries.append)
    try:
        for auth, requested in [(None, 'tenant-a'), ('tenant-a', 'tenant-b')]:
            try:
                read_rule(db, auth, requested, 7)
            except PermissionError:
                continue
            raise AssertionError('Expected tenant authorization to be denied')
        assert queries == []
    finally:
        db.set_trace_callback(None)


def main():
    with closing(sqlite3.connect(':memory:')) as db, closing(sqlite3.connect(':memory:')) as restored:
        baseline(db)
        assert db.execute('PRAGMA foreign_keys').fetchone() == (1,)
        print(f'SQLite {sqlite3.sqlite_version} | foreign_keys=ON | candidate SHA-256 '
              f'{sha256(Path(__file__).read_bytes()).hexdigest()}')
        try:
            migrate(db, interrupt=True)
        except SimulatedInterruption:
            assert db.execute(
                "SELECT count(*) FROM sqlite_master WHERE name = 'dispatch_rules'"
            ).fetchone() == (0,)
            assert db.execute('SELECT * FROM legacy_rules ORDER BY tenant_id').fetchall() == list(FIXTURE)
        else:
            raise AssertionError('Expected the simulated interruption')
        print('PASS | partial copy rolled back, legacy rows preserved')

        migrate(db)
        migrate(db)
        verify_rules(db)
        assert db.execute('PRAGMA foreign_key_check').fetchall() == []
        print('PASS | retry and repeat preserved exact rows by tenant and both local ID 7 values')
        print('PASS | existing overrides and authorized shared fallback')

        verify_authorization(db)
        print('PASS | absent or mismatched authorized context denied before database access')

        db.backup(restored)
        restored.execute('PRAGMA foreign_keys = ON')
        restored_source = restored.execute(
            'SELECT * FROM legacy_rules ORDER BY tenant_id, local_id'
        ).fetchall()
        restored_rules = restored.execute(
            'SELECT * FROM dispatch_rules ORDER BY tenant_id, local_id'
        ).fetchall()
        assert restored_source == restored_rules == list(FIXTURE)
        verify_rules(restored)
        verify_authorization(restored)
        assert restored.execute('PRAGMA foreign_key_check').fetchall() == []
        print('PASS | isolated snapshot restore preserved exact legacy and migrated rows, lookups and tenant controls')


if __name__ == '__main__':
    main()
