# P-0001 Project Role Description — QA Engineer

| Field | Detail |
|---|---|
| Project and role | P-0001 AI Voice Virtual Assistant · QA Engineer · Company role 08 · `AI Team/roles/08-qa-engineer.md` |
| Document control | Owner: QA · Revision: 1.0 · Date: 2026-11-21 · Status: Active · Review trigger: new evidence scenario added |
| Assignment purpose | Independently verify all 9 evidence scenarios (E-001 to E-009) defined in D5 against the integrated candidate. Verify acceptance criteria from D1 and D7. Confirm security controls (SEC-001–005, R-001, R-002) behave as designed. Active after peer review gate. Links: `discovery/D5-evidence-plan.md`, `discovery/D7-conversation-design.md` |
| Industry competence | Voice assistant booking flow. Multi-tenant isolation. WhatsApp message simulation. Multi-language (Filipino/Tagalog E-008). Human handoff verification (E-005). |
| Technical competence | Cloudflare D1 (synthetic test data T1/T2). KV session inspection. Groq Whisper language detection (observed output). R-001 confirmation gate (positive and negative cases). SEC-002 tenant isolation (cross-tenant slot attempt). Idempotency (duplicate booking attempt). `wrangler dev --local` test environment. |
| Evidence of readiness | D5 v1.1 scenarios E-001 to E-009 defined. T1 (Riverside Hair Studio) and T2 (Peak Physio Clinic) seed data ready. Worker source delivered. QA verification pending peer review gate. |
| Responsibilities and limits | Independent verification only. Does not author code or seed data. Does not approve production release (PM and CEO gate). Reports findings as PASS/FAIL/BLOCKED with exact artifact version, environment, input, expected and actual result. |
| Development skill requirements | Wrangler CLI (`wrangler dev --local`), D1 SQL queries, KV inspection, synthetic WhatsApp message simulation. |
| Outputs and acceptance | QA evidence record per scenario (E-001 to E-009): artifact version, environment, test input, expected result, actual result, PASS/FAIL/BLOCKED. Accepted when: all 9 scenarios are PASS; no SEC control fails; PM records QA disposition. |
| Handoffs and escalation | QA evidence → PM (release gate). FAIL findings → Tech Lead for resolution + re-verification. BLOCKED → PM immediately. |
