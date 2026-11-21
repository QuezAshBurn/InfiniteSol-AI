# D6 — Draft Project Charter
# P-0001 AI Voice Virtual Assistant

| Field | Value |
|---|---|
| **Project** | P-0001 AI Voice Virtual Assistant |
| **Document ID** | D6 |
| **Owner** | PM |
| **Governing assignment** | DA-0006 |
| **Source documents** | D1 v1.2, D2 v1.2, D3 v1.1, D4 v1.0, D5 v1.1 |
| **Revision** | v1.2 — updated pre-approval: WhatsApp channel (DEC-0011); multi-language (DEC-0012) |
| **Date** | 2026-11-21 |
| **Status** | AWAITING CEO BUILD APPROVAL |

---

## 1. Project purpose

Build a multi-tenant voice assistant that helps customers schedule appointments with businesses. The assistant must be hospitable, respectful, and jolly in tone; calm and helpful when customers are frustrated. It must operate at AUD 0 across all stages — development, deployment, and operation — using free-tier hosted services and open-source components.

---

## 2. Outcomes

| # | Outcome | Evidence scenario |
|---|---|---|
| 1 | Customer can book an appointment by voice in five turns or fewer | E-001 |
| 2 | Booking is only confirmed after explicit customer confirmation and tool success — no premature bookings | E-002, E-003 |
| 3 | Each tenant's data is fully isolated — no cross-tenant leakage | E-004 |
| 4 | Assistant answers tenant-specific questions from approved knowledge sources only | E-005 |
| 5 | Tool execution is gated by tenant approval flags — unapproved tools cannot be called | E-006 |
| 6 | Duplicate bookings are prevented under retry and concurrent access | D1 §4 |
| 7 | VA introduces itself with tenant-configured name and company before presenting the main menu | D1 §1 INTRODUCTION |
| 8 | Customer can reach booking, slot suggestion, services info, or other services from the main menu without navigating blind | D1 §1 MENU_PROMPT |

---

## 3. Scope

### In scope

- VA introduction: "Hi, this is [VA Name] from [Company], your Voice Assistant, how can I help you?" — VA Name and Company set in tenant configuration
- Main menu: four options in caller-logical order — (1) book an appointment, (2) find the next available time, (3) learn about our services, (4) other enquiries
- Voice booking flow: introduction → menu → greeting, clarification, availability check, slot offer, confirmation, booking, failure handling, human handoff
- Human handoff: VA collects customer's email and phone number; flags to tenant's product manager for follow-up (DEC-0010)
- Booking failure recovery: VA automatically finds and offers the nearest available slot on `book_appointment` failure — no customer prompt needed
- Multi-tenant isolation: per-tenant knowledge sources, tool approval flags, calendar isolation
- Tenant-specific RAG: approved knowledge sources, source/revision references
- MCP tool stubs: `check_availability` and `book_appointment` with approval gating and R-001 confirmation gate
- Two synthetic tenants (T1 Riverside Hair Studio, T2 Peak Physio Clinic) for build and evidence
- SaaS deployment: Cloudflare (Pages, Workers, D1, KV, Vectorize, Workers AI) + Groq free tier
- Local development track: Ollama + FastAPI + Chroma + SQLite (8 GB constraint)
- Voice channel: WhatsApp Business Cloud API (Meta free tier) — customer sends voice note; Worker transcribes via Groq Whisper; VA replies as WhatsApp text message (DEC-0011)
- Multi-language: Groq Whisper auto-detects language; VA responds in the same language; all dialogue states support any language Whisper can detect (DEC-0012)
- Phase 2 (planned, separate CEO budget decision): Twilio live voice calls + audio TTS response in customer's language

### Out of scope

- Payment processing
- Real customer data
- Native mobile app
- ~~Multi-language support~~ — moved to in-scope (DEC-0012)
- Production operations beyond the free-tier demo

---

## 4. Architecture summary

**Primary track (SaaS):** Cloudflare Workers (webhook) + D1 + KV + Vectorize + Workers AI embeddings + Groq LLM (`openai/gpt-oss-120b`) + Groq Whisper (STT) + WhatsApp Business Cloud API (Meta free tier)

**Phase 2 (future, separate budget):** + Twilio Voice (live call, real-time STT/TTS in customer language)

**Fallback track (local 8 GB):** Ollama + Phi-3.5-mini Q4_K_M + FastAPI + Chroma + SQLite + sentence-transformers/all-MiniLM-L6-v2 + Browser Web Speech API

Full detail in D2 v1.1.

---

## 5. Key decisions carried into build

