# Release and rollback runbook | Project and release ID

## Before deployment

- Owner, exact artifact and configuration baseline, document revision, target environment and release window
- Approved change and CEO Production decision, authorised operator and backup, support contacts and escalation route
- Affected services, dependencies, prechecks, Staging rehearsal evidence, parity gaps, QA disposition and promotion record
- Backup, restore or forward recovery dependencies and verification, with a readiness check before irreversible steps

## During deployment

| Step and order | Operator and approved workflow or procedure | Expected observation and threshold | Stop condition or recovery step | Actual evidence and time |
|---|---|---|---|---|
| | | | | |

- Define timed rollback triggers and authority, previous known-good artifact, data compatibility checks, and approved restoration or forward recovery steps.
- Define smoke checks, monitored signals, thresholds, observation window and who decides the next action.

## After the release attempt

- Record actual version, outcome, post-deployment checks and observation evidence. Link the completed promotion record.
- If recovery was used, record the trigger, steps taken, observed service and data state, and remaining impact.
- Link release notes and the current support procedure. Record support-owner acceptance or open handoff actions with owner and target date.
