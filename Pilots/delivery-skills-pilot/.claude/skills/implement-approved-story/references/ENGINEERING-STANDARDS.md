# Engineering standards and architecture

The Solution Architect owns the technical design and decisions. Developers own implementation quality and the project coding standard. QA verifies behaviour independently. The PM routes decisions that change scope, cost, capacity or material risk and preserves the existing approval path. Store project copies of the templates with the project's design documentation and link them from `project-record.md`.

## Establish the architecture before building

1. Fill `starter/templates/architecture-brief.md` to match the size and risk of the work. Identify requirements, quality targets and constraints, the system boundary, responsibilities, data ownership, integrations, deployment environments and how the system is supported. For an existing application, inspect its actual architecture and migration constraints. For a new application, compare the simplest viable option with credible alternatives.
2. Use diagrams where they answer a decision. Trace a typical request and a failure route from the user through the components and data. Identify authority and trust boundaries, data and interface contracts, accessibility or performance requirements, and how to observe or recover the system. Define verifiable targets when the project calls for them and name who owns each check. Mark unsolved assumptions for discovery or prototype evidence.
3. Record consequential choices in `starter/templates/architecture-decision.md`, including the decision maker, reasons, tradeoffs, implications, dependencies and criteria for revisiting. Share approved constraints with both developers and QA. Route material changes through the PM and `change-request.md`. Keep superseded records so the team can understand why the design changed.
4. Make the stack recommendation explicit. Compare viable options by requirement fit, lifecycle, security, team capability, total cost and operational burden. Cite the versioned inventory, vendor sources or measured results. Document module and repository layout, dependency direction and where domain rules live. Agree controls and verification owners with the Security and Database Architects where their mandates apply. Tie engineering practices to project risks and configure applicable checks with the developers.

Use `policies/COST-AND-OPEN-SOURCE.md` for the stack recommendation and budget evidence. Show how each environment and support obligation can operate within the approved ceiling.

## Write the project coding standard

Copy `starter/templates/coding-standard.md`. Start with the actual repository instructions, architecture decisions and configured formatter, linter, type check, build and tests. For a new repository, agree on naming, modules, configuration, test and build commands, and review rules before writing production implementation. Record missing tooling and scope approved work to set it up. Avoid unrelated style or tooling changes. Apply these defaults unless the applicable repository standard requires a different practice:

- Use clear names, focused functions and modules, and established patterns. Reuse sound code and preserve intended compatibility. Add abstractions when they solve a demonstrated need.
- Validate inputs at boundaries, enforce access server side, handle errors explicitly, and log relevant context without exposing secrets or sensitive data. Check timeouts, retries and duplicate operations where they affect correctness.
- Keep data changes reviewable. Plan migration, rollback or recovery as applicable. Test important constraints and realistic failure paths. Give user-facing flows appropriate accessible labels, focus, responsive layout and meaningful loading, error and empty states.
- Pin or record resolved dependencies through the project's approved tooling. Protect secrets and restrict access by environment. Keep configuration external to code and use isolated data in nonproduction.
- Add or update meaningful checks for the change. Record exact commands, actual results and the reference build or commit. A missing result stays unverified. Keep relevant documentation and operational notes aligned with the candidate.

The author links the coding standard and architecture decisions in the review packet. The independent peer checks the relevant rules and evidence and records any exception with an owner and decision. Material exceptions follow the project authority and remain visible to QA. CI result, peer review and independent QA are distinct records. Follow `workflows/DELIVERY-ENVIRONMENTS.md` for deployment evidence and `workflows/PEER-REVIEW.md` for counterpart review.
