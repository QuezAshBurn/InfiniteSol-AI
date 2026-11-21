# D2 — Architecture Brief
# P-0001 AI Voice Virtual Assistant

| Field | Value |
|---|---|
| **Project** | P-0001 AI Voice Virtual Assistant |
| **Document ID** | D2 |
| **Owner** | Solution Architect (Role 03) |
| **Governing assignment** | DA-0002 v1.0, `REQ-0001-discovery-auth.md` v1.0 |
| **Decisions applied** | DEC-0003 (8 GB hardware), DEC-0004 (prototype in timebox), DEC-0006 (SaaS-first), DEC-0009 (Web Speech API — superseded), DEC-0011 (WhatsApp channel), DEC-0012 (multi-language) |
| **Revision** | v1.2 |
| **Date** | 2026-11-21 |
| **Status** | Updated pre-charter approval — WhatsApp channel replaces browser Web Speech API (DEC-0011); multi-language added (DEC-0012) |

---

## 1. SaaS feasibility verdict

**FEASIBLE (with stated caveats) for a development demo and early-stage production SaaS deployment at AUD 0, using the Cloudflare-native stack.**

The Cloudflare free tier provides persistent storage, always-on serverless compute (no cold starts), and hard daily/monthly limits that return errors rather than charges — the strongest AUD 0 safety profile of all options assessed. Combined with the Groq free tier for LLM inference and STT, and Meta's WhatsApp Business Cloud API for the voice channel, all core capability gaps can be bridged at AUD 0.

**Channel (DEC-0011 — updated from browser Web Speech API):** Customer sends a voice note (audio message) via WhatsApp. Cloudflare Worker receives the webhook, downloads the audio, transcribes via Groq Whisper (free tier), processes with the LLM, and replies with a WhatsApp text message. Phase 2 (Twilio, separate budget decision) will add live voice call support.

**Multi-language (DEC-0012):** Groq Whisper auto-detects the customer's language during transcription. The Worker passes the detected language to the LLM system prompt. The LLM responds in the same language. No explicit language selector is required.

**Primary caveat:** Customer voice notes are sent to Meta (WhatsApp) and to Groq (Whisper transcription). Voice data leaves the customer's device via two third-party services. Tenants must disclose this in their privacy policy.

**Key limits at AUD 0 (Cloudflare free tier):**

| Service | Free limit | At-limit behaviour | Permanent? |
|---|---|---|---|
| Workers | 100K requests/day | Error returned, not charged | Inferred — permanent |
| D1 (SQLite) | 5 GB storage; daily read/write limits | Error returned, not charged | Inferred — permanent |
| KV | 100K reads/day, 1K writes/day | Error returned, not charged | Inferred — permanent |
| Vectorize | ~30M queried dimensions/month | Not confirmed — flag for build verification | Inferred |
| Pages | Unlimited static hosting | N/A | Inferred — permanent |

