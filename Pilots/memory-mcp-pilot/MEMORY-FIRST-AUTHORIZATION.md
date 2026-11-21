# Local memory prototype authorization

**MEM-PILOT-A1-M1 | Approved for the memory slice | 20 November 2026 AWST**

The CEO's instruction, “Ok lets work with memory first”, authorizes the memory slice of [MEM-PILOT-A1](PILOT-AUTHORIZATION.md). The approval covers the activities and boundaries below. All rule and approval data in the prototype are synthetic. The broader proposal remains at draft stage.

**Controlling design** [Memory, MCP and RAG design](MEMORY-MCP-DESIGN.md), SHA-256 `6cb549f04814d227d6cbd78664498854f35d9efc0a6ccdafc6883e8b9860a12b`.

**Goal** Read versioned Markdown from a pinned local snapshot and show which approved invoicing rule applies to each of two synthetic tenants, with its source and approval reference.

**Scope** Write the synthetic records, approval fixtures, snapshot manifest, dependency-free Python exact lookup and local tests under `Projects/memory-mcp-pilot/memory/`. Record proof and closeout under `Projects/memory-mcp-pilot/`. Use existing tooling and the proposed AUD 0 new cash limit. Dispatch ends at the two-hour work limit, closeout or a material scope change. Maintain a read-only lookup interface. MCP transport, RAG, model-client testing and real data require their separate approved assignment.

**Acceptance** Tenant A receives its approved invoice exception. Tenant B receives the shared rule. Both tenants receive the same platform invariant. Unscoped requests, inconsistent approvals, conflicting applicable rules and missing or changed sources fail explicitly. Timing applies to a pinned snapshot and the same lookup time.

**Roles and evidence** The Solution Architect owns the prototype. The BA owns the synthetic business rule definitions. Development records code, checks and outputs. A separate verification pass checks observed results. The PM closes the authorized memory slice against that evidence.
