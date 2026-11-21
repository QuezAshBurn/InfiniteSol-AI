# Work Authorization | REQ-0001 Discovery Authorization
# AI Voice Virtual Assistant

| Field | Value |
|---|---|
| **Request ID** | REQ-0001 |
| **Owner** | Project Manager |
| **Revision** | v1.0 |
| **Status** | READY FOR PM DISPATCH — all decisions recorded 2026-11-21 |
| **Received** | 2026-11-21 08:02 GMT+8 |
| **Portfolio entry** | `AI Team/starter/portfolio.md` row REQ-0001 |

---

## 1. Original request (preserved verbatim summary)

Build a multi-tenant voice assistant that helps customers schedule appointments. Introduces itself as a virtual assistant; hospitable, respectful, and jolly. Calm and helpful when a customer is frustrated or a booking fails.

**First booking flow** — understand requests like "next Friday after 3"; clarify ambiguous dates; check availability; offer a slot; repeat date, time, and service for confirmation; say "you're booked" only after the booking tool returns success; handle unavailable slots, failed bookings, and requests to speak to a person.

**Tenant-specific RAG** — each tenant has its own approved knowledge sources for services, business hours, FAQs, and policies; tenant identity set through trusted application configuration; retrieval limited to the assigned tenant's approved sources; source and revision references kept for verification; missing or conflicting evidence triggers clarification or human handoff; live scheduling tool used for availability.

**MCP automation** — start with two narrowly scoped tools: `check_availability` and `book_appointment`; verify current approval and tenant scope on each call; require explicit customer confirmation before changing the calendar; recheck slot and handle retries without duplicate bookings; reminders, cancellations, rescheduling, and support tickets assessed as optional tools for separate scope decisions.

**Budget** — AUD 0 out-of-pocket for development, deployment, and ongoing operation of the first version. Assess local browser demo, local voice components, local retrieval, and test calendar on existing equipment. Identify hardware and service assumptions. Flag any capability that cannot meet the budget.

**Discovery evidence requested** — two synthetic tenants giving different answers to the same FAQ; verify: tenant isolation, missing-evidence handling, revoked tool approvals, booking accuracy, duplicate prevention, and assistant tone during interruptions.

---

## 2. Proposed discovery scope

### Architectural direction (DEC-0006, recorded 2026-11-21)

The CEO has stated a preference for **SaaS architecture if feasible within AUD 0**. The Solution Architect must assess free-tier hosted options as the primary direction. If SaaS cannot meet AUD 0 for any required environment, the Architect documents the gap and cost, and local-only deployment remains the fallback. This direction does not change the discovery scope or spend limit.

### In scope
- Document the booking dialogue rules and confirmation logic (first booking flow)
- Document tenant isolation model: how tenant identity is set and enforced before any retrieval or tool call
- Assess open-source, AUD 0 options for each component: voice input/output, RAG retrieval, local LLM or API, test calendar
- Draft the architecture brief with component choices and a local-deployment map
- Assess AUD 0 feasibility separately for development, local demo, and any future hosted environment
- Identify all hardware and service assumptions required for each feasibility claim
- Draft the discovery evidence plan with test scenarios for two synthetic tenants
- Identify and record any capability that cannot meet the AUD 0 constraint

### Out of scope for discovery
- Implementation, prototype execution, or build of any component
- Real customer data or live calendar systems
- External service sign-ups, API key purchases, or any spend
- Prototype execution (requires a separate CEO-approved prototype authorization)
- Deployment environment setup of any kind

---

## 3. Deliverables

| # | Deliverable | Owner | Form |
|---|---|---|---|
| D1 | Requirements summary: booking flow rules, tenant isolation model, RAG source model, tool approval and retry model | BA | Markdown |
| D2 | Architecture brief: component options, local deployment map, AUD 0 feasibility assessment per environment, hardware assumptions | Solution Architect | Markdown |
| D3 | Risk register: capabilities that cannot meet AUD 0, known gaps, hardware assumption dependencies | PM + Architect | Markdown |
| D4 | Security and tenant-isolation assessment: data handling, isolation enforcement, tool approval model | Security Architect | Markdown |
| D5 | Discovery evidence plan: test scenarios for each evidence item in §6, expected inputs/outputs, synthetic data description | BA + Architect | Markdown |
| D6 | Draft project charter (not approved): scope, measurable acceptance criteria, exclusions, AUD 0 budget, milestones, risks, alternatives | PM | Markdown |

All deliverables go to `Projects/<assigned ID>/` after the PM assigns a project ID.

---

## 4. Time limit

Proposed discovery window: **5 business days** from CEO approval date.  
Discovery spend cap: **AUD 0** (no exceptions without a separate CEO decision).  
Discovery time cap per portfolio allowance: **[CEO to confirm — record in portfolio Discovery Allowance table].**

---

## 5. Spend limit

**AUD 0.** No new software purchases, subscriptions, API credits, hardware, or cloud services.  
Discovery uses existing local equipment only.  
The Solution Architect must assess and document feasibility separately for each environment (development, demo, production-equivalent) before any build commitment is made.  
If any required component cannot operate within AUD 0 and existing hardware, that capability is flagged as a gap and escalated to the CEO before the discovery proposal is submitted.

---

## 6. Expected evidence

The discovery team will document the following test scenarios in the evidence plan (D5). No code runs until a prototype authorization is separately approved. These define what a later prototype or build must demonstrate.

