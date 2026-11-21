# D1 — Requirements Summary
# P-0001 AI Voice Virtual Assistant

| Field | Value |
|---|---|
| **Project** | P-0001 AI Voice Virtual Assistant |
| **Document ID** | D1 |
| **Owner** | Business Analyst (Role 02) |
| **Governing assignment** | DA-0001 |
| **Decisions applied** | DEC-0001 through DEC-0012 |
| **Revision** | v1.2 |
| **Date** | 2026-11-21 |
| **Status** | Updated pre-charter approval — WhatsApp channel (DEC-0011); multi-language (DEC-0012) |

---

## 1. Booking flow dialogue states

The assistant progresses through the following named states. Each state may transition forward or loop back depending on customer input.

### State map

```
INTRODUCTION
  └─► MENU_PROMPT
        ├─► GREETING (book a schedule)
        │     └─► SERVICE_CLARIFICATION  (if service not stated)
        │     └─► DATE_CLARIFICATION     (if date/time not stated or ambiguous)
        │     └─► AVAILABILITY_CHECK     (check_availability tool call)
        │           ├─► SLOT_OFFER        (slot available)
        │           │     ├─► CONFIRMATION_REPEAT  (customer says yes)
        │           │     │     ├─► BOOKING_SUCCESS   (book_appointment returns success)
        │           │     │     └─► BOOKING_FAILURE   (book_appointment returns failed)
        │           │     │           ├─► SLOT_OFFER   (auto check_availability → nearest slot offered)
        │           │     │           └─► HUMAN_HANDOFF (no slot found)
        │           │     └─► DATE_CLARIFICATION   (customer says ambiguous or asks again)
        │           └─► UNAVAILABLE_SLOT  (no slot found)
        │                 └─► HUMAN_HANDOFF (customer requests, or no alternative)
        ├─► SLOT_OFFER (suggest a schedule — VA finds next available slot unprompted)
        ├─► RAG_RESPONSE (inform about services)
        └─► RAG_RESPONSE (other services)
```

### State definitions

| State | Entry condition | Required assistant action | Exit condition |
|---|---|---|---|
| **INTRODUCTION** | Conversation start (customer sends first WhatsApp message or voice note) | VA says: "Hi, this is [VA Name] from [Company], your Voice Assistant, how can I help you?" in the customer's detected language — VA Name and Company from tenant configuration | Customer responds |
| **MENU_PROMPT** | After INTRODUCTION, or when customer requests the main menu | VA offers four options in this order: (1) book an appointment, (2) find the next available time, (3) learn about our services, (4) other enquiries. Order is intentional: booking actions first (most callers have booking intent), information second, catch-all last. VA presents these conversationally — not as a robotic list unless the customer is confused. | Customer selects an option or states their need directly |
| **GREETING** | Customer selects "book a schedule" from MENU_PROMPT, or states a booking intent directly | Warm acknowledgement; invite the customer to describe what they need (service and time) | Customer speaks |
| **SERVICE_CLARIFICATION** | Service not identified from greeting | Ask what service they'd like | Customer names a service |
| **DATE_CLARIFICATION** | Date/time absent, ambiguous, or unresolvable | Ask for preferred date and time; accept natural language ("next Friday", "sometime Tuesday afternoon") | Customer provides a date hint |
| **AVAILABILITY_CHECK** | Service and date hint known | Call `check_availability`; do not offer a slot before the tool returns | Tool returns a result |
| **SLOT_OFFER** | `check_availability` returned an available slot | State date, time, and service clearly; ask if the customer would like to book | Customer responds |
| **CONFIRMATION_REPEAT** | Customer gave explicit confirmation ("yes", "confirm", "book it", "go ahead", "please", "sure", "do it") | Repeat date, time, and service back to the customer; ask once more to confirm before calling `book_appointment` — **[Assumed]** this double-confirmation is required by the original request ("repeat date/time/service for confirmation") | Customer gives final explicit yes |
| **SUGGEST_SCHEDULE** | Customer selects "suggest a schedule" from MENU_PROMPT | VA calls `check_availability` for the soonest available slot across all services (or a chosen service if stated); presents the next available slot with date, time, and service — no date prompt needed | Customer accepts, declines, or requests a different service |
| **BOOKING_SUCCESS** | `book_appointment` returned `{"status": "success"}` | Say "you're booked" (or equivalent); state booking reference if returned; offer to help with anything else | Conversation end or new request |
| **BOOKING_FAILURE** | `book_appointment` returned `{"status": "failed"}` | Apologise; do NOT say "you're booked"; immediately call `check_availability` to find the nearest available slot and offer it to the customer — do not make the customer ask. If no slot is found, offer human handoff. | Customer accepts new slot (→ CONFIRMATION_REPEAT) or requests handoff (→ HUMAN_HANDOFF) |
| **UNAVAILABLE_SLOT** | `check_availability` returned no available slot | Apologise; offer an alternative date or human handoff | Customer chooses alternative or handoff |
| **HUMAN_HANDOFF** | Customer explicitly requests a human, or the assistant cannot resolve the booking after two failed attempts — **[Assumed]** two-attempt limit | VA tells the customer it will follow up: collect the customer's email address and phone number; confirm it has been noted; say that the tenant's team will get back to them. Flag the interaction to the tenant's product manager (or designated contact) for follow-up. End the booking flow gracefully. | Conversation end |

