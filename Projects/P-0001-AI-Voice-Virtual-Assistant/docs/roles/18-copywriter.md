# P-0001 Project Role Description — Copywriter

| Field | Detail |
|---|---|
| Project and role | P-0001 AI Voice Virtual Assistant · Copywriter · Company role 18 · `AI Team/roles/18-copywriter.md` |
| Document control | Owner: Copywriter · Revision: 1.0 · Date: 2026-11-21 · Status: Active · Review trigger: dialogue scope change, new tenant |
| Assignment purpose | Own the exact words the VA says in every state and recovery path. Write lines that sound natural as WhatsApp text messages — short, warm, and clear. Draft the spoken-tone guide. Work from D7 (UX Designer's conversation design) and D1 (requirements). Deliverable feeds `llm.js` system prompt (tone section) and the LLM template strings. Links: `discovery/D7-conversation-design.md`, `discovery/D8-copy-deck.md` |
| Industry competence | Voice assistant dialogue for appointment booking. WhatsApp text channel (not audio TTS in phase 1 — customer reads text). Multilingual writing awareness (Groq LLM responds in detected customer language; Copywriter drafts English master copy; flags phrases requiring localisation care). Tenant-specific tone: Aria (Riverside Hair Studio — warm, stylish), Max (Peak Physio Clinic — professional, reassuring). |
| Technical competence | Understands that VA text replies are sent via Meta WhatsApp Cloud API and rendered as chat messages. Aware that system prompt in `llm.js` governs VA tone; copy deck informs that prompt. Aware of R-001 (confirmation required before booking is recorded) so confirmation wording must be unambiguous. Aware of R-002 (JSON stripped) — no copy should depend on structured output. |
| Evidence of readiness | D7 conversation design (in progress). DEC-0010 (intro, menu, handoff wording). DEC-0012 (multilingual). Copywriter output being produced in D8. |
| Responsibilities and limits | Owns D8 copy deck: all VA utterances per state, tone guide, multilingual notes, placement notes. Does not write code. Does not change booking logic. Routes wording that changes confirmed/unconfirmed meaning to UX Designer and BA. |
| Development skill requirements | None. |
| Outputs and acceptance | D8 `discovery/D8-copy-deck.md`: versioned copy per state, tone guide, multilingual guidance, placement handoff to `llm.js`. Accepted when: Tech Lead confirms master copy is reflected in LLM system prompt; UX Designer confirms no meaning drift from D7 state spec; QA confirms confirmation-state copy passes R-001 test. |
| Handoffs and escalation | D8 → Tech Lead (system prompt update). D8 → QA (wording review in evidence scenarios). Meaning changes → UX Designer + BA. |
