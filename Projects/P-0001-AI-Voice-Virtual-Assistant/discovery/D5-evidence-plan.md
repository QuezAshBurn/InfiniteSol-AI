# D5 — Discovery Evidence Plan
# P-0001 AI Voice Virtual Assistant

| Field | Value |
|---|---|
| **Project** | P-0001 AI Voice Virtual Assistant |
| **Document ID** | D5 |
| **Owner** | Business Analyst (Role 02) |
| **Governing assignment** | DA-0005 |
| **Source documents** | D1 v1.0, D2 v1.1 |
| **Decisions applied** | DEC-0006 (SaaS-first), DEC-0007 (R-001), DEC-0009 (Web Speech API accepted) |
| **Revision** | v1.0 |
| **Date** | 2026-11-21 |
| **Status** | Draft — awaiting PM review |

---

## 1. Purpose

This plan defines the evidence required to close discovery and approve the build phase. Evidence demonstrates that the proposed architecture and requirements are sufficient to deliver the stated outcomes. All evidence uses synthetic data only.

---

## 2. Synthetic tenants

Two tenants are used for all evidence scenarios.

| Tenant | Name (synthetic) | Service type | Knowledge sources |
|---|---|---|---|
| T1 | Riverside Hair Studio | Hair salon — haircuts, colour, blowouts | Service menu, pricing, operating hours, FAQ |
| T2 | Peak Physio Clinic | Physiotherapy — initial assessment, follow-up, sports rehab | Service descriptions, appointment types, referral policy, FAQ |

Tenant isolation is evidenced by running scenarios across both tenants in the same session and verifying that T1 data never appears in T2 responses and vice versa.

---

## 3. Evidence scenarios

### E-001 — Happy path booking (T1)

**Demonstrates:** GREETING → AVAILABILITY_CHECK → SLOT_OFFER → BOOKING_SUCCESS; "you're booked" only after tool success.

| Step | Input | Expected output |
|---|---|---|
| 1 | "I'd like a haircut next Friday afternoon" | Assistant checks availability, offers a slot with date, time, service |
| 2 | "Yes, book it" | Assistant calls `book_appointment`; says "you're booked" with booking reference |

**Pass condition:** `book_appointment` called after explicit yes; "you're booked" (or equivalent) only after `{"status": "success"}`.

---

### E-002 — Ambiguous confirmation gate (T1)

**Demonstrates:** R-001 server-side gate holds; `book_appointment` not called on ambiguous reply.

| Step | Input | Expected output |
|---|---|---|
| 1 | "I'd like a colour appointment next Tuesday" | Assistant offers slot |
| 2 | "What time is that?" | Assistant re-states slot; asks again — does NOT call `book_appointment` |
| 3 | "Yes, go ahead" | Assistant calls `book_appointment`; confirms booking |

**Pass condition:** `book_appointment` NOT called on step 2; called on step 3 only.

---

### E-003 — Booking failure and recovery (T1)

**Demonstrates:** BOOKING_FAILURE state; no "you're booked" on failure; graceful retry.

| Step | Input | Expected output |
|---|---|---|
| 1 | "Book a blowout for Saturday morning" | Assistant offers slot |
| 2 | "Yes" | `book_appointment` returns `{"status": "failed"}`; assistant apologises, does NOT say "you're booked"; offers retry or handoff |

**Pass condition:** "you're booked" not in response after failure.

---

### E-004 — Tenant isolation (T1 and T2 in same session)

**Demonstrates:** T1 assistant has no knowledge of T2 services and vice versa.

| Step | Tenant | Input | Expected output |
|---|---|---|---|
| 1 | T1 | "Do you offer physio?" | "I don't have information about that" (or similar); no T2 data visible |
| 2 | T2 | "Do you do haircuts?" | "I don't have information about that" (or similar); no T1 data visible |
| 3 | T2 | "Book an initial assessment" | Correctly books against T2's calendar, not T1's |

**Pass condition:** No cross-tenant data visible; bookings written to correct tenant's calendar only.

---

### E-005 — RAG retrieval (T1)

**Demonstrates:** Assistant answers FAQ questions from T1's approved knowledge source; cites source.

| Step | Input | Expected output |
|---|---|---|
| 1 | "How long does a colour appointment take?" | Answer sourced from T1 service menu (e.g. "About 2 hours"); source reference available if challenged |
| 2 | "What are your Saturday hours?" | Answer sourced from T1 operating hours chunk |

