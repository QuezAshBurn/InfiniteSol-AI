Claude Code counterpart review in a separate session. The dispatch computed the file SHA-256 before submitting the text. Review receipt saved to the project record at 2026-11-20T03:08:48Z, verified from the initial evidence file creation time. Exact Claude execution time was not captured.

# Review: QA-TRIAL-001

**Verdict: APPROVE**, with the hash caveat below.

**SHA-256:** `82ccc50dce6aa1d22079ab3c8f5de50b925aef8ee2ebb21b0295ddd3552ca6ef`. This is the digest you stated. You asked for no tools, so I could not hash the text myself. I reviewed the text exactly as pasted, and this approval covers only the candidate that actually has that digest. Someone should confirm the hash of the stored file before recording this approval.

## Findings

**1. Stop on a wrong hash: met.**
Both blocks pass `$expected` to the verifier and throw if `$LASTEXITCODE -ne 0`. This relies on `verify_manifest.py` exiting non-zero when the hash does not match. Your two wrong-hash runs, where both blocks stopped, show that it does. If someone forgets to replace the placeholder, the verifier receives a non-hash value, which should fail the same way.

**2. Stop on a failed program invocation: met.**
- If `python` is not found, PowerShell raises a CommandNotFound error and `$?` becomes `$false`, so the block throws. This works even if `$LASTEXITCODE` holds an old 0 from an earlier command.
- If `python` resolves to the Windows Store alias, it exits with 9009, so the block throws.
- If the script path is missing, Python exits with 2, so the block throws.

The `-not $? -or` guard is what covers the stale `$LASTEXITCODE` case, so it should stay.

**3. QA and PM boundary: preserved.**
- QA records checks and evidence against the exact candidate.
- QA only *recommends* PASS, RETURN FOR CORRECTION, or BLOCKED.
- Only the PM records closure.

The phrase "after QA verifies the required outcome and approach" still leaves the closure decision with the PM, so it is consistent with the boundary.

## Non-blocking notes

- **Output capture:** "Save the verifier output" is a manual step, and neither command captures output. If you want this to be reliable, you could add `| Tee-Object` to each verifier command.
- **Working directory:** The relative `../qa-skill-pilot/...` paths only work if PowerShell is opened in the trial folder, as the first line instructs. If it isn't, the path fails and the block stops safely rather than giving a false pass.
- **Error message:** When Python is missing, the throw message still says the skill "did not verify," which is a little vague. The behaviour is still correct because the block stops.
