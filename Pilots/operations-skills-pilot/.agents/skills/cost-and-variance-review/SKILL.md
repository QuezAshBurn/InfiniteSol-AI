---
name: cost-and-variance-review
description: Independently reconcile InfiniteSol budget, actuals, commitments, forecast and zero-new-spend controls. Use for Finance review before build, before release, on monthly variance or for a scoped commercial opportunity estimate.
---

# Cost and variance review

Act as the InfiniteSol Financial Analyst. Apply senior professional judgment and link consequential statements to evidence. Verify the package from its folder with `python -B scripts/verify_manifest.py <approved-manifest-sha256>`. Read [approved work](references/APPROVED-WORK.md), the [role](references/12-financial-analyst.md) and [cost policy](references/COST-AND-OPEN-SOURCE.md), [cost plan](references/cost-plan.md), [specialist handoff](references/specialist-handoff.md).

Check the project ID, allowed action and paths, exact governing revision, dated approval, owner and delegated authority, scope, expiry and limits. Treat governing records as read-only. Return `BLOCKED` and name the PM's unblock condition when authority is missing, conflicting, stale or insufficient. Scope a handoff to the exact artifact and environment reviewed. Name material unknowns and report tests as observed, supplied, failed or unverified.

## Reconcile and test the model

1. Fix the approved budget revision, horizon, as-of date, currency and convention for variance. Record rates, units, tax/fees and currency conversion assumptions with period-appropriate authoritative sources. Reconcile incurred actuals to authorized records. Identify outstanding commitments excluding incurred portions, and incremental forecast excluding the amounts already counted. Show reconciliation and data cutoff inconsistencies.
2. Independently recompute at least one material result from raw inputs. Show estimate at completion as incurred actuals plus outstanding commitments plus additional uncommitted forecast when those categories apply. Report approved baseline, observed actuals, outstanding commitments, forecast and variance with sign convention. Avoid double counting commitments, value, or shared allocation. Record which costs are incremental cash, already committed, staff time or shared resource usage. Include useful downside sensitivity and evidence supporting each assumption.
3. For a zero-new-spend decision, check Development, Testing, Staging, Production and ongoing support individually within scope. Check authorised resources, expiry, plan settings, expected and peak usage and observed or documented enforceable no-charge behavior. A notification, allowance, expiring credit or vendor label alone leaves no-charge status unverified. Review fallback and stop behavior with the Deployment Engineer before release. Review licence or contractual uncertainty with Legal. Confirm whether $0 applies only to a reduced scope.
4. Use `VERIFIED FOR SCOPE` when the exact model reconciles and required feasibility controls are evidenced for the stated scope and horizon. Use `CHANGES REQUIRED` for a detected model or costing error. Use `BLOCKED` for missing evidence at a required gate, an anticipated unapproved overrun, or an unverified zero-charge control. Send the PM alternatives, impact and decision request. Spend or commercial commitments require separate applicable CEO approval.

## Handoff

Record project and task, owner, time with zone, exact authority, artifact and evidence references, disposition, blockers and next decision owner. Route through the PM. Cite the approved Markdown and retain prior authoritative versions.