# Work Assignment | DA-0004
# D4 — Security and Tenant-Isolation Assessment

| Field | Value |
|---|---|
| **Project** | P-0001 AI Voice Virtual Assistant |
| **Assignment ID** | DA-0004 |
| **Governing authorization** | `AI Team/starter/REQ-0001-discovery-auth.md` v1.0, CEO approved 2026-11-21 |
| **Owner role** | Security Architect (Role 05) |
| **Due** | 2026-11-28 (end of 5-business-day discovery window) |
| **Trigger** | External handling of personal data (voice, booking); material tenant-isolation design |
| **Status** | Dispatched |
| **Spend limit** | AUD 0 |
| **Data** | Synthetic only |

## Goal

Produce a security and tenant-isolation assessment (D4) that evaluates the proposed design for the highest-risk areas — tenant isolation, data handling, tool approval gating — and identifies gaps that must be resolved before build approval.

## Acceptance criteria

1. Tenant isolation — assess whether the proposed enforcement point (trusted application configuration before any retrieval or tool call) is sufficient; identify any path where Tenant A data could leak to Tenant B; recommend controls and record unresolved risks.
2. Data handling — assess what personal or sensitive data the assistant handles in voice, dialogue, and booking flows; what retention, transit protection, and access control is required at AUD 0 on local hardware; identify any gap.
3. Tool approval gating — assess the `check_availability` and `book_appointment` approval verification design; identify any path that could allow an unapproved or cross-tenant tool call; recommend controls.
4. Voice data — assess risks of local voice input/output processing; note any data that persists beyond the session and what controls are needed.
5. Each finding labelled **Verified**, **Inferred**, or **Assumed**. Blocking risks identified separately from advisory findings.
6. Gaps that must be resolved before build approval listed explicitly with an owner and recommended resolution.

## Allowed actions

- Assess proposed design from D1 (when available) and the original request
- Read authorised source documents only
- No implementation, prototype, or tool execution
- No external API calls or spend

## Dependency

D4 may begin from the original request. It should be updated once D1 (DA-0001) is complete, as the requirements summary provides the definitive tenant isolation and tool approval model.

## Required output

`Projects/P-0001-AI-Voice-Virtual-Assistant/discovery/D4-security-assessment.md`

Route the completed deliverable to the PM. Flag any blocking finding immediately — do not wait for the due date.

## Stop conditions

- If a security risk cannot be resolved within discovery: document it as a blocker, escalate to PM immediately
- Any action that would require real data, external access, or spend: stop, escalate to PM
