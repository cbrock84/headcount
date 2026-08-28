# agents-v1

An agent organization structured as a company: a chief executive over ten departments, each led by
a C-level agent with specialists beneath it.

Every department is an independently installable plugin, so a project loads only the functions it
needs rather than all 100 skills at once.

There are 100 skills across the ten departments.

```
/plugin marketplace add cbrock84/agents-v1
/plugin install technology@agents-v1
```

Skills are addressed as `department:skill` — `marketing:seo-audit`, `revenue:pricing`.

See [`docs/org-chart.md`](docs/org-chart.md) for the reporting structure and a ranked analysis of
which functions are still missing.

## Departments

### `executive` — Office of the CEO (Chief Executive) · 6 skills

| Skill | What it does |
|---|---|
| `agent-hierarchy` | Designs orchestrator-and-subagent hierarchies for a repository — splitting agents by exclusive write surface, pairing every producer with an independent auditor, and enforcin…. |
| `ai-research-analyst` | Conducts executive-level market research, competitor analysis, trend discovery, and strategic business intelligence grounded in current, cited sources. |
| `business-growth-consultant` | Identifies the real constraint on a business's growth and the highest-leverage moves to increase revenue, profitability, and retention while scaling sustainably. |
| `ceo-advisor` | Acts as an experienced CEO coach and strategic advisor who helps founders make better decisions, prioritize ruthlessly, pressure-test plans, and lead with clarity. |
| `chief-executive` | Sets direction, allocates capital and attention, and makes the calls no one else can make. |
| `saas-idea-validator` | Evaluates SaaS and startup ideas with brutal honesty across problem, market, competition, monetization, defensibility, and execution, and returns a clear verdict rather than…. |

### `technology` — Technology (CTO / CIO) · 16 skills

