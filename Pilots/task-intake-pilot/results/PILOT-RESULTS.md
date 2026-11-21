# Task intake pilot results

Version 0.1.0. Source pack 6278e4f6664daa97. Manifest SHA-256 758ce73cef1238e67667325af51b4f3e42a6180240912a2acab62b6e4d60301d.

| Case | Expected disposition | Codex | Claude Code |
|---|---|---|---|
| No approval | AWAITING APPROVAL | AWAITING APPROVAL | AWAITING APPROVAL |
| Current delegated approval | READY FOR PM DISPATCH | READY FOR PM DISPATCH | READY FOR PM DISPATCH |
| Expired approval | BLOCKED | BLOCKED | BLOCKED |

Claude Code loaded the installed project skill. A fresh Codex session evaluated the same installed skill by explicit file path. Both used the same synthetic fixtures. Neither issued an approval, dispatched work, or updated the portfolio.

A later [native Codex loading test](../../qa-skill-pilot/results/NATIVE-CODEX-RESULTS.md) verified discovery and dollar-name invocation through a local request capture. A signed-in model response through that invocation remains unverified.
