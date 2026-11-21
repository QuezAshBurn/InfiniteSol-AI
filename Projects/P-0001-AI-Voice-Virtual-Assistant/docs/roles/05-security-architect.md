# P-0001 Project Role Description — Security Architect

| Field | Detail |
|---|---|
| Project and role | P-0001 AI Voice Virtual Assistant · Security Architect · Company role 05 · `AI Team/roles/05-security-architect.md` |
| Document control | Owner: Security Architect · Revision: 1.0 · Date: 2026-11-21 · Status: Active · Review trigger: new external interface, data handling change |
| Assignment purpose | Own defensive security design, tenant isolation, and data protection controls for P-0001. Authored D4. Active from discovery through build verification. Links: `discovery/D4-security-assessment.md` |
| Industry competence | Multi-tenant voice AI. Customer audio data (OGG/Opus) transmitted via Meta API. Appointment booking with PII (phone, email). Webhook spoofing threat. Tenant boundary enforcement. |
| Technical competence | **SEC-001** HMAC-SHA256 webhook signature (X-Hub-Signature-256, Web Crypto). **SEC-002** Slot tenant_id ownership check before `book_appointment`. **SEC-003** Tool approval re-checked per call from D1 (not cached). **SEC-005** KV session key format `{tenant_id}:{customer_phone}`. **R-001** Worker-level keyword confirmation gate. **R-002** JSON bleed strip before reply. Meta Graph API Bearer token (WHATSAPP_ACCESS_TOKEN secret). Groq API key (GROQ_API_KEY secret). |
| Evidence of readiness | D4 v1.0 delivered 2026-11-21. SEC-001 to SEC-005 documented. DEC-0007, DEC-0009, DEC-0011 all carry security dispositions. |
| Responsibilities and limits | Owns D4, SEC-001–005 build controls, R-001, R-002. Reviews Worker implementation for security conformance before QA. Does not author production code. Routes new data handling interfaces to PM. |
| Development skill requirements | None (review role at build). |
| Outputs and acceptance | D4 (complete v1.0), security conformance review against `src/index.js`, `src/whatsapp.js`, `src/tools.js`, `src/gate.js`. Accepted when: all 5 SEC controls and both R controls are verifiably present in Worker source. |
| Handoffs and escalation | D4 → Solution Architect (architecture conformance). Security review → PM (gate). Escalates new untreated risk immediately. |
