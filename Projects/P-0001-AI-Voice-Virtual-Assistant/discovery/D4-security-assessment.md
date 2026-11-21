# D4 — Security and Tenant-Isolation Assessment
# P-0001 AI Voice Virtual Assistant

| Field | Value |
|---|---|
| **Project** | P-0001 AI Voice Virtual Assistant |
| **Document ID** | D4 |
| **Owner** | Security Architect (Role 05) |
| **Governing assignment** | DA-0004 |
| **Source documents** | REQ-0001-discovery-auth.md v1.0; D2-architecture-brief.md v1.1; D1-requirements.md v1.0 |
| **Decisions applied** | DEC-0006 (SaaS-first), DEC-0007 (R-001 confirmation gate) |
| **Revision** | v1.0 |
| **Date** | 2026-11-21 |
| **Status** | Draft — awaiting PM review |

---

## 1. Tenant isolation assessment

### Proposed enforcement model

Tenant identity is set by trusted application configuration at the Worker layer before any retrieval or tool call. No customer input can alter tenant identity. Worker queries Vectorize using the tenant's dedicated namespace and reads/writes D1 rows scoped to the tenant ID.

### Assessment

| Risk path | Assessment | Severity | Control required |
|---|---|---|---|
| Customer supplies a tenant ID in their utterance | Not applicable — tenant identity is never read from user input | None | None — by design |
| Worker misconfiguration passes wrong tenant namespace to Vectorize | Possible if D1 config row is incorrect or missing | **HIGH** | Validate tenant config row on Worker startup; return hard error if tenant ID is absent or unrecognised; never default to a fallback tenant |
| Cross-tenant RAG leak via shared Vectorize index | Not applicable if each tenant has a dedicated namespace | None | Confirm Cloudflare Vectorize namespaces are physically isolated, not just filtered — **[Unknown; verify at build]** |
| Cross-tenant booking write (Tenant A books on Tenant B's calendar) | Possible if slot validation does not check tenant ownership | **HIGH** | Worker must verify slot belongs to the requesting tenant's D1 calendar before writing; reject mismatched tenant ID |
| Session state (KV) cross-contamination | Possible if KV key is not tenant-scoped | **MEDIUM** | KV keys must include tenant ID as prefix; e.g. `{tenant_id}:{session_id}` |
| Groq LLM receives context from multiple tenants | Not applicable if each request is scoped to one tenant's retrieved context | None | Ensure each LLM call carries only the current tenant's retrieved chunks |

### Verdict

**Isolation model is sound in design.** Two HIGH-severity controls must be implemented before build:
1. Hard error on absent/unrecognised tenant config (not a silent default)
2. Tenant ownership check on every `book_appointment` write

One Unknown to verify at build: Cloudflare Vectorize namespace isolation guarantee.

---

## 2. Data handling assessment

### What personal or sensitive data the assistant handles

| Data type | Where it appears | Sensitivity | Retained beyond session? |
|---|---|---|---|
| Customer voice audio | Browser only (Web Speech API) | **HIGH** — biometric-adjacent | No — not sent to Worker; only the text transcript is sent — **[Inferred]** |
| Customer voice audio (alternative: Web Speech API) | Google/browser vendor backend | **HIGH** — sent to external vendor | Unknown — depends on browser vendor policy — **[Unknown]** |
| Text transcript of customer utterances | Worker, KV (session state), D1 (booking record) | Medium | Session transcript in KV: expired after session. Booking record in D1: retained until deleted. |
| Booking details (name, service, date/time) | D1 | Medium | Retained — required for appointment management |
| Tenant configuration | D1 | Low | Retained — operational data |

### Data handling requirements at AUD 0

| Requirement | Mechanism | Confidence | Gap? |
|---|---|---|---|
| Voice audio does not reach the Worker | Web Speech API transcribes client-side; only text is sent | **Inferred** | No — by browser API design |
| Text transcript in transit is encrypted | Cloudflare Workers use HTTPS by default | **Verified** | No |
| Session transcript not persisted beyond session | KV TTL set to session duration; Worker does not write transcripts to D1 | **Inferred** | Confirm TTL is set at build |
| Booking records accessible only to the owning tenant | D1 rows scoped by tenant ID; Worker enforces read/write scope | **Inferred** | No additional gap |
| No personal data in Groq LLM calls | Customer utterances are sent to Groq as text; no additional PII should be injected into the prompt | **Assumed** | Assess at build: does the system prompt or RAG context include any customer PII? |

### GAP-001 — Web Speech API voice data privacy (BLOCKING)

The browser's Web Speech API sends audio to the browser vendor's backend (Google in Chrome) for transcription. Customer voice is processed by a third party.

**Risk:** Customer voice data leaves the browser and is processed by Google (or another vendor) under that vendor's terms of service, not the tenant's or operator's privacy policy.

**Severity: HIGH — Blocking CEO decision required before build.**

| Option | Cost | Privacy | Quality | Recommendation |
|---|---|---|---|---|
| Accept Web Speech API (current design) | AUD 0 | Audio sent to Google | Excellent (Chrome) | Acceptable for a demo; not recommended for production without disclosure |
| Whisper.cpp (offline, local track only) | AUD 0 | Audio stays on device | Good (~1-2s latency) | Recommended for privacy-sensitive tenants on local track |
| Self-hosted Whisper (server-side) | AUD 0 for small volume on Cloudflare Workers AI | Audio sent to Cloudflare | Good | Viable SaaS alternative — **[Unknown: Workers AI audio support; verify at build]** |

**Decision required (OQ-D4-001):** Does the CEO accept Web Speech API for the SaaS prototype, with the understanding that customer voice is sent to Google? If yes, tenants must disclose this in their privacy policy. If no, the SaaS track must use an alternative STT approach.

---

## 3. Tool approval gating assessment

### Proposed design

The Worker enforces two gates before executing `book_appointment`:
1. Tool approval flag in D1 for the tenant and tool
2. Customer confirmation keyword check (R-001, DEC-0007)

`check_availability` requires only the approval flag (no confirmation gate).

### Assessment

| Risk path | Assessment | Severity | Control |
|---|---|---|---|
| LLM calls `book_appointment` without customer confirmation | Mitigated by R-001 (server-side keyword gate, DEC-0007) | Was HIGH; now MEDIUM (gate is at Worker, not LLM) | R-001 implementation is mandatory at build |
| Tenant disables `book_appointment` approval flag but it is ignored | Possible if Worker doesn't re-check on each call | **HIGH** | Worker must re-check D1 approval flag on every `book_appointment` call, not just once at session start |
| Approval flag spoofed by customer input | Not applicable — approval flags are in D1, inaccessible to customers | None | None — by design |
| Cross-tenant tool call (Tenant A triggers tool on Tenant B's calendar) | Possible without slot ownership check | **HIGH** | Same as §1: Worker verifies slot's tenant ID before executing |
| Duplicate booking on retry | Mitigated by D1 duplicate check and slot re-check | MEDIUM | Idempotency key implementation required at build (see D1 §4) |
| `check_availability` called in an infinite loop (model re-calls after failure) | Observed in prototype S3 (model attempted second check_availability call after failure) | LOW | Worker should rate-limit tool calls per session turn (e.g. max 2 tool calls per user turn) |

### Verdict

**Gate design is correct in principle.** Three controls must be implemented:
1. R-001 keyword gate (DEC-0007) — already approved
2. D1 approval flag re-checked on every tool call (not cached)
3. Slot tenant ownership verification on `book_appointment`

---

## 4. Voice data risks

### Local track (Track C — Ollama, Whisper.cpp)

| Risk | Assessment | Control |
|---|---|---|
| Voice audio persists on disk | Whisper.cpp processes audio in memory; no disk write by default | Confirm no temp file written — **[Inferred; verify at build]** |
| Transcript retained in session state | In-memory only on local track; lost on process restart | Acceptable for development |
| Microphone access without consent | Browser requests permission on first use; standard browser UX | No additional control needed |

### SaaS track (Track A — Web Speech API)

| Risk | Assessment | Control |
|---|---|---|
| Voice audio sent to Google | See GAP-001 — blocking CEO decision | CEO must decide before build |
| Transcript in transit | HTTPS between browser and Worker — **[Verified]** | None needed |
| Transcript stored in KV | Acceptable if TTL is enforced; not persisted to D1 | Set TTL at build |
| Microphone access without consent | Browser requests permission on first use | Tenant must include mic permission disclosure in their UI |

---

## 5. Blocking findings (must resolve before build approval)

| ID | Finding | Severity | Owner | Resolution |
|---|---|---|---|---|
| SEC-001 | Hard error required on absent/unrecognised tenant config | HIGH | Build — Architect | Implement in Worker; no silent fallback |
| SEC-002 | Tenant ownership check required on `book_appointment` | HIGH | Build — Architect | Worker verifies slot's tenant ID before write |
| SEC-003 | D1 tool approval flag must be re-checked on every tool call | HIGH | Build — Architect | No session-level caching of approval flags |
| SEC-004 | GAP-001: Web Speech API sends voice to Google | HIGH | CEO | **RESOLVED 2026-11-21 (DEC-0009)** — Accepted for prototype; tenant privacy policy disclosure required before production |

---

## 6. Advisory findings (non-blocking)

| ID | Finding | Severity | Owner | Resolution |
|---|---|---|---|---|
| SEC-005 | KV session keys must include tenant ID as prefix | MEDIUM | Build — Architect | Key format: `{tenant_id}:{session_id}` |
| SEC-006 | Worker should rate-limit tool calls per session turn | LOW | Build — Architect | Max 2 tool calls per user turn recommended |
| SEC-007 | Confirm Whisper.cpp writes no temp audio files | LOW | Build — Architect | Verify at build on local track |
| SEC-008 | Cloudflare Vectorize namespace physical isolation not confirmed | LOW | Build — Deployment Engineer | Verify from Cloudflare docs |

---

## 7. CEO decisions required before build

| ID | Question | Blocking | Decision |
|---|---|---|---|
| OQ-D4-001 | Accept Web Speech API for SaaS prototype (customer audio sent to Google)? If yes, tenant privacy policy must disclose. If no, SaaS track needs an alternative STT. | **YES** | **ACCEPTED 2026-11-21 (DEC-0009)** — Web Speech API permitted for prototype. Tenants must disclose in privacy policy before production. Alternative STT to be evaluated at build if requirements change. |

---

## 8. Claim confidence summary

| Count | Level |
|---|---|
| 3 | Verified |
| 12 | Inferred |
| 4 | Assumed |
| 3 | Unknown (flagged for build verification) |

---

*Deliverable complete. Routed to PM for review. SEC-004 / OQ-D4-001 is a blocking CEO decision — flagged immediately per DA-0004 stop conditions.*
