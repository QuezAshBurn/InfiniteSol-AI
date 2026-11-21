# DEL-001 | Exclude archived pending orders

Revision S1. Derived from [the request](REQUEST.md) and [the Business Analyst draft](STORY-DRAFT.md). The draft used `story-specification` v0.1.0. The PM checked the draft against the approved-work policy, business analyst role and goal-and-quality workflow from source pack `6278e4f6664daa97` before dispatch.

Goal: return the number of orders with exact status `pending` that are active. A boolean `archived` value of `True` marks an archived order. A missing value or `False` marks an active order. Other values are outside this pilot's input contract. Preserve the input order data, function signature and all existing tests. Use standard-library Python only. Capture the original baseline, then reproduce the missing archived-order exclusion with a test before changing the helper.

| Criterion | Required result |
|---|---|
| AC-1 | One archived pending order and one active pending order count as 1. All archived pending orders count as 0. |
| AC-2 | Orders without an archive key still count as active when pending. An archived pending and a legacy pending order count as 1. |
| AC-3 | Other statuses, alternative capitalisations, whitespace variants and empty input contribute 0. |
| AC-4 | Counting leaves the input list and records exactly as supplied. Existing tests continue to pass. |

Implementation scope covers `src/orders.py` and `tests/test_orders.py` only. Evidence records are separate. Budget AUD 0 new spend. No dependency, customer, integration, deployment or Production changes. Developer hands the exact candidate and test evidence to the independent counterpart. QA checks the same candidate and returns a verdict to the PM.
