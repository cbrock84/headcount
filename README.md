# agents-v1

An agent organization structured as a company: a chief executive over eleven departments, each led
by a C-level agent with specialists beneath it.

Every department is an independently installable plugin, so a project loads only the functions it
There are 79 skills across the eleven departments.

needs.

```
/plugin marketplace add cbrock84/agents-v1
/plugin install finance@agents-v1
```

This repository is **private**, so the installing machine must be authenticated to it. Visibility is
an open question — see D16.

Skills are addressed as `department:skill` — `finance:unit-economics`, `revenue:pricing-and-packaging`.

All content in this repository is original. See [`docs/org-chart.md`](docs/org-chart.md) for the
reporting structure and remaining gaps.

## Departments

### `executive` — Office of the CEO (Chief Executive) · 6 skills

| Skill | What it does |
|---|---|
| `agent-hierarchy` | Designs orchestrator-and-subagent hierarchies for a repository — splitting agents by exclusive write surface, pairing every producer with an independent auditor, and enf…. |
| `ai-research-analyst` | Conducts executive-level market research, competitor analysis, trend discovery, and strategic business intelligence grounded in current, cited sources. |
| `business-growth-consultant` | Identifies the real constraint on a business's growth and the highest-leverage moves to increase revenue, profitability, and retention while scaling sustainably. |
| `ceo-advisor` | Acts as an experienced CEO coach and strategic advisor who helps founders make better decisions, prioritize ruthlessly, pressure-test plans, and lead with clarity. |
| `chief-executive` | Sets direction, allocates capital and attention, and makes the calls no one else can make. |
| `saas-idea-validator` | Evaluates SaaS and startup ideas with brutal honesty across problem, market, competition, monetization, defensibility, and execution, and returns a clear verdict rather…. |

### `technology` — Technology (CTO / CIO) · 12 skills

| Skill | What it does |
|---|---|
| `ai-workflow-architect` | Designs complete AI systems, automations, and agent workflows for businesses using tools like Claude, ChatGPT, MCP servers, APIs, and automation platforms. |
| `branch-and-worktree-workflow` | Isolates feature work in its own branch or worktree and integrates it cleanly when done. |
| `chief-technology-officer` | Owns architecture, engineering delivery, infrastructure, data platform, and internal systems. |
| `code-review` | Conducts and responds to code review — reviewing a change for correctness, design, and risk, and evaluating review feedback received on your own work. |
| `completion-verification` | Verifies that work is actually complete before it is claimed to be — running the checks, reading the output, and confirming the original request was satisfied rather tha…. |
| `implementation-planning` | Turns a spec or requirement into a written plan a separate session or agent can execute, then drives that plan through review checkpoints. |
| `parallel-agent-delivery` | Splits work across multiple agents or sessions running at once, keeping their surfaces disjoint so results merge cleanly. |
| `prompt-optimizer` | Transforms rough ideas and weak prompts into production-quality prompts for Claude, ChatGPT, Gemini, and other AI models using real prompt-engineering technique, not sup…. |
| `skill-authoring` | Writes and revises agent skills so they trigger at the right moments and give usable instruction when they do. |
| `solution-exploration` | Explores the problem and the range of possible approaches before any code is written — clarifying what is actually being asked, surfacing options with their tradeoffs, a…. |
| `systematic-debugging` | Finds the root cause of a bug, test failure, or unexpected behavior before proposing any fix. |
| `test-driven-development` | Drives implementation by writing a failing test first, then the smallest code that passes it. |

### `product` — Product (CPO) · 9 skills

| Skill | What it does |
|---|---|
| `brand-identity` | Defines and applies visual brand — logo usage, palette, typography, imagery direction, and the guidelines that keep expression consistent across product and marketing su…. |
| `chief-product-officer` | Owns what gets built and why: product strategy, roadmap, discovery, user experience, and the definition of success for each release. |
| `design-styles` | Applies a deliberate visual direction to an interface — minimalist editorial, industrial utilitarian, or high-polish commercial — each with its own type scale, palette b…. |
| `design-system` | Builds and maintains the design system a product is assembled from — tokens for color, type, spacing and elevation, component contracts, and the rules that keep them coh…. |
| `interface-craft` | Raises the visual and interaction quality of an interface — layout, hierarchy, type, spacing, density, and the details that separate a considered product from a generic…. |
| `interface-redesign` | Upgrades an existing interface to a higher standard without rebuilding it — auditing what is there, identifying what reads as generic or unfinished, and sequencing chang…. |
| `presentation-design` | Designs slide decks, one-pagers, and marketing graphics that carry an argument rather than decorate one. |
| `ux-product-auditor` | Performs senior-level UX, conversion (CRO), usability, and product-strategy audits that tie every finding to a business outcome. |
| `visual-reference-generation` | Produces design reference imagery before implementation — screen concepts, layout directions, and flows for web or mobile that make a verbal brief concrete enough to arg…. |

