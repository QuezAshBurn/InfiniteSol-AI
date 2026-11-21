# Verdict: PASS FOR LOCAL PILOT

The scope is accurately limited to the synthetic fixture. Every behavioral claim the ADR makes about the local script maps to a PASS line in the run log. You report independent recomputation of the script hash and assertions on exact restored tuples. I relied on that and did not inspect the script.

## Claim-to-evidence check

| ADR claim | Log support |
|---|---|
| Partial failure leaves no partial copy (R3) | PASS: partial copy rolled back, legacy rows preserved |
| Retry and repeat preserve exact assignments, same local ID across tenants (R2, R3) | PASS: exact rows by tenant, both local ID 7 values |
| Own rule if present, shared default otherwise (R1) | PASS: overrides and authorized shared fallback |
| Absent or mismatched context denied before data access (R1) | PASS: denied before database access |
| Snapshot restore preserves records and lookups (R3) | PASS: isolated snapshot restore |
| Zero cash spend, local runtime only | Consistent; Staging, Production, licences and cost correctly marked unverified |
| Server-side tenant binding, per-tenant cost, rollout steps | Correctly framed as proposed or unverified |

## No material unsupported claims

These are minor wording fixes and don't block the pilot:

1. **"Actual runtime version … appear in the run log."** The log gives the SQLite version (3.50.4) but no Python version. Either add `python --version` to the log or change the wording to "SQLite version."
2. **"Input row counts."** The log counts 3 tenants and 2 legacy rows, but the shared default row isn't counted. Add it so the fixture description ("one shared default…") is fully reflected.
3. **"Candidate SHA-256."** "Candidate" could read as unconfirmed. Since independent verification matched the hash, consider noting that next to the digest, with who verified it and when.

Before any architecture routing, the ADR's existing conditions still apply: Database and Security review, linked specialist dispositions, and Finance and environment evidence.
