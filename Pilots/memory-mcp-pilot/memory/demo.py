"""Show the exact synthetic rule for two independently scoped fixtures."""

from datetime import datetime
import json
from pathlib import Path

from rule_memory import FIXTURE_SHA256, PROJECT, ReaderGrant, RuleMemory


def main():
    root = Path(__file__).resolve().parent / "snapshot"
    fixture_time = datetime.fromisoformat("2026-11-20T12:00:00+08:00")
    cases = (
        ("tenant-a", "INVOICE.POD_REQUIRED"),
        ("tenant-b", "INVOICE.POD_REQUIRED"),
        ("tenant-a", "PLATFORM.TENANT_ISOLATION"),
        ("tenant-b", "PLATFORM.TENANT_ISOLATION"),
    )
    results = []
    for tenant, rule_id in cases:
        grant = ReaderGrant(PROJECT, tenant, "business-analyst")
        reader = RuleMemory(root, grant, expected_digest=FIXTURE_SHA256, clock=lambda: fixture_time)
        results.append(reader.lookup(rule_id))

    print(json.dumps(results, indent=2))
    return 0 if all(row["status"] == "RESOLVED" for row in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