### `marketing` — Marketing (CMO) · 16 skills

| Skill | What it does |
|---|---|
| `brand-voice` | Captures how a person or brand actually writes and turns it into reusable voice instructions every other content skill draws from. |
| `chief-content-officer` | Acts as a strategic Head of Content who researches the market, analyzes competitors, and builds content strategies and production-ready assets optimized for business out…. |
| `chief-marketing-officer` | Owns brand, demand generation, content, communications, and how the market understands what the business does. |
| `content-strategy` | Decides what content to make and why — topic territory, format mix, cadence, and how content connects to a business outcome rather than to traffic. |
| `customer-research` | Plans, runs, and synthesizes customer research — interviews, surveys, win-loss analysis, and message testing — into findings that change decisions. |
| `marketing-campaign-planner` | Designs complete, coordinated multi-channel marketing campaigns and product launches built around one clear story, from strategy through timeline, content, and launch ch…. |
| `marketing-copywriting` | Writes and edits marketing copy for any surface — homepage, product and pricing pages, ads, emails, and collateral — and sharpens existing copy that is not working. |
| `marketing-planning` | Builds the marketing plan of record — objectives, channel mix, budget allocation, sequencing, and the measurement that says whether it worked. |
| `newsletter-writer` | Writes high-performing newsletters and marketing emails that people actually look forward to opening, built to educate, engage, and convert without sacrificing trust. |
| `partnership-marketing` | Builds reach through other people's audiences — co-marketing partnerships, creator and influencer programs, community building, and affiliate arrangements. |
| `positioning-and-messaging` | Establishes what a product is understood to be, for whom, and instead of what — then turns that into the messaging every other surface inherits. |
| `public-relations` | Plans and executes earned media — press strategy, journalist outreach, announcements, commentary, and crisis response. |
| `social-post-craft` | Writes, structures, and evaluates social posts end to end — hooks, body, formatting for how each platform renders, and a quality check before publishing. |
| `video-content` | Plans and scripts short-form and long-form video, and designs the packaging — titles, thumbnails, and openings — that determines whether it gets watched. |
| `visual-content` | Designs and directs the visual assets that carry content — carousels, infographics, quote graphics, diagrams, and social imagery — including the generation prompts where…. |
| `youtube-producer` | Plans, packages, scripts, and optimizes long-form YouTube videos for retention and channel growth. |

### `demand-generation` — Demand Generation (CMO) · 11 skills

| Skill | What it does |
|---|---|
| `ai-search-optimization` | Optimizes for AI assistants and AI-generated answers — being retrievable, being cited, and being represented accurately when a model answers on your behalf. |
| `app-store-optimization` | Improves visibility and conversion in the App Store and Google Play — metadata, keywords, screenshots, ratings, and the listing experience that turns an impression into…. |
| `experimentation` | Designs, runs, and reads A/B tests and growth experiments — hypothesis, sample size, duration, and honest interpretation. |
| `landing-page-cro-expert` | Audits, optimizes, and rewrites landing pages and sales pages using proven conversion-rate-optimization principles to increase signups, sales, and leads. |
| `lead-capture` | Converts anonymous traffic into known contacts — lead magnets, gated content, free tools, popups, and the forms behind them. |
| `lifecycle-messaging` | Designs automated email and SMS programs — welcome and onboarding sequences, nurture, re-engagement, transactional messaging, and the timing and segmentation behind them. |
| `listing-distribution` | Gets a product listed where buyers and crawlers look — directories, marketplaces, review sites, comparison pages, and aggregators. |
| `marketing-analytics` | Sets up, audits, and reports on marketing measurement — tracking plans, event schemas, attribution models, and the dashboards built on them. |
| `paid-advertising` | Plans, runs, and optimizes paid acquisition across search, social, and display — account structure, targeting, creative, bidding, budget, and the analysis that says whet…. |
| `programmatic-seo` | Builds large sets of search-targeted pages from a template and a dataset — the location, comparison, integration, and use-case pages that capture long-tail demand at sca…. |
| `seo-strategy` | Audits and improves organic search performance — technical health, site architecture, internal linking, structured data, and the content decisions that determine what ca…. |

### `revenue` — Revenue (CRO) · 8 skills

| Skill | What it does |
|---|---|
| `activation` | Gets new users from signup to first real value — signup flow, onboarding, time-to-value, and the early experience that determines whether someone becomes a user or a lap…. |
| `chief-revenue-officer` | Owns the revenue engine end to end: sales, monetization, pricing, customer success, retention, and partnerships. |
| `outbound-prospecting` | Finds, qualifies, and reaches prospects through cold outreach — list building, qualification criteria, cold email and multi-channel sequences, and the follow-up that act…. |
| `pricing-and-packaging` | Sets price, structures packages and tiers, and designs the monetization surfaces that carry them — upgrade paths, paywalls, and offer construction. |
| `referral-programs` | Designs and improves referral, affiliate, and word-of-mouth programs — incentive structure, mechanics, timing, and fraud control. |
| `retention` | Diagnoses and reduces churn — cancellation flows, save offers, failed-payment recovery, at-risk detection, and the product and service causes underneath. |
| `revenue-operations` | Runs the mechanics of the revenue engine — lead lifecycle definitions, routing, CRM hygiene, forecasting process, pipeline reporting, and the marketing-to-sales handoff. |
| `sales-enablement` | Builds what a sales team needs to sell — pitch decks, one-pagers, objection handling, competitive battlecards, demo scripts, and case studies. |

