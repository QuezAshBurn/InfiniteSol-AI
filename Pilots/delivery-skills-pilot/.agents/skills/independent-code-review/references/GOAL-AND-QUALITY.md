# Task goals and quality verification

## Agree what done means

Record one clear, observable goal for every task or story in its approved Markdown assignment. Link the business requirement or decision, approved approach and constraints, existing behaviour to preserve, named owner and verifier, and measurable acceptance criteria. Record which evidence will prove each criterion. A goal can be a verified answer for research, an approved document, or an observed product outcome. If the goal or criteria are unclear, route the ambiguity through the PM and BA before starting the affected work. Use `starter/templates/work-authorization.md` and link evidence in the project record.

## Assign testing by responsibility

| Owner | Evidence required |
|---|---|
| Developer or other technical author | Own developer testing of authored code. Run applicable unit and component tests, targeted integration and contract tests, build and static checks, and checks of affected dependencies and existing behaviour. For a bug fix, capture baseline failure evidence when feasible, then show the fix passes. Link commands, results, and the exact revision before handing the change to QA. |
| Independent QA | Own the plan, execution or coordination, and evidence for all applicable independent verification. Review developer evidence as an entry check. Trace the goal to the approved criteria, verify the agreed steps and constraints were followed, and observe the outcome on the exact candidate. Cover affected and adjacent workflows with independent regression tests. |
| Specialists, business owner and authorised operator | Supply specialist evidence where needed. QA coordinates and evaluates coverage. The named business owner records user acceptance where required. The authorised operator runs Production actions under the approved runbook and permissions. |

QA assesses and records applicable functional, end-to-end, system integration, data and migration, regression, smoke, exploratory, negative and boundary, accessibility, compatibility, performance, approved defensive security, recovery and user-acceptance checks. Select depth and environments according to the goal, change impact and risk. Document any test type deemed inapplicable and why. Keep a required check open when it fails, is blocked, or was not run. For non-code tasks, apply the same goal-to-evidence check through source review, reproducing calculations or inspecting the actual deliverable as appropriate.

## Keep unresolved goals open

When QA finds the wrong outcome, a required step skipped, a regression or insufficient evidence, return the work to the responsible owner with the failing criterion, observed impact and evidence. Correct it and rerun affected checks. Repeat within approved scope, time, spend and permissions until QA verifies all required criteria and applicable regression checks for the current revision. Where a candidate, required configuration or approved criterion changes, invalidate affected evidence and reverify it.

When an approval expires, a blocker requires a decision, or a limit is reached, record the task as open and blocked or paused. Preserve the checkpoint and tell the PM the evidence, owner, next action and decision needed. An authorised scope change, deferral or cancellation must be recorded as such. Report completion only when the required goal, applicable approach and protection of existing behaviour have current evidence. Peer review, business acceptance and release approval retain their separate owners.