### Edge cases

| Edge case | Required behaviour | Confidence |
|---|---|---|
| Ambiguous reply to slot offer ("what time?", "maybe", "I think so") | Re-offer the slot; do NOT call `book_appointment` | **Verified** (prototype S2, DEC-0007) |
| Customer changes service or date after SLOT_OFFER | Return to DATE_CLARIFICATION or SERVICE_CLARIFICATION; call `check_availability` again | **Inferred** |
| Customer says "cancel" or "never mind" mid-flow | Exit gracefully; do not call `book_appointment` | **Inferred** |
| Customer is frustrated or raises voice | Stay calm and helpful; do not rush to close the booking | **Verified** (original requirement) |
| `check_availability` returns no result or errors | Apologise; offer human handoff; do not retry silently | **Inferred** |
| `book_appointment` fails on retry (slot already taken) | Apologise; call `check_availability` again for a fresh slot | **Inferred** |
| Customer asks a non-booking question (FAQ, pricing, hours) | Answer from RAG context if available; return to booking flow after | **Inferred** |
| Customer skips MENU_PROMPT and states intent directly ("I want to book a haircut") | Accept intent directly; skip MENU_PROMPT and proceed to the appropriate state | **Inferred** |
| No available slot found during SUGGEST_SCHEDULE | Apologise; offer to check a specific service or date instead; offer human handoff | **Inferred** |
| Customer in HUMAN_HANDOFF declines to give email or phone | Acknowledge; say a team member can be reached via the tenant's contact details; end gracefully | **Inferred** |

### Multi-language behaviour (DEC-0012)

| Aspect | Requirement | Confidence |
|---|---|---|
| Language detection | Groq Whisper detects the customer's language from each voice note automatically | **Verified** (Whisper multilingual capability) |
| Response language | VA responds in the same language as the customer's input across all dialogue states | **Verified** (DEC-0012) |
| Language persistence | Detected language is stored in KV session state; VA maintains the same language for the full session unless the customer switches | **Inferred** |
| Language switch mid-session | If the customer switches language, Whisper will detect the new language on the next voice note; VA follows | **Inferred** |
| Unsupported language | If Whisper cannot detect a language or returns a low-confidence result, VA defaults to English and notes it cannot confirm the language | **Assumed** |
| Phase 1 limitation | VA responds as a text message (not audio). Text is in the detected language. Audio voice response in the customer's language is deferred to Phase 2 (Twilio). | **Verified** (DEC-0011) |

---

## 2. Tenant isolation model

### How tenant identity enters the system

Tenant identity is set by **trusted application configuration** at the Worker layer. It is NOT derived from user input, URL parameters, or customer-supplied data.

Mechanism (Inferred from DEC-0006 / D2):
- Each tenant deployment has a fixed configuration record in Cloudflare D1 identifying the tenant ID
- The Cloudflare Worker reads this configuration at request time before any retrieval or tool call
- No customer action can alter the tenant identity in a session

### Enforcement before retrieval and tool calls

| Check | When | How | Confidence |
|---|---|---|---|
| Tenant identity present | Before any RAG query | Worker reads tenant config from D1; if absent, request is rejected | **Inferred** |
| RAG query scoped to tenant | Before Vectorize query | Worker passes tenant namespace ID as a filter; queries outside the tenant namespace are not issued | **Inferred** |
| Tool approval flag per tenant | Before each tool execution | Worker checks the tenant's `tool_approvals` row in D1 for each tool name | **Inferred** |
| Tenant scope on booking write | Before `book_appointment` executes | Worker verifies the slot belongs to the requesting tenant's calendar before writing | **Inferred** |

### Absent or unrecognised tenant

If tenant identity is absent or cannot be resolved from configuration:
- The Worker returns an error response — **[Inferred]**
- No RAG query is issued — **[Inferred]**
- No tool is called — **[Inferred]**
- The customer receives a generic "unable to help right now" message — **[Assumed]**

> **Unknown:** Exact error response wording for unrecognised tenant. PM to decide at build.

---

## 3. RAG source model

### Per-tenant knowledge sources

Each tenant has an isolated set of approved knowledge sources — their service menu, pricing, FAQs, policies, and operating hours.

| Aspect | Requirement | Confidence |
|---|---|---|
| Source definition | Each tenant's approved sources are defined by the tenant operator (not by customers) | **Verified** (original requirement: "per-tenant approved knowledge sources") |
| Storage | Embeddings stored in a dedicated Vectorize namespace per tenant; source text and revision metadata stored in D1 | **Inferred** (from D2 architecture) |
| Isolation | Worker queries only the requesting tenant's namespace; cross-namespace queries are not issued | **Inferred** |
| Source reference | Each retrieved chunk carries a source ID and revision tag; the assistant may cite these if challenged | **Inferred** |
| Revision tracking | When a knowledge source is updated, the new revision is ingested and tagged; old revision chunks are retired or overwritten | **Inferred** |