### `finance` — Finance (CFO) · 4 skills

| Skill | What it does |
|---|---|
| `budgeting-and-forecasting` | Runs the planning cycle — annual budget, rolling forecast, consolidation of business unit inputs, and the variance analysis that explains actuals against plan. |
| `chief-financial-officer` | Owns the financial position: planning, budgeting, forecasting, unit economics, cash, and the numbers the business is run and reported on. |
| `financial-modeling` | Builds and stress-tests financial models for forecasting, scenario planning, and decision support — revenue build, cost structure, driver logic, and the sensitivities th…. |
| `unit-economics` | Establishes whether the business makes money on each customer or unit — contribution margin, acquisition cost, payback period, lifetime value, and the cohort behavior un…. |

### `operations` — Operations (COO) · 4 skills

| Skill | What it does |
|---|---|
| `chief-operating-officer` | Owns execution: how work actually gets done across the organization, including process, program management, capacity, vendors, supply chain, and service delivery. |
| `process-design` | Designs, documents, and fixes operational processes — mapping the current state, finding where work actually stalls, redesigning the flow, and building controls that hold. |
| `program-management` | Plans and drives cross-functional programs to delivery — scope, sequencing, dependencies, status, risk, and the escalations that keep work moving. |
| `vendor-management` | Selects, contracts, and manages suppliers and vendors — requirements, evaluation, negotiation support, onboarding, performance management, and exit. |

### `people` — People (CHRO) · 4 skills

| Skill | What it does |
|---|---|
| `chief-human-resources-officer` | Owns the organization itself: org design, hiring, performance, compensation, development, culture, and employee relations. |
| `compensation-and-leveling` | Builds and maintains the leveling framework and pay structure — level definitions, salary bands, benchmarking, pay equity, and how raises and promotions are decided. |
| `hiring-and-interviewing` | Designs and runs hiring — role definition, sourcing, interview loop design, structured evaluation, and the decision itself. |
| `org-design` | Designs how an organization is structured — reporting lines, team boundaries, spans and layers, role definition, and workforce planning against the strategy. |

### `legal-risk` — Legal & Risk (CLO / CCO) · 4 skills

| Skill | What it does |
|---|---|
| `chief-legal-and-risk-officer` | Owns legal, contracts, intellectual property, regulatory compliance, privacy, security governance, enterprise risk, and audit readiness. |
| `contract-review` | Reviews and negotiates commercial agreements — MSAs, SOWs, order forms, NDAs, vendor and data-processing agreements — identifying material risk, proposing positions, and…. |
| `enterprise-risk` | Identifies, assesses, and tracks organizational risk — building and maintaining a risk register, scoring exposure, assigning owners and treatments, and preparing for aud…. |
| `privacy-and-data-protection` | Assesses and improves how personal data is collected, used, shared, and retained — data mapping, lawful basis, consent, processor agreements, subject rights, and breach…. |

### `administration` — Administration (CAO) · 1 skills

| Skill | What it does |
|---|---|
| `chief-administrative-officer` | Owns corporate services and the administrative spine: facilities, corporate records, board and governance support, insurance, internal communications, and the shared ser…. |

## Provenance

Every skill in this repository was written for it. An earlier revision vendored four MIT-licensed
open-source collections; those were removed in full — skills, reference material, bundled datasets,
fonts, and license files — and the capabilities were re-authored from scratch rather than
paraphrased. Nothing in this repository carries a third-party license obligation.

The gap-department skills in `finance`, `people`, `legal-risk`, and `operations` were scoped against
current senior job postings for those functions, so the remit matches what the roles actually cover.

## Structure

```
plugins/<department>/
  .claude-plugin/plugin.json   department manifest
  skills/<skill>/SKILL.md      frontmatter name must equal the directory name
```

Adding a department: create the directory pair, write the manifest, add it to
`.claude-plugin/marketplace.json`, and give it a chief before any specialists.

## Related docs

- [`docs/DECISION-LOG.md`](docs/DECISION-LOG.md) — open decisions, numbered, with recommendations
- [`docs/org-chart.md`](docs/org-chart.md) — reporting structure and remaining gaps
- [`docs/cross-org-sweep-prompt.md`](docs/cross-org-sweep-prompt.md) — sweeping other GitHub orgs
- `executive:agent-hierarchy` — the method behind this structure
