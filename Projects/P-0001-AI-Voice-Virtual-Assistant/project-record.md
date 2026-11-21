# Project record | P-0001

- **Title:** AI Voice Virtual Assistant
- **Requested outcome:** Multi-tenant voice assistant that helps customers schedule appointments; hospitable, respectful, and jolly; calm and helpful when frustrated; AUD 0 development, deployment, and operation
- **Original request:** REQ-0001, received 2026-11-21 08:02 GMT+8 — full text preserved in `AI Team/starter/REQ-0001-discovery-auth.md`
- **Requester:** CEO / Operator
- **Project owner:** Project Manager
- **Priority:** 1 — only active project
- **Stage:** Build — CEO approved D6 v1.2 on 2026-11-21
- **Trusted source locations:** `Projects/P-0001-AI-Voice-Virtual-Assistant/` (project files); `AI Team/` (policies, templates, roles, workflows); synthetic data only during discovery
- **Permitted tools:** Read, Edit, Write for authorised paths; no external API calls, no spend, no live data
- **Scope:** See `AI Team/starter/REQ-0001-discovery-auth.md` §2
- **Exclusions:** See `AI Team/starter/REQ-0001-discovery-auth.md` §9
- **Budget ceiling:** AUD 0 (all environments, all lifecycle stages); no spend without separate CEO approval
- **Authoritative approval:** `AI Team/starter/REQ-0001-discovery-auth.md` v1.0, CEO approved 2026-11-21
- **Document register:** `Projects/P-0001-AI-Voice-Virtual-Assistant/docs/document-register.md`

## Team assignments

Formal role assignments added 2026-11-21 (role catalog v1.8 — includes roles 15–22). The Solution Architect defines project-specific role descriptions in `docs/roles/`. The PM records the approval before dispatching each role. UI Designer, Conversion Expert, SEO Expert, AI Search Expert, and Content Strategist are not assigned at this phase (no visual surface; no public launch; no pipeline).

| Role | Company prompt | Phase | Owner (runtime) | Primary deliverable | Status |
|---|---|---|---|---|---|
| Project Manager | `AI Team/roles/01-project-manager.md` | All | PM | Project record, gates, CEO updates | Active |
| Business Analyst | `AI Team/roles/02-business-analyst.md` | Discovery, Build | BA | D1 requirements, D5 evidence plan, acceptance criteria | Active |
| Solution Architect | `AI Team/roles/03-solution-architect.md` | Discovery, Build | Architect | D2 architecture brief, DEC series, role descriptions | Active |
| Database Architect | `AI Team/roles/04-database-architect.md` | Build | DB Architect | Schema review (schema.sql), migration notes | Active |
| Security Architect | `AI Team/roles/05-security-architect.md` | Discovery, Build | Security Architect | D4 security assessment, SEC-001–005 build controls | Active |
| Tech Lead | `AI Team/roles/15-tech-lead.md` | Build | Tech Lead | Implementation sequence, conformance review, dev guidance | Active |
| UX Designer | `AI Team/roles/16-ux-designer.md` | Build | UX Designer | D7 conversation design (turn-taking, state map, persona, recovery) | Active |
| Copywriter | `AI Team/roles/18-copywriter.md` | Build | Copywriter | D8 copy deck (all VA utterances, tone guide, multilingual) | Active |
| Senior Full Stack Developer A | `AI Team/roles/06-senior-full-stack-developer-a.md` | Build | Dev A | Worker source author (index.js, llm.js, tools.js, whatsapp.js, gate.js) | Active |
| Senior Full Stack Developer B | `AI Team/roles/07-senior-full-stack-developer-b.md` | Build | Dev B | Independent peer review of Worker source | Active |
| QA Engineer | `AI Team/roles/08-qa-engineer.md` | Build, Evidence | QA | Independent verification of E-001 to E-009 | Active |
| Technical Writer | `AI Team/roles/09-technical-writer.md` | All | Tech Writer | Document register, versioned documentation index | Active |
| Deployment Engineer | `AI Team/roles/13-deployment-engineer.md` | Build, Release | Deploy Eng | BUILD-LOG deployment checklist, staging rehearsal | Active |

Project role descriptions are stored in `Projects/P-0001-AI-Voice-Virtual-Assistant/docs/roles/`.

## Decisions and approvals

