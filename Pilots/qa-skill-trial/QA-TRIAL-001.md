# QA-TRIAL-001 | Windows QA handoff guide

- **Approval:** Emerson's “proceed” in the 20 November 2026 InfiniteSol conversation following the QA pilot. Scope interpretation: select and test one low-risk internal documentation story. Authorize this story, its local execution and evidence, and read-only counterpart review. Approval is current for this trial and ends when it is completed or superseded.
- **Goal:** An InfiniteSol operator can verify either project-scoped QA skill copy and prepare a handoff from a Windows PowerShell terminal.
- **Scope:** `RUN-QA.md`, the trial records and read-only checks against the existing QA skill copies. The trial uses no customer data and incurs no new cash spend.
- **Required approach:** Use the existing QA skill verifier and manifest. Exercise the documented success command and demonstrate that a wrong expected hash blocks progression.
- **AC-1:** Both documented commands run from this trial directory and return the current skill version, source pack and expected manifest SHA-256 when given the independently verified hash.
- **AC-2:** A wrong expected hash fails with a nonzero exit. The guide tells the operator to stop on failure and record the exact candidate and QA evidence before closure.
- **AC-3:** The guide distinguishes author evidence from independent QA, preserves PM closure, and keeps tabletop results separate from project evidence.
- **Assignments:** Codex authors the document and its developer-equivalent checks. A separate Claude Code session reviews it. A fresh QA session independently checks the exact artifact through `qa-verify` after peer review. The PM records closure only after required evidence passes.