| Skill | What it does |
|---|---|
| `ai-workflow-architect` | Designs complete AI systems, automations, and agent workflows for businesses using tools like Claude, ChatGPT, MCP servers, APIs, and automation platforms. |
| `brainstorming` | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and desig…. |
| `chief-technology-officer` | Owns architecture, engineering delivery, infrastructure, data platform, and internal systems. |
| `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. |
| `executing-plans` | Use when you have a written implementation plan to execute in a separate session with review checkpoints. |
| `finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work. |
| `prompt-optimizer` | Transforms rough ideas and weak prompts into production-quality prompts for Claude, ChatGPT, Gemini, and other AI models using real prompt-engineering technique, not supersti…. |
| `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and veri…. |
| `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements. |
| `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session. |
| `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes. |
| `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code. |
| `using-git-worktrees` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or…. |
| `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making an…. |
| `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code. |
| `writing-skills` | Use when creating new skills, editing existing skills, or verifying skills work before deployment. |

### `product` — Product (CPO) · 15 skills

| Skill | What it does |
|---|---|
| `banner-design` | Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with AI-generated visuals. Actions: design, create, generate…. |
| `brand` | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of voice, marketing assets, brand compliance, styl…. |
| `brandkit` | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. Trained for minimalist,…. |
| `chief-product-officer` | Owns what gets built and why: product strategy, roadmap, discovery, user experience, and the definition of success for each release. |
| `design-image-direction` | Generates premium design reference images for a product surface before any code is written — screen concepts, flows, and conversion-aware layouts for web or mobile. |
| `design-styles` | Applies a defined visual style to an interface — minimalist editorial, industrial brutalist, or high-end agency polish — covering type scale, spacing, palette, shadows, grid,…. |
| `design-system` | Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→component), CSS variables, spacing/typography scales, component spe…. |
| `design-taste-frontend` | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look tem…. |
| `design` | Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini AI), corporate identity program (50 deliverables, CIP mockups), HTML…. |
| `image-to-code` | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then implement the webs…. |
| `redesign-existing-projects` | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking function…. |
| `slides` | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies. |
| `ui-styling` | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based visual designs. Us…. |
| `ui-ux-pro-max` | UI/UX design intelligence for web and mobile. Searchable local database with 84 styles, 192 color palettes, 74 font pairings, 192 product types, 98 UX guidelines, 104 icon en…. |
| `ux-product-auditor` | Performs senior-level UX, conversion (CRO), usability, and product-strategy audits that tie every finding to a business outcome. |

### `marketing` — Marketing (CMO) · 46 skills

| Skill | What it does |
|---|---|
| `ab-testing` | When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program. Also use when the user mentions "A/B test," "split tes…. |
| `ad-creative` | When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad variations — for any paid advertising platform. Also use wh…. |
| `ads` | When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platforms. Also use when the user mentions…. |
| `ai-seo` | When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the user mentions 'AI SEO,' 'AEO,' 'GEO,' '…. |
| `analytics` | Sets up, audits, and reports on measurement — tracking plans, event schemas, GA4 and product analytics instrumentation, and the dashboards and reporting built on top. |
| `aso` | When the user wants to audit or optimize an App Store or Google Play listing. Also use when the user mentions 'ASO audit,' 'app store optimization,' 'optimize my app listing,…. |
| `attribution` | When the user wants to figure out which marketing actually drives conversions and revenue, choose or interpret an attribution model, or reconcile conflicting numbers across t…. |
| `chief-content-officer` | Acts as a strategic Head of Content who researches the market, analyzes competitors, and builds content strategies and production-ready assets optimized for business outcomes…. |
| `chief-marketing-officer` | Owns brand, demand generation, content, communications, and how the market understands what the business does. |
| `co-marketing` | When the user wants to find co-marketing partners, plan joint campaigns, or brainstorm partnership opportunities. Use when the user says 'co-marketing,' 'partner marketing,'…. |
| `community-marketing` | Build and leverage online communities to drive product growth and brand loyalty. Use when the user wants to create a community strategy, grow a Discord or Slack community, ma…. |
| `competitors` | When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. Also use when the user mentions 'alternative page,' 'vs page,' 'competi…. |
| `content-matrix` | Generate 32+ LinkedIn post ideas in a single table by pairing the user's content pillars with 8 proven content formats. Based on the Justin Welsh content matrix. |
| `copy-editing` | When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content. Also use when the user mentions 'edit this copy,' 'review my copy,' 'cop…. |
| `copywriting` | When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages, pricing pages, feature pages, about pages, or product pages…. |
| `customer-research` | When the user wants to conduct, analyze, or synthesize customer research. Use when the user mentions "customer research," "ICP research," "talk to customers," "analyze transc…. |
| `directory-submissions` | When the user wants to submit their product to startup, SaaS, AI, agent, MCP, no-code, or review directories for backlinks, domain rating, and discovery. Also use when the us…. |
| `emails` | When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. Also use when the user mentions "email sequence,…. |
| `free-tools` | When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or brand awareness. Also use when the user mentions "engineer…. |
| `gemini-carousel` | Generate a branded slide-by-slide LinkedIn carousel using Gemini. Takes source content, builds a design brief, waits for approval, then outputs per-slide image generation pro…. |
| `gemini-infographic` | Generate the hand-drawn whiteboard infographic prompt that pulled 480k impressions across 3 posts. Takes source content (a post, newsletter, blog, research note) and returns…. |
| `graphic-designer` | Create LinkedIn post graphics. Decides between an HTML/CSS structured graphic or an AI-generated infographic based on the post content. |
| `hook-generator` | Generate 6 clickbait-style LinkedIn hook variations for any topic. Two-line hooks built on the formula: a 40-char opening line, a 40-char bold contrast line. Includes digits,…. |
| `influencer-marketing` | When the user wants to run influencer, creator, or ambassador partnerships to promote their product — finding and vetting partners, structuring deals, briefing creators, disc…. |
| `landing-page-cro-expert` | Audits, optimizes, and rewrites landing pages and sales pages using proven conversion-rate-optimization principles to increase signups, sales, and leads. |
| `lead-magnets` | When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation. Also use when the user mentions "lead magnet," "gated content," "content…. |
| `marketing-campaign-planner` | Designs complete, coordinated multi-channel marketing campaigns and product launches built around one clear story, from strategy through timeline, content, and launch checkli…. |
| `marketing-plan` | When the user needs a comprehensive marketing plan for a client, a company they advise, or their own product. Also use when the user mentions "marketing plan," "growth plan,"…. |
| `marketing-psychology` | When the user wants to apply psychological principles, mental models, or behavioral science to marketing. Also use when the user mentions 'psychology,' 'mental models,' 'cogn…. |
| `newsletter-writer` | Writes high-performing newsletters and marketing emails that people actually look forward to opening, built to educate, engage, and convert without sacrificing trust. |
| `niche-research` | Surface the 20 most relevant stories in a niche from the last 7 days using Claude for Chrome. Verified dates, real links, shareable angles. Claude drives the browser to scrol…. |
| `popups` | When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. Also use when the user mentions "exit intent," "popup conve…. |
| `post-writer` | Writes, formats, and scores social posts end to end — drafting in a defined voice, shaping them for how each platform actually renders text, and grading them against engageme…. |
| `product-marketing` | When the user wants to create or update their product marketing context document. Also use when the user mentions 'product context,' 'marketing context,' 'set up context,' 'p…. |
| `profile-optimizer` | Rebuild a LinkedIn profile for maximum conversions. Produces new headline options, about section, experience section, featured section strategy, and 4 image generation prompt…. |
| `programmatic-seo` | When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions "programmatic SEO," "template pages," "pages at scale," "dir…. |
| `public-relations` | When the user wants help with public relations, earned media, press coverage, journalist outreach, or media strategy (not pull requests). Also use when the user mentions 'PR,…. |
| `quote-post` | Two-step workflow for creating quote posts on LinkedIn. Claude generates viral motivational quotes to accompany a caption, then produces a Gemini prompt that recreates a refe…. |
| `reels-scripting` | Turn a reference Instagram Reel into a script for your own Reel, tuned to your voice and repurposed from your newsletter content. Takes a Reel URL or Notion reference link, u…. |
| `schema` | When the user wants to add, fix, or optimize schema markup and structured data on their site. Also use when the user mentions "schema markup," "structured data," "JSON-LD," "…. |
| `seo-audit` | When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO audit," "technical SEO," "why am I not ranking," "SEO issues,…. |
| `site-architecture` | When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal linking. Also use when the user mentions "sitemap," "s…. |
| `sms` | When the user wants to plan, build, or optimize SMS or MMS marketing — including welcome flows, abandoned cart texts, post-purchase, win-back, promotional sends, or transacti…. |
| `voice-builder` | Captures how someone actually writes and turns it into reusable voice instructions every other content skill draws on — analyzing existing samples where they exist, or buildi…. |
| `youtube-producer` | Plans, packages, scripts, and optimizes long-form YouTube videos for retention and channel growth. |
| `youtube-thumbnail` | Generate a branded YouTube thumbnail from a video title. Uses a reference photo of the creator, high-CTR thumbnail principles, and brand colours to produce a ready-to-generat…. |

### `revenue` — Revenue (CRO) · 12 skills

| Skill | What it does |
|---|---|
| `chief-revenue-officer` | Owns the revenue engine end to end: sales, monetization, pricing, customer success, retention, and partnerships. |
| `churn-prevention` | When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments, or implement retention strategies. Also use when the user mentions…. |
| `cold-email` | Write B2B cold emails and follow-up sequences that get replies. Use when the user wants to write cold outreach emails, prospecting emails, cold email campaigns, sales develop…. |
| `offers` | When the user wants to design, construct, or improve an offer — the thing they actually sell — including value framing, bonus stacking, guarantee design, scarcity/urgency, na…. |
| `onboarding` | When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. Also use when the user mentions "onboarding flow," "activatio…. |
| `paywalls` | When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. Also use when the user mentions "paywall," "upgrade screen," "upg…. |
| `pricing` | When the user wants help with pricing decisions, packaging, or monetization strategy. Also use when the user mentions 'pricing,' 'pricing tiers,' 'freemium,' 'free trial,' 'p…. |
| `prospecting` | When the user wants to find, qualify, and build a list of prospects to reach out to — across B2B SaaS, general B2B, or local small businesses. Also use when the user mentions…. |
| `referrals` | When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy. Also use when the user mentions 'referral,' 'affiliate,'…. |
| `revops` | When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes. Also use when the user mentions 'RevOps,' 'revenue opera…. |
| `sales-enablement` | When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts. Also use when the user mentions 'sales deck,' 'pitch deck,'…. |
| `signup` | When the user wants to optimize signup, registration, account creation, or trial activation flows. Also use when the user mentions "signup conversions," "registration frictio…. |

### `finance` — Finance (CFO) · 1 skill — **executive only, specialists not yet built**

| Skill | What it does |
|---|---|
| `chief-financial-officer` | Owns the financial position: planning, budgeting, forecasting, unit economics, cash, and the numbers the business is run and reported on. |

### `operations` — Operations (COO) · 1 skill — **executive only, specialists not yet built**

| Skill | What it does |
|---|---|
| `chief-operating-officer` | Owns execution: how work actually gets done across the organization, including process, program management, capacity, vendors, supply chain, and service delivery. |

### `people` — People (CHRO) · 1 skill — **executive only, specialists not yet built**

| Skill | What it does |
|---|---|
| `chief-human-resources-officer` | Owns the organization itself: org design, hiring, performance, compensation, development, culture, and employee relations. |

### `legal-risk` — Legal & Risk (CLO / CCO) · 1 skill — **executive only, specialists not yet built**

| Skill | What it does |
|---|---|
| `chief-legal-and-risk-officer` | Owns legal, contracts, intellectual property, regulatory compliance, privacy, security governance, enterprise risk, and audit readiness. |

### `administration` — Administration (CAO) · 1 skill — **executive only, specialists not yet built**

| Skill | What it does |
|---|---|
| `chief-administrative-officer` | Owns corporate services and the administrative spine: facilities, corporate records, board and governance support, insurance, internal communications, and the shared services…. |

## Attribution

Skills in `technology`, `product`, `marketing`, and `revenue` were adapted from four
MIT-licensed open-source collections. MIT requires the copyright notice be kept in copies and
substantial portions, so each department retains the upstream license in its `licenses/`
directory. Author names and personal branding have been removed from skill bodies; the notices
remain because the prose is still substantially upstream text.

Three files under `marketing/marketing-plan/references/` carry a citation to *Founding Marketing*.
That is a source credit for excerpted book material, not license boilerplate, and is kept for that
reason.

The executive charters, `design-styles`, `design-image-direction`, and the consolidated
`post-writer`, `voice-builder`, and `analytics` framing are original to this repo.

## Structure

```
plugins/<department>/
  .claude-plugin/plugin.json   department manifest
  skills/<skill>/SKILL.md      frontmatter name must equal the directory name
  licenses/                    upstream notices, where content was adapted
```

Adding a department: create the directory pair above, write the manifest, add the entry to
`.claude-plugin/marketplace.json`, and give it a chief before any specialists.

## Related docs

- [`docs/org-chart.md`](docs/org-chart.md) — reporting structure, gap analysis, structural notes
- [`docs/cross-org-sweep-prompt.md`](docs/cross-org-sweep-prompt.md) — sweeping other GitHub orgs
- `executive:agent-hierarchy` — the method behind this structure
