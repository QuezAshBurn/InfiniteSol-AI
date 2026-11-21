# P-0001 Build Log

**Project:** AI Voice Virtual Assistant  
**CEO approval:** D6 v1.2 — 2026-11-21  
**Build started:** 2026-11-21  

---

## Status: Build complete — awaiting deployment

---

## Files built

### Database (D1 / SQLite)

| File | Purpose | Status |
|------|---------|--------|
| `build/db/schema.sql` | D1 schema: tenants, tool_approvals, services, time_slots, bookings, handoff_requests, knowledge_sources | ✅ Done |
| `build/db/seed-t1.sql` | T1: Riverside Hair Studio (Aria) — 3 services, 20 slots, 3 KB entries | ✅ Done |
| `build/db/seed-t2.sql` | T2: Peak Physio Clinic (Max) — 3 services, 19 slots, 3 KB entries | ✅ Done |

### Cloudflare Worker (`build/worker/`)

| File | Purpose | Status |
|------|---------|--------|
| `src/index.js` | Main handler: webhook GET/POST, HMAC verify, session, Whisper, LLM loop, tool exec, reply | ✅ Done |
| `src/llm.js` | buildSystemPrompt, TOOLS definition, callLLM (Groq) | ✅ Done |
| `src/tools.js` | checkAvailability, bookAppointment, recordHandoff (all D1-backed) | ✅ Done |
| `src/whatsapp.js` | verifySignature, getMediaUrl, downloadMedia, sendWhatsApp | ✅ Done |
| `src/gate.js` | R-001 gateBooking (keyword check), R-002 stripJson | ✅ Done |
| `wrangler.toml` | D1 + KV bindings, verify token var, secrets list | ✅ Done |
| `package.json` | Minimal — wrangler devDependency only | ✅ Done |

---

## Security controls implemented

| Control | Location | Description |
|---------|----------|-------------|
| SEC-001 | `whatsapp.js` + `index.js` | HMAC-SHA256 webhook signature verification; hard-stop on tenant not found |
| SEC-002 | `tools.js:bookAppointment` | Slot tenant_id ownership check before booking |
| SEC-003 | `tools.js` | Tool approval re-checked per call from D1 (not cached) |
| SEC-005 | `index.js` | KV session key format: `{tenant_id}:{customer_phone}` |
| R-001 | `gate.js` + `index.js` | Keyword confirmation gate before book_appointment |
| R-002 | `gate.js` + `index.js` | JSON bleed stripped from LLM reply before sending |

---

## Deployment checklist (for Deployment Engineer)

### Pre-deploy actions required

1. **Meta WhatsApp Business account approval** (GAP-009)
   - Apply at: https://business.facebook.com
   - Expected: ~1–2 business days
   - Needed before any live webhook traffic

2. **Create Cloudflare D1 database**
   ```
   wrangler d1 create p0001-va-db
   ```
   Copy the `database_id` into `wrangler.toml`.

3. **Create Cloudflare KV namespace**
   ```
   wrangler kv:namespace create p0001-va-sessions
   ```
   Copy the `id` into `wrangler.toml`.

4. **Apply schema and seed data**
   ```
   wrangler d1 execute p0001-va-db --file=build/db/schema.sql
   wrangler d1 execute p0001-va-db --file=build/db/seed-t1.sql
   wrangler d1 execute p0001-va-db --file=build/db/seed-t2.sql
   ```

5. **Set secrets**
   ```
   wrangler secret put WHATSAPP_APP_SECRET
   wrangler secret put WHATSAPP_ACCESS_TOKEN
   wrangler secret put GROQ_API_KEY
   ```

6. **Set verify token** in `wrangler.toml` `[vars]` block (any random string; must match what you configure in Meta webhook settings).

7. **Update tenant WhatsApp numbers** in seed SQL files with actual Meta-approved numbers before running seed.

8. **Confirm Groq model ID** — check Groq dashboard for current model availability; default in `llm.js` is `openai/gpt-oss-120b` (DEC-0004 build note).

9. **Deploy**
   ```
   cd build/worker
   npm install
   wrangler deploy
   ```

10. **Register webhook** in Meta Developer Console:
    - URL: `https://<your-worker>.workers.dev/webhook`
    - Verify token: matches `WHATSAPP_VERIFY_TOKEN` in wrangler.toml
    - Subscribe to: `messages`

11. **Local dev with ngrok** (for testing before Meta approval):
    ```
    wrangler dev --local --persist
    ngrok http 8787
    ```
    Use ngrok URL as webhook URL in Meta Developer Console.

---

## Evidence scenarios outstanding (D5 v1.1)

| ID | Scenario | Status |
|----|---------|--------|
| E-001 | Full booking flow — Aria, Haircut, Mon 9am | ⏳ Pending |
| E-002 | Explicit confirmation gate (R-001) | ⏳ Pending |
| E-003 | Duplicate booking idempotency | ⏳ Pending |
| E-004 | BOOKING_FAILURE → auto check_availability recovery | ⏳ Pending |
| E-005 | Human handoff (OQ-005) — email + phone collection | ⏳ Pending |
| E-006 | Tenant isolation — T1 slot rejected for T2 | ⏳ Pending |
| E-007 | RAG response — services/hours query | ⏳ Pending |
| E-008 | Multi-language booking (Filipino/Tagalog) | ⏳ Pending |
| E-009 | WhatsApp voice note end-to-end | ⏳ Pending |

---

## Decisions reference

DEC-0001 through DEC-0012 — see `project-record.md`.
