# Memory prototype QA handoff

**Task** MEM-PILOT-A1-M1. **Authorization** [approved memory scope](../MEMORY-FIRST-AUTHORIZATION.md), SHA-256 `eedae610c9ce2a4588663be82b63d88ab4c84770aae6c9c316a00a046cc1e0fd`.

The PM recorded and dispatched the approved memory assignment at approximately 13:37:17 AWST, 20 November 2026, when the authorization file was created. The two-hour verification window ends at 15:37:17 AWST or on scope change or closure.

**Candidate** `fcb3cd28ffca8046a01d47f66eece989a924ad13da7900d4d99ec29722fb8a60`. It supersedes the initial candidate after checks for missing grants and conflicting approval links were added. [Candidate file manifest](CANDIDATE.json), [developer checks](DEVELOPER-TESTS.txt), and [demo output](DEMO-RESULTS.json).

Development author is the parent Codex session. The separate Claude Code session owns counterpart review of the supplied code. The fresh `memory_qa` Codex session owns independent local verification. The PM supplied QA skill v0.1.0, manifest `c49f21a72c13bfcb5d8197a44ee362ec848d6abdd9771a6c1572121faf72ad7f` and source pack `6278e4f6664daa97`.

Verify the exact files, rerun the candidate tests and compare the active tenant and invariant results with their Markdown and approval evidence. Confirm failures close the affected lookup without substituting the default. The walkthrough uses synthetic fixture dates and the assigned local scope.