| ID | Date and zone | Decision required | Decision owner and authority | Scope/budget/version affected | Decision / limitations | Supporting evidence |
|---|---|---|---|---|---|---|
| DEC-0001 | 2026-11-21 GMT+8 | Approve discovery authorization | CEO | REQ-0001 discovery scope, AUD 0, 5 business days | APPROVED — revision v1.0 | `REQ-0001-discovery-auth.md` §12 |
| DEC-0002 | 2026-11-21 GMT+8 | Discovery time cap | CEO | P-0001 discovery allowance | 5 business days (expires 2026-11-28) | `REQ-0001-discovery-auth.md` §13 |
| DEC-0003 | 2026-11-21 GMT+8 | Hardware assumption | CEO | Architecture feasibility (D2) | 8 GB RAM or less; Architect to document constraint and gaps | `REQ-0001-discovery-auth.md` §13 |
| DEC-0004 | 2026-11-21 GMT+8 | Prototype scope within discovery | CEO | Discovery timebox | Included; Architect may run local synthetic-data-only prototype within 5-day AUD 0 window | `REQ-0001-discovery-auth.md` §13 |
| DEC-0005 | 2026-11-21 GMT+8 | Portfolio priority | CEO | Build scheduling | Confirmed — P-0001 first priority | `REQ-0001-discovery-auth.md` §13 |
| DEC-0006 | 2026-11-21 GMT+8 | Architectural direction | CEO | DA-0002 scope; feasibility framing | SaaS-first if feasible within AUD 0. Architect must assess free-tier hosted options as the primary direction and flag any cost gap. Local-only remains the fallback if SaaS cannot meet AUD 0. | CEO instruction 2026-11-21 |
| DEC-0007 | 2026-11-21 GMT+8 | Confirmation gate architecture requirement | CEO | Build scope; Worker design | APPROVED — R-001 mandatory: Worker must enforce a keyword confirmation gate before executing book_appointment, independent of the LLM. Prompt-level gate alone is insufficient (prototype confirmed GAP-005). | PROTOTYPE-LOG.md F-001, R-001 |
| DEC-0008 | 2026-11-21 GMT+8 | SaaS prototype account creation | CEO | Prototype scope; AUD 0 budget | COMPLETE — Groq free-tier account created 2026-11-21 (emersonricaza@gmail.com, Personal / Default Project). Cloudflare free-tier account created 2026-11-21 (emersonricaza@gmail.com, account ID 11a072cb00f0cc8f965b56dad967e6e5). No credit card required; AUD 0 budget satisfied. | CEO instruction 2026-11-21 |
| DEC-0009 | 2026-11-21 GMT+8 | Web Speech API privacy tradeoff (OQ-D4-001) | CEO | SaaS prototype STT approach; GAP-001; SEC-004 | ACCEPTED for prototype — Web Speech API permitted on SaaS track. Customer voice is sent to Google for transcription. Tenants must disclose this in their privacy policy before production use. Alternative STT (Whisper.cpp or Workers AI audio) to be evaluated at build if production privacy requirements change. | D4 SEC-004; CEO instruction 2026-11-21 |
| DEC-0010 | 2026-11-21 GMT+8 | VA introduction, main menu options, and human handoff mechanism (OQ-005) | CEO | D1 v1.1; D6 v1.1; dialogue scope | APPROVED — (1) VA introduction: "Hi, this is [VA Name] from [Company], your Voice Assistant, how can I help you?" — name and company from tenant config. (2) Main menu: four options — book a schedule, suggest a schedule (find next available slot unprompted), other services, information about services. (3) Human handoff: VA collects customer email and phone; flags to tenant PM for follow-up. OQ-005 resolved. | CEO instruction 2026-11-21 (pre-charter approval) |
| DEC-0011 | 2026-11-21 GMT+8 | Voice delivery channel — WhatsApp replaces browser Web Speech API | CEO | D2; D6 §3; DEC-0009 superseded | APPROVED — Phase 1: WhatsApp Business Cloud API (Meta free tier). Customer sends voice note → Cloudflare Worker webhook receives audio → Groq Whisper STT transcribes → LLM processes → VA replies as WhatsApp text message. VA does NOT send audio back in phase 1. Phase 2: Twilio voice (live call, real-time) — separate CEO budget decision required when ready. DEC-0009 (Web Speech API) SUPERSEDED for SaaS track. | CEO instruction 2026-11-21 (pre-charter approval) |
| DEC-0012 | 2026-11-21 GMT+8 | Multi-language support added to scope | CEO | D1; D2; D6 §3; previously out of scope | APPROVED — Groq Whisper auto-detects customer language from voice note. LLM responds in the same detected language. No explicit language selection UI required in phase 1. Multi-language moves from out-of-scope to in-scope. | CEO instruction 2026-11-21 (pre-charter approval) |

## Risks, dependencies and blocked work

