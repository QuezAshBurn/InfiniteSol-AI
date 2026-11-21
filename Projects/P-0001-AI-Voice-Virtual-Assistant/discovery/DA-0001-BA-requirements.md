# Work Assignment | DA-0001
# D1 — Requirements Summary

| Field | Value |
|---|---|
| **Project** | P-0001 AI Voice Virtual Assistant |
| **Assignment ID** | DA-0001 |
| **Governing authorization** | `AI Team/starter/REQ-0001-discovery-auth.md` v1.0, CEO approved 2026-11-21 |
| **Owner role** | Business Analyst (Role 02) |
| **Due** | 2026-11-28 (end of 5-business-day discovery window) |
| **Status** | Dispatched |
| **Spend limit** | AUD 0 |
| **Data** | Synthetic only |

## Goal

Produce a requirements summary (D1) that captures the booking flow dialogue rules, tenant isolation model, RAG source model, and tool approval and retry model, with enough precision that the Solution Architect can assess feasible AUD 0 component choices and that a future story author can write testable acceptance criteria.

## Acceptance criteria

1. Booking flow — all named dialogue states documented: greeting, service clarification, date/time clarification, availability check, slot offer, confirmation repeat (date + time + service), "you're booked" condition (tool success only), unavailable slot, booking failure, human handoff request. Edge cases noted.
2. Tenant isolation model — how tenant identity enters the system (trusted application configuration), how it is enforced before any retrieval or tool call, and what happens if tenant identity is absent or unrecognised.
3. RAG source model — how each tenant's approved knowledge sources are defined, stored, and limited to that tenant; how source and revision references are kept for verification; what triggers a clarification request or human handoff when evidence is missing or conflicting.
4. Tool approval and retry model — when `check_availability` and `book_appointment` are permitted to execute; how approval and tenant scope are verified on each call; how the assistant confirms with the customer before changing the calendar; how retries work without creating duplicates.
5. All claims labelled **Verified**, **Inferred**, or **Assumed**. Unresolved details marked rather than invented.

## Allowed actions

- Elicit requirements from the original request and any clarifying input from the PM
- Document requirements and business rules in Markdown
- Challenge and record assumptions
- No implementation, prototype, or tool execution
- No external API calls or spend

## Required output

`Projects/P-0001-AI-Voice-Virtual-Assistant/discovery/D1-requirements.md`

Route the completed deliverable to the PM for review. Note any unresolved ambiguities requiring CEO or PM input.

## Stop conditions

- If a requirement cannot be resolved from available evidence: mark **Unknown**, record the question, and route to PM
- If any action would exceed AUD 0 or the 2026-11-28 deadline: stop and escalate to PM immediately
