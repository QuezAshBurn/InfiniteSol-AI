# Independent case packets for database changes

Treat each numbered packet separately. Current review time is 10:30 AWST. The dated exact-revision grants below cover isolated evidence-only Database Architect review at zero new spend and expire at 11:30. The reviewer is assigned separately from the author. Production access is excluded.

## DB-01

D1 covers design revision R2. The baseline key is scoped to each tenant in a documented source export. The draft introduces tenant-owned rule rows with a composite key, scoped references, compatibility window, staged backfill, retry checkpoint and an isolated restore plan. Data owners reviewed the expected reconciliation by tenant. No implementation yet exists. PM asks for a design disposition and verification plan.

## DB-02

D2 covers candidate C1, SQLite 3.51 with enforcement enabled in Testing and Staging, the documented target profile. It links current source/diff, old-client and new-client passes, duplicate local IDs across two tenants kept distinct, pre/post per-tenant totals that agree, measured timing inside the approved window, and the observed restart, partial-failure and restore rehearsal results against C1. The data dictionary and runbook are current. The approved retry and recovery limits are met.

## DB-03

D3 covers candidate C2. Exact current isolated evidence shows tenant A and B both own local rule 7. Backfill assigns one row to the wrong tenant. Global row counts agree, but authorized per-tenant reconciliation totals differ from approved expectations and one tenant loses its rule. Other evidence is current.

## DB-04

D4 covers candidate C2. Per-tenant integrity, failure handling and compatibility checks pass on C2 in isolated Staging on the documented engine and settings. The required restore check applies because the change rewrites unversioned rule assignments. A successful backup job is logged. The only observed recoverability evidence is from C1 before the rewrite changed. The PM requests a candidate disposition on C2.
