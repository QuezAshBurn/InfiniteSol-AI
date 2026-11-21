# InfiniteSol specialist skills pilot

20 November 2026, Perth time. This build brings the local catalog to **8 of 14 planned skills**. The three new packages are v0.1.0 and pinned to approved source pack v1.8, revision `6278e4f6664daa97`. The scope and expected package hashes are recorded in the [authorization](../AUTHORIZATION.md) and [manifest register](../MANIFESTS.md).

| Skill | Role and output | Codex | Claude Code |
|---|---|---:|---:|
| `architecture-decision` | Solution Architect drafts a decision backed by requirements, viable alternatives, technical boundaries, and evidence of cost by environment. | 3/3 | 3/3 |
| `database-change-review` | Database Architect reports whether the exact candidate preserves existing records, tenant boundaries, compatibility and recovery. | 4/4 | 4/4 |
| `defensive-security-review` | Security Architect reviews scoped control design and exact-candidate evidence and routes findings to the PM. | 5/5 | 5/5 |

Both tools matched the expected disposition on all 12 synthetic cases. Cases covered conflicting requirements, an expired grant, a backfill that lost a tenant's rule despite matching global counts, a stale restore rehearsal, a failed isolation control, changed configuration and a severity dispute. The final database skill keeps the gate blocked when the required restore evidence is stale. The security skill carries the higher severity when reviewers disagree, pending resolution. The PM routes the architecture decision only after required specialists disposition the same revision and blockers are resolved. [Codex scenarios](CODEX-SCENARIOS.txt) and [Claude Code scenarios](CLAUDE-SCENARIOS.txt)

All nine copies passed package-integrity checks. Both project runtimes loaded all three skills by name. The controlled Codex activation test used a loopback request with no model response. A signed-in native Codex inference run remains unverified. Codex scenario judgments came from a separate session and Claude's scenario judgments from text-only sessions. [Codex activation](CODEX-ACTIVATION.txt) and [Claude activation](CLAUDE-ACTIVATION.jsonl)

## Tenant-rule rehearsal

The local exercise compared a shared service with tenant-owned rules against separate deployments and drafted a decision for the synthetic scope. A developer run and independent Codex QA verified all five checks on script SHA-256 `75db44471afa32a451589585c26667b054743a029e149e0fa61835e15db34b8b`. The SQLite 3.50.4 run kept identical local rule IDs distinct across two tenants, preserved authorized fallback, denied absent or mismatched tenant context before SQL, rolled back a partial copy, and preserved every original and migrated row through snapshot restore. The test checked a local script and in-memory database. [Draft architecture decision](../rehearsal/RULE-DECISION.md), [rehearsal script](../rehearsal/check_tenant_rules.py), and [observed results](../rehearsal/REHEARSAL-RESULTS.txt)

Claude Code challenged the draft about fallback, actual identity binding, recovery scope and traceability. The revised draft distinguishes proposed controls from observed results. The final independent read-only assessment returned `PASS FOR LOCAL PILOT` and relied on the recorded run and Codex verification. PM closes the skill pilot for the pinned package snapshots and rehearsal revision.

The rehearsal adds AUD 0 in cash spend. Real identity issuance, target-engine parity, load, deployment and recovery targets, licences and operating cost by production environment need separate evidence and approval. The local rehearsal scope ends with this closeout.

## Remaining backlog

`documentation-update`, `positioning-brief`, `legal-draft-review`, `cost-and-variance-review`, `release-readiness`, and `data-contract-and-quality`.
