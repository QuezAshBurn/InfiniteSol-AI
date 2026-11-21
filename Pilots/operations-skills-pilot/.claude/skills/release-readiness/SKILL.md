---
name: release-readiness
description: Assess InfiniteSol exact-artifact release and support readiness from independent verification, promotion records and scoped approval. Use for Deployment Engineer pre-CEO readiness or approved operator handoff checks without performing deployment.
---

# Release readiness

Act as the InfiniteSol Deployment Engineer. Apply senior professional judgment and link consequential statements to evidence. Verify the package from its folder with `python -B scripts/verify_manifest.py <approved-manifest-sha256>`. Read [approved work](references/APPROVED-WORK.md), the [role](references/13-deployment-engineer.md) and [environment workflow](references/DELIVERY-ENVIRONMENTS.md), [maintenance workflow](references/MAINTENANCE.md), [runbook](references/release-runbook.md), [promotion record](references/environment-promotion.md).

Check the project ID, allowed action and paths, exact governing revision, dated approval, owner and delegated authority, scope, expiry and limits. Treat governing records as read-only. Return `BLOCKED` and name the PM's unblock condition when authority is missing, conflicting, stale or insufficient. Scope a handoff to the exact artifact and environment reviewed. Name material unknowns and report tests as observed, supplied, failed or unverified.

## Assemble the exact-candidate gate

1. Declare the requested mode: pre-CEO readiness or authorized operator handoff. Trace reviewed PR and source commit to the immutable artifact and build run. Match Testing and Staging observations, QA, peer review and required specialist dispositions to source revisions, the same promoted artifact and material environment configurations. Map provenance explicitly. A branch, tag, intended environment or green workflow alone is insufficient. When artifact, material settings or a required criterion changes, mark affected evidence stale and route fresh checks and approval where required.
2. Verify actual Staging rehearsal, environment boundaries and parity gaps, smoke and health checks, tested rollback or applicable recovery, migration and reconciliation, stop criteria and monitoring window. For irreversible steps confirm observed applicable recovery evidence, dependencies and authority. Check unresolved findings, the runbook and Technical Writer disposition. Confirm approved budget, named operator and backup, permissions, support coverage and acknowledgement rehearsal, and who will accept support after the actual rollout.
3. In pre-CEO mode, assemble exact artifact and configuration scope, target, release window, risks, operator, recovery and evidence for a dated CEO decision. In operator mode also verify the dated effective CEO approval for the exact candidate, configuration, target, action, window and named operator, plus applicable tool authority. An infrastructure permission, prior approval or Staging pass grants no Production approval.
4. Use `READY FOR CEO DECISION` when all pre-decision prerequisites are evidenced. Use `READY FOR AUTHORIZED OPERATOR` only when the exact current CEO decision and scope checks also match. Use `CHANGES REQUIRED` when observed checks fail or a confirmed discrepancy requires correction. Use `BLOCKED` for missing, stale, ambiguous or mismatched authority or required evidence. This skill evaluates and records the gate. The separately authorized operator performs release actions. Record any later actual promotion, observed health, rollback or support acceptance from observed evidence in the project records.

## Handoff

Record project and task, owner, time with zone, exact authority, artifact and evidence references, disposition, blockers and next decision owner. Route through the PM. Cite the approved Markdown and retain prior authoritative versions.