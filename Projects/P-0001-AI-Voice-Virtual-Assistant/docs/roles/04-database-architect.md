# P-0001 Project Role Description — Database Architect

| Field | Detail |
|---|---|
| Project and role | P-0001 AI Voice Virtual Assistant · Database Architect · Company role 04 · `AI Team/roles/04-database-architect.md` |
| Document control | Owner: DB Architect · Revision: 1.0 · Date: 2026-11-21 · Status: Active · Review trigger: schema change |
| Assignment purpose | Own schema design integrity, migration safety, and persistence rules for P-0001. Active during build. Schema already authored; role owns review and sign-off. Links: `build/db/schema.sql` |
| Industry competence | Appointment booking persistence: slot availability, duplicate booking prevention, idempotency, human handoff records, knowledge sources. Multi-tenant data isolation (tenant_id on every table). |
| Technical competence | **Cloudflare D1** (SQLite-compatible, batch writes, `INSERT OR REPLACE`, UNIQUE constraints). Schema tables: `tenants`, `tool_approvals`, `services`, `time_slots`, `bookings`, `handoff_requests`, `knowledge_sources`. Idempotency key on `bookings` (UNIQUE `idempotency_key = tenant_id:slot_id`). Indexes: `idx_time_slots_tenant_available`, `idx_bookings_tenant`. |
| Evidence of readiness | `build/db/schema.sql` delivered 2026-11-21. T1 (`seed-t1.sql`) and T2 (`seed-t2.sql`) seed data delivered 2026-11-21. |
| Responsibilities and limits | Reviews schema for integrity, tenant isolation, idempotency, and migration safety. Does not alter production data. Routes any breaking schema change through PM and Solution Architect. |
| Development skill requirements | None (review role at build). |
| Outputs and acceptance | Schema review record (to be completed before staging). Accepted when: tenant_id isolation confirmed on all tables, idempotency_key UNIQUE constraint verified, no unindexed join on hot queries. |
| Handoffs and escalation | Schema review → Tech Lead (implementation). Migration notes → Deployment Engineer. Escalates integrity risks to PM. |
