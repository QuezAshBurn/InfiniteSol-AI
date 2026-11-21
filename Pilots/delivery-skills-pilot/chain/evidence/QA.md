# Independent QA for DEL-001

**PASS.** A fresh Codex QA session verified candidate SHA-256 `6da0f6734829acf9c727fb44921f25aaf1b3c03eae3bac9d581e9c1478e96f93` at approximately 11:35–11:36 AWST on 20 November 2026. The session independently computed the digest from the ordered paths and file contents, and matched it to the frozen candidate and the separate Claude Code peer approval received at 11:34:55 AWST.

QA verified the approved S1 SHA-256 `cbd8c689e593aa70a00f33859c1f2efe48514b1dfeed663a69139774eaf0eff2` against the dispatch, verified the pre-change baseline and frozen diff, and confirmed the delivered paths match the scoped authorization. The installed `qa-verify` v0.1.0 manifest matched `c49f21a72c13bfcb5d8197a44ee362ec848d6abdd9771a6c1572121faf72ad7f` from source pack `6278e4f6664daa97`.

| Criterion | Observed result |
|---|---|
| AC-1 | Archived plus active pending counted as 1. All archived pending counted as 0. |
| AC-2 | Legacy pending counted as 1 on its own and alongside archived pending. |
| AC-3 | Other statuses, case and whitespace variants, and empty input counted as 0. |
| AC-4 | Input contents, record identities, order and the `(orders)` signature were preserved. All three original tests passed. |

- `python -B -m unittest discover -s tests -v` passed 8 of 8 candidate tests, exit 0.
- All three baseline tests passed independently. Running the eight candidate tests with the baseline helper in memory reproduced exactly the three archive-related failures.
- A further 20,440 in-memory cases passed across nine status variants, three supported archive modes and input lengths of zero through three. QA checked returned counts, deep equality and record identities in order.

The run was local and read-only. S1 covers records with a missing or Boolean archive flag. QA recommends the PM close the story for this candidate within the synthetic pilot.

Evidence: [approved story](../STORY.md), [authorization](../IMPLEMENTATION-AUTHORIZATION.md), [baseline](BASELINE.json), [frozen candidate](CANDIDATE.json), [diff](CANDIDATE.diff), [developer run](DEVELOPER-TESTS.txt), and [counterpart review](PEER-REVIEW.md).
