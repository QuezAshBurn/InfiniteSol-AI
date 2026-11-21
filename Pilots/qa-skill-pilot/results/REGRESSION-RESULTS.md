# InfiniteSol skill regression tests | 20 November 2026

Both project skills are version 0.1.0 and reference the approved v1.8 pack fingerprint `6278e4f6664daa97`. The masters and four installed project copies matched their manifests. All 14 fixture hashes matched the frozen pre-run snapshot.

| Check | Result |
|---|---|
| `qa-verify` decisions | 8 of 8 expected decisions in both a fresh Codex session and Claude Code. Covered clean pass, regression, skipped required step, stale candidate, expired approval, same-session authorship and QA, missing developer evidence, and missing peer disposition. |
| `task-intake` decisions | 6 of 6 expected decisions in both runtimes. Covered absent approval, valid delegated approval, expired approval, wrong path, invalid delegation, and spend outside the approved ceiling. |
| Package integrity | Each skill rejected an incorrect expected hash, edited skill file, missing reference, unexpected file and edited manifest. All 10 negative checks passed using disposable copies. |
| Native Codex loading | Both skills were discovered and their full instructions appeared in the model request when selected explicitly or invoked by dollar-prefixed name. The request was captured on Windows loopback. |
| Approved Windows guide | Reran both exact commands in `RUN-QA.md`. Each accepted the correct hash and stopped on a wrong one. The closed trial candidate digest matched before and after. |
| Signed-in Codex smoke test | BLOCKED. Automatic review rejected the isolated sign-in attempt after detecting an unapproved connection to `github.com`. A signed-in native model response still needs verification. |

[Codex behavioral results](REGRESSION-CODEX.txt) used the installed files directly in an independent session. [Claude Code behavioral results](REGRESSION-CLAUDE.txt) used the installed `task-intake` skill directly. An automatic telemetry block interrupted the native `qa-verify` regression session. The completed read-only retest supplied the exact skill body and synthetic fixtures as text. Its earlier native five-case QA test is recorded separately.

Synthetic scenario decisions are pilot test evidence. The Windows guide checks verify the already closed documentation artifact and do not represent application or Production QA.
