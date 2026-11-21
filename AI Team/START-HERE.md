# Running your AI company locally

The pack contains 14 self-contained prompts. Each begins with the same company charter. The Role 01 Project Manager owns intake and scheduling. The two senior developer roles share the same standards and alternate author and reviewer assignments for application features. For Data Engineer-authored code, the PM assigns an independent senior developer to review within the same build slot. Codex and Claude Code are runtime identities. A role name alone does not identify the author, reviewer or runtime.

## Find the right file

Paths in the role prompts and guides are relative to the AI Team folder unless they name a project location.

Read the [approved-work policy](policies/APPROVED-WORK.md) first, then open the [Project Manager prompt](roles/01-project-manager.md). For delivery, use the [project documentation workflow](workflows/PROJECT-DOCUMENTATION.md) and [environment workflow](workflows/DELIVERY-ENVIRONMENTS.md).

| Folder | Contents |
|---|---|
| [policies/](policies/) | Approved-work rules, engineering standards, and open-source and cost policy. |
| [workflows/](workflows/) | Steps for discovery, prototyping, documentation, peer review, release, maintenance and continuous improvement. |
| [roles/](roles/) | The 14 standalone role prompts. |
| [starter/](starter/) | Portfolio starter and reusable project templates. |
| [reviews/](reviews/) | Review instructions and prompt-pack review history. |

## First launch

1. Choose a private local folder for company records. Copy `starter/` into it. Keep the portfolio folder separate from production repositories, or keep it in a private local repository with no configured remote. Keep real credentials, customer records and secrets outside the record tree.
2. Open the folder as a workspace in Codex and Claude Code. Use a separate session for each assigned role. Paste that role's complete prompt as the first instruction, or load it using the runtime's instruction configuration if it supports the required scope. Include the current task and authorised working paths. Run two separate sessions when an independent reviewer and author are required.
3. Start with the PM prompt and give it your request. The PM registers it in `portfolio.md` and drafts the discovery authorization in Markdown. Follow `policies/APPROVED-WORK.md` and wait for the recorded CEO decision. Following approval, the PM classifies it, creates the named project folder, copies the project record and document register, and assigns authorised discovery work. Follow `workflows/PROJECT-DOCUMENTATION.md` for what to create next. At first you can dispatch handoff files manually between the two runtimes. Use the portfolio as the routing record. This pack supplies the prompts and records for that workflow. Automatic execution requires a separately configured coordinator, runtime access and permission controls.
4. Restrict each session to authorised paths and tools. Use a separate local branch or worktree for each feature, a separately scoped reviewer session, and isolated test databases. Preserve known user edits. Keep live credentials and data out of review context. Running tools from a local folder does not establish that model inputs stay on the machine. Confirm the data handling and transfer permissions of each configured runtime before using real customer data.
5. Use a single PM session as the writer of portfolio status, priorities and the approval log. Specialists write role-specific files and submit handoffs. PM assigns the next available identifier, records it before delegating, and resolves conflicting records against the source evidence. Store artefacts by path and revision so sessions can resume without relying on chat memory.
6. Fill in the emergency contact and operator section in `starter/portfolio.md`. Confirm the CEO's authorised way to receive an alert, who acts when the PM is unavailable, and how delivery is acknowledged. With the CEO or operator, rehearse the route using a labelled synthetic alert. If the notification route is missing or fails, record the limitation and retain the pending alert for the operator. Require a working route before commencing the first build.
7. Record the authorised discovery budget or time allowance per request and across the portfolio for a defined review window. Record both usage and remaining room before starting additional discovery. If the discovery authorization or applicable limits are missing, log the request, draft the proposed authorization and wait.

## Route the work

Use [Task goals and quality verification](workflows/GOAL-AND-QUALITY.md) on every task and story. Return failed work for correction and recheck. Keep an unresolved or blocked goal open.

| State | Owner and next gate |
|---|---|
| Received | PM logs the request and drafts its Markdown authorization. |
| Awaiting discovery approval | CEO decides on the exact proposed discovery authorization. PM waits for the recorded decision before assigning work. |
| Discovery | BA elicits and challenges requirements and maps workflows. The PM and Architect choose whether to test a key uncertainty through `workflows/PROTOTYPING.md`, within authorised limits. The PM prepares the proposal with supporting evidence. |
| Awaiting build approval | PM presents the proposal and draft charter with scope, acceptance criteria, the architecture brief, prototype evidence when applicable, alternatives, budget, milestones, risks and dependencies. Record the CEO's dated decision against that charter version. |
| Queued for build | Approved scope and budget are recorded. PM waits for capacity or an authorised priority change. |
| Build / Development | PM assigns approved Markdown work to an author, independent peer reviewer and QA owner. Developers trace GitHub pull requests, source, checks and builds. Follow `policies/ENGINEERING-STANDARDS.md`. The peer checks the code, documentation and engineering evidence before integration. |
| Integrated verification / Testing | Developers supply their test evidence. QA independently verifies the task goal, required approach, and applicable regression checks on the identified candidate. Record the exact artifact and environment. |
| Release rehearsal / Staging | The Deployment Engineer coordinates Staging rehearsal of the same candidate under the approved runbook in `workflows/DELIVERY-ENVIRONMENTS.md`, with independent QA verification. The Technical Writer verifies current documents. PM checks readiness, adoption evidence where applicable, and any required specialist dispositions. |
| Awaiting production approval | CEO reviews the exact candidate, risks, operational readiness, validation and rollback plan. |
| Deployed / Production handoff | The authorised operator deploys the exact approved candidate and verifies health. The Deployment Engineer records the observed outcome and coordinates the handoff. PM confirms support acceptance and records any unresolved operating gap. |
| Live / active maintenance | After handoff acceptance, PM records delivery closeout and tracks open obligations. The support owner follows `workflows/MAINTENANCE.md`. Track maintenance changes through the same delivery gates while the application remains live. |
| Support transferred / retired | PM records who accepted a transfer and where support now lives, or records the approved retirement decision and evidence. Archive once outstanding responsibilities have an owner or a recorded disposition. |

