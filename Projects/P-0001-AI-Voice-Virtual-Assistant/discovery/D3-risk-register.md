# D3 — Risk Register
# P-0001 AI Voice Virtual Assistant

| Field | Value |
|---|---|
| **Project** | P-0001 AI Voice Virtual Assistant |
| **Document ID** | D3 |
| **Owner** | PM (compiled from D1, D2, D4) |
| **Governing assignment** | DA-0003 |
| **Source documents** | D1 v1.0, D2 v1.1, D4 v1.0, PROTOTYPE-LOG.md |
| **Revision** | v1.0 |
| **Date** | 2026-11-21 |
| **Status** | Draft — awaiting PM review |

---

## Risk scoring

**Likelihood:** 1 Low · 2 Medium · 3 High  
**Impact:** 1 Low · 2 Medium · 3 High  
**Score = Likelihood × Impact**

| Score | Priority |
|---|---|
| 7–9 | P1 — Blocking |
| 4–6 | P2 — Mitigate before build |
| 1–3 | P3 — Monitor |

---

## Risk register

| ID | Risk | Source | Likelihood | Impact | Score | Priority | State | Mitigation / Owner |
|---|---|---|---|---|---|---|---|---|
| RSK-001 | **LLM confirmation gate not reliable at prompt level alone** — small local models (8B) call `book_appointment` on ambiguous replies | PROTOTYPE-LOG F-001 | 3 | 3 | 9 | **P1** | Mitigated — R-001 (DEC-0007): server-side keyword gate mandatory at build | Architect at build |
| RSK-002 | **Web Speech API sends voice to Google** — customer audio processed by third party under Google's terms | D4 SEC-004 / GAP-001 | 3 | 2 | 6 | **P2** | Accepted for prototype (DEC-0009); tenant privacy policy must disclose; evaluate Workers AI audio at build | CEO / Tenant operator |
| RSK-003 | **Cloudflare Vectorize overage behaviour unconfirmed** — not verified as hard stop vs charge | D2 GAP-002 | 2 | 3 | 6 | **P2** | Verify from official Cloudflare Vectorize terms before build approval | Deployment Engineer |
| RSK-004 | **Groq model catalog changed** — `llama-3.3-70b-versatile` no longer listed; model IDs may change again | PROTOTYPE-LOG (SaaS) | 2 | 2 | 4 | **P2** | Re-confirm model ID from live Groq console at build; do not hardcode model name | Architect at build |
| RSK-005 | **Groq rate limits unconfirmed** — free tier exact per-model limits not verified from console | D2 GAP-003 | 2 | 2 | 4 | **P2** | Confirm from Groq console at account setup; design prompts to minimise tokens-per-turn | Architect at build |
| RSK-006 | **Tenant config absent or misconfigured** — Worker could fail silently and serve wrong tenant data | D4 SEC-001 | 2 | 3 | 6 | **P2** | SEC-001: hard error required; no silent fallback; validate on every request | Architect at build |
| RSK-007 | **Cross-tenant booking write** — slot ownership not verified before `book_appointment` write | D4 SEC-002 | 1 | 3 | 3 | **P3** | SEC-002: Worker verifies slot's tenant ID before every write | Architect at build |
| RSK-008 | **Tool approval flag cached** — approval checked at session start only; flag change mid-session not enforced | D4 SEC-003 | 2 | 2 | 4 | **P2** | SEC-003: re-check D1 approval flag on every tool call | Architect at build |
| RSK-009 | **Duplicate booking on retry** — model retries `book_appointment` without re-checking slot | D1 §4 / D4 SEC-006 | 2 | 2 | 4 | **P2** | Idempotency key + slot re-check before every write (D1 §4) | Architect at build |
| RSK-010 | **8 GB RAM headroom** — 5.7 GB estimated; heavy browser use or OS updates could exhaust headroom | D2 §4 | 2 | 1 | 2 | **P3** | Monitor RAM during development; close non-essential browser tabs; fallback to Llama 3.2 3B (~2.0 GB) | Architect (dev) |
| RSK-011 | **Workers AI embedding daily limits unconfirmed** | D2 GAP-004 | 2 | 2 | 4 | **P2** | Verify from Cloudflare Workers AI docs; fallback to pre-computed embeddings at deploy time | Architect at build |
| RSK-012 | **Firefox support limited** — Web Speech API unreliable on Firefox; Chrome required | D2 GAP-007 | 3 | 1 | 3 | **P3** | Document Chrome requirement; not a build blocker | PM |
| RSK-013 | **Human handoff mechanism** — HUMAN_HANDOFF state implementation defined | D1 OQ-005 | — | — | — | **Resolved** | DEC-0010: VA collects customer email and phone; flags to tenant PM for follow-up | PM / CEO |
| RSK-014 | **CONFIRMATION_REPEAT ambiguity** — unclear if double confirmation (repeat slot + second yes) is required | D1 OQ-001 | 1 | 2 | 2 | **P3** | PM to clarify before story writing; default assumed: single explicit yes after slot offer | PM |
| RSK-015 | **Cloudflare Workers 100K req/day** — multi-tenant concurrent demo could hit limit | D2 GAP-006 | 1 | 2 | 2 | **P3** | Monitor during demo; acceptable at AUD 0 for discovery and early build | PM at build |
| RSK-016 | **Raw JSON leak in LLM text responses** — model serialises tool call as text after failure (observed in prototype S3) | PROTOTYPE-LOG F-002 | 2 | 1 | 2 | **P3** | R-002: Worker strips raw JSON from assistant text before TTS (regex filter) | Architect at build |
| RSK-017 | **RAG chunk relevance threshold undefined** — no minimum score set; irrelevant chunks could be returned | D1 OQ-003 | 2 | 2 | 4 | **P2** | Define threshold at build; default to cosine similarity ≥ 0.75 — **[Assumed]** | Architect at build |
| RSK-018 | **Meta WhatsApp Business account approval** — Meta must approve the account; can take 1–2 days or be rejected | D2 GAP-009 | 2 | 2 | 4 | **P2** | Apply for Meta Business account early in build phase; have a test number as backup | Deployment Engineer at build |
| RSK-019 | **Groq Whisper language detection accuracy** — accented speech, mixed-language input, or short utterances may return wrong language | DEC-0012 | 2 | 2 | 4 | **P2** | Test across target languages during build; add fallback: if detected language changes mid-session, re-confirm with customer before switching | Architect at build |
| RSK-020 | **WhatsApp API policy change** — Meta can change Cloud API pricing or availability; free tier not guaranteed long-term | DEC-0011 | 1 | 3 | 3 | **P3** | Monitor Meta developer announcements; Twilio phase provides alternative channel | PM |
| RSK-021 | **Customer expectation mismatch** — customer sends voice note, receives text reply; may expect voice back | D2 GAP-010 | 2 | 2 | 4 | **P2** | VA introduction message should clarify it replies via text in phase 1; manage expectation explicitly | PM at build |

---

## P1 risks summary (blocking — must resolve before build approval)

| ID | Risk | Resolution |
|---|---|---|
| RSK-001 | LLM confirmation gate unreliable at prompt level | R-001 server-side gate approved (DEC-0007) — implement at build |

---

## P2 risks summary (mitigate before build)

RSK-002, RSK-003, RSK-004, RSK-005, RSK-006, RSK-008, RSK-009, RSK-011, RSK-017, RSK-018, RSK-019, RSK-021

RSK-013 resolved (DEC-0010). All remaining P2 items are build-stage technical verifications.

---

## Decisions still required from CEO / PM

| Risk | Decision needed | Owner | Status |
|---|---|---|---|
| RSK-013 | ~~Human handoff mechanism~~ | CEO / PM | **Resolved — DEC-0010** |

No open CEO/PM decisions remain. Build may proceed upon charter approval.

---

*Deliverable complete. Routed to PM for review.*
