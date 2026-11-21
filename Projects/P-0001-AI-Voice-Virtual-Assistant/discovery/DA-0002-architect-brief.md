# Work Assignment | DA-0002
# D2 — Architecture Brief

| Field | Value |
|---|---|
| **Project** | P-0001 AI Voice Virtual Assistant |
| **Assignment ID** | DA-0002 |
| **Governing authorization** | `AI Team/starter/REQ-0001-discovery-auth.md` v1.0, CEO approved 2026-11-21; DEC-0006 architectural direction recorded 2026-11-21 |
| **Owner role** | Solution Architect (Role 03) |
| **Due** | 2026-11-28 (end of 5-business-day discovery window) |
| **Status** | Dispatched |
| **Spend limit** | AUD 0 |
| **Data** | Synthetic only |

## Goal

Produce an architecture brief (D2) that maps AUD 0, open-source component choices to the voice assistant requirements. The **primary direction is SaaS** (DEC-0006): assess free-tier hosted deployment first. If SaaS cannot meet AUD 0, document the cost gap and fall back to local-only. Provide explicit feasibility assessments per environment and document the hardware constraint.

## SaaS-first direction (DEC-0006)

The CEO has stated a preference for SaaS architecture if feasible within AUD 0. Assess this as the primary track:

- **Free-tier hosting candidates** (examples; Architect to evaluate): Railway, Render, Fly.io, Vercel, Hugging Face Spaces, Cloudflare Workers — assess which accept the full stack (voice, LLM or API, RAG, multi-tenant routing) on a free tier with no credit card or time-limited trial.
- **Free-tier LLM/inference candidates**: Groq free tier, Hugging Face Inference API free tier, Ollama served locally but accessed via browser — assess latency, rate limits, and whether they satisfy the AUD 0 constraint sustainably (not a trial).
- **Voice in SaaS**: browser-based Web Speech API (client-side, no server cost) is the primary candidate for speech-to-text and text-to-speech; assess its quality, offline limitations, and browser compatibility.
- **Multi-tenant RAG in SaaS**: assess a lightweight vector store (e.g. Chroma in-memory per session, or a free-tier managed option) that can enforce per-tenant source isolation.
- **Test calendar in SaaS**: assess a free self-hostable CalDAV server or an in-process synthetic calendar stub.

For each option assessed: name it, state its licence, confirm whether the free tier is permanent (not a trial), state any usage ceiling that could affect operation, and give a verdict (FEASIBLE / MARGINAL / NOT FEASIBLE at AUD 0).

If no viable SaaS path exists within AUD 0, state this explicitly, give the minimum cost and what it covers, and present the local-only architecture as the fallback.

## Hardware constraint (DEC-0003)

The available machine has **8 GB RAM or less**. Every component recommendation must be assessed against this constraint. Any capability that cannot run within 8 GB on existing hardware must be flagged as a gap with the upgrade path or alternative.

## Prototype authorization (DEC-0004)

The CEO has authorised a local, synthetic-data-only prototype within this 5-day discovery window and within the AUD 0 limit. The Architect may build and run a minimal local proof of concept to verify a key uncertainty (e.g. whether a chosen LLM and RAG stack fit in 8 GB). Keep prototype code outside any delivery branch. Record findings and unanswered questions separately from the architecture recommendation.

## Acceptance criteria

1. **SaaS feasibility verdict** (primary track): can the full stack — voice, LLM/inference, RAG with tenant isolation, MCP tool interface, test calendar — be hosted on free-tier services at AUD 0 sustainably? FEASIBLE / MARGINAL (with stated caveats) / NOT FEASIBLE (with minimum cost to make it feasible).
2. Component map covering: voice input (STT), voice output (TTS), dialogue management / LLM, RAG retrieval, tenant isolation enforcement point, MCP tool stub interface, test calendar.
3. For each component: recommended open-source option, licence, AUD 0 rationale, SaaS feasibility verdict, 8 GB RAM feasibility verdict (for local fallback), free-tier permanence (permanent / trial / unclear), and any usage ceiling or assumption.
4. Feasibility assessed separately for: (a) SaaS on free-tier hosting (primary), (b) development on the stated local hardware, (c) local demo fallback if SaaS is not feasible.
5. Any capability that cannot meet AUD 0 on either track: flagged as a gap with the minimum cost and a named upgrade path or alternative.
6. Prototype findings (if run): question tested, track tested (SaaS or local), synthetic inputs/outputs, observed result, unanswered questions.
7. All claims labelled **Verified**, **Inferred**, or **Assumed**.

## Allowed actions

- Assess open-source component options using public documentation and the Architect's existing knowledge
- Run a local synthetic-data-only prototype for a named key uncertainty, within the 5-day window and AUD 0 limit
- No external API calls, no account creation, no spend
- No production, staging, or test environment provisioning
- Keep prototype code in `Projects/P-0001-AI-Voice-Virtual-Assistant/discovery/prototype/` — not in a delivery branch

## Required outputs

- `Projects/P-0001-AI-Voice-Virtual-Assistant/discovery/D2-architecture-brief.md`
- `Projects/P-0001-AI-Voice-Virtual-Assistant/discovery/prototype/` (if prototype is run)

Route the completed deliverable to the PM. D2 unblocks DA-0005 (evidence plan).

## Stop conditions

- Capability confirmed as infeasible within AUD 0 and 8 GB: document gap, escalate to PM before continuing
- Any spend or external commitment required: stop immediately, escalate to PM
- Discovery forecast to exceed 2026-11-28: stop, escalate to PM
