# InfiniteSol skills pilot closeout

20 November 2026, Perth time. The local catalog contains all **14 planned skills**. This pilot adds the final six at v0.1.0 against approved source pack v1.8, revision `6278e4f6664daa97`. Both project runtime installations contain the complete catalog. The [pilot authorization](../AUTHORIZATION.md) and [manifest register](../MANIFESTS.md) identify the scope and all 14 versions.

| Skill | Output | Cases |
|---|---|---:|
| `documentation-update` | Candidate-specific document register, corrected records and owner verification. | 4 |
| `positioning-brief` | Evidence-backed positioning, claims register and measurable experiment draft. | 5 |
| `legal-draft-review` | Internal issue and source review, corrected draft and qualified-review handoff. | 4 |
| `cost-and-variance-review` | Reconciled budget, forecast, downside and enforceable no-charge checks. | 4 |
| `release-readiness` | Exact-candidate recommendation for a CEO decision or authorized operator handoff. | 4 |
| `data-contract-and-quality` | Versioned contract, tenant-level reconciliation and scoped quality disposition. | 4 |

## Evidence

The cases cover expired authorization, a rollback that was still documented as success, unsupported results and outreach, superseded legal sources, double-counted costs, automatic billing, stale Production approval, a failed restore, and a tenant data swap masked by an unchanged aggregate. Codex and Claude independently matched the expected dispositions across all 25 synthetic cases. The marketing skill now requires direct outcome evidence for claims of less work or time, including wording without a number. [Codex cases](CODEX-SCENARIOS.txt) and [Claude cases](CLAUDE-SCENARIOS.txt)

All 14 master manifests and 28 installed copies matched the exact approved package bytes. Claude Code loaded all six new skills by name and reloaded the revised marketing skill. Its case judgments ran in separate text-only sessions. Codex independently read the installed packages and evaluated their behavior. Automatic review blocked the additional Codex loopback activation check after an unexpected connection to GitHub. A signed-in native Codex run remains unverified. [Claude activation](CLAUDE-ACTIVATION.jsonl)

The synthetic tenant invoice report and cost model passed seven local checks. Separate Codex QA reproduced the results and independently confirmed the script and artifact hashes. The release checks simulated artifact comparisons in memory. Claude challenged the supplied evidence and assessed the handoff as sufficient for a local rehearsal. The PM recorded local pilot closure. Cash spend was AUD 0. [Rehearsal and handoff](../rehearsal/PM-HANDOFF.md), [run evidence](../rehearsal/OBSERVED-CHECKS.txt), and [counterpart review](CLAUDE-REHEARSAL-REVIEW.md)

## Complete local catalog

| Use | Skills |
|---|---|
| Intake and design | `task-intake`, `story-specification`, `architecture-decision` |
| Build and independent verification | `implement-approved-story`, `independent-code-review`, `qa-verify` |
| Technical specialist review | `database-change-review`, `defensive-security-review`, `data-contract-and-quality` |
| Business and launch review | `positioning-brief`, `legal-draft-review`, `cost-and-variance-review` |
| Documentation and deployment readiness | `documentation-update`, `release-readiness` |

Project loads are available from the local `operations-skills-pilot` project directory. To use a skill on a real project, start with that project's own scope and approved Markdown. Install the project-scoped packages for that project and verify the pinned manifest before dispatch.
