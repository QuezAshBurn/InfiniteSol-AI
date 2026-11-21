# Tenant rules

**Project:** P-0001 AI Voice Virtual Assistant  
**Revision:** v1.0, 2026-11-21 AWST  
**Maintainers:** Business Analyst and designated tenant owner

The [charter v1.2](../discovery/D6-draft-charter.md) identifies two synthetic tenants for build and verification, T1 Riverside Hair Studio and T2 Peak Physio Clinic. Their fixture settings are test data. The register currently contains no approved tenant-specific exceptions.

| Scope | Configurable item | Source and approval owner |
|---|---|---|
| Each tenant | Assistant name and company name used in the introduction. | DEC-0010 and D6 §3. The designated tenant owner confirms values. |
| Each tenant | Its own approved source set, including services, pricing, FAQs, policies and hours where available. Record source owner, revision, approval and retirement date when applicable. | D6 §§2–3 and [D1 v1.2 §3](../discovery/D1-requirements.md#3-rag-source-model). The tenant operator identifies approved sources. |
| Each tenant | Separate calendar and tool approval settings. Record the scoped configuration source and approval before relying on it. | D6 §§2–3 and 7. The Solution Architect and Security Architect verify isolation and per-call approval. |

The [shared project rules](project-rules.md) apply to both tenants, including confirmation, slot ownership and data isolation. Use a tenant override only when the project permits one and the PM can cite its approval, exact scope and effective period. Escalate conflicts and missing authority before implementation or use.
