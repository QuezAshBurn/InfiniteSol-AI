# Local memory prototype

20 November 2026 AWST. This prototype exercises the memory scope in [MEM-PILOT-A1-M1](MEMORY-FIRST-AUTHORIZATION.md). It uses two synthetic tenants, existing Python tooling and AUD 0 new cash spend.

## What the memory stores

| Record | Scope | Observed result |
|---|---|---|
| `INVOICE.POD_REQUIRED` r1 | Shared product default | Tenant B requires proof of delivery before invoicing. Decision `SYN-DEC-001`. |
| `INVOICE.POD_REQUIRED` r2 | Tenant A override | Tenant A can invoice early after supervisor approval and an audit reason. Decision `SYN-DEC-002`. |
| `PLATFORM.TENANT_ISOLATION` r1 | Platform invariant | Both tenants receive the same access boundary. Decision `SYN-DEC-003`. |

The rule bodies and synthetic decisions are Markdown. The pinned snapshot manifest links the exact record bytes to the rule ID, revision, tenant scope, effective interval and decision. The lookup returns the selected Markdown and the approval reference. An active override with inconsistent approval does not fall back to the default. A future or ended override can fall back when a valid shared default applies.

The launcher's trusted grant supplies the project, tenant and role. The lookup accepts a rule ID. These checks demonstrate scoped lookup behavior on synthetic files. Host identity, isolation from direct filesystem access, and real approval publishing require their own verification.

## Observed evidence

- Exact [candidate](memory/CANDIDATE.json) SHA-256 `fcb3cd28ffca8046a01d47f66eece989a924ad13da7900d4d99ec29722fb8a60`.
- Published fixture [manifest](memory/snapshot/manifest.json) SHA-256 `baa7cf19c58515e17f6d4d95355acfe37466596c0832edbe04665f4290f40ad4`.
- All 18 developer checks passed. They covered both tenant outcomes, shared invariants, scope denial before retrieval, effective dates, stale and conflicting authority, and unavailable or changed records. The final candidate also denies a missing grant and blocks a decision that cites a conflicting source link, even if the decision document's hash is valid. [Test output](memory/DEVELOPER-TESTS.txt)
- The demo returned the expected rule and decision for both tenants. [Demo output](memory/DEMO-RESULTS.json)
- An independent Codex QA session recomputed all ten candidate file hashes and reran all 18 tests on Python 3.14.7. All four live demo results matched the recorded output. The reviewer independently matched the source and approval bytes and checked that invalid grants read no files, the lookup uses one evaluation time, and conflicting or changed evidence never triggers a fallback for the affected tenant.

The local behavior checks passed. Formal closeout remains blocked on the required Claude Code counterpart review. Automatic approval review rejected the attempts because they triggered an unrelated, unverified Visual Studio telemetry connection. The peer gate stays open pending an approved Claude Code review path. [QA handoff](memory/QA-HANDOFF.md)

## Try the example locally

Run from the `memory` directory inside this project.

```powershell
python -B demo.py
python -B -m unittest discover -s tests -v
```

Compare the `revision`, `source`, and `approval_id` for the two invoice results. The same rule ID resolves differently because the approved Tenant A exception is in scope for Tenant A. The separate platform invariant resolves the same way for both.

This result covers the local memory layer. MCP connection, RAG retrieval and integration with live NimbusFlow are outside this prototype.
