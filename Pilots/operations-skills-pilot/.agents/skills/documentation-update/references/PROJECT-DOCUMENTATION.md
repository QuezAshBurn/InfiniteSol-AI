# Project documentation from proposal to closeout

Keep each project's documents inside `Projects/<Project Name>/`. Copy `starter/templates/document-register.md` to `docs/document-register.md` when the PM registers the project and link it from `project-record.md`. Store initiation documents under `docs/01-initiation/`, delivery documents under `docs/02-delivery/`, and closeout and handoff documents under `docs/03-handover/`. Keep live incident and maintenance records in the project's existing `maintenance/` folder. Link any authoritative version held elsewhere in the project instead of creating a second master copy.

## Before, during and after

| Stage | Records and templates | Owner and decision |
|---|---|---|
| Before build | Original request and project record, `project-proposal.md`, `project-charter.md`, versioned requirements and acceptance criteria. Use `process-flow.md` where a workflow or handoff affects design or acceptance. | PM owns the proposal and charter, with BA and specialist input. BA owns the business flow. The CEO's build decision references the exact charter version and approved scope and budget. |
| During delivery | Current requirements and flows, technical design, risks and decisions, code and build documentation, and test and review evidence. Use `change-request.md` for changes to approved scope, budget, dates or material requirements. Use `change-management-plan.md` where people or processes are affected. | PM routes change decisions and coordinates adoption. BA and Architect update affected requirements and diagrams. Developers record each change and build, QA verifies, and the Technical Writer keeps affected documentation current. |
| Before release | Release and rollback plan, current documentation, QA and peer review evidence, the maintenance record, and adoption readiness evidence when applicable. | PM verifies readiness. The Deployment Engineer owns the versioned release and rollback runbook and records Staging rehearsal evidence. The named authorised operator confirms execution readiness. The CEO's production decision identifies the exact candidate. |
| After delivery | Promotion and deployment attempt records, post-release verification, recovery evidence where applicable, release notes, support or owner acceptance, `project-closeout.md`, lessons learned and open obligations. For a live app, link the operating runbook and maintenance record. | PM records closeout and the handoff decision. Technical Writer reconciles final documentation. The named support owner continues maintenance, with an owner and due date for any open work. |

The PM records why a conditional document is not applicable. For a small project, keep the proposal and charter short and link to shared evidence. Preserve the distinct purpose and decision for each. For a cancelled or declined item, record the actual disposition and unfinished obligations rather than inventing approvals or test results.

Use `workflows/PROTOTYPING.md` for experimental evidence and `policies/ENGINEERING-STANDARDS.md` for the architecture brief, decision records and coding standard. Register each applicable document against the project and keep the technical deliverables with the project files. Carry forward the decision and the evidence from a prototype. Record the explicit decision when considering reuse of experimental code.

Use `workflows/DELIVERY-ENVIRONMENTS.md` to keep development, Testing, Staging and Production verification linked to the project record. Register the environment and promotion record with the design and release documentation. Link environment check results so the release decision can identify the artifact and relevant configuration.

Register the open-source and cost plan from `policies/COST-AND-OPEN-SOURCE.md` with the architecture and budget evidence. Link the approved ceiling, cost verification before build and release, and material updates during maintenance.

When data or BI scope applies, use `starter/templates/data-bi-contract.md` for source and target mappings, lineage, access, approved metrics, independent reconciliation and support handoff. Store it with project technical documentation and link its approved revision from the project record.

For commercial engagements, link the existing approved records and rehearsals in `workflows/BUSINESS-OPERATIONS.md` from the portfolio and project record. Record the customer acceptance and billing condition with the actual evidence. Keep the service handoff linked to the maintenance record.

## Keep three kinds of change distinct

- **Project change control** records what would change in the approved baseline, the options and impact, and the authorised decision. An idea stays proposed until that decision is recorded. After approval, revise requirements, acceptance criteria, schedule, cost and affected documents as applicable.
- **People and process change management** plans how affected users and teams learn and adopt the change. Start the plan during delivery. Record impacts, communications, training, readiness measures and post-launch feedback. Drafts and readiness checks do not authorise customer contact or a production change.
- **Technical release change** records the exact build, test evidence, rollout, rollback, operator and production approval. Use the existing release checklist and `workflows/MAINTENANCE.md`. The same project may require all three records. Link their IDs so an approved scope change or adoption plan cannot be mistaken for production approval.

## Draw the flow that supports the decision

The BA maps current and target business workflows where applicable. The Architect diagrams system boundaries or integration sequences when they matter to a decision. Show who performs each step, the branch conditions and at least the relevant failure or exception routes. Mark an unknown step or describe why a current-state map does not apply. Link flow steps to requirements, decisions and QA scenarios. Record who checked the flow and which version it describes. The `process-flow.md` template includes a small Mermaid example.

## Use the current approved version

Follow `policies/APPROVED-WORK.md`. Record which approved Markdown paths, exact revisions and dated decisions govern each assignment. Capture all material business rules, technical changes, build and verification outcomes, deployment and support decisions within the project. Resolve contradictions through the PM before dependent work proceeds.

The Technical Writer maintains the register and checks links and version consistency. Document owners verify accuracy. The PM checks required items at the build, release and handoff gates. Record the project ID, owner, version or revision, status, evidence and decision reference. Mark replaced drafts or versions as superseded and retain the decision history. Use the existing decision log for approvals and link to it from the document. A file marked ready for review establishes no approval by itself.