### Clarification and handoff on missing or conflicting evidence

| Situation | Required behaviour | Confidence |
|---|---|---|
| No RAG result for a customer question | Assistant acknowledges it doesn't have that information; offers human handoff | **Inferred** |
| Conflicting results from multiple chunks | Assistant states the most recent source; flags uncertainty; offers human handoff if the customer presses | **Assumed** |
| Customer asks about another tenant's services | Assistant cannot see another tenant's data; responds only from its own context | **Verified** (isolation model) |

> **Unknown:** Minimum chunk relevance threshold before a result is used. To be decided at build.

---

## 4. Tool approval and retry model

### When tools are permitted to execute

| Tool | Permitted when | Confidence |
|---|---|---|
| `check_availability` | Tenant identity confirmed + tool approval flag is true in D1 | **Inferred** |
| `book_appointment` | All `check_availability` conditions met + customer has given explicit confirmation in their most recent utterance (server-side keyword gate, R-001, DEC-0007) | **Verified** (DEC-0007, prototype) |

### Approval and tenant scope verification

On every tool call, the Worker verifies:
1. Tenant identity is present and matches the session — **[Inferred]**
2. The tool is in the tenant's approved tool list in D1 — **[Inferred]**
3. For `book_appointment`: the slot was returned by this tenant's `check_availability` in this session — **[Inferred]**

If any check fails, the tool is not executed and the assistant informs the customer it cannot proceed.

### Customer confirmation before calendar change

The confirmation gate is enforced at two levels (DEC-0007):

1. **LLM level (prompt):** System prompt instructs the model to wait for explicit confirmation before calling `book_appointment`
2. **Server level (R-001):** The Worker independently checks the customer's last utterance for explicit confirmation keywords before forwarding `book_appointment` to the calendar service. If keywords are absent, the Worker returns `{"error": "awaiting_confirmation"}` to the LLM, forcing it to re-ask.

Explicit confirmation keywords: "yes", "confirm", "book it", "go ahead", "please", "sure", "do it" — **[Inferred]** list; to be finalised at build.

### Duplicate prevention

| Mechanism | Description | Confidence |
|---|---|---|
| Slot re-check | Worker calls `check_availability` immediately before writing the booking, even if it was checked moments earlier | **Inferred** |
| Booking ID check | Before writing, Worker checks D1 for an existing booking with the same tenant + customer + slot combination | **Inferred** |
| Idempotency key | Each booking attempt carries a session-scoped key; a second call with the same key within the session is a no-op | **Assumed** |

### Retry behaviour

| Failure scenario | Retry permitted | Duplicate risk | Required behaviour |
|---|---|---|---|
| `book_appointment` returns `{"status": "failed"}` | Yes — automatically | Low (slot confirmed available again) | Immediately call `check_availability`; offer the nearest available slot to the customer without waiting for them to ask; require fresh customer confirmation before retrying `book_appointment` |
| `check_availability` returns no slot | Yes — with a new date hint from customer | None | Return to DATE_CLARIFICATION |
| Network or tool error (non-business failure) | Yes — once | Low | Retry once silently; on second failure, offer human handoff |

---

## 5. Claim confidence summary

| Count | Level | Notes |
|---|---|---|
| 5 | Verified | Original requirement text, prototype results, CEO decisions (incl. DEC-0010: VA intro and menu) |
| 24 | Inferred | Logical from architecture (D2), CEO decisions, and industry practice (incl. INTRODUCTION, MENU_PROMPT, SUGGEST_SCHEDULE states) |
| 5 | Assumed | Details not yet decided; marked Unknown where CEO/PM input needed |
| 2 | Unknown | Listed in §2, §3 — require PM decision before build (OQ-005 resolved) |

---

## 6. Open questions for PM / CEO

| # | Question | Blocking? | Section |
|---|---|---|---|
| OQ-001 | Confirm that CONFIRMATION_REPEAT (double confirmation) is required before calling `book_appointment` — the original request says "repeat date/time/service for confirmation" but does not explicitly require a second yes | Medium — affects booking turn count | §1 |
| OQ-002 | What is the exact "unable to help" message for an unrecognised tenant? | No — wording only | §2 |
| OQ-003 | Minimum RAG chunk relevance threshold before a result is used | No — build detail | §3 |
| OQ-004 | Finalise the explicit confirmation keyword list (yes, confirm, book it, go ahead, please, sure, do it) | No — build detail | §4 |
| OQ-005 | ~~What is the human handoff mechanism at AUD 0?~~ **RESOLVED (DEC-0010):** VA collects the customer's email address and phone number during HUMAN_HANDOFF, then flags the interaction to the tenant's product manager (or designated contact) for follow-up. No automated notification at this stage — tenant follows up manually. | Resolved — 2026-11-21 | §1 |

---

*Deliverable complete. Routed to PM for review. See open questions above.*
