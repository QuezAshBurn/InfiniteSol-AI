# InfiniteSol delivery skills pilot

20 November 2026, Perth time. Five project-scoped skills at version 0.1.0 were installed for Codex and Claude Code in the isolated pilot. The approved source pack is v1.8, revision `6278e4f6664daa97`.

| Added skill | Role and output | Codex expected decisions | Claude Code expected decisions |
|---|---|---:|---:|
| `story-specification` | Business Analyst drafts an evidence-backed story with measurable criteria and an explicit approval request. | 3/3 | 3/3 |
| `implement-approved-story` | Senior developer checks scope, records the baseline, implements and tests the change, and updates affected documentation. | 3/3 | 3/3 |
| `independent-code-review` | The other senior developer checks the exact candidate and returns a documented disposition. | 4/4 | 4/4 |

The fixtures cover authorized work, missing or expired authority, conflicting requirements, legacy regressions, self-review, material defects, and stale candidate evidence. The expected decisions matched in all 10 cases per tool. The case-by-case outputs are recorded in [Codex scenarios](CODEX-SCENARIOS.txt) and [Claude Code scenarios](CLAUDE-SCENARIOS.txt).

All five master packages and both sets of installed copies passed file-integrity checks. A controlled local Codex request verified that all five could be selected by name and included in the model request. A native signed-in Codex inference run remains unverified. An independent Codex session separately tested the three new skill instructions. Claude Code ran the specification and development fixtures with native skill loading. A telemetry-related review block interrupted native peer-review fixture execution. A separate Claude Code text-only run with the installed instructions and synthetic evidence completed those cases. The end-to-end Claude BA and counterpart used separate text-only sessions on the synthetic task.

## Full delivery chain

The PM routed DEL-001 through intake, story specification and approved dispatch. The developer reproduced three archive-related failures on the baseline and passed all eight candidate tests. The separate Claude Code developer approved the actual diff. Independent Codex QA matched the candidate digest, verified all four acceptance criteria, reran all eight tests, and checked 20,440 in-memory cases. A separate PM assessment supported closing the story, and the closeout was recorded for the same candidate.

The pilot used a synthetic orders helper and stayed local at AUD 0 new spend. [Closeout and evidence index](../chain/CLOSURE.md)
