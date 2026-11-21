# Review status

## v1.8 task goals and independent QA

Round 9. Emerson supplied the independent Claude Code review for fingerprint `6278e4f6664daa97`. The reviewer confirmed the fingerprint and returned **APPROVE**, with no material findings.

| Tabletop scenario | Observed workflow disposition |
|---|---|
| Developer tests pass and QA finds a regression | PASS. QA returns the task to the author for correction and reruns the affected checks before recommending completion. |
| A required step was skipped | PASS. QA requires evidence that the approved approach and required steps were followed. Incomplete approval blocks affected work. |
| The candidate changed | PASS. Affected evidence is superseded. QA and peer review checks use the relevant exact revision before release. |
| Approval expires before the goal is reached | PASS. The task stays open and blocked or paused. The PM receives the checkpoint, evidence, owner and decision needed to proceed. |

Codex verified links, shared role rules and revision consistency. The results cover the written workflow and its decision paths. Application test results are outside this review.

## v1.7 commercial handoffs and critical-incident pause

The CEO approved the workflow changes. Claude Code independently reviewed fingerprint `3cef03b1bac3170b` and returned `APPROVE`. Codex confirmed the 14 role prompts, linked documents, and exact archive and installed revision.

| Tabletop case | Observed workflow disposition |
|---|---|
| SIM-COM-1 | A synthetic lead waits for an authorised signatory and agreement and then for approved build scope. Premature milestone billing is blocked. After synthetic milestone acceptance, the named billing owner can prepare the invoice with Finance checks. The scenario routes onboarding, support handoff and renewal to their recorded owners. |
| SIM-INC-1 | A synthetic critical incident during another build allows the named backup to checkpoint and pause under a current 30-minute sample delegation and record escalation. An absent or expired delegation blocks the pause and routes escalation. Spending and a new Production release require their own authority. A recorded restart decision is required. |

The exercises used fictional inputs and validated the written workflow. Actual owner availability, contact acknowledgement, operator permissions and signed incident delegation remain to be recorded for the applicable readiness gate. No customer was contacted, no invoice was issued and no live action was taken.

## v1.6 Data Engineer and document organisation

Claude Code independently reviewed the staged v1.6 package at fingerprint `cd02c450c3ac74c6` and reported no loopholes, contradictions or stale paths in its review. Codex checked the 14 role prompts, the approved Markdown and experience standards, the data and BI contract template, the relocated policy and workflow references, and the installed release against the reviewed packet. This was a review of the written operating model.

## v1.5 open-source-first and zero-new-spend design

Claude Code independently reviewed the staged v1.5 cost workflow at fingerprint `2b1f622fd8602bc9` and reported no concrete loopholes or contradictions. Codex checked all 13 common-charter role prompts, linked Markdown references, the cost template across the lifecycle, and the installed files against the exact review packet. This review verified the written rules and templates. No vendor, service, project cost or deployment was tested.

## v1.4 approved Markdown, architecture and deployment

Claude Code reviewed the staged workflow identified by fingerprint `d0648326c2754471` in a fresh session and reported no material blockers. The review covered work authorization, discovery bootstrap, architecture, QA, artifact promotion, operator authority, rollback and support handoff. Codex verified the exact staged fingerprint, all 13 shared-charter role prompts and their linked templates, then matched the archive and installed files to the reviewed material. This was a written workflow review. No application environment was provisioned or release executed.

## v1.3 project documentation lifecycle

Claude Code approved the documentation workflow and its templates at fingerprint `c93d28f7788a79c6`. The review kept proposal, build decision, project change, adoption readiness and production approval distinct, and checked that delivery closeout retained ongoing support. Codex verified all seven template paths and the flowchart's branch and correction loop, and matched installed files to the approved artifact. This was a written review. No project was started and no application was released.

## v1.2 requirements, opportunities and ways of working

Claude Code approved the requirements improvement, business opportunity and applied study workflow at fingerprint `7417ca2e49541920`. The tabletop review distinguished unapproved ideas and experiments from implementation authority, and verified that multiple projects using one developer pair remain a portfolio priority issue. The reviewer noted that the two linked templates were outside the files it read. Codex verified both template paths and their actual contents in the exact reviewed archive and the installed local pack. No live project or external experiment was run.

## v1.1 maintenance update

