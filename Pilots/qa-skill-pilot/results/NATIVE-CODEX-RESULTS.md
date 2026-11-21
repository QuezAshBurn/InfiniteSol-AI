# Native Codex skill loading | 20 November 2026

The installed Codex CLI 0.154.0 was tested with a writable diagnostic profile and its native app-server. No account credentials were copied into that profile.

| Project skill | Native catalog | Explicit skill selection | Plain prompt containing the dollar-prefixed skill name |
|---|---|---|---|
| `qa-verify` v0.1.0 | PASS | PASS | PASS |
| `task-intake` v0.1.0 | PASS | PASS | PASS |

For discovery, the app-server returned the exact `.agents/skills/<name>/SKILL.md` path in the relevant pilot workspace. For selection and dollar-name invocation, distinct text from the body of the installed skill was present in the assembled model request. The request went only to the temporary Windows loopback test listener. The listener stopped the test after capturing the request, so no hosted model answered that invocation.

The default signed-in Codex profile remains restricted in this Windows execution session. Native skill loading is verified. An authenticated model response through the native invocation path still needs a smoke test. Prior fresh Codex file-path evaluations and direct Claude Code runs cover skill behaviour separately.