| # | Evidence item | Test method | Data |
|---|---|---|---|
| E1 | Tenant A and Tenant B return different answers to the same FAQ question | Same query routed to each tenant's isolated knowledge source | Synthetic |
| E2 | Tenant isolation: Tenant A's data never appears in a Tenant B query response | Query containing a keyword present only in Tenant A's approved sources, routed as Tenant B | Synthetic |
| E3 | Missing-evidence handling: assistant asks for clarification or offers human handoff when no approved evidence exists | Query for which neither tenant has an approved source entry | Synthetic |
| E4 | Revoked tool approval: `check_availability` and `book_appointment` reject calls when the tenant's approval flag is false | Mock tool returning revoked-approval state; assistant must not proceed | Synthetic |
| E5 | Booking accuracy: assistant confirms correct date, time, and service only after tool returns success | Synthetic calendar tool returning success; verify confirmation matches the offered slot | Synthetic |
| E6 | Duplicate prevention: a second booking attempt for an already-booked slot does not create a duplicate | Synthetic tool returning already-booked state on second call | Synthetic |
| E7 | Tone during frustration/interruption: assistant remains calm, helpful, and does not escalate or abandon the booking | Synthetic customer input expressing frustration mid-booking flow | Synthetic |

---

## 7. Required specialist assignments (if approved)

Triggered by `START-HERE.md` specialist review table:

| Trigger | Specialist | Timing |
|---|---|---|
| External collection or transfer of personal data; material tenant-isolation change | Security Architect | At design (D2, D4); before any build approval |
| New interface between projects or systems (voice, RAG, MCP tools, calendar) | Solution Architect | At design (D2); before integration |

No payment processing, schema migration, pipeline/BI, commercial product, or marketing publication triggers apply at discovery stage.

---

## 8. Allowed actions (if approved)

- **PM:** log request; assign discovery work to BA, Solution Architect, Security Architect within approved scope and time cap; track deliverables; submit proposal to CEO
- **BA:** elicit and document requirements; challenge assumptions; draft D1 and D5; no implementation
- **Solution Architect:** assess open-source components; draft D2; document AUD 0 feasibility; no implementation
- **Security Architect:** assess tenant isolation and data handling; draft D4; no implementation
- **All discovery roles:** read authorised sources; use synthetic data only; no live credentials, real customer data, or external commitments; no spend

---

## 9. Exclusions

- No implementation, prototype execution, or build work — requires a separate CEO-approved authorization
- No external API calls, service sign-ups, or any spend
- No production, staging, or test environment provisioning (discovery documents only)
- No real calendar, customer, or personal data

---

## 10. Stop and escalation conditions

- Discovery forecast to exceed approved time or AUD 0 cap: **stop, escalate to CEO before continuing**
- Any component identified that cannot meet AUD 0 for any required environment: **document gap, escalate to CEO, do not proceed past that component**
- Hardware assumption invalidated (equipment unavailable or insufficient): **stop, record gap, escalate**
- Security or privacy concern with tenant isolation design: **stop, escalate immediately**

---

## 11. Decisions the CEO must make

| # | Decision | Context |
|---|---|---|
| **A** | **Approve, reject, or amend this authorization** | Record against exact revision v1.0. Work may not begin until this decision is recorded. |
| **B** | **Discovery time cap** | What is the approved time allowance for REQ-0001 (hours or business days)? Record in portfolio Discovery Allowance table. |
| **C** | **Hardware assumptions** | What local equipment is available for the demo (approximate RAM, GPU if any, storage, OS)? This determines which AUD 0 voice and RAG components are feasible. If unknown, the Architect will document the assumption and flag it as unverified. |
| **D** | **Prototype scope within discovery** | Does the CEO authorise the BA and Architect to run a bounded local prototype within the discovery timebox, or must prototype authorization be a separate CEO decision after the proposal is submitted? |
| **E** | **Portfolio priority** | No other build is currently active. Confirm REQ-0001 receives discovery priority, or state if another request should go first. |

---

## 12. Approval

| Field | Value |
|---|---|
| Approver | CEO / Operator |
| Decision | **APPROVED** — revision v1.0 |
| Date | 2026-11-21 |
| Approved revision | v1.0 |
| Amended limits | None stated |
| Authority delegated | None — scope, spend, and production decisions remain with the CEO |

### Skill verification record

| Field | Value |
|---|---|
| Skill | task-intake |
| Version | 0.1.0 |
| Source pack | 6278e4f6664daa97 |
| Manifest SHA-256 | 758ce73cef1238e67667325af51b4f3e42a6180240912a2acab62b6e4d60301d |
| Pin source | `Pilots/operations-skills-pilot/MANIFESTS.md` |
| Verification result | PASS |

---

## 13. Intake disposition

**Decision A — APPROVED** by CEO, 2026-11-21, against revision v1.0.

**Decisions B–E — RECORDED 2026-11-21.**

| Decision | CEO answer | Recorded |
|---|---|---|
| B — Discovery time cap | 5 business days from 2026-11-21 (expires 2026-11-28) | 2026-11-21 |
| C — Hardware available | 8 GB RAM or less. Architect must document this constraint in D2 and flag any AUD 0 component that does not fit. | 2026-11-21 |
| D — Prototype scope within discovery | Included in discovery timebox. Architect may run a local, synthetic-data-only prototype within the 5-day window and AUD 0 limit. No additional authorization required. | 2026-11-21 |
| E — Portfolio priority | Confirmed — REQ-0001 is first priority. | 2026-11-21 |

**Next owner:** PM — dispatch discovery roles per §8.

---

**READY FOR PM DISPATCH**

All decisions recorded. PM to assign BA, Solution Architect, and Security Architect to discovery within approved scope, time (by 2026-11-28), and AUD 0 spend limit.
