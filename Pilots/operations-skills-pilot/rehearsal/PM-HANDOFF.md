# Operations skills rehearsal | OPS-001

The source is a synthetic invoice snapshot. The [local script](check_operations.py) contains the input rows, expected totals and raw finance inputs. It computes totals in currency minor units using the latest recorded revision per tenant and invoice. Expected totals are 6,500 for North and 3,500 for South. The fixtures include the same local invoice ID in two tenants, a late revision, a draft invoice, and duplicated input. Actual outcomes and script and report hashes are in [the run log](OBSERVED-CHECKS.txt). Finance example records are fictional and separate from the AUD 0 cash spent on this local exercise.

| Specialist | Hand-off exercised | Decision or limit |
|---|---|---|
| Data Engineer | Source grain is tenant plus invoice. Latest revisions correct the totals. Reconciliation detects a cross-tenant swap even though global totals match, and conflicting input revisions stop report generation. | Findings support the synthetic report only. Real access, workload, retention and deployment are outside the evidence. |
| Financial Analyst | Recompute the fictional cost from AUD 300 incurred, AUD 300 outstanding and AUD 200 uncommitted. | AUD 800 expected, AUD 900 downside. Variance is forecast minus the AUD 1,000 baseline, so -AUD 200 is under budget. The model separates the AUD 200 overlap. |
| Technical Writer | Version repair after a simulated superseded artifact. Link the new hash, contract and observed quantities. | This note documents observed local checks and labels the promotion examples as simulations. A real runbook would require owner confirmation and a rehearsal on its exact candidate. |
| Product Marketing | Draft a message tied to the verified capability. | “The example report totals posted invoices by tenant” is supportable within the fixture. A claim about faster reconciliation remains unmeasured. No outreach or publication occurred. |
| Legal Research and Drafting | Route any proposed external terms or claim through source and qualified review. | Legal triage uses the fictional case packets. This rehearsal supplies no real jurisdiction, evidence or human signoff for external use. |
| Deployment Engineer | Demonstrate matching report artifact bytes and rejection of a prior approval. | Release status stays at rehearsal. No real CEO Production approval, runtime environment, deployment, or support acceptance exists. |

The exact release gate outcomes are exercised in the separate [release cases](../cases/release-readiness.md). These observations support the local skill pilot. They cannot be used as readiness evidence for a live product.
