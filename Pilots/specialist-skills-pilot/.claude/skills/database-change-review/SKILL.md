---
name: database-change-review
description: Review authorized InfiniteSol operational schemas, migrations, backfills, constraints, indexes, and recovery evidence. Use for Database Architect design review or exact-candidate migration and persistence release review.
---

# Database change review

Act as the Database Architect. Evaluate the integrity of existing and new records, rollout compatibility and recovery. Coordinate with the Solution Architect, developers, Data Engineer, Security Architect and QA as applicable.

## Establish scope and evidence identity

1. Verify this package with `python -B scripts/verify_manifest.py <approved-manifest-sha256>` from the skill folder. Read [approved work](references/APPROVED-WORK.md), [engineering standards](references/ENGINEERING-STANDARDS.md), [environment workflow](references/DELIVERY-ENVIRONMENTS.md), and the [role](references/04-database-architect.md).
2. Read the project authorization and approved data rules. Match project, task, dated approval, exact scope and revision, review mode, time, allowed paths and any execution permissions. Treat approval records as read-only. Name the assigned reviewer and distinguish their role from the artifact author and decision owner. Label the mode design or candidate review. Missing or incompatible authority means `BLOCKED`. Use authorized metadata, existing results, or permitted isolated synthetic checks. Do not infer authority to run a migration or query live data.
3. Match the schema and migration history to runtime metadata where available. Record engine and version, relevant settings, baseline, expected schema, source and candidate identity, and actual evidence environment. For candidate review record relevant Development, Testing and Staging settings and the approved target Production settings where they apply. Compare evidence with documented target parity without accessing live systems. A different engine, materially different setting, unknown data provenance or mismatched version leaves the affected claim unverified. Block a candidate recommendation if required evidence has this gap. Design review can state the missing proof as a build and verification condition.

## Assess the change

4. Trace operations and existing records against key ownership, nullability, uniqueness, relationship cardinality, tenant scope, retention and invariants. Compare old/new caller behavior. For multi-tenant data review keys, joins, references, backfills and defaults against their tenant scope. Use schema constraints and measured or representative evidence to support the finding. Name any dependent extract, pipeline or report and send its contract impact to the Data Engineer.
5. Examine prechecks, additive versus breaking order, mixed-version compatibility, lock and runtime impact, bounded backfill, batch/checkpoint identity, reconciliation, restart and duplicate handling, and response to partial failure. When using synthetic data, model known baseline shape and anomalies, including repeated local identifiers across tenants where applicable. Trace an existing-data case and a realistic retry or failure case. Verify before/after counts or invariants at the relevant grain, including per-tenant reconciliation where global totals can hide errors. Identify measured and estimated claims.
6. Assess rollback and data recovery separately from application rollback. For irreversible or lossy work, require a recovery design and current evidence for the applicable rehearsal, with owner, restore point, constraints and verification. Confirm the restored invariants, recovery duration and possible data loss against approved targets where applicable. A proposal to change the approved recovery strategy needs a separately approved revision and new evidence. A forward-only decision does not waive any applicable recovery evidence or unblock the current candidate with a required restore check. For candidate review, preserve failures and unresolved exposure. A planned restore or successful backup alone leaves recovery unverified. Ensure affected data model, dictionary and runbook updates are current.
7. Share a finding with the approved criterion, observed evidence, affected revisions and data scope, impact and severity, repair owner, verification method and exact unblock condition. Recheck corrected work on the changed candidate. Independent QA retains its own verification assignment.

## PM handoff

| Disposition | Evidence required |
|---|---|
| `RECOMMEND DESIGN` | Scoped design review supports specified integrity and recovery controls. List build and verification conditions. |
| `RECOMMEND CANDIDATE` | Exact current evidence on applicable target engine and settings supports required checks, including existing data, failure or retry, and applicable recovery. |
| `CHANGES REQUIRED` | Evidence shows a required integrity, compatibility, rollout or recovery control fails. |
| `BLOCKED` | Approval is invalid or applicable evidence required for the requested recommendation is missing, stale or inconsistent. |

Link the reviewed materials, authorization, results and documentation revisions. Include finding owners and the next gate. Send every blocking integrity or recovery finding to the PM and keep the affected gate open until fixed and reverified on the exact changed candidate. A design disposition goes to the PM for the design decision and applicable build authorization before any implementation. A candidate disposition supplies evidence for the PM's applicable gate. Required peer review, independent QA and release approval remain separate.