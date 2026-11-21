# Tenant dispatch-rule decision | draft ADR-01 R1

**PM request.** Compare ways to support separately owned tenant dispatch rules on the synthetic R1 fixture at zero new spend. The local pilot authorization covers drafting and isolated demonstration. The recommendation is conditional on Database and Security review.

## Requirements and baseline

| ID | Observable outcome |
|---|---|
| R1 | For an authorized tenant, use its own rule if present and the shared default otherwise. Missing or mismatched tenant context is denied before data access. |
| R2 | The same local rule ID can exist in different tenants. The migration preserves each tenant's exact rule assignment and all original rows. |
| R3 | A partial failure leaves no partial copy. Retry, repeated migration and snapshot restore preserve the specified records and lookup behavior. |

The fixture represents one shared default and legacy rules keyed by tenant and local ID. Each of two tenants overrides that shared default. A third tenant uses it. The table design and exact inputs are in [the rehearsal](check_tenant_rules.py).

## Options and recommendation

Recommend a shared service with explicit tenant context and tenant-keyed configuration for the synthetic scope. The rehearsal exercises a scope-matched read and composite key in a local script. Server-side binding to the authenticated tenant is a proposed application control. It needs separate verification on an actual system. A per-tenant deployment would give separate operational boundaries and introduce additional configuration, deployment and recovery responsibilities. The comparative operating cost and scale of that alternative remain unverified.

For an actual rollout, keep the legacy table during the compatibility window, reconcile exact tuples by tenant before switching the read path, and check restored records before resuming service. These are proposed requirements. The local script verifies copied and restored fixture rows, transaction rollback, retry, permitted fallback and denial before any SQL for absent or mismatched context. The Database Architect owns migration review. The Security Architect owns the tenant binding control review. Independent QA owns observation of the required behavior.

## Cost and scope

Development and Testing are feasible for the synthetic check using the installed Python and SQLite runtime and existing equipment. The SQLite version and foreign key setting appear in the run log. The pilot adds AUD 0 in cash spend and consumes local compute and review time. Staging, Production, operational support, workload limits, exact production dependency licences and ongoing infrastructure costs remain unverified. Finance review and environment-specific evidence apply before an actual stack or release commitment.

The recommendation covers the fixture and its measured data only. The [run log](REHEARSAL-RESULTS.txt) identifies the exact script, input row counts, command, digest and result. Revisit on different engine or configuration, change to fallback or authorization, requirement to remove the old table, or material cost, data volume or recovery change. PM must link the exact specialist dispositions before routing an architecture decision.
