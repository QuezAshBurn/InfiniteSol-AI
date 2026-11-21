# Ways of working and applied study

Use Agile principles as a delivery mindset and the smallest set of practices that solves the project's coordination, quality or service needs. The PM records the choices, their purpose, who is accountable and when the team will reassess. Keep one project record, one ordered delivery backlog and the existing approval and evidence trail. Use separate opportunity and incident IDs for traceability and link related work to the backlog where appropriate.

## Choose the practice by need

| Practice | When to use it at InfiniteSol | Apply it on the project |
|---|---|---|
| Agile principles | Default across project delivery. | Deliver a small usable slice, gather feedback, adapt plans when evidence changes, and sustain a realistic pace. Surface tradeoffs and preserve approved boundaries. |
| Scrum | Use a Scrum-informed cadence with one delivery team. Use the name Scrum for a setup that implements the Scrum Guide's accountabilities, events and artifacts. | Agree on a short cycle and a goal. Order work, plan the slice, inspect progress, review the tested result and run a retrospective. Record the project outcome, selected work and Definition of Done. If adopting Scrum, explicitly designate a Product Owner, a Scrum Master and Developers, and use the full event and artifact structure. |
| SAFe | Consider selected practices when multiple teams share meaningful dependencies, a product outcome or integration timing. | Start with a shared objective, dependency owners and integration milestones or demos. Escalate unresolved dates or capacity conflicts through the PM. Treat a full SAFe rollout as a separate operating decision. |
| Lean Six Sigma | Use DMAIC for a recurring, measurable problem in an existing process. Consider Design for Six Sigma and DMADV for a new or substantially redesigned process where structured design verification adds value. | Define the problem and measure the baseline, investigate causes using evidence, test an improvement and confirm how the result will be sustained. When designing a new process, validate needs, compare designs and verify outcomes before adopting it. |
| PMI project practices and PMP study | Use project governance for scope, tradeoffs, dependencies, risks and stakeholder decisions across delivery approaches. | Keep the project brief, approved boundaries, milestone forecast, risks and decision evidence current. Study the PMI references and practise with real or synthetic decision packages. PMP is a professional certification. |
| ITIL practices | Use selected service management practices when preparing for release and operating live applications. | Restore service through incident management, follow up recurring causes through problem management, assess and authorise changes through change enablement, and track continual improvements. Use the project maintenance record and runbook. |

## Run the work

1. **Kickoff.** Record the product objective, scope and capacity, decision owner, working cadence, and the evidence needed for a done item. The Product Owner, when designated, orders the product backlog within approved bounds. The PM coordinates delivery and routes scope, budget, priority or production decisions to the CEO. Developers manage their implementation plan within the approved scope. Use a distinct person or role assignment where accountabilities would otherwise conflict. Scrum work ordering does not override portfolio decisions or production approval.
2. **Delivery cycle.** Choose a small outcome and testable acceptance criteria. Inspect progress and blockers against the goal. Demonstrate a working, checked increment and capture real stakeholder feedback or label it missing. Compare actual evidence to expected results, then pick one improvement to try and record its owner and how it will be checked. Use the existing peer review, QA and documentation gates. A demonstration does not authorise a production release.
3. **Scaling decision.** If genuine cross-team dependencies make delivery harder, record which coordination problem needs solving, the teams, the dependency owners and the expected benefit. Start with a lightweight shared planning and integration check. Consider formal SAFe adoption only as a separate decision with capacity and accountability. Two projects waiting for the same developer pair are a portfolio priority problem under the existing one-active-build rule.
4. **Service operation.** Use `workflows/MAINTENANCE.md`. Route a live symptom to incident response and recurring causes to the improvement register. Match maintenance changes to the authorised operator, approvals and evidence requirements. Use the same project record rather than a duplicate process ledger.

## Study and show application

Use approved time at kickoff or as needs arise. Study the official source, work through one relevant exercise, and have the PM or an appropriate specialist check the resulting artifact. Record source and version where available, objective, artifact, observed evidence, review and improvement action in `starter/templates/practice-study-record.md`. Use these exercises as a study sequence when starting from scratch:

| Topic | Practical exercise | Evidence to retain |
|---|---|---|
| Agile and Scrum | Plan one small delivery goal and run a short retrospective on a completed or simulated slice. | Goal, ordered backlog, checked result, feedback and one reviewable improvement. |
| PMI practices and PMP study | Prepare a decision package when a risk changes the scope or milestone forecast. | Options, evidence, updated forecast, authority and decision record. |
| Lean Six Sigma and DFSS | Measure rework before changing an existing workflow, or compare alternative designs for a new workflow. | Metric definition, baseline/sample, hypothesis, test results or verification plan, and owner. |
| ITIL | Run a synthetic incident from acknowledgement to restoration and review. | Observed timeline, authorised response, verification, problem follow-up and documentation changes. |
| SAFe | Simulate a dependency between two delivery teams. | Shared objective, dependency owner, needed date, integration checkpoint and resolution. |

Use `planned`, `practised`, or `evidence reviewed` for study status. Mark simulations as simulations. Do not claim certification from a reading session or practice output. Revisit the study notes when results or retrospectives expose a gap. Transfer effective changes into the project playbook only after the relevant owner agrees.

## Primary study references

- Agile Manifesto authors, [Agile Manifesto](https://agilemanifesto.org/) and [principles](https://agilemanifesto.org/principles.html).
- Ken Schwaber and Jeff Sutherland, [The Scrum Guide](https://scrumguides.org/scrum-guide).
- Scaled Agile, [Agile Release Train](https://framework.scaledagile.com/agile-release-train/) and [PI Planning](https://framework.scaledagile.com/pi-planning/).
- ASQ, [Lean Six Sigma](https://asq.org/quality-resources/six-sigma) and [DMAIC and DMADV](https://asq.org/quality-resources/dmaic).
- PMI, [Project Management Professional and exam content outline](https://www.pmi.org/certifications/project-management-pmp/) and official project management guides linked from that page.
- PeopleCert, [ITIL practice scope](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/itil-practice-manager) and [ITIL certifications and learning](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1).

Source links checked 19 November 2026. Recheck current editions and credential requirements for formal study or certification decisions.