Use **Blocked** or **Paused** as a flag alongside a state. Record the affected work, why, owner, next action and proposed restart condition. If a release fails, follow the authorised change and rollback procedure, record observed service impact and return the work to the relevant verification state. If a new request arrives during an active build, keep the first build running under its current priority and start bounded discovery on the new request if resources permit.

Use one support record per deployed application. Copy `starter/templates/maintenance-record.md` into `Projects/<Project Name>/maintenance/` and link it from the project record. Keep project-specific runbooks, checks, incidents and maintenance evidence in the same project folder. Before the first production deployment, name the support owner and backup, authorise the support route and verify it. For an application already live, record any missing controls as gaps with an owner and due date before claiming that maintenance is operating.

### Required specialist reviews

At intake and whenever scope or a candidate changes, the PM applies this table, records which triggers apply and links specialist dispositions at the affected gate. These are minimum assignments. Add other specialists when justified. For a triggered gate, record the recommendation, evidence, and unresolved blocking findings before asking the CEO for approval. Route qualified human reviews when the Legal or Finance role identifies them.

| Trigger | Required specialists and timing |
|---|---|
| Commercial product or material change to the customer proposition | Product Marketing during discovery; Finance before commercial terms or delivery costs are approved. |
| Payment processing or material changes to funds handling | Security Architect, Legal Research and Drafting, and Financial Analyst during discovery and before release. |
| External collection or transfer of personal data, or material identity, privilege or tenant-isolation change | Security Architect at design and before release. Add Legal for personal data collection or transfer. |
| Schema migration, backfill, data integrity rule or material change to persistence | Database Architect at design and before release. |
| New or materially changed pipeline, analytics dataset, BI metric, source-to-report mapping or data contract | Data Engineer at design and before release. Involve the Database Architect for affected operational schema or load, the BA for business definitions, and QA for independent verification. |
| New or materially changed interface between projects or systems | Solution Architect at design and before integration. |
| External marketing publication or a new substantive claim | Product Marketing and Legal Research and Drafting before publication. |

## Apply process where it helps

Use `workflows/WAYS-OF-WORKING.md` to select and study the practices useful to the project. Start with Agile principles and a Scrum-informed delivery cadence. Use PMI project practices for approvals and tradeoffs, Lean Six Sigma to improve measured workflows, and ITIL practices for live service management. Adopt SAFe practices only when multiple teams have genuine dependencies that need regular coordination. Use one source of truth and keep the charter's approval and evidence requirements.

During discovery, at material feedback and at live service reviews, use `workflows/IMPROVEMENTS-AND-OPPORTUNITIES.md` to surface requirement improvements and business opportunities. Keep each project's proposals in its named folder using `starter/templates/improvement-opportunity.md`. Keep study and applied evidence there using `starter/templates/practice-study-record.md`.

## Cost and technology default

Use `policies/COST-AND-OPEN-SOURCE.md` and `starter/templates/cost-plan.md`. The architect starts with open-source options and $0 in new project spend, Finance verifies the plan, and the PM routes any requested additional spend for CEO approval. Record feasibility separately by environment before making a release commitment.

## Commercial operations and critical incidents

Use [Customer commitments and business operations](workflows/BUSINESS-OPERATIONS.md) before the first paid customer commitment and again before the first live release. Assign the named signatory, billing owner, business requirements decision owner, and service and release owners. Rehearse the customer handoff and a critical incident against current approvals. Record a bounded critical-incident pause delegation if you authorise one.

## CEO decision check

- **Build approval.** Confirm the outcome, measurable acceptance criteria, exclusions, budget ceiling and currency, significant dependencies or risks, and who owns the work. Record the exact scope version, approval limits and date.
- **Priority, scope or budget change.** Compare the current baseline and proposed change. Check the forecast and the effect on other projects and responsibilities. Record which baseline changes, when it takes effect, and what work may continue.
- **Production approval.** Check that the candidate matches the release record, QA report, required check evidence and current documentation index. Confirm that reviewed source revisions map to it and blockers are resolved. Check rollout, rollback, support acceptance readiness and the verified operating controls in `workflows/MAINTENANCE.md`. Record the decision for that exact candidate, with any limits, before the release operator proceeds. Defer a decision with missing required evidence and record what will unblock it.

## Example intake

You ask for a payment system. PM logs the request, then records `P-0001` in Discovery after you approve the discovery Markdown. PM assigns the BA and architect, and requests Finance, Legal and Security input on the proposed scope. After your build approval, developer A can build a feature and developer B independently review it. On a second feature, their roles can reverse. QA verifies the integrated behaviour using authorised test facilities and synthetic data.

You then ask for a customer portal. PM logs the request separately. After you approve its discovery Markdown, that work can proceed while the developer pair builds `P-0001`. If the portal needs a dependency from `P-0001`, record its owner, target interface and required revision. If both now need build capacity, PM presents a choice with consequences to you and records your priority decision. Until then, the active build keeps its slot.
