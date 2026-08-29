<h1 align="center">headcount</h1>

<p align="center"><b>Add a department, not a prompt.</b></p>

<p align="center">
  <a href="https://claude.com/claude-code"><img alt="Built for Claude Code" src="https://img.shields.io/badge/built%20for-Claude%20Code-D97757?style=flat-square"></a>
  <img alt="16 departments" src="https://img.shields.io/badge/departments-16-3F4B5B?style=flat-square">
  <img alt="135 skills" src="https://img.shields.io/badge/skills-135-3F4B5B?style=flat-square">
  <a href="LICENSE"><img alt="MIT licensed" src="https://img.shields.io/badge/license-MIT-3F4B5B?style=flat-square"></a>
  <a href="CONTRIBUTING.md"><img alt="PRs welcome" src="https://img.shields.io/badge/PRs-welcome-2EA043?style=flat-square"></a>
</p>

An agent organization for [Claude Code](https://claude.com/claude-code), structured as a company:
a chief executive over 16 departments, 135 skills in total.

Every department is an independently installable plugin, so a project loads only the functions it
needs rather than all of them at once.

## Install

```
/plugin marketplace add cbrock84/headcount
/plugin install security@headcount
```

Install as many departments as the project needs. Skills are addressed as `department:skill` —
`security:threat-modeling`, `finance:unit-economics` — so names never collide.

## Use

Skills load themselves when a request matches. Ask a question in the department's territory and the
right specialist engages:

| You ask | What loads |
|---|---|
| "why isn't this landing page converting?" | `demand-generation:landing-page-cro-expert` |
| "review this design before we build it" | `security:threat-modeling` |
| "can we afford this hire?" | `finance:unit-economics` |
| "our growth has stalled" | `executive:business-growth-consultant` |

Invoke one directly by name when you want a specific lens: `/finance:financial-modeling`.

Seven situations that cross departments — a SOC 2 demand from an enterprise prospect, a
security incident, a stalled funnel — are worked through end to end in
[docs/USE-CASES.md](docs/USE-CASES.md), including where a reviewer-class department stops the
work rather than adding an opinion.

Each department also ships an agent charter in `.claude/agents/`, so a department can be delegated
to as a subagent with its own exclusive write surface.

## Departments

<details>
<summary><b>Office of the CEO</b> (Chief Executive) — 6 skills</summary>

| Skill | What it does |
|---|---|
| `agent-hierarchy` | Designs orchestrator-and-subagent hierarchies for a repository — splitting agents by exclusive write surface, pairing every producer with an independent auditor, an…. |
| `ai-research-analyst` | Produces executive-level research — market sizing, competitor mapping, trend analysis, and strategic intelligence — grounded in cited sources with the confidence in…. |
| `business-growth-consultant` | Finds the single constraint currently limiting a business's growth and the highest-leverage moves against it, rather than producing a list of everything that could…. |
| `ceo-advisor` | Pressure-tests a decision, plan, or idea before it is committed to — surfacing the assumption it rests on, the case against it, and what would have to be true for i…. |
| `chief-executive` | Sets direction, allocates capital and attention, and makes the calls no one else can make. |
| `saas-idea-validator` | Evaluates a software or startup idea against problem, market, competition, monetization, defensibility, and execution, and returns a verdict rather than encourageme…. |

</details>

<details>
<summary><b>Technology</b> (CTO / CIO) — 18 skills</summary>

| Skill | What it does |
|---|---|
| `ai-workflow-architect` | Designs AI systems, automations, and agent workflows for a business — identifying which manual work is worth automating, how to structure the system, which tools fi…. |
| `api-design` | Designs interfaces that survive their consumers — resource modelling, errors, versioning, pagination, and compatibility. |
| `branch-and-worktree-workflow` | Isolates feature work in its own branch or worktree and integrates it cleanly when done. |
| `chief-technology-officer` | Owns architecture, engineering delivery, infrastructure, data platform, and internal systems. |
| `cloud-infrastructure` | Designs and runs cloud infrastructure — environments, infrastructure as code, networking and isolation, scaling, and cost. |
| `code-review` | Conducts and responds to code review — reviewing a change for correctness, design, and risk, and evaluating review feedback received on your own work. |
| `completion-verification` | Verifies that work is actually complete before it is claimed to be — running the checks, reading the output, and confirming the original request was satisfied rathe…. |
| `implementation-planning` | Turns a spec or requirement into a written plan a separate session or agent can execute, then drives that plan through review checkpoints. |
| `observability-and-reliability` | Makes systems debuggable and reliably operable — instrumentation, alerting that is worth waking for, service objectives, and learning from failure. |
| `parallel-agent-delivery` | Splits work across multiple agents or sessions running at once, keeping their surfaces disjoint so results merge cleanly. |
| `prompt-optimizer` | Turns rough intent or a weak prompt into a reliable one — diagnosing why output is inconsistent, restructuring the instruction, and adapting it across models. |
| `release-and-deployment` | Ships changes safely and often — pipelines, deployment strategies, feature flags, rollback, and database changes. |
| `skill-authoring` | Writes and revises agent skills so they trigger at the right moments and give usable instruction when they do. |
| `solution-architecture` | Designs system structure and makes architectural decisions defensible — boundaries, coupling, trade-offs, and recording why. |
| `solution-exploration` | Explores the problem and the range of possible approaches before any code is written — clarifying what is actually being asked, surfacing options with their tradeof…. |
| `systematic-debugging` | Finds the root cause of a bug, test failure, or unexpected behavior before proposing any fix. |
| `technical-debt-management` | Makes technical debt visible and decidable — distinguishing real debt from mess, quantifying its cost, and arguing for remediation in business terms. |
| `test-driven-development` | Drives implementation by writing a failing test first, then the smallest code that passes it. |

</details>

<details>
<summary><b>Security</b> (CISO) — 6 skills · **reviewer-class**</summary>

| Skill | What it does |
|---|---|
| `access-and-identity` | Designs and audits who can reach what — authentication, authorization models, privileged access, service credentials, and joiner-mover-leaver process. |
| `chief-information-security-officer` | Owns the security posture of the organization — architecture, program strategy, risk acceptance, incident command, and the authority to stop work that creates unacc…. |
| `incident-response` | Runs a security incident from detection to closure — triage, containment, investigation, communication, and the review afterward. |
| `security-architecture-review` | Reviews a design or change for security before it ships — authentication and authorization, data handling, secrets, dependencies, and the secure-development practic…. |
| `threat-modeling` | Identifies what could go wrong in a system before it is built or changed — the assets worth attacking, the entry points, the trust boundaries, and the controls that…. |
| `vulnerability-management` | Runs the loop from discovering a weakness to confirming it is fixed — scanning, triage, prioritization by real exploitability, remediation tracking, and patch policy. |

</details>

<details>
<summary><b>IT Operations</b> (CIO) — 7 skills</summary>

| Skill | What it does |
|---|---|
| `backup-and-recovery` | Protects and restores data — backup coverage and scope, retention, immutability against ransomware, and proving restores actually work. |
| `endpoint-management` | Manages laptops, desktops and mobile devices — enrolment, configuration, patching, software distribution, and lost or compromised devices. |
| `identity-lifecycle-administration` | Executes joiner, mover and leaver processes — provisioning, group membership, access changes on role change, and complete deprovisioning. |
| `it-asset-management` | Tracks hardware and software assets through their life — procurement, ownership, licensing, refresh, and disposal. |
| `network-administration` | Designs and operates the corporate network — segmentation, remote access, wireless, DNS and addressing, and diagnosing network problems. |
| `service-desk` | Runs the IT service desk — intake, triage, prioritisation, escalation, knowledge, and the metrics that improve service rather than distort it. |
| `systems-administration` | Runs servers and corporate systems — patching, configuration baselines, change control, capacity, and the routine that prevents incidents. |

</details>

<details>
<summary><b>Product</b> (CPO) — 9 skills</summary>

| Skill | What it does |
|---|---|
| `brand-identity` | Defines and applies visual brand — logo usage, palette, typography, imagery direction, and the guidelines that keep expression consistent across product and marketi…. |
| `chief-product-officer` | Owns what gets built and why: product strategy, roadmap, discovery, user experience, and the definition of success for each release. |
| `design-styles` | Applies a deliberate visual direction to an interface — minimalist editorial, industrial utilitarian, or high-polish commercial — each with its own type scale, pale…. |
| `design-system` | Builds and maintains the design system a product is assembled from — tokens for color, type, spacing and elevation, component contracts, and the rules that keep the…. |
| `interface-craft` | Raises the visual and interaction quality of an interface — layout, hierarchy, type, spacing, density, and the details that separate a considered product from a gen…. |
| `interface-redesign` | Upgrades an existing interface to a higher standard without rebuilding it — auditing what is there, identifying what reads as generic or unfinished, and sequencing…. |
| `presentation-design` | Designs slide decks, one-pagers, and marketing graphics that carry an argument rather than decorate one. |
| `ux-product-auditor` | Audits a website, app, onboarding flow, or design for usability, conversion, and product problems, tying every finding to a business outcome and a severity. |
| `visual-reference-generation` | Produces design reference imagery before implementation — screen concepts, layout directions, and flows for web or mobile that make a verbal brief concrete enough t…. |

</details>

<details>
<summary><b>Marketing</b> (CMO) — 17 skills</summary>

| Skill | What it does |
|---|---|
| `behavioral-marketing` | Applies decision science and cognitive bias research to marketing and product decisions — how people actually choose under uncertainty, and how framing, defaults, s…. |
| `brand-voice` | Captures how a person or brand actually writes and turns it into reusable voice instructions every other content skill draws from. |
| `chief-content-officer` | Runs content as an operation — the production pipeline, editorial calendar, repurposing engine, competitive content intelligence, and audits of what already exists. |
| `chief-marketing-officer` | Owns brand, demand generation, content, communications, and how the market understands what the business does. |
| `content-strategy` | Decides what content to make and why — topic territory, format mix, cadence, and how content connects to a business outcome rather than to traffic. |
| `customer-research` | Plans, runs, and synthesizes customer research — interviews, surveys, win-loss analysis, and message testing — into findings that change decisions. |
| `marketing-campaign-planner` | Designs a coordinated multi-channel campaign or product launch around one story — objective, message, channel sequencing, timeline, assets, and the checklist that g…. |
| `marketing-copywriting` | Writes and edits marketing copy for any surface — homepage, product and pricing pages, ads, emails, and collateral — and sharpens existing copy that is not working. |
| `marketing-planning` | Builds the marketing plan of record — objectives, channel mix, budget allocation, sequencing, and the measurement that says whether it worked. |
| `newsletter-writer` | Writes and edits newsletters and marketing emails people actually open — subject lines, opening, structure, voice, and the conversion turn where there is one. |
| `partnership-marketing` | Builds reach through other people's audiences — co-marketing partnerships, creator and influencer programs, community building, and affiliate arrangements. |
| `positioning-and-messaging` | Establishes what a product is understood to be, for whom, and instead of what — then turns that into the messaging every other surface inherits. |
| `public-relations` | Plans and executes earned media — press strategy, journalist outreach, announcements, commentary, and crisis response. |
| `social-post-craft` | Writes, structures, and evaluates social posts end to end — hooks, body, formatting for how each platform renders, and a quality check before publishing. |
| `video-content` | Plans and scripts short-form and long-form video, and designs the packaging — titles, thumbnails, and openings — that determines whether it gets watched. |
| `visual-content` | Designs and directs the visual assets that carry content — carousels, infographics, quote graphics, diagrams, and social imagery — including the generation prompts…. |
| `youtube-producer` | Plans, packages, and scripts long-form video for retention and channel growth — idea selection, titles and thumbnails, script structure, and diagnosing why a video…. |

</details>

<details>
<summary><b>Demand Generation</b> (CMO) — 11 skills</summary>

| Skill | What it does |
|---|---|
| `ai-search-optimization` | Optimizes for AI assistants and AI-generated answers — being retrievable, being cited, and being represented accurately when a model answers on your behalf. |
| `app-store-optimization` | Improves visibility and conversion in the App Store and Google Play — metadata, keywords, screenshots, ratings, and the listing experience that turns an impression…. |
| `experimentation` | Designs, runs, and reads A/B tests and growth experiments — hypothesis, sample size, duration, and honest interpretation. |
| `landing-page-cro-expert` | Audits and rewrites landing pages, homepages, and sales pages to increase conversion — diagnosing why a page is not converting, rewriting headlines, hero copy and c…. |
| `lead-capture` | Converts anonymous traffic into known contacts — lead magnets, gated content, free tools, popups, and the forms behind them. |
| `lifecycle-messaging` | Designs automated email and SMS programs — welcome and onboarding sequences, nurture, re-engagement, transactional messaging, and the timing and segmentation behind…. |
| `listing-distribution` | Gets a product listed where buyers and crawlers look — directories, marketplaces, review sites, comparison pages, and aggregators. |
| `marketing-analytics` | Sets up, audits, and reports on marketing measurement — tracking plans, event schemas, attribution models, and the dashboards built on them. |
| `paid-advertising` | Plans, runs, and optimizes paid acquisition across search, social, and display — account structure, targeting, creative, bidding, budget, and the analysis that says…. |
| `programmatic-seo` | Builds large sets of search-targeted pages from a template and a dataset — the location, comparison, integration, and use-case pages that capture long-tail demand a…. |
| `seo-strategy` | Audits and improves organic search performance — technical health, site architecture, internal linking, structured data, and the content decisions that determine wh…. |

</details>

<details>
<summary><b>Revenue</b> (CRO) — 8 skills</summary>

| Skill | What it does |
|---|---|
| `activation` | Gets new users from signup to first real value — signup flow, onboarding, time-to-value, and the early experience that determines whether someone becomes a user or…. |
| `chief-revenue-officer` | Owns the revenue engine end to end: sales, monetization, pricing, customer success, retention, and partnerships. |
| `outbound-prospecting` | Finds, qualifies, and reaches prospects through cold outreach — list building, qualification criteria, cold email and multi-channel sequences, and the follow-up tha…. |
| `pricing-and-packaging` | Sets price, structures packages and tiers, and designs the monetization surfaces that carry them — upgrade paths, paywalls, and offer construction. |
| `referral-programs` | Designs and improves referral, affiliate, and word-of-mouth programs — incentive structure, mechanics, timing, and fraud control. |
| `retention` | Diagnoses and reduces churn — cancellation flows, save offers, failed-payment recovery, at-risk detection, and the product and service causes underneath. |
| `revenue-operations` | Runs the mechanics of the revenue engine — lead lifecycle definitions, routing, CRM hygiene, forecasting process, pipeline reporting, and the marketing-to-sales han…. |
| `sales-enablement` | Builds what a sales team needs to sell — pitch decks, one-pagers, objection handling, competitive battlecards, demo scripts, and case studies. |

</details>

<details>
<summary><b>Finance</b> (CFO) — 9 skills</summary>

| Skill | What it does |
|---|---|
| `budgeting-and-forecasting` | Runs the planning cycle — annual budget, rolling forecast, consolidation of business unit inputs, and the variance analysis that explains actuals against plan. |
| `capital-allocation` | Evaluates where to spend limited capital — investment appraisal, hurdle rates, payback, and comparing proposals that are not alike. |
| `chief-financial-officer` | Owns the financial position: planning, budgeting, forecasting, unit economics, cash, and the numbers the business is run and reported on. |
| `financial-modeling` | Builds and stress-tests financial models for forecasting, scenario planning, and decision support — revenue build, cost structure, driver logic, and the sensitiviti…. |
| `financial-reporting-and-close` | Runs the period-end close and produces reporting — close calendar, reconciliations, accruals, variance analysis, and reporting that gets read. |
| `internal-controls-and-audit` | Designs and tests controls over financial reporting — segregation of duties, approval limits, evidence, and preparing for audit. |
| `revenue-recognition` | Determines when and how revenue is recognised — performance obligations, contract terms that change the answer, and the deal structures that create accounting probl…. |
| `treasury-and-liquidity` | Manages cash and liquidity — cash forecasting, runway, working capital, banking structure, and currency and counterparty exposure. |
| `unit-economics` | Establishes whether the business makes money on each customer or unit — contribution margin, acquisition cost, payback period, lifetime value, and the cohort behavi…. |

</details>

<details>
<summary><b>Operations</b> (COO) — 8 skills</summary>

| Skill | What it does |
|---|---|
| `business-continuity-and-resilience` | Plans for operating through disruption — impact analysis, recovery objectives, continuity plans, and the exercises that prove they work. |
| `capacity-and-demand-planning` | Matches operational capacity to expected demand — forecasting load, sizing teams and systems, managing queues, and deciding when to add capacity. |
| `chief-operating-officer` | Owns execution: how work actually gets done across the organization, including process, program management, capacity, vendors, supply chain, and service delivery. |
| `process-design` | Designs, documents, and fixes operational processes — mapping the current state, finding where work actually stalls, redesigning the flow, and building controls tha…. |
| `quality-management` | Builds quality into operations — defining standards, catching defects at the right point, root cause analysis, and continuous improvement. |
| `service-level-management` | Defines and manages service levels — setting targets that reflect what customers need, measuring honestly, and handling breaches. |
| `supply-chain-and-logistics` | Manages the flow of goods and inputs — sourcing, inventory, lead times, fulfilment, and supply risk. |
| `vendor-management` | Selects, contracts, and manages suppliers and vendors — requirements, evaluation, negotiation support, onboarding, performance management, and exit. |

</details>

<details>
<summary><b>Programme Management Office</b> (EPMO / COO) — 6 skills</summary>

| Skill | What it does |
|---|---|
| `benefits-realization` | Ensures projects deliver the value they were approved on — defining measurable benefits, baselining, tracking after delivery, and honest post-implementation review. |
| `change-and-adoption` | Gets people to actually use what was delivered — stakeholder analysis, communication, training, resistance, and measuring adoption. |
| `dependency-and-risk-management` | Manages delivery risk and cross-team dependencies — identifying, sizing, mitigating and escalating what could stop the work. |
| `portfolio-governance` | Governs the portfolio of work — intake, prioritisation, stage gates, resource contention, and stopping things. |
| `program-management` | Plans and drives cross-functional programs to delivery — scope, sequencing, dependencies, status, risk, and the escalations that keep work moving. |
| `project-delivery` | Plans and delivers a single project — scope, estimation, scheduling, critical path, tracking, and recovering when it slips. |

</details>

<details>
<summary><b>Customer Experience</b> (CCO) — 5 skills</summary>

| Skill | What it does |
|---|---|
| `chief-customer-officer` | Owns the customer's experience after the sale — support, success, escalation, and the feedback loop back into product. |
| `escalation-management` | Handles customer situations that have exceeded normal support — severity assessment, incident communication, executive escalation, and recovering a relationship aft…. |
| `self-service-and-knowledge` | Builds the help centre, in-product guidance, and knowledge base that let customers resolve problems without contacting anyone — content, findability, maintenance, a…. |
| `support-operations` | Designs and runs the support function — channels, queues, routing, staffing, service levels, quality, and the metrics that show whether it is working. |
| `voice-of-customer` | Builds the loop from what customers say to what gets changed — collecting feedback, distinguishing signal from noise, routing it to owners, and closing the loop bac…. |

</details>

<details>
<summary><b>Data & Analytics</b> (CDO) — 6 skills</summary>

| Skill | What it does |
|---|---|
| `ai-ml-governance` | Governs models and AI systems in production — intended use, evaluation, monitoring, human oversight, documentation, and the decision to deploy or retire. |
| `business-intelligence` | Builds reporting and self-serve analytics that people actually use — metric trees, dashboard design, distribution, and the discipline that stops dashboards prolifer…. |
| `chief-data-officer` | Owns data as an asset — governance, quality, the warehouse and semantic layer, analytics capability, and the governance of models built on top. |
| `data-engineering` | Builds and operates data pipelines — ingestion, transformation, orchestration, quality testing, and reliability of data delivery. |
| `data-governance` | Establishes ownership, definitions, quality, access, and lineage for the organization's data. |
| `data-modeling` | Designs the warehouse and semantic layer — source-to-mart structure, dimensional modeling, grain, slowly changing dimensions, and the metric layer analytics reads t…. |

</details>

<details>
<summary><b>Corporate Strategy</b> (CSO) — 5 skills</summary>

| Skill | What it does |
|---|---|
| `chief-strategy-officer` | Owns where the business plays and how it wins over a multi-year horizon — portfolio choices, corporate development, strategic partnerships, and planning under uncer…. |
| `mergers-and-acquisitions` | Runs corporate development — deal thesis, target screening, valuation framing, diligence, and integration planning. |
| `portfolio-strategy` | Decides where capital and attention go across business lines, products, and markets — what to fund, hold, harvest, or exit, and on what evidence. |
| `scenario-planning` | Plans under genuine uncertainty — building scenarios, identifying which assumptions are load-bearing, setting early-warning indicators, and stress-testing a plan ag…. |
| `strategic-alliances` | Structures partnerships that change what the business can do — technology integrations, channel and reseller arrangements, joint ventures, and OEM relationships. |

</details>

<details>
<summary><b>People</b> (CHRO) — 9 skills</summary>

| Skill | What it does |
|---|---|
| `chief-human-resources-officer` | Owns the organization itself: org design, hiring, performance, compensation, development, culture, and employee relations. |
| `compensation-and-leveling` | Builds and maintains the leveling framework and pay structure — level definitions, salary bands, benchmarking, pay equity, and how raises and promotions are decided. |
| `employee-relations` | Handles the difficult human situations — grievances, complaints, investigations, conflict, and separations conducted properly. |
| `hiring-and-interviewing` | Designs and runs hiring — role definition, sourcing, interview loop design, structured evaluation, and the decision itself. |
| `learning-and-development` | Builds capability — skills gaps, career frameworks, training that transfers to the job, and internal mobility. |
| `onboarding-and-offboarding` | Designs the joining and leaving experience — first-day readiness, ramp to productivity, knowledge capture, and clean exits. |
| `org-design` | Designs how an organization is structured — reporting lines, team boundaries, spans and layers, role definition, and workforce planning against the strategy. |
| `performance-management` | Runs performance systems that change behaviour — expectations, feedback, review cycles, calibration, and handling underperformance. |
| `workforce-planning` | Plans the shape and size of the workforce — demand for roles, build-versus-buy, attrition, and sequencing hiring against budget. |

</details>

<details>
<summary><b>Legal & Risk</b> (CLO / CCO) — 5 skills · **reviewer-class**</summary>

| Skill | What it does |
|---|---|
| `chief-legal-and-risk-officer` | Owns legal, contracts, intellectual property, regulatory compliance, privacy, security governance, enterprise risk, and audit readiness. |
| `contract-review` | Reviews and negotiates commercial agreements — MSAs, SOWs, order forms, NDAs, vendor and data-processing agreements — identifying material risk, proposing positions…. |
| `corporate-governance` | Maintains the corporate record and the governance machinery — entity records, board and committee support, resolutions and minutes, delegations of authority, insura…. |
| `enterprise-risk` | Identifies, assesses, and tracks organizational risk — building and maintaining a risk register, scoring exposure, assigning owners and treatments, and preparing fo…. |
| `privacy-and-data-protection` | Assesses and improves how personal data is collected, used, shared, and retained — data mapping, lawful basis, consent, processor agreements, subject rights, and br…. |

</details>

**Reviewer-class departments** (`security`, `legal-risk`) review what other departments build, and
their blocking findings are not overrulable by the department under review. That is why the CISO
and the CLO report to the chief executive rather than into the function they oversee.

## How it is organized

```
plugins/<department>/
  .claude-plugin/plugin.json   department manifest
  skills/<skill>/SKILL.md      frontmatter name equals the directory name
.claude/agents/<id>.md         one charter per department
docs/AGENT-SURFACES.md         every path has exactly one owner, enforced in CI
docs/DECISION-LOG.md           numbered decisions with options and recommendations
docs/USE-CASES.md              situations worked end to end across departments
```

Agents split by **exclusive write surface**, not by topic — a topic split has no checkable
boundary, and two agents working on "SEO" and "UI" both end up in the same file. See
`executive:agent-hierarchy` for the method.

## Contributing

```
./scripts/check-all.sh
```

Verifies the surface map is coherent, every skill's frontmatter is valid and unique, no
third-party licence text has appeared, the generated README and social card are current, every
`department:skill` reference in the docs resolves, and every manifest parses. CI runs the same
script, so local and CI cannot drift.

A new department needs its roster row in `docs/AGENT-SURFACES.md`, a surface block, a charter in
`.claude/agents/`, and an entry in `.claude-plugin/marketplace.json` — all in the same change, or
the check fails.

## Licence

MIT — see [LICENSE](LICENSE). Every skill here was written for this repository.

Built by [Chris Brock](https://chrisbrock.io).

---

<sub>README generated by `scripts/build-readme.py` — edit that, not this file.</sub>
