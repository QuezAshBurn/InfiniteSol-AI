# P-0001 Project Role Description — UX Designer

| Field | Detail |
|---|---|
| Project and role | P-0001 AI Voice Virtual Assistant · UX Designer · Company role 16 · `AI Team/roles/16-ux-designer.md` |
| Document control | Owner: UX Designer · Revision: 1.0 · Date: 2026-11-21 · Status: Active · Review trigger: dialogue scope change |
| Assignment purpose | Own the conversation design for the WhatsApp voice assistant. Specify turn-taking, clarification, confirmation, recovery, interruption, and human handoff behaviour. No visual surface exists in phase 1 (WhatsApp text channel). Deliverable feeds the Copywriter (D8) and the LLM system prompt (llm.js). Links: `discovery/D1-requirements.md`, `discovery/D7-conversation-design.md` |
| Industry competence | Conversational AI for appointment booking. WhatsApp messaging (async, not real-time voice). Multi-tenant persona (Aria/Riverside Hair Studio, Max/Peak Physio Clinic). Multi-language dialogue (Groq Whisper auto-detects; LLM responds in detected language). |
| Technical competence | Dialogue state machines (INTRODUCTION, MENU_PROMPT, SUGGEST_SCHEDULE, GREETING, RAG_RESPONSE, BOOKING_PENDING, BOOKING_SUCCESS, BOOKING_FAILURE → SLOT_OFFER, HUMAN_HANDOFF). Recovery design for: mishearing (voice note transcription errors), ambiguous intent, slot unavailable, booking failure, customer declines handoff. Turn-taking over async WhatsApp messages (no interruption; each reply is a complete turn). |
| Evidence of readiness | D1 v1.2 conversation state map reviewed. DEC-0010 (introduction, menu, handoff). DEC-0012 (multi-language). UX outputs being produced in D7. |
| Responsibilities and limits | Owns D7 conversation design. Does not write production code or copy (Copywriter owns exact words). Routes new states or recovery paths requiring architecture change to Solution Architect via PM. |
| Development skill requirements | None. |
| Outputs and acceptance | D7 `discovery/D7-conversation-design.md`: annotated state map, turn specification per state, recovery and handoff paths, persona spec, QA scenario hooks. Accepted when: Tech Lead confirms D7 state map is consistent with LLM system prompt design in `llm.js`; QA confirms each state has at least one testable pass condition. |
| Handoffs and escalation | D7 → Copywriter (exact words per state). D7 → Tech Lead (system prompt conformance). D7 → QA (scenario definition). Scope decisions → PM. |
