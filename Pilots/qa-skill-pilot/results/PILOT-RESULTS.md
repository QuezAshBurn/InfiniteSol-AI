# QA skill pilot results

The project-scoped qa-verify skill version 0.1.0 was built from the approved InfiniteSol v1.8 prompt pack. Source pack fingerprint 6278e4f6664daa97. Manifest SHA-256 c49f21a72c13bfcb5d8197a44ee362ec848d6abdd9771a6c1572121faf72ad7f.

The master skill and both installed copies matched the manifest. The verifier rejected an incorrect expected hash.

| Scenario | Expected verdict | Codex | Claude Code |
|---|---|---|---|
| Clean evidence | PASS | PASS | PASS |
| QA regression after developer tests pass | RETURN FOR CORRECTION | RETURN FOR CORRECTION | RETURN FOR CORRECTION |
| Required step skipped | RETURN FOR CORRECTION | RETURN FOR CORRECTION | RETURN FOR CORRECTION |
| Candidate changed after approval | BLOCKED | BLOCKED | BLOCKED |
| Approval expired | BLOCKED | BLOCKED | BLOCKED |

Both runtimes matched all five frozen expected outcomes. See [the Codex evaluation](codex-forward-test.txt) and [the Claude Code evaluation](claude-code.txt). Claude Code loaded the project skill. Codex evaluated the installed file in a fresh session by explicit file path after two native CLI launch attempts returned Windows access denied. A later [native Codex loading test](NATIVE-CODEX-RESULTS.md) verified discovery and dollar-name invocation through a local request capture. A signed-in model response through that invocation remains unverified.

The fixtures are synthetic and their results cannot establish project QA or close a story. The separate [internal documentation trial](../../qa-skill-trial/CLOSURE.md) used real candidate evidence and was closed after independent QA.
