# P-0001 Project Role Description — Senior Full Stack Developer A (Author)

| Field | Detail |
|---|---|
| Project and role | P-0001 AI Voice Virtual Assistant · Senior Full Stack Developer A · Company role 06 · `AI Team/roles/06-senior-full-stack-developer-a.md` |
| Document control | Owner: Dev A · Revision: 1.0 · Date: 2026-11-21 · Status: Active · Review trigger: build scope change |
| Assignment purpose | Author the Cloudflare Worker source code for P-0001. Work within approved architecture (D2), security controls (D4), and Tech Lead guidance. Senior Dev B provides independent peer review of all authored code. Active during build. |
| Industry competence | Multi-tenant voice assistant. Appointment booking with confirmation gate. WhatsApp webhook event handling. Async message processing (not real-time). |
| Technical competence | **Cloudflare Workers** ES modules, `fetch`, Web Crypto API. **D1** `prepare().bind().first()`, `.all()`, `.batch()`, idempotency. **KV** `get`, `put` with TTL. **Groq Whisper** `multipart/form-data`, `verbose_json`. **Groq LLM** chat completions, tool calls, `tool_call_id`. **Meta WhatsApp Cloud API** v18.0 webhook GET/POST, media download, messages endpoint. **gate.js** R-001/R-002 patterns. `wrangler.toml` bindings. No bundler (native ES modules). |
| Evidence of readiness | Worker source authored 2026-11-21: `index.js`, `llm.js`, `tools.js`, `whatsapp.js`, `gate.js`. `wrangler.toml`, `package.json` authored 2026-11-21. |
| Responsibilities and limits | Authors Worker source. Owns developer-level checks (self-testing against schema, manual trace of normal and failure paths). Does not deploy to production. Does not review own code. Routes architecture boundary decisions to Tech Lead. |
| Development skill requirements | Cloudflare Workers, D1, KV, Groq APIs, Meta WhatsApp Business Cloud API, ES modules. |
| Outputs and acceptance | `build/worker/src/` (5 files), `wrangler.toml`, `package.json`. Accepted when: Dev B peer review is complete with no open critical or high findings; Tech Lead conformance record confirms D2/D4 alignment. |
| Handoffs and escalation | Authored source + test evidence → Dev B (peer review). Deviation from D2/D4 → Tech Lead. Build blockers → PM. |
