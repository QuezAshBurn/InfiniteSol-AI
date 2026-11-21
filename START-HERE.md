# Start a project in InfiniteSol

| Folder | Contents |
|---|---|
| `AI Team/` | Company roles, policies and starter templates. [Role catalog](AI%20Team/ROLE-CATALOG.md) |
| `Skills/` | Company intake skills and company templates for architect-proposed adaptations |
| `Workflows/` | Shared processes for discovery, development, QA, and release |
| `Projects/` | A separate folder for each project, with `Skills/` for development capabilities, `Memory/` for project rules and regulations, and `docs/roles/` for job descriptions |
| `Pilots/` | Internal trials, sample projects, and their verification evidence |

## First prompt

Open the `InfiniteSol AI` parent folder as the workspace and use this prompt.

```text
Act as the InfiniteSol Project Manager. Use the InfiniteSol AI parent
folder as your workspace. Resolve the following paths from that folder:

- AI Team/START-HERE.md
- Skills/task-intake/SKILL.md
- Pilots/operations-skills-pilot/MANIFESTS.md

Read the company guide and apply the task-intake skill and its references.
Verify the skill package against its task-intake hash in the manifest
register before writing intake records. If any required file is missing,
inaccessible or fails verification, return BLOCKED with the exact path
and stop. A role prompt alone cannot satisfy the skill check.

Use Workflows/ for shared processes once work is approved.

I want to start [project name].
The outcome I want is [describe the result].

Log my request and draft the discovery authorization. Include
the scope, deliverables, time and spend limits, and decisions
I need to make. Stop at AWAITING APPROVAL.
```

If the request already has an ID, give the PM that ID. Ask it to validate the existing draft and preserve the portfolio row for that request.

Use the company instructions for approval and routing. Use the top-level `Workflows/` directory for shared processes on new projects. [Company guide](AI%20Team/START-HERE.md)

The workflow files inside `AI Team/` are the copy carried by the existing prompt pack. They preserve the pack's internal references.

## After discovery approval

The PM sets up the project under `Projects/<project name>/` and records the dated decision. Initialise `docs/project-skills.md` from the [project skills and competencies template](AI%20Team/starter/templates/project-skill-index.md) and create `Skills/` for the development bundles. Both can start with zero skills. Store project-specific job descriptions under `docs/roles/`.

Only a written Solution Architect proposal can trigger creation of a project skill, including adaptation of a company template. Propose only capabilities that directly support this project's approved design, implementation, integration or testing. Examples include Python development, API development, database development and QA testing when those capabilities are needed. Tie each capability to a project deliverable, relevant industry rules, exact technology and planned verification. The PM records scoped Markdown approval before assigning authoring work and records approval for the exact verified version before use. Work authorizations identify the approved skill and version when needed.

The Solution Architect defines the job description for each role the project needs, including its technical and industry competencies, scope, outputs, evidence and handoffs. Role owners contribute their specialist requirements. The PM uses the exact approved descriptions for assignments. The shared role catalog supplies company-wide responsibilities and decision rights. [Role catalog](AI%20Team/ROLE-CATALOG.md) [Project role description template](AI%20Team/starter/templates/project-role-description.md)

For project work, use only approved skill bundles sourced from that project's `Skills/<skill name>/` folder and listed in `docs/project-skills.md`. Every project skill is bound to its owning project. Each new project defines and verifies its own bundles. Company intake runs at the parent folder.

When the assignment authorises skill setup, verify the approved project bundle and place its runtime copy as follows.

| Runtime | Skill path from the named project folder |
|---|---|
| Codex | `.agents/skills/<skill name>/SKILL.md` |
| Claude Code | `.claude/skills/<skill name>/SKILL.md` |

Open the named project folder for those sessions. Match each runtime copy to the approved project source and revision. If a required skill is missing, unapproved, or mismatched, pause the affected task and tell the PM. The existing pilot manifests record the expected hashes for the current master packages. [Manifest register](Pilots/operations-skills-pilot/MANIFESTS.md)

## When the business requirements are in place

The BA documents the business requirements and the PM records the approval that covers the exact requirements revision and scope. That recorded baseline triggers project memory setup. Copy the [project memory starter folder](AI%20Team/starter/templates/project-memory/) to `Projects/<project name>/Memory/`. Add the project ID and approved requirements reference to the memory index and register it in `docs/document-register.md`.

Keep only rules, tenant variations and regulatory decisions or applicability questions that relate to this project's requirements. Link each entry to the requirement or approved project decision that makes it applicable. Keep company-wide policies in the company folders, and record the project-specific application where it is needed. Each project derives its own memory from its own approved requirements.

Start each assignment from its approved Markdown. Once project memory is active, read only the relevant entries from that project's `Memory/`. Check the controlling source, exact revision, project and tenant scope, and applicable approval before relying on a rule. The BA maintains business and tenant rules with their owners, technical specialists verify constraints, Legal routes applicability for qualified review, and the Technical Writer updates the register. The PM handles unresolved conflicts and records approvals. When a requirements change is approved, reassess the affected memory entries and retain the previous references for traceability.