**Groq free tier:**
- No credit card required — Inferred (community-confirmed, [Groq community](https://community.groq.com/t/is-there-a-free-tier-and-what-are-its-limits/790))
- Overuse returns 429 error, not a charge — Inferred ([Groq community](https://community.groq.com/t/do-i-get-charged-for-anything-on-the-groq-free-plan/832))
- Exact per-model rate limits vary; treat third-party figures as provisional; confirm in Groq console at account creation

> **Build-stage verification required:** Before build approval, the Deployment Engineer must confirm current Cloudflare Vectorize and Workers overage behaviour from official terms, and confirm Groq free-tier rate limits from the Groq console.

---

## 2. Options assessed and excluded

| Option | Verdict | Reason |
|---|---|---|
| **Cloudflare SaaS stack** | **RECOMMENDED** | Hard-stop limits, no auto-charges, persistent storage, no cold starts, all free tiers permanent |
| Render.com | EXCLUDED from primary | Free tier spins down after 15 min; cold start ~1 min — unacceptable for real-time voice assistant; acceptable only as a demo fallback if Cloudflare fails |
| Hugging Face Spaces | EXCLUDED | Free CPU Basic quota reported restricted/zero for new accounts since July 2026; status uncertain — too risky for AUD 0 planning |
| Railway | EXCLUDED | Minimum $5 AUD/month on Hobby plan — not AUD 0 |
| Local-only (Ollama) | FALLBACK | Used for development; not SaaS; presented as Track C |

---

## 3. Recommended architecture — Track A (SaaS, Cloudflare)

### System diagram

```
Customer (WhatsApp)
  │  sends voice note (OGG/Opus audio)
  ▼
Meta WhatsApp Business Cloud API (free tier)
  │  webhook POST — audio media URL + message metadata
  ▼
┌──────────────────────────────────────────────────────────┐
│  Cloudflare Worker (always-on serverless)                │
│                                                          │
│  0. Verify webhook signature (HMAC-SHA256, X-Hub-Sig)    │
│  1. Verify tenant identity (from WhatsApp number → D1)   │
│  2. Download audio from WhatsApp media URL               │
│  3. Send audio to Groq Whisper API → transcript + lang   │
│  4. Load tenant config from D1                           │
│  5. Retrieve from Vectorize (tenant namespace only)      │
│  6. Call Groq LLM (transcript + context + language hint) │
│  7. If tool call in response:                            │
│     a. Verify tool approval flag in D1                   │
│     b. Verify tenant scope                               │
│     c. Gate on explicit customer confirmation (R-001)    │
│     d. Execute check_availability / book_appointment     │
│        against D1 test calendar                          │
│  8. Send text reply via Meta Cloud API → customer        │
└──────────────┬───────────────────────────────────────────┘
               │
   ┌───────────┼─────────────────┐
   ▼           ▼                 ▼
┌──────┐  ┌──────────┐  ┌──────────────────┐
│  D1  │  │    KV    │  │   Vectorize      │
│SQLite│  │ sessions │  │ per-tenant       │
│tenant│  │          │  │ namespaces       │
│config│  │          │  │ (source+revision │
│cal.  │  │          │  │  metadata)       │
└──────┘  └──────────┘  └──────────────────┘

Phase 2 (Twilio — separate CEO approval):
Customer places a voice call → Twilio routes to Worker → real-time STT/TTS
```

### Component selection

| Layer | Component | Licence | AUD 0 rationale | SaaS feasibility | 8 GB dev feasibility | Free-tier permanent? |
|---|---|---|---|---|---|---|
| **Voice channel** | WhatsApp Business Cloud API (Meta) | Meta — free tier | No charge for messaging; free webhook | FEASIBLE — requires Meta Business account approval (~1–2 days) | N/A — webhook only | Inferred permanent |
| **Voice STT** | Groq Whisper API (free tier) | OpenAI Whisper / free | Transcribes audio files; free tier; auto-detects language | FEASIBLE | FEASIBLE (Whisper.cpp locally) | Inferred permanent |
| **Voice response** | WhatsApp text message via Meta Cloud API | Meta — free tier | Phase 1: text reply only; AUD 0 | FEASIBLE | N/A | Yes |
| **Voice TTS (phase 2)** | Twilio Voice (live call) | Twilio — small cost | Phase 2 only; separate CEO budget decision; not in this build | DEFERRED | DEFERRED | No — per-use cost |
| **LLM / dialogue** | Groq free tier (`openai/gpt-oss-120b`) | Model licence / free | No credit card; 429 on overuse, not charge | FEASIBLE with rate-limit caveat | N/A (SaaS) | Inferred permanent |
| **Multi-language** | Groq Whisper language detection + LLM | Same as STT + LLM | No extra cost; Whisper returns detected language; LLM prompted to respond in same language | FEASIBLE | FEASIBLE | Yes |
| **Frontend host** | Cloudflare Pages | Proprietary / free tier | Static hosting, no limit stated | FEASIBLE | N/A | Inferred permanent |
| **Backend compute** | Cloudflare Workers | Proprietary / free tier | 100K req/day hard stop | FEASIBLE | N/A | Inferred permanent |
| **Tenant config + calendar** | Cloudflare D1 (SQLite) | Proprietary / free tier | 5 GB, hard-stop limits | FEASIBLE | SQLite locally FEASIBLE | Inferred permanent |
| **Session state** | Cloudflare KV | Proprietary / free tier | 100K reads/day hard stop | FEASIBLE | N/A (use dict locally) | Inferred permanent |
| **RAG vector store** | Cloudflare Vectorize | Proprietary / free tier | 30M queried dim/month; overage unconfirmed | MARGINAL — verify before build | Chroma in-process locally FEASIBLE | Inferred permanent (verify) |
| **Embeddings** | Workers AI (BGE-small-en) | Apache 2.0 | Free tier with daily limits | FEASIBLE for demo volume | sentence-transformers/all-MiniLM locally FEASIBLE | Inferred permanent (verify) |
| **MCP tool stubs** | Cloudflare Worker functions | N/A — in-process | No extra cost | FEASIBLE | FastAPI routes locally | N/A |

### Data and trust flow

1. Customer sends a voice note on WhatsApp. Meta Cloud API delivers it to the Cloudflare Worker via webhook. Worker verifies the request signature (HMAC-SHA256) before processing.
2. Worker derives tenant identity from the recipient WhatsApp number — mapped to a tenant record in D1. No customer input can override tenant identity.
3. Worker downloads the audio file from WhatsApp's temporary media URL and forwards it to Groq Whisper. Whisper returns the transcript and detected language.
4. Worker queries only the requesting tenant's Vectorize namespace. Cross-namespace queries are not issued.
5. LLM receives system prompt with tenant identity, retrieved context, and detected language instruction ("The customer is speaking [lang]. Respond in [lang]."). No other tenant's data is in context.
6. If the LLM response includes a tool call, Worker checks the approval flag in D1 for that tenant and that tool. If the flag is false or absent, the tool is not executed.
7. `book_appointment` requires explicit customer confirmation. The Worker independently checks the customer's last message text for confirmation keywords (R-001). No audio re-check needed — the transcript is used.
8. Worker sends the reply as a WhatsApp text message via Meta Cloud API. Customer receives it in their WhatsApp conversation.
9. Booking ID is stored; a duplicate check runs before every booking write.

### Environment map

| Environment | Hosting | LLM | Vector store | Storage | Channel | STT | Status |
|---|---|---|---|---|---|---|---|
| **Development** | Local (8 GB) | Ollama Phi-3.5-mini Q4_K_M | Chroma (in-process) | SQLite local | WhatsApp webhook (ngrok tunnel) | Whisper.cpp locally | FEASIBLE (see §4) |
| **SaaS demo / staging** | Cloudflare free tier | Groq free tier | Cloudflare Vectorize | Cloudflare D1 + KV | WhatsApp Business Cloud API | Groq Whisper (free tier) | FEASIBLE (see §1 caveats) |
| **SaaS production** | Cloudflare free tier | Groq free tier | Cloudflare Vectorize | Cloudflare D1 + KV | WhatsApp Business Cloud API | Groq Whisper (free tier) | MARGINAL — rate limits and Vectorize overage must be verified |
| **Phase 2 (future)** | Cloudflare + Twilio | Groq free tier | Cloudflare Vectorize | Cloudflare D1 + KV | Twilio Voice (live call) | Twilio STT + TTS | DEFERRED — separate CEO budget decision |

---

## 4. Local fallback — Track C (8 GB development)

For development and local testing without a Cloudflare account. Not SaaS.

| Layer | Component | Licence | 8 GB feasibility | Notes |
|---|---|---|---|---|
| Voice channel | WhatsApp webhook via ngrok tunnel | Free (ngrok free tier has rate limits) | FEASIBLE | Use ngrok to expose local FastAPI to Meta webhook during dev; not for production |
| Voice STT | Whisper.cpp (base, ~150 MB; multilingual) | MIT | FEASIBLE | Offline; ~1-2s latency; auto-detects language; preferred for local dev |
| Voice STT (online alt.) | Groq Whisper API | Free tier | FEASIBLE | Same as SaaS track; requires internet |
| Voice TTS | Phase 1: text reply only (no TTS needed) | N/A | FEASIBLE | VA responds as text; TTS deferred to Twilio phase |
| LLM | Ollama + Phi-3.5-mini Q4_K_M | MIT / Meta | FEASIBLE — ~2.4 GB RAM | Adequate for booking dialogue; smaller vocabulary than 70B |
| LLM alt. | Ollama + Llama 3.2 3B Q4_K_M | Meta Llama licence | FEASIBLE — ~2.0 GB RAM | Slightly lower quality than Phi-3.5 on instruction following |
| Backend | FastAPI (Python) | MIT | FEASIBLE | Minimal footprint |
| Vector store | Chroma (in-process) | Apache 2.0 | FEASIBLE — <200 MB for small corpora | Persistent local mode available |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 | Apache 2.0 | FEASIBLE — ~100 MB | Good quality for FAQ and policy retrieval |
| Storage | SQLite (via Python) | Public domain | FEASIBLE | Tenant config and test calendar |

**Combined 8 GB RAM estimate (development track):**

| Item | Approximate RAM |
|---|---|
| OS + browser | ~2.0 GB |
| Ollama + Phi-3.5-mini Q4_K_M | ~2.4 GB |
| Python (FastAPI + Chroma + sentence-transformers) | ~0.8 GB |
| Whisper.cpp (multilingual, base model, ~150 MB) | ~0.3 GB |
| **Total** | **~5.7 GB** |
| **Remaining headroom** | **~2.3 GB** |

Verdict: **FEASIBLE** on 8 GB. Tight but workable. Recommend closing non-essential browser tabs during development.

---

## 5. Gaps and risks

| ID | Gap or risk | Severity | Environment | Recommended action | Owner |
|---|---|---|---|---|---|
| GAP-001 | ~~Web Speech API sends voice data to Google~~ — SUPERSEDED by DEC-0011. New concern: customer voice notes sent to Meta (WhatsApp) and Groq (Whisper). Two third parties receive audio. | High | SaaS WhatsApp track | Tenant privacy policy must disclose Meta and Groq audio processing. Security Architect to assess webhook security (D4 SEC-004 updated). | Security Architect |
| GAP-009 | WhatsApp Business account requires Meta approval — typically 1–2 business days but can be rejected or delayed | Medium | SaaS | Apply for Meta Business account early in build phase; have a fallback test number. | Deployment Engineer at build |
| GAP-010 | VA replies as text in phase 1 — customer sends voice, receives text. This breaks the voice-only experience. Phase 2 (Twilio) adds audio response. | Medium | SaaS phase 1 | Acceptable for prototype; document limitation for CEO. Text replies in the customer's language mitigate the gap. | PM |
| GAP-011 | Multi-language TTS deferred to Twilio phase — Groq Whisper handles multilingual transcription but audio response requires a multilingual TTS engine not in this build | Medium | Phase 2 | Assess multilingual TTS options (ElevenLabs free tier, Cloudflare Workers AI TTS) at Twilio phase planning. | Architect at phase 2 |
| GAP-002 | Cloudflare Vectorize overage behaviour not confirmed from official terms (search returned no explicit statement) | High | SaaS | Verify from official Vectorize docs at build approval; if no hard stop confirmed, switch RAG to Chroma on a Cloudflare Worker with D1-backed persistence or Qdrant free cloud | Deployment Engineer at build |
| GAP-003 | Groq free tier exact rate limits not confirmed from console — third-party figures provisional | Medium | SaaS | Confirm rate limits in Groq console at account setup; design system prompt and dialogue to minimise tokens-per-turn | Architect at build |
| GAP-004 | Cloudflare Workers AI embedding daily limits not confirmed | Medium | SaaS | Verify from Workers AI pricing docs; fallback to pre-computed embeddings loaded at deploy time | Architect at build |
| GAP-005 | **CONFIRMED by prototype 2026-11-21.** llama3.1:8b (best-case local model) called `book_appointment` on an ambiguous reply ("What time did you say?"). A prompt-level gate is not reliable. Mitigation: server-side confirmation gate in Worker (R-001 in PROTOTYPE-LOG). | High | All tracks | Implement R-001 (Worker-level keyword gate) at build — required before booking tool is live | Architect (build) |
| GAP-006 | Cloudflare Workers 100K req/day limit may constrain multi-tenant concurrent demo | Low | SaaS demo | Monitor usage during demo; at AUD 0 this is acceptable; flag for build if expected volume exceeds limit | PM at build |
| GAP-007 | Web Speech API has limited Firefox support; Chrome required for reliable STT/TTS | Low | All browser tracks | Document browser requirement; not a build blocker |  Architect |
| GAP-008 | HuggingFace Spaces excluded: free CPU Basic tier uncertain since July 2026 | Informational | — | Do not use HF Spaces; Cloudflare is preferred | — |

---

## 6. Prototype results (DEC-0004 — executed 2026-11-21)

**Question tested:** GAP-005 — does the LLM reliably hold the two-part confirmation gate?

**Model used:** `llama3.1:8b` via Ollama (Phi-3.5-mini not installed; llama3.1:8b is a stronger model — findings represent a best-case local LLM result).

**Result: 6/7 checks passed — FAIL on confirmation gate (S2)**

| Scenario | Checks | Verdict |
|---|---|---|
| S1 — Happy path: explicit yes, tool succeeds | 3/3 | PASS |
| S2 — Ambiguous reply ("What time did you say?") | 1/2 | **FAIL** |
| S3 — Tool failure: explicit yes, tool fails | 2/2 | PASS |

**Key finding — F-001 (HIGH):** The LLM called `book_appointment` on "What time did you say?" — a clarification question, not a confirmation. A prompt-level gate alone is not sufficient.

**Key finding — F-002 (LOW):** After a tool failure in S3, the model leaked raw JSON in its text response (attempted to chain a second tool call and serialised it as text instead of a tool_calls object).

**Recommendations recorded:**
- **R-001 (BLOCKING):** Add a server-side confirmation gate in the Worker. Before executing `book_appointment`, the Worker checks the customer's last utterance for explicit confirmation keywords. Returns `{"error": "awaiting_confirmation"}` if none found, forcing the LLM to re-ask. No new component required.
- **R-002 (advisory):** Strip raw JSON from the assistant text response before TTS using a lightweight regex in the Worker.

**Full prototype log:** `discovery/prototype/PROTOTYPE-LOG.md`
**Machine-readable results:** `discovery/prototype/prototype-results.json`

**Architecture impact of R-001:** Step 5c in the §3 Worker diagram ("Gate on explicit customer confirmation") must become an independent Worker check, not an LLM-enforced prompt rule. No new service required — a keyword check in the Worker's tool-dispatch logic.

**SaaS prototype complete — 2026-11-21.** Groq account created; model used: `openai/gpt-oss-120b` (Llama 3.3 70B no longer listed on Groq free tier as of 2026-11-21). Result: 7/7 PASS. GAP-005 does not reproduce on the hosted 120B model. See PROTOTYPE-LOG.md for full transcript.

> **Build note:** Groq's available model IDs have changed since this brief was drafted. The LLM component selection (`llama-3.3-70b-versatile`) must be re-confirmed at build against the live Groq model catalog. Current best available: `openai/gpt-oss-120b`.

---

## 7. Architecture decisions required before build

| Decision | Owner | Required before |
|---|---|---|
| Confirm Cloudflare Vectorize overage is a hard stop (not a charge) | Deployment Engineer | Build approval |
| Confirm Groq free tier rate limits from console; assess whether limits allow intended demo volume | Architect + Deployment Engineer | Build approval |
| Confirm Workers AI embedding daily limits | Architect | Build approval |
| ~~Decide: browser Web Speech API accepted~~ | ~~CEO~~ | **SUPERSEDED — DEC-0011. Channel is now WhatsApp. D4 SEC-004 to be updated.** |
| Confirm WhatsApp Business account approved by Meta | Deployment Engineer | Before build integration test |
| ~~Decide: proceed with Cloudflare + Groq account creation for SaaS prototype~~ | ~~CEO / PM~~ | **AUTHORIZED 2026-11-21 (DEC-0008)** — accounts to be created at next session |

---

## 8. Nonfunctional targets (preliminary, to be confirmed at build)

| Target | Value | Basis |
|---|---|---|
| STT round-trip latency (WhatsApp) | ~2–5s end-to-end (audio upload → Groq Whisper → Worker → WhatsApp reply) | Assumed — async message; not real-time call |
| LLM response (first token) | < 1s via Groq on free tier (reported) | Inferred — community benchmarks |
| Booking flow turns to completion | ≤ 5 (greeting → clarify → check → offer → confirm) | Inferred from requirement |
| Tenant isolation check overhead | < 50ms (single D1 lookup) | Assumed |
| Duplicate booking prevention | 0 duplicates under single-tenant concurrent test | Requirement |

---

## 9. Handoff to PM

**Disposition:** D2 complete. Architecture is viable at AUD 0 for SaaS using Cloudflare + Groq. Five build-stage verification items recorded (§7). Two CEO decisions required before account creation or prototype on SaaS track.

**D2 unblocks:** DA-0005 (evidence plan — BA can now design test scenarios around the Cloudflare + Groq stack and the local fallback).

**Open items routed to PM:**
- GAP-001 (voice data privacy) → D4 Security Architect
- GAP-002, GAP-003, GAP-004 → Deployment Engineer at build approval
- GAP-005 → prototype decision (see §6)
- Decisions in §7 → CEO / PM

| Claim type | Count |
|---|---|
| Verified | 5 (Web Speech API browser-native; Chroma/Ollama/FastAPI/sentence-transformers open source; Render spin-down still active) |
| Inferred | 14 (Cloudflare hard-stop behaviour; Groq free-tier no-charge on 429; free-tier permanence; model RAM estimates) |
| Assumed | 6 (latency targets; Phi-3.5-mini dialogue quality; RAM budget breakdown) |
| Unknown | 2 (Vectorize overage behaviour; Workers AI embedding daily limit) |

---

*Sources used in this brief:*
- [Groq free plan — no charge on overuse](https://community.groq.com/t/do-i-get-charged-for-anything-on-the-groq-free-plan/832)
- [Groq free tier — no credit card](https://community.groq.com/t/is-there-a-free-tier-and-what-are-its-limits/790)
- [Groq rate limits overview](https://www.grizzlypeaksoftware.com/articles/p/groq-api-free-tier-limits-in-2026-what-you-actually-get-uwysd6mb)
- [Cloudflare D1 limits](https://developers.cloudflare.com/d1/platform/limits)
- [Cloudflare KV limits](https://developers.cloudflare.com/kv/platform/)
- [Cloudflare Vectorize pricing](https://developers.cloudflare.com/vectorize/platform/pricing/)
- [Render free tier spin-down — still active 2026](https://render.com/articles/platforms-with-a-real-free-tier-for-developers-in-2026)
- [HuggingFace Spaces CPU Basic quota issues July 2026](https://discuss.huggingface.co/t/official-community-complaint-revert-free-cpu-basic-spaces-and-remove-anti-developer-sdk-restrictions/177703)