| Decision | ID | Summary |
|---|---|---|
| AUD 0 budget — all stages | DEC-0001 | No spend at any stage without separate CEO approval |
| 8 GB RAM constraint | DEC-0003 | Architecture must fit; local track verified FEASIBLE at ~5.7 GB |
| SaaS-first | DEC-0006 | Cloudflare + Groq primary; local-only fallback |
| R-001 confirmation gate | DEC-0007 | Worker-level keyword check mandatory before `book_appointment` |
| Groq + Cloudflare accounts | DEC-0008 | Created 2026-11-21; free tier; AUD 0 satisfied |
| Web Speech API accepted for prototype | DEC-0009 | Tenant privacy policy must disclose before production |
| VA introduction and menu options added to scope | DEC-0010 | VA intro phrasing confirmed; suggest-schedule = find next available slot unprompted; human handoff = collect email and phone, flag to tenant PM |
| WhatsApp channel — replaces browser Web Speech API | DEC-0011 | Phase 1: WhatsApp voice notes → Groq Whisper STT → LLM → WhatsApp text reply. Phase 2 (Twilio, separate budget): live voice call. DEC-0009 superseded. |
| Multi-language support added to scope | DEC-0012 | Groq Whisper auto-detects language; LLM responds in same language; audio TTS response in customer language deferred to Twilio phase |

---

## 6. Build-stage verification required

These items must be confirmed before build approval is considered complete:

| Item | Owner | Blocking? |
|---|---|---|
| Cloudflare Vectorize overage is a hard stop, not a charge | Deployment Engineer | Yes |
| Groq free tier rate limits from console | Architect | Yes |
| Workers AI embedding daily limits | Architect | Yes |
| Groq model ID confirmed from live catalog | Architect | Yes |
| Meta WhatsApp Business account approved | Deployment Engineer | Yes |
| Groq Whisper language detection accuracy confirmed on target languages | Architect | Yes |
| Vectorize namespace physical isolation confirmed | Deployment Engineer | No |
| KV TTL enforcement at session end | Architect | No |

---

## 7. Build-stage controls required (from D4)

| Control | ID | Description |
|---|---|---|
| Hard error on absent tenant config | SEC-001 | No silent fallback; reject request if tenant unrecognised |
| Tenant ownership check on `book_appointment` | SEC-002 | Verify slot belongs to requesting tenant before write |
| Re-check tool approval flag per call | SEC-003 | No session-level caching of approval flags |
| KV key includes tenant ID prefix | SEC-005 | Format: `{tenant_id}:{session_id}` |
| R-001 keyword gate | DEC-0007 | Worker-level confirmation gate before `book_appointment` |
| R-002 JSON strip | — | Regex filter on assistant text before TTS |

---

## 8. Open question for PM before story writing

| ID | Question | Urgency | Status |
|---|---|---|---|
| OQ-005 | ~~Human handoff mechanism at AUD 0?~~ | — | **RESOLVED (DEC-0010):** VA collects customer email and phone; flags to tenant PM for follow-up |
| OQ-001 | Is CONFIRMATION_REPEAT (double confirmation) required? | Before booking flow stories are written | Open |

---

## 9. Risk summary

22 risks identified in D3 v1.1. One P1 (RSK-001) mitigated by DEC-0007. 13 P2 risks to be mitigated during build (RSK-013 resolved). Full register in D3 v1.1.

---

## 10. Timeline and budget

| Phase | Duration | Budget |
|---|---|---|
| Discovery | 5 business days (2026-11-21 to 2026-11-28) | AUD 0 |
| Build | To be scheduled after charter approval | AUD 0 — all free tiers |
| Operation | Ongoing | AUD 0 — Cloudflare + Groq free tiers |

**Hard ceiling:** AUD 0 at all stages. Any spend requires a separate CEO decision before it is incurred.

---

## 11. Team roles

| Role | Responsibility |
|---|---|
| CEO / Operator | Approves scope, budget, and decisions; first priority |
| Project Manager | Owns charter, risk register, delivery coordination |
| Solution Architect | D2 architecture, build design, prototype |
| Business Analyst | D1 requirements, D5 evidence plan, story writing |
| Security Architect | D4 assessment, build security controls |
| Deployment Engineer | Cloudflare setup, verification items |

---

## 12. Discovery sign-off

All six discovery deliverables are complete:

| Document | Version | Status |
|---|---|---|
| D1 — Requirements summary | v1.2 | Updated 2026-11-21; WhatsApp channel + multi-language (DEC-0011/DEC-0012) |
| D2 — Architecture brief | v1.2 | Updated 2026-11-21; WhatsApp architecture; Groq Whisper STT; multi-language flow |
| D3 — Risk register | v1.1 | Updated 2026-11-21; RSK-018–021 added; 22 risks total |
| D4 — Security assessment | v1.0 | Delivered 2026-11-21 — webhook signature verification added as build control |
| D5 — Evidence plan | v1.1 | Updated 2026-11-21; E-008 multi-language + E-009 WhatsApp channel added |
| D6 — Draft charter (this document) | v1.2 | Awaiting CEO approval |

All blocking CEO decisions resolved. No unresolved P1 risks. Build may commence upon CEO approval of this charter.

---

## 13. CEO build approval

> **PM recommendation:** Discovery is complete. All deliverables are in. All blocking decisions are recorded. The architecture is feasible at AUD 0. Prototype evidence (Groq 7/7, local 6/7 — gap mitigated) supports proceeding to build.
>
> **This charter requires CEO approval before build begins.**

| Field | Value |
|---|---|
| CEO approval | **APPROVED** |
| Date | 2026-11-21 |
| Revision approved | v1.2 |
