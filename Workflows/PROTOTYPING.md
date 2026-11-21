# Prototyping and technical spikes

Use a prototype to answer a specific question before committing to a design. Default to a simple prototype for a new or changed user workflow with meaningful uncertainty. Use a short technical experiment, often called a spike, for an integration, performance, data or architecture risk. If prior evidence already answers the question, record why a prototype adds little value.

## Choose the smallest useful experiment

| Type | Question to answer | Typical evidence |
|---|---|---|
| Sketch or process flow | Do users and reviewers agree on the steps, rules and exceptions? | Annotated flow, synthetic cases, unresolved decisions and agreed corrections. |
| Clickable interface | Can someone complete the proposed task and understand what happens on success or failure? | Mock screens, observed outcome, confusing steps and feedback limitations. |
| Technical spike | Can a specific approach meet a testable constraint in an isolated environment? | Reproducible check, versions and configuration, expected and actual result, and limits on what was proved. |

## Run it and decide

1. Use `starter/templates/prototype-record.md`. The BA or Architect defines the assumption, expected result and stop condition. The PM records the owner, allowed access, timebox and spend allowance. A read-only discovery allowance permits read-only work. Check the charter before running code, contacting anyone, spending or using non-synthetic data.
2. Work in an approved sandbox or disposable branch or folder. Keep versioned experimental artifacts under a project-local location such as `prototypes/<Prototype ID>/` or link to the approved isolated worktree. Use synthetic or mock data and services by default. Keep the experiment out of delivery branches, normal promotion and live systems.
3. Save what was actually tried, the observed result and limits. For a UI prototype, verify at least the risky user task and the related exception. For a spike, give enough context to reproduce the result and state what remains untested. Record the recommendation to proceed, revise, run one more targeted check, or stop. Update the requirement or architecture decision through the usual authority.
4. Link the result or skip rationale from the project record and draft charter. Build approval remains a separate decision. To reuse any experimental work, record the reuse decision and treat the selected changes as production code in a normal branch, with coding standards, peer review, QA and release approval. A prototype artifact itself is never promoted.

For example, before building a Supplier Portal, make an isolated two-screen prototype using mock delivery documents. Test whether a reviewer can reject a document with a reason and the supplier understands how to resubmit it. If the reason is unclear, revise the workflow and acceptance criteria before assigning the production build.
