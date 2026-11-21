# Local MCP pilot authorization

**MEM-PILOT-A1-M2 | Proposed | Awaiting CEO decision | 20 November 2026 AWST**

**Owner** Project Manager. **Decision owner** CEO. Record the dated decision against this exact revision before dispatch.

## Goal and scope if approved

Verify that a local MCP client can retrieve the exact rule and evidence for an authorized synthetic tenant through one read-only tool, `resolve_business_rule`.

The proposed assignment covers local discovery, implementation of a disposable MCP prototype over stdio, and scoped verification under `Projects/memory-mcp-pilot/mcp/`. Store the approval, evidence and closeout in the same project. The proposed limit is two hours after PM dispatch and AUD 0 in new cash spend. The scope ends at the time limit, closeout or a material change. Identify any open-source dependency, its availability and licence before relying on it.

Use only synthetic data. Bind the role, project, tenant and approval scope in trusted launch configuration. The tool accepts the rule ID. Verify the current action approval and its exact revision before each applicable read, including subsequent calls in a running session. Record a minimal local audit event with scope, rule ID, outcome and revision where available. Keep real data, credentials, write actions, hosted servers and RAG outside this assignment.

Use a separate synthetic fixture to verify the protocol and approval gate while the prior memory candidate awaits counterpart review. Connecting the reviewed memory candidate requires its exact peer disposition and PM confirmation. The proposed host checks use only permitted synthetic evidence and must record what ran separately for Codex and Claude Code.

## Acceptance criteria

| Check | Evidence required |
|---|---|
| MCP protocol | A local client can list the single read-only tool, call it by rule ID and receive a structured result. |
| Rule and provenance | Two separately scoped launches return the expected tenant override and shared default, each with the rule revision, source and approval evidence. Record whether the run used the separate fixture or the reviewed memory candidate. |
| Approval enforcement | Calls with no current approval, mismatched scope, or expired or revoked approval return a blocker. Demonstrate revocation between two requests in the same session. |
| Scope and limits | The client cannot set tenant or grant fields. The configured caller sees only its authorized fixture results. Audit events omit rule text and secrets. |
| Independent verification | QA independently reruns the local checks. Record Codex and Claude Code host call results and the current counterpart disposition before claiming the integrated pilot is complete. |

The Solution Architect owns the MCP boundary. Development records the exact candidate and observed outcomes. Independent QA verifies them. The PM records the approval, dispatch, blocked items and closure.

## Controlling references

- [Memory, MCP and RAG design](MEMORY-MCP-DESIGN.md), SHA-256 `6cb549f04814d227d6cbd78664498854f35d9efc0a6ccdafc6883e8b9860a12b`.
- [Approval and evidence gate](APPROVAL-AND-EVIDENCE.md), SHA-256 `5523ec3e8b4d45fe716fe4d017789963f720b7f9f541e1807aa6edcb7675963e`.
- [Memory prototype results](MEMORY-PROTOTYPE-RESULTS.md), including the open counterpart review for candidate `fcb3cd28ffca8046a01d47f66eece989a924ad13da7900d4d99ec29722fb8a60`.