Claude Code approved the maintenance workflow at fingerprint `13fecff4bc2aa5a1` with no remaining actionable findings. The review was of the written workflow and a targeted recheck. It did not operate or monitor a deployed application.

| Review round | Fingerprint | Independent disposition |
|---|---|---|
| Maintenance review | `1e061f915e2b76ca` | `APPROVE`. Reviewed support handoff, operating evidence and production approval. One low observation requested a deadline to escalate blocked support acceptance. |
| Maintenance recheck | `13fecff4bc2aa5a1` | `APPROVE`. Verified the project records a deadline before release and escalates critical handoff gaps, missed deadlines, or missing deadlines on already-live applications. No actionable findings remained. |

## v1.0 baseline

Codex and Claude Code accepted the written prompt pack at fingerprint `104f2bc8c2a5f1cb`. The archive was checked against the exact review packet. Use `reviews/REVIEW-REQUEST.md` and `workflows/PEER-REVIEW.md` to repeat the process on future changes.

| Review round | Fingerprint | Independent disposition |
|---|---|---|
| 1 | `162b5e26a010933d` | `CHANGES REQUIRED`. Three high, four medium and four low findings. Claude Code inspected the initial pack. |
| 2 | `a22294e8301ff094` | `APPROVE`. All 11 original findings resolved. The reviewer walked through the stale API guide and rebuilt candidate scenarios. One low observation remained about the runtime requirement for a substitute reviewer. |
| 3 | `104f2bc8c2a5f1cb` | `APPROVE`. The reviewer verified the two-file change on substitute independence and the required Codex or Claude Code counterpart. No remaining findings were reported. |

| Finding | Codex correction in the next revision |
|---|---|
| F-01 | Added a practical CEO decision check for build, priority, scope, spend and production approval. The CEO remains the human decision maker, with 12 agent roles. |
| F-02 | Defined immediate recovery for an unavailable reviewer or runtime and kept the peer gate open until a valid reviewer is available. |
| F-03 | Required authors to supersede approvals and notify the peer and PM when the candidate changes; PM checks the actual candidate against the recorded approval. |
| F-04 | Added approved alert routes, backup operator, acknowledgement and a synthetic rehearsal. |
| F-05 | Added required specialist triggers, gate timing and evidence records. |
| F-06 | Added a release check and separate review IDs for integration-originated content. |
| F-07 | Made the PM the explicit owner of developer assignments in the shared charter. |
| F-08 | Separated immediate blocked-work recovery from substantive review rounds. |
| F-09 | Set discovery allowance rules across requests and the portfolio, with a limited no-new-spend triage default. |
| F-10 | Added a dedicated field for evidence that would change a recommendation. |
| F-11 | Made the release, QA and required check revisions explicit and mapped reviewed source work to the candidate. |

The walkthrough below is a review of the written workflow. It does not represent a live agent run, a production test or an independently approved result.

| Scenario | What the written process requires |
|---|---|
| New system requested during an existing build | PM gives it a request ID, classifies it and starts bounded discovery if possible. The developer pair keeps its assigned build until a priority decision changes it. |
| Request could be a change to an existing system | Retain the intake ID while classification is open. Link to the existing project and change ID once established. |
| New revision after code review | Peer approval attaches to the old revision. Re-review the new revision before integration. |
| Peer reviewer is unavailable | Record `BLOCKED`. Escalate the capacity or tooling issue. Keep the review gate open. |
| QA evidence relates to an older integrated revision | Invalidate affected evidence and rerun the required checks against the current candidate. |
| A critical issue occurs while the PM is unavailable | The finder stops affected work where authorised and uses the configured CEO channel. If unavailable, the report remains pending for the operator. |
| A test pass has no evidence | Mark it blocked or unrun as applicable. A claimed pass without evidence cannot close a gate. |
| A forecast exceeds the approved budget | Finance records inputs and variance, then passes options to the PM. CEO decides on a revised budget or scope. |
| An API change makes its client guide stale | The author logs the documentation impact and updates the technical reference. The peer checks technical documents before integration. The Technical Writer updates and verifies affected guides and references, and PM blocks closure or release until they are current. |
| A rebuilt candidate supersedes documentation references | The developer produces new build evidence and marks older review superseded as applicable. The Technical Writer rechecks the impact list and affected documents against the proposed candidate. PM compares the candidate against the current registers before advancing the gate. |
