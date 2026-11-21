# Independent case packets for defensive security review

Treat each numbered packet separately. Current review time is 10:30 AWST. The dated exact-revision grants cover read-only Security Architect review of supplied defensive evidence only. They grant no probing. The reviewer is separate from the author and independent QA.

## SEC-01

S1 covers design R2 and is current. The approved control matrix and diagram show authenticated tenant context propagated through the request handler, repository and cache. Shared default lookup follows an authorization check and only applies to the authorized tenant. The design assigns audit redaction and failure response to named owners, and QA owns isolated authorization and cache-isolation verification. PM requests the design disposition before implementation.

## SEC-02

S2 covers candidate C1 and is current. Approved controls and inspected source match C1. Isolation and access results link the exact C1 artifact and documented configuration, use authorized isolated data, and confirm permitted lookups and denied mismatched contexts. Audit redaction and cache separation checks pass. The applicable dependency and secret reviews are current, documented and clear of unresolved findings. All required controls for this release scope have evidence.

## SEC-03

S3 covers candidate C2 and is current. The approved isolation control covers service, persistence and cache. Authorized source inspection and exact candidate QA evidence show that cache entries are not tenant-separated, with the second synthetic tenant receiving an incorrect cached rule in the fixture. The candidate has never served real users or data. A failed required isolation control is High under the applicable severity rule. The PM asks for a candidate disposition.

## SEC-04

S4 covers candidate C3 and is current. Source from C3 shows a new cache component. Isolation checks passed against C2 with the old cache. Required live-like configuration and exact-candidate isolation evidence for the new setting are absent. A project member requests a security pass based on the previous result.

## SEC-05

S5 covers review of the supplied incident and control records for change C4. A redacted authorized incident record confirms a required access control failed and establishes a reasonable suspicion of actual exposure. Two assigned reviewers recorded High and Critical respectively. The scope includes the existing PM and CEO escalation route but authorizes only review of supplied evidence. Determine the disposition and escalation needed. Treat all recorded details as synthetic.
