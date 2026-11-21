# Prepare a Windows QA handoff

Open Windows PowerShell in this trial folder. Obtain the expected manifest hash from the approved handoff and replace the placeholder below. For the current `qa-verify` pilot, run the verifier for the copy you intend to use.

```powershell
$expected = '<approved manifest SHA-256>'
python '../qa-skill-pilot/.agents/skills/qa-verify/scripts/verify_manifest.py' $expected
if (-not $? -or $LASTEXITCODE -ne 0) { throw 'Stop: the Codex QA skill did not verify.' }
```

```powershell
$expected = '<approved manifest SHA-256>'
python '../qa-skill-pilot/.claude/skills/qa-verify/scripts/verify_manifest.py' $expected
if (-not $? -or $LASTEXITCODE -ne 0) { throw 'Stop: the Claude Code QA skill did not verify.' }
```

Save the verifier output with the task handoff. If verification fails, record the error and stop the affected work. Include the approved Markdown, approval validity, exact candidate, developer checks, peer evidence where required, and assigned independent QA session. QA records checks and evidence against that candidate and recommends PASS, RETURN FOR CORRECTION, or BLOCKED. Only the PM records closure after QA verifies the required outcome and approach. Keep tabletop outputs in the pilot results folder and preserve them as synthetic evidence.
