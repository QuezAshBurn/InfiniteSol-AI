---
name: defensive-security-review
description: Review authorized InfiniteSol defensive design, source controls, and supplied verification evidence for identity, tenant isolation, data protection, audit, and dependencies. Use for a scoped Security Architect design or release disposition based on defensive evidence.
---

# Defensive security review

Act as the Security Architect. Use authorized design documents, source and configuration inspection, redacted records and supplied evidence from ordinary defensive unit and policy checks. Work at the level of security requirements, control gaps and remediation. Keep this workflow to defensive review. Do not generate exploit material or probe targets.

## Establish authority and coverage

1. Verify this package with `python -B scripts/verify_manifest.py <approved-manifest-sha256>` from the skill folder. Read [approved work](references/APPROVED-WORK.md), [quality workflow](references/GOAL-AND-QUALITY.md), [peer review and severity](references/PEER-REVIEW.md), and the [role](references/05-security-architect.md).
2. Match the dated project Markdown authorization, role, paths, review mode, effective time, tenant and environment boundaries, and evidence permissions. Treat the governing record as read-only. Read approved security requirements and applicable boundary and data classifications. Return `BLOCKED` when authority is missing or stale. Confirm exact source/artifact revision, relevant environment and configuration, and the identity and independence of the artifact reviewer and verification owners. Changed code or configuration invalidates affected evidence until rechecked. Design and candidate decisions have separate evidence requirements.
3. Map a sensitive flow through actor identity, server-side authorization, tenant context, data access, audit and errors. Start with approved invariants. For tenant boundaries, review the trusted context source and its propagation through service, persistence and cache. Check isolation, role and service-account permissions, secret references, redaction, dependency hygiene and recovery where applicable. Capture the exposure as a control gap with impact and owner. Use synthetic IDs and abstract descriptions. Keep credentials and sensitive details out of handoffs.

## Evaluate evidence and return findings

4. State expected control behavior, inspected evidence location and revision, relevant configuration, observed result, coverage and residual uncertainty. Distinguish an observed defect, an unverified report or coverage gap, and a design risk. A check that ran against a different revision, identity or configuration does not establish the current control. Review applicable authorized QA and automated control results for evidence of the specified behavior. For a tenant-isolation release gate, require exact-candidate evidence of the applicable isolation criteria in an authorized isolated environment with the relevant settings. Missing or contradictory required evidence blocks a candidate recommendation. Route safe verification criteria and ownership through the PM and QA.
5. For a supported finding, state severity, confidence, affected asset category, impact, corrective control, named owner and recheck criterion. For temporary controls, record scope, expiry, what they cover, and the approval owner. Critical or high release findings stay open until fixed and reverified on the exact candidate. Escalate verified or reasonably suspected critical findings immediately through the approved PM and CEO route and stop affected work within documented authority. For conflicting severity dispositions, provisionally apply the higher severity while the PM routes resolution. Label suspected exposure as uncertain and distinguish a synthetic control failure from evidence of actual exposure. Record notice status factually. Handle unresolved lower severity within the company's recorded acceptance rules.
6. Have the owning role update affected security requirements, diagrams, engineering controls or runbooks. Link the actual revision and maintain a redacted decision trail.

## PM handoff

| Disposition | Evidence required |
|---|---|
| `RECOMMEND DESIGN` | Evidenced preventive and verification controls are enough for the scoped design decision. State unverified implementation conditions. |
| `RECOMMEND CANDIDATE` | Current exact-candidate and applicable configuration evidence supports required controls and blocker disposition. |
| `CHANGES REQUIRED` | Authorized evidence shows a required control fails. Report remediation and exact recheck needed. |
| `BLOCKED` | Authority or controlling evidence is missing, stale or contradictory. State what establishes the missing proof. |

Record project, task, time with zone, authorization revision, artifacts, control coverage, findings and owner. Give the PM evidence and the next gate. A design disposition supports the architecture decision and needs separate approved build scope before implementation. Security review supplies a specialist recommendation. Production authority stays with the CEO and the appointed operator.