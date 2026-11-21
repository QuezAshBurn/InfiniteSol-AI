# Work authorization for the local memory, MCP and RAG pilot

**MEM-PILOT-A1 | Proposed | Awaiting CEO decision | 20 November 2026 AWST**

**Owner** Project Manager. **Decision owner** CEO. Decision and dispatch time to be recorded against this revision.

## Goal and authorized scope if approved

Demonstrate that an agent can retrieve the exact approved business rule for a synthetic tenant, then answer a related question using authorized sources it can cite.

The proposal covers discovery and a disposable local prototype in `Projects/memory-mcp-pilot/`. Use existing local tools, two synthetic tenants and a read-only MCP server over stdio. The proposed limit is two hours of pilot work after dispatch and AUD 0 in new cash spend. The scope ends on closeout, at the time limit or on any material scope change.

Use a versioned synthetic Markdown snapshot for rules and evidence. Add exact rule lookup first, then keyword and synonym retrieval against the same authorized snapshot. An optional dependency requires an identified licence, verified availability and zero new spend. The two model clients may receive only the synthetic context for their assigned scope. Keep production systems, real customer records, secrets, application changes and write-enabled MCP tools outside the pilot.

## Evidence required

| Check | Expected evidence |
|---|---|
| Exact rule | An authorized Tenant A lookup returns its approved override. An independently scoped Tenant B lookup returns the shared rule with exact source and revision. |
| Access and approval | A role or tenant outside the authorized scope gets no record details. Conflicting or stale authority and an unavailable snapshot return a blocker. |
| RAG | Known questions retrieve the expected approved sources with citations. A question with insufficient evidence identifies the gap. The exact lookup independently establishes the governing rule. |
| Host verification | Independent QA compares Codex and Claude Code results for the same authorized fixtures and records which client checks actually ran. |

The Solution Architect owns the prototype. The BA provides the synthetic rule examples. The Development owner records the commands and outputs, and independent QA verifies the results and source references. The PM records the approval, dispatch, evidence and closure under this project folder. Keep any unresolved check open.

**Controlling design reference** [Memory, MCP and RAG design](MEMORY-MCP-DESIGN.md), SHA-256 `6cb549f04814d227d6cbd78664498854f35d9efc0a6ccdafc6883e8b9860a12b`. This proposal is the first pilot authorization record. It takes effect only when a dated CEO approval is recorded against the exact revision and scope.
