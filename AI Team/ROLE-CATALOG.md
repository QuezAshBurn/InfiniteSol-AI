# InfiniteSol role catalog

The local catalog contains 22 role prompts. Every assignment needs a current, approved Markdown record. The PM assigns the roles relevant to the project's scope and records the owner, required output, and review path. A role listing grants no project, spending, or publication authority. [Approved work](policies/APPROVED-WORK.md)

## Architecture and engineering leadership

The existing Solution Architect designs the application structure. This role owns the architecture brief, stack recommendation, component and repository boundaries, interfaces, data flows, security and recovery design, and technical interpretation of architecture decisions. Changes spanning components, modifying a public or internal interface contract, or making a hard-to-reverse choice go to the Solution Architect through the PM. The applicable decision owner records approval when required. [Solution Architect prompt](roles/03-solution-architect.md)

The Tech Lead turns that design into an implementation sequence and owns engineering choices inside approved boundaries. The Tech Lead helps enforce quality and conformance, identifies deviations, and routes architecture decisions to the Architect. The PM assigns the existing build and reviewer slots. An independent senior developer in the counterpart runtime reviews authored code. QA retains independent verification. [Tech Lead prompt](roles/15-tech-lead.md)

The Solution Architect defines the job description for each assigned project role and is the sole proposer of project development skills. The PM records scoped approval before assigning skill authoring or using a project role description. A project role description applies the company role to the project's industry, stack, deliverables and handoffs. Project agents use verified skills from their own project's `Skills/` folder, as recorded in `docs/project-skills.md`. [Project setup guide](../START-HERE.md#after-discovery-approval)

## Additional assignments

| Role | Assign when | Main handoff |
|---|---|---|
| [Tech Lead](roles/15-tech-lead.md) | Design needs to be translated into engineering tasks and guided through integration. | Implementation sequence, coding and test expectations, architecture conformance evidence. |
| [UX Designer](roles/16-ux-designer.md) | The project needs a usable interaction, customer journey, or conversation flow. | Flows, wireframes or dialogue behavior, recovery paths, usability findings and QA scenarios. |
| [UI Designer](roles/17-ui-designer.md) | The product needs a visual interface or consistent components. | Responsive screens, design tokens, visual states and implementation handoff. |
| [Copywriter](roles/18-copywriter.md) | The product needs customer-facing wording, spoken scripts, or campaign copy. | Versioned copy, tone guidance, placement, and claims or source references. |
| [Conversion Expert](roles/19-conversion-expert.md) | A team needs to improve a measurable action such as booking or onboarding completion. | Funnel definition, baseline, test proposal, guardrail metrics and evidence. |
| [SEO Expert](roles/20-seo-expert.md) | Approved public pages need organic search readiness. | Technical audit, search intent map, content requirements, and release checks. |
| [AI Search Expert](roles/21-ai-search-expert.md) | Approved public content needs analysis of mentions, citations and accuracy in AI search responses. | Query baseline, citation accuracy audit, improvement backlog and retest plan. |
| [Content Strategist](roles/22-content-strategist.md) | The project needs a plan for public content, product guidance, support content, or tenant knowledge. | Content inventory, briefs, source ownership, approval route and lifecycle. |

## Main handoffs

| Decision or artifact | Accountable role and collaborators |
|---|---|
| Approved service rules and acceptance criteria | BA prepares the requirements with the business owner. UX turns them into interaction and recovery paths. |
| Voice persona and customer experience | UX owns the conversation and persona specification. The Copywriter drafts the words and tone guide with Product Marketing. UI designs the visible states where a screen exists. |
| Voice performance and recovery | UX states what the customer needs. The Solution Architect owns technical targets. The Tech Lead confirms testability and supports implementation checks. QA verifies behavior, interruptions, clarity and response time on the exact candidate. |
| Audio data and permissions | The BA records what the service needs. Security assesses protections and Legal handles applicable legal review. The PM routes approval. |
| Public launch and content | Product Marketing owns positioning and launch readiness. Content Strategy briefs and maintains content. The Copywriter drafts words. SEO owns technical organic-search recommendations. AI Search assesses public answers and citations. |
| Conversion measurement | The designated business owner agrees the metric. The Conversion Expert proposes the method. Data Engineering and QA verify instrumentation and outcomes when assigned. |
| Private tenant RAG | The BA and tenant owner approve business content. Content Strategy can organise it. The Solution Architect owns technical retrieval design and isolation, with independent QA. |

For a voice scheduling project, the PM can consider the Tech Lead, UX Designer and Copywriter for implementation planning, dialogue behavior and scripts. UI has a role where there is a visual surface. Conversion, SEO and AI Search join when their outcomes are part of an approved assignment.

## Existing role prompts

| Role | Main ownership |
|---|---|
| [Project Manager](roles/01-project-manager.md) | Intake, assignments, project decisions, gates and portfolio |
| [Business Analyst](roles/02-business-analyst.md) | Approved requirements, rules and business acceptance criteria |
| [Solution Architect](roles/03-solution-architect.md) | Application architecture and technical design |
| [Database Architect](roles/04-database-architect.md) | Persistence, integrity and migration design and review |
| [Security Architect](roles/05-security-architect.md) | Defensive controls and scoped security review |
| [Senior Full Stack Developer A](roles/06-senior-full-stack-developer-a.md) | Approved implementation and independent review when assigned |
| [Senior Full Stack Developer B](roles/07-senior-full-stack-developer-b.md) | Approved implementation and independent review when assigned |
| [QA Engineer](roles/08-qa-engineer.md) | Independent acceptance and regression verification |
| [Technical Writer](roles/09-technical-writer.md) | Project documentation, versioned guides and evidence register |
| [Product Marketing Specialist](roles/10-product-marketing-specialist.md) | Positioning, approved claims and launch readiness |
| [Legal Research and Drafting Agent](roles/11-legal-research-and-drafting-agent.md) | Scoped issue review and qualified human review handoff |
| [Financial Analyst](roles/12-financial-analyst.md) | Cost, viability, and independent forecast checks |
| [Deployment Engineer](roles/13-deployment-engineer.md) | Release readiness, promotion and support handoff |
| [Data Engineer](roles/14-data-engineer.md) | Data contracts, pipelines, and reconciliation |
