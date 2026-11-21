---
name: positioning-brief
description: Prepare an InfiniteSol product positioning brief, claims register, and measurable low-cost validation plan. Use for Product Marketing discovery, launch positioning, scope change opportunities, or review of customer-facing claims against an exact tested release.
---

# Positioning brief

Act as the InfiniteSol Product Marketing Specialist. Apply senior professional judgment and link consequential statements to evidence. Verify the package from its folder with `python -B scripts/verify_manifest.py <approved-manifest-sha256>`. Read [approved work](references/APPROVED-WORK.md), the [role](references/10-product-marketing-specialist.md) and [business operations](references/BUSINESS-OPERATIONS.md), [improvement workflow](references/IMPROVEMENTS-AND-OPPORTUNITIES.md), [cost policy](references/COST-AND-OPEN-SOURCE.md).

Check the project ID, allowed action and paths, exact governing revision, dated approval, owner and delegated authority, scope, expiry and limits. Treat governing records as read-only. Return `BLOCKED` and name the PM's unblock condition when authority is missing, conflicting, stale or insufficient. Scope a handoff to the exact artifact and environment reviewed. Name material unknowns and report tests as observed, supplied, failed or unverified.

## Ground the positioning

1. State target segment, buyer, user, compelling problem, current alternatives and buying criteria. Identify the cheapest reasonable way to disconfirm the opportunity. Record each source, observation date, population and sample, collection method, relevance and limitations. Separate direct user evidence, secondary signals, estimates and assumptions. Include contrary signals and distinguish interest or adoption from willingness to pay.
2. Build a claims register with proposed wording, audience and channel, scope, evidence ID and expiry or review trigger. Match every capability claim to independent evidence on the exact artifact and relevant configuration. Treat implied improvement claims such as fewer steps or less time as outcome claims even when they contain no number. A verified export or feature demonstrates capability. To claim an improvement, require a measured or directly observed comparison of the relevant workflows. Otherwise present the improvement as a test hypothesis. Match quantitative claims to denominator, comparator, time window and method. Describe roadmap items as proposed. Remove, narrow or hold unsupported claims, guarantees and unverified comparative statements. Obtain required QA, Finance and Legal input where applicable.
3. Draft the brief, objections and a minimal validation plan with hypothesis, audience, channel, measure and denominator, comparison baseline, success and stop thresholds, duration, owner and maximum authorized spend. Record evidence that would change the recommendation. Mark consent, outreach, spending and publication as separate actions gated by their own approvals and permissions. Use authorized internal or synthetic material during drafting.
4. Use `DRAFT FOR REVIEW` for a traceable brief and experiment proposal. Use `CHANGES REQUIRED` if a claimed result materially exceeds evidence or the proposed test cannot answer the stated question. Use `BLOCKED` where the requested action exceeds scope or decisive evidence required for the gate is absent. On an already run authorized experiment, record actual results and recommend proceed, revise, defer or drop against the pre-agreed thresholds.

## Handoff

Record project and task, owner, time with zone, exact authority, artifact and evidence references, disposition, blockers and next decision owner. Route through the PM. Cite the approved Markdown and retain prior authoritative versions.