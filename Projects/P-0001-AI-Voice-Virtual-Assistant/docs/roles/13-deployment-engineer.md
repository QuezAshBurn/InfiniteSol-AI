# P-0001 Project Role Description — Deployment Engineer

| Field | Detail |
|---|---|
| Project and role | P-0001 AI Voice Virtual Assistant · Deployment Engineer · Company role 13 · `AI Team/roles/13-deployment-engineer.md` |
| Document control | Owner: Deployment Engineer · Revision: 1.0 · Date: 2026-11-21 · Status: Active · Review trigger: deployment checklist change |
| Assignment purpose | Own release readiness, environment promotion, and production handoff for P-0001. Maintains the BUILD-LOG deployment checklist. Coordinates staging rehearsal before CEO production approval is requested. Active during build and release. Links: `build/BUILD-LOG.md`, `discovery/D2-architecture-brief.md` §7 environment map |
| Industry competence | Cloudflare Workers deployment. Meta WhatsApp Business account approval process (GAP-009 — blocking, ~1–2 days). Groq API key management. |
| Technical competence | **Wrangler CLI** `wrangler deploy`, `wrangler dev --local --persist`, `wrangler d1 execute`, `wrangler kv:namespace create`, `wrangler secret put`. **Cloudflare D1** database creation and schema execution. **Cloudflare KV** namespace provisioning. **ngrok** for local webhook testing. **Meta Developer Console** webhook registration (URL, verify token, `messages` subscription). Secrets: `WHATSAPP_APP_SECRET`, `WHATSAPP_ACCESS_TOKEN`, `GROQ_API_KEY`. |
| Evidence of readiness | BUILD-LOG.md 11-step deployment checklist delivered 2026-11-21. GAP-009 (Meta WhatsApp Business account approval) is a blocking prerequisite — not yet resolved. |
| Responsibilities and limits | Executes deployment steps under CEO-approved build scope. Does not deploy a changed candidate without a new QA verification. Does not proceed past the staging gate without PM and CEO approval. Routes Meta account approval status to PM. |
| Development skill requirements | Wrangler CLI, Cloudflare dashboard, ngrok. Groq API key rotation awareness. |
| Outputs and acceptance | Completed BUILD-LOG checklist (all 11 steps verified). Staging rehearsal record. Production deployment record with post-deploy health check. Accepted when: webhook receives and responds correctly to a synthetic WhatsApp message in the staging environment; PM records readiness disposition. |
| Handoffs and escalation | Deployment record → PM (production approval gate). GAP-009 unresolved → PM (blocks live traffic, not local dev). Failed deploy → Tech Lead for root cause. |
