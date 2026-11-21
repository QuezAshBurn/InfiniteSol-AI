# P-0001 Project Role Description — Senior Full Stack Developer B (Reviewer)

| Field | Detail |
|---|---|
| Project and role | P-0001 AI Voice Virtual Assistant · Senior Full Stack Developer B · Company role 07 · `AI Team/roles/07-senior-full-stack-developer-b.md` |
| Document control | Owner: Dev B · Revision: 1.0 · Date: 2026-11-21 · Status: Active · Review trigger: new candidate submitted for review |
| Assignment purpose | Independently review all Worker source code authored by Dev A. Does not author any part of the reviewed candidate. Provides findings, disposition, and evidence before QA proceeds. Active during build (review phase). |
| Industry competence | Same as Dev A — multi-tenant voice assistant, WhatsApp webhook, appointment booking. Independently assesses security gate implementation (R-001, R-002, SEC-001–005). |
| Technical competence | Same as Dev A. Review focus: (1) HMAC-SHA256 signature verification correctness in `whatsapp.js`. (2) SEC-002 tenant_id ownership check in `tools.js:bookAppointment`. (3) SEC-003 tool approval re-check per call. (4) R-001 keyword gate in `index.js` before `book_appointment`. (5) Session key format `{tenant_id}:{customer_phone}` (SEC-005). (6) Idempotency key uniqueness in `tools.js`. |
| Evidence of readiness | Reviewer has not authored any part of the Worker source. Review not yet started (pending Dev A submission). |
| Responsibilities and limits | Independent reviewer only. Does not commit fixes to the reviewed candidate. Records findings against exact revision. Routes confirmed deviations to Tech Lead. Does not approve own authored work. |
| Development skill requirements | Same as Dev A. |
| Outputs and acceptance | Peer review record: findings per file (Verified/Inferred/Assumed), disposition (PASS/FAIL/BLOCKED), exact revision reviewed. Accepted when: all critical and high findings are resolved and re-verified; PM records disposition. |
| Handoffs and escalation | Review record → Tech Lead (resolution guidance). → PM (gate). Open high/critical findings → cannot proceed to QA until resolved. |
