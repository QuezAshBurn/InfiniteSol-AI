# Approval and evidence gate for memory, MCP and RAG

20 November 2026 AWST. This note records how InfiniteSol's [approved-work policy](../../AI%20Team/policies/APPROVED-WORK.md) applies to the [memory, MCP and RAG architecture](MEMORY-MCP-DESIGN.md).

**No approved Markdown, no project work.** This applies to discovery, analysis, design, coding, testing, deployment, and changes to memory or retrieval settings. Before approval, the PM can log the request and prepare the proposed authorization for decision.

## Before starting or resuming

1. Confirm the exact current Markdown revision, dated decision, authorized approver and any delegated authority. Check that it covers the assigned role, action, project, tenant, data, environment, permitted tools, time and spend where applicable.
2. Identify the approved inputs that govern the task, including the business rules, coding standard and chosen delivery practices where relevant. Pin their versions and record what will demonstrate the task is done.
3. If the authorization is missing, expired, superseded, conflicting, incomplete or out of scope, mark the task `BLOCKED`. Give the PM the specific gap and the decision needed. Resume only with the current authorization and evidence for the affected checks.

## What an agent may claim

| Record or evidence | How the agent uses it |
|---|---|
| Approved decision or requirement | Cite the approved record and exact revision for what is authorized or expected. |
| Observed test or implementation result | Cite the actual input, candidate, environment and result for what was verified. |
| Draft, hypothesis or incomplete evidence | Label it as proposed or unverified. Disclose the gap and route it to the owner if it affects the work. |

Memory supplies versioned records. MCP applies the scoped access path. RAG finds passages and helps explain them. Retrieval, chat history, an inference or a proposed change carries no authority to act. An approved plan authorizes its stated actions. Claims about actual behavior require evidence of that behavior.

**Example.** If RAG retrieves a draft tenant invoicing exception, the PM first verifies which approved rule applies to that tenant and whether the requested change has its own approval. A missing or conflicting governing record blocks the affected work. A passing test can be reported only with observed results on the affected candidate.

When runtime enforcement is built under approved scope, QA verifies that a missing or mismatched approval blocks both direct memory lookup where work authorization is required and access through MCP. QA also checks that RAG labels unsupported claims and keeps exact source and revision references for factual answers.