| ID | Observed issue or dependency | Severity / confidence | Impact | Evidence | Accountable owner | Next check / next date | State |
|---|---|---|---|---|---|---|---|
| RSK-0001 | 8 GB RAM may exclude local LLM options sufficient for real-time voice + RAG | High / Assumed | May require API-based LLM or cloud dependency; could conflict with AUD 0 | CEO confirmed 8 GB; Architect to assess in D2 | Solution Architect | D2 delivery | Open |
| RSK-0002 | Real-time voice input/output on AUD 0 may require browser-based Web Speech API; quality and offline limits unconfirmed | Medium / Assumed | Demo quality may be limited; not suitable for production without further assessment | Architect to assess | Solution Architect | D2 delivery | Open |
| RSK-0003 | Test calendar service: AUD 0 synthetic calendar must be confirmed functional before evidence plan (D5) is drafted | Low / Assumed | Evidence plan cannot be completed without a confirmed test calendar approach | Architect to assess | Solution Architect | D2 delivery | Open |
| DEP-0001 | Architecture brief (D2) must precede evidence plan (D5) — hardware feasibility drives test scenario design | — | D5 blocked until D2 is confirmed | Logical dependency | PM | D2 delivery | Open |

## Specialist review applicability

| Trigger or documented reason it does not apply | Specialist | Required gate | Evidence and disposition | Follow-up owner |
|---|---|---|---|---|
| External collection / transfer of personal data; material tenant-isolation change | Security Architect | At design (D4); before build approval | Pending — discovery assignment issued | Security Architect |
| New interface between projects or systems (voice, RAG, MCP tools, calendar) | Solution Architect | At design (D2); before integration | Pending — discovery assignment issued | Solution Architect |
| Payment processing | Not triggered | — | No payment feature in scope | — |
| Schema migration / backfill | Not triggered | — | No database schema in scope at discovery stage | — |
| Commercial product / marketing | Not triggered | — | No commercial terms or marketing publication at discovery stage | — |

## Discovery assignments

| Assignment ID | Deliverable | Owner role | Due | Status |
|---|---|---|---|---|
| DA-0001 | D1 — Requirements summary (booking flow, tenant isolation, RAG source model, tool approval model) | Business Analyst | 2026-11-28 | Complete — D1 v1.0 delivered 2026-11-21; 5 open questions for PM (OQ-001 to OQ-005) |
| DA-0002 | D2 — Architecture brief (component options, AUD 0 feasibility per environment, 8 GB constraint, hardware assumptions) + prototype execution | Solution Architect | 2026-11-28 | Complete — D2 v1.0 delivered 2026-11-21; prototype run 2026-11-21; findings in PROTOTYPE-LOG.md; GAP-005 CONFIRMED; R-001 required at build |
| DA-0003 | D3 — Risk register (compiled from D1, D2, D4 findings) | PM (compiled from specialist inputs) | 2026-11-28 | Complete — D3 v1.0 delivered 2026-11-21; 17 risks; 1 open CEO decision (RSK-013 human handoff) |
| DA-0004 | D4 — Security and tenant-isolation assessment | Security Architect | 2026-11-28 | Complete — D4 v1.0 delivered 2026-11-21; SEC-004 resolved (DEC-0009); 3 build controls remaining |
| DA-0005 | D5 — Discovery evidence plan | Business Analyst | 2026-11-28 | Complete — D5 v1.0 delivered 2026-11-21; 7 scenarios; 2 synthetic tenants (T1, T2) |
| DA-0006 | D6 — Draft project charter | PM | 2026-11-28 | Complete — D6 v1.2 delivered 2026-11-21; CEO BUILD APPROVED 2026-11-21 |
| DA-0007 | D7 — Conversation design (state map, turn spec, recovery, QA hooks) | UX Designer | Build phase | In progress — D7 v1.0 delivered 2026-11-21; awaiting Tech Lead system prompt review and QA scenario confirmation |
| DA-0008 | D8 — Copy deck (all VA utterances, tone guide, multilingual guidance) | Copywriter | Build phase | In progress — D8 v1.0 delivered 2026-11-21; OQ-D8-001 raised (R-001 keyword gate English-only — blocks E-008 multi-language confirmation); awaiting Tech Lead and UX Designer review |

## Reviews and learning

| Review ID / round | Candidate revision | Author / runtime | Reviewer / runtime | Findings / evidence | Correction or rebuttal | Disposition / date | Follow-up |
|---|---|---|---|---|---|---|---|
| (none yet) | | | | | | | |

## Release checklist

*(Not applicable at discovery stage.)*

## Change, build and documentation register

| Task / requirement | Change and before / after impact | Source or build revision | Build command or CI job and environment | Result and artifact or log | Technical change record / docs | Reviewer and disposition |
|---|---|---|---|---|---|---|
| (none yet — discovery only) | | | | | | |
