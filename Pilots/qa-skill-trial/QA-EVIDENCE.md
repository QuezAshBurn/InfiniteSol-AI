# Independent QA evidence | QA-TRIAL-001

**PASS** for `RUN-QA.md`, SHA-256 `82ccc50dce6aa1d22079ab3c8f5de50b925aef8ee2ebb21b0295ddd3552ca6ef`.

A fresh Codex QA session followed the installed `qa-verify` skill by explicit path and independently verified its manifest. The independent execution window was 20 November 2026, 03:09–03:10 UTC. The candidate digest matched the developer and Claude Code counterpart evidence before and after testing. The review receipt was recorded at 03:08:48 UTC.

| Criterion | Independent evidence |
|---|---|
| AC-1 | Both exact documented commands, run independently from the trial directory in Windows PowerShell 5.1, exited 0 and returned `qa-verify` 0.1.0, source pack `6278e4f6664daa97`, and approved manifest SHA-256 `c49f21a72c13bfcb5d8197a44ee362ec848d6abdd9771a6c1572121faf72ad7f`. The files matched the manifest. |
| AC-2 | Both runs with an incorrect hash printed the mismatch, threw the copy-specific Stop error and exited 1. The guide directs operators to stop and record failure evidence against the exact candidate. |
| AC-3 | The guide distinguishes developer, peer and independent QA evidence. QA provides a recommendation and the PM owns closure. Synthetic results stay in the pilot folder. |

Only local read-only checks ran. No application or Production activity was in scope. Recommend closure to the PM.
