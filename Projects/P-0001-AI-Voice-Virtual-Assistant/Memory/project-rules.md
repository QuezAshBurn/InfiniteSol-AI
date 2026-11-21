# Project rules

**Project:** P-0001 AI Voice Virtual Assistant  
**Revision:** v1.0, 2026-11-21 AWST  
**Maintainers:** Business Analyst and Solution Architect

The following entries point to recorded project decisions and requirements. Decision IDs refer to the [project decision log](../project-record.md#decisions-and-approvals). D6 refers to [charter v1.2](../discovery/D6-draft-charter.md), whose approval section records the CEO's decision. Confirm the exact scope and current authority before each assignment. Verification links describe planned scenarios unless a separate results record is cited.

| ID and scope | Rule | Controlling source | Owner and verification reference |
|---|---|---|---|
| VA-CHANNEL-01, Phase 1 | Accept WhatsApp voice notes and send WhatsApp text replies. Reply in the detected language. Live calls and audio replies are Phase 2. | DEC-0011 and DEC-0012, D6 §3 | Solution Architect. [D5 v1.1](../discovery/D5-evidence-plan.md) E-008 and E-009. |
| VA-UX-01, all tenants | Introduce the assistant using the tenant-configured name and company. Offer booking, next available time, service information and other enquiries. Use the tone defined in the charter and stay calm when a customer is frustrated. | DEC-0010, D6 §§1–3 | Business Analyst. Verify the introduction, each menu path and tone. |
| VA-BOOK-01, all tenants | Require explicit customer confirmation at the Worker before calling `book_appointment`. The prompt alone cannot satisfy the gate. Confirm the booking to the customer only after the tool succeeds. | DEC-0007, D6 §§2 and 7 | Solution Architect. D5 E-001 and E-002. See the open double-confirmation decision below. |
| VA-BOOK-02, all tenants | On booking failure, automatically check for and offer the nearest available slot. Prevent duplicate bookings on retry and concurrent access. | D6 §§2–3 | Business Analyst and Solution Architect. Reconcile D5 E-003 and the build log before assigning QA coverage for recovery and duplicates. |
| VA-HANDOFF-01, all tenants | The approved handoff flow collects email and phone and flags the request to the tenant's designated contact for follow-up. Use synthetic contact details in project testing. | DEC-0010, D6 §3 and D1 v1.2 OQ-005 | Business Analyst. Verify the handoff record and recipient routing in approved testing. |
| VA-TEN-01, all tenants | Isolate tenant knowledge and calendars. Reject unrecognised tenant configuration, verify slot ownership before a booking write and recheck the tenant's tool approval before each call. | D6 §§2–3 and 7, SEC-001–003 | Solution Architect and Security Architect. D5 E-004 and E-006. |
| VA-KNOW-01, all tenants | Answer tenant-specific questions from that tenant's approved knowledge sources. Preserve source and revision references. | D6 §§2–3 | Business Analyst and Solution Architect. D5 E-005. |
| VA-SCOPE-01, project lifecycle | Keep spend within AUD 0 and obtain a separate CEO decision for any spend. Use the two synthetic tenants for build and evidence. Payment processing and real customer data are outside the recorded scope. | D6 §§3 and 10 | Project Manager and Financial Analyst. Verify the cost conditions and test data against the task approval. |

## Open decisions

- **OQ-001** remains open on whether a second customer confirmation is required. The BA and PM must record the disposition before work relies on double confirmation. [D6 §8](../discovery/D6-draft-charter.md#8-open-question-for-pm-before-story-writing)
- **OQ-002 to OQ-004** cover unrecognised-tenant wording, the minimum source relevance threshold and the exact confirmation keyword list. Treat those details as open until the relevant owner records a decision. [D1 v1.2](../discovery/D1-requirements.md)
- The PM reconciles approval references. The BA and QA reconcile mismatched scenario IDs before dependent verification. [Specialist role plan](../docs/specialist-role-plan.md#decisions-to-resolve-before-dependent-assignments-and-release)