**Pass condition:** Answer matches T1 knowledge source content; no hallucinated information.

---

### E-006 — Tool approval gating (T1)

**Demonstrates:** `book_appointment` not executed if approval flag is false in D1.

| Step | Setup | Input | Expected output |
|---|---|---|---|
| 1 | Set T1 `book_appointment` approval flag to false in D1 | "Book a haircut next Friday" | Assistant offers slot; on confirmation, Worker blocks tool; assistant says it cannot complete the booking and offers handoff |

**Pass condition:** `book_appointment` not executed; no booking written to calendar.

---

### E-007 — Frustrated customer (T2)

**Demonstrates:** Calm and helpful tone under customer frustration; no premature booking.

| Step | Input | Expected output |
|---|---|---|
| 1 | "This is ridiculous, I've been trying to book for a week, just book me in!" | Assistant acknowledges frustration calmly; asks for preferred date and service; does not rush to call `book_appointment` without slot confirmation |

**Pass condition:** Tone remains calm and helpful; `book_appointment` not called without a confirmed slot and explicit yes.

---

### E-008 — Multi-language booking (T1)

**Demonstrates:** Groq Whisper detects a non-English language; VA responds in the same language throughout.

| Step | Input | Expected output |
|---|---|---|
| 1 | Voice note in a non-English language (e.g. Filipino/Tagalog): "Gusto ko mag-book ng haircut" | Whisper transcribes correctly; VA responds in Filipino confirming it understood and asking for preferred date |
| 2 | Customer replies in Filipino with a date | VA checks availability and offers a slot — all in Filipino |
| 3 | Customer confirms | VA books and confirms — still in Filipino |

**Pass condition:** VA's full dialogue is in the customer's language from first message to booking confirmation.

---

### E-009 — WhatsApp voice note channel (T1)

**Demonstrates:** End-to-end flow through WhatsApp — voice note in, text reply out; session maintained across multiple messages.

| Step | Input | Expected output |
|---|---|---|
| 1 | Customer sends voice note via WhatsApp: "I'd like a haircut next Saturday" | Worker receives webhook; Whisper transcribes; VA replies via WhatsApp text with slot offer |
| 2 | Customer sends text "Yes, book it" | VA calls `book_appointment`; replies with booking confirmation as WhatsApp text message |

**Pass condition:** Full booking completes via WhatsApp; session state persists across separate webhook events; booking reference appears in final text reply.

---

## 4. Evidence collection method

| Scenario | Environment | Method | Output |
|---|---|---|---|
| E-001 to E-003 | SaaS (Groq + Cloudflare + WhatsApp) or local (Ollama + ngrok) | Run scenario via WhatsApp test number; capture webhook logs and tool call log | JSON transcript + pass/fail record |
| E-008 | SaaS (Groq Whisper + LLM) | Send voice note in target language; verify transcript and reply language | Language detection log + transcript |
| E-009 | SaaS (WhatsApp Business Cloud API + Cloudflare Worker) | Send voice note + text follow-up via WhatsApp test number; verify session persistence and booking completion | Webhook log + WhatsApp message thread |
| E-004 | SaaS or local | Run two-tenant isolation script; check RAG queries and calendar writes | Isolation verification log |
| E-005 | Local (seeded Chroma) | Seed T1 knowledge base; run RAG query; compare output to source | RAG retrieval log |
| E-006 | Local (SQLite flag) | Set flag to false; run booking scenario; verify tool blocked | Tool gate log |
| E-007 | Local or SaaS | Run scenario with frustrated-customer input; review transcript | Transcript review |

All scripts to be written at build stage. Discovery evidence is design-level only.

---

## 5. Acceptance criteria for discovery sign-off

All 7 scenarios must have a documented expected output and a defined pass condition. Actual execution occurs at build.

| Deliverable | Status |
|---|---|
| E-001 to E-009 scenarios defined | ✓ This document (E-008 multi-language; E-009 WhatsApp channel added DEC-0011/DEC-0012) |
| Synthetic tenant definitions (T1, T2) | ✓ This document |
| Evidence collection method per scenario | ✓ This document |
| Prototype scripts (actual execution) | At build |

---

*Deliverable complete. Routed to PM for review.*
