# agents-v1

An in-house organization of Claude agents, built up as **skills**.

Two tiers:

- **Core** — `.claude/skills/`. Twelve general business advisors plus `agent-hierarchy`, the method
  for structuring the organization itself. These load automatically in this repo.
- **Departments** — `plugins/`. Specialist teams installed per-project, so only the relevant ones
  occupy context.

## Installing a department

```
/plugin marketplace add cbrock84/agents-v1
/plugin install marketing@agents-v1
```

Each department is independent — install only what a project needs. Plugin skills are addressed as
`department:skill` (e.g. `marketing:seo-audit`), so names never collide with the core skills or with
each other.

## Core (always on)

| Skill | What it does |
|---|---|
| `agent-hierarchy` | Designs orchestrator-and-subagent hierarchies for a repository — splitting agents by exclusive write surface, pairing every producer with an independent auditor, and enforcing the split with a script that runs in CI. |
| `ai-research-analyst` | Conducts executive-level market research, competitor analysis, trend discovery, and strategic business intelligence grounded in current, cited sources. |
| `ai-workflow-architect` | Designs complete AI systems, automations, and agent workflows for businesses using tools like Claude, ChatGPT, MCP servers, APIs, and automation platforms. |
| `business-growth-consultant` | Identifies the real constraint on a business's growth and the highest-leverage moves to increase revenue, profitability, and retention while scaling sustainably. |
| `ceo-advisor` | Acts as an experienced CEO coach and strategic advisor who helps founders make better decisions, prioritize ruthlessly, pressure-test plans, and lead with clarity. |
| `chief-content-officer` | Acts as a strategic Head of Content who researches the market, analyzes competitors, and builds content strategies and production-ready assets optimized for business outcomes, not vani…. |
| `landing-page-cro-expert` | Audits, optimizes, and rewrites landing pages and sales pages using proven conversion-rate-optimization principles to increase signups, sales, and leads. |
| `marketing-campaign-planner` | Designs complete, coordinated multi-channel marketing campaigns and product launches built around one clear story, from strategy through timeline, content, and launch checklist. |
| `newsletter-writer` | Writes high-performing newsletters and marketing emails that people actually look forward to opening, built to educate, engage, and convert without sacrificing trust. |
| `prompt-optimizer` | Transforms rough ideas and weak prompts into production-quality prompts for Claude, ChatGPT, Gemini, and other AI models using real prompt-engineering technique, not superstition. |
| `saas-idea-validator` | Evaluates SaaS and startup ideas with brutal honesty across problem, market, competition, monetization, defensibility, and execution, and returns a clear verdict rather than encouragem…. |
| `ux-product-auditor` | Performs senior-level UX, conversion (CRO), usability, and product-strategy audits that tie every finding to a business outcome. |
| `youtube-producer` | Plans, packages, scripts, and optimizes long-form YouTube videos for retention and channel growth. |

The `agent-hierarchy` skill carries the governance method for this repo's own growth, vendored
from [`cbrock84/agent-hierarchy`](https://github.com/cbrock84/agent-hierarchy):

- `references/playbook.md` — the full playbook (surface splitting, the guard, registry, decision
  log, anti-patterns, sizing, multi-repo layouts, charter format, day-one checklist).
- `references/starter-rosters.md` — rosters for mobile-app, game, and shared-core portfolios.
- `references/bootstrap-prompt.md` — fill-in-the-blanks prompt for a fresh session.
- `scripts/agent-guard.mjs` — the executable guard: `check` proves the surface map is coherent,
  `diff <agent>` proves a diff obeyed it. No dependencies, Node 18+.

## Departments

### `engineering` — 13 skills

Development workflow discipline: TDD, systematic debugging, planning, code review, and verification.

| Skill | What it does |
|---|---|
| `brainstorming` | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before i…. |
| `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. |
| `executing-plans` | Use when you have a written implementation plan to execute in a separate session with review checkpoints. |
| `finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work. |
| `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification,…. |
| `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements. |
| `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session. |
| `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes. |
| `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code. |
| `using-git-worktrees` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git workt…. |
| `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success…. |
| `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code. |
| `writing-skills` | Use when creating new skills, editing existing skills, or verifying skills work before deployment. |

### `marketing` — 39 skills

Demand generation, SEO, paid acquisition, lifecycle, pricing, and revenue operations.

| Skill | What it does |
|---|---|
| `ab-testing` | When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program. Also use when the user mentions "A/B test," "split test," "exper…. |
| `ad-creative` | When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad variations — for any paid advertising platform. Also use when the use…. |
| `ads` | When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platforms. Also use when the user mentions 'PPC,' 'p…. |
| `ai-seo` | When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the user mentions 'AI SEO,' 'AEO,' 'GEO,' 'LLMO,' 'an…. |
| `analytics` | When the user wants to set up, improve, or audit analytics tracking and measurement. Also use when the user mentions "set up tracking," "GA4," "Google Analytics," "conversion tracking,…. |
| `aso` | When the user wants to audit or optimize an App Store or Google Play listing. Also use when the user mentions 'ASO audit,' 'app store optimization,' 'optimize my app listing,' 'improve…. |
| `attribution` | When the user wants to figure out which marketing actually drives conversions and revenue, choose or interpret an attribution model, or reconcile conflicting numbers across tools. Also…. |
| `churn-prevention` | When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments, or implement retention strategies. Also use when the user mentions 'churn,'…. |
| `co-marketing` | When the user wants to find co-marketing partners, plan joint campaigns, or brainstorm partnership opportunities. Use when the user says 'co-marketing,' 'partner marketing,' 'joint cam…. |
| `cold-email` | Write B2B cold emails and follow-up sequences that get replies. Use when the user wants to write cold outreach emails, prospecting emails, cold email campaigns, sales development email…. |
| `community-marketing` | Build and leverage online communities to drive product growth and brand loyalty. Use when the user wants to create a community strategy, grow a Discord or Slack community, manage a for…. |
| `competitors` | When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. Also use when the user mentions 'alternative page,' 'vs page,' 'competitor compar…. |
| `copy-editing` | When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content. Also use when the user mentions 'edit this copy,' 'review my copy,' 'copy feedback…. |
| `copywriting` | When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages, pricing pages, feature pages, about pages, or product pages. Also use…. |
| `customer-research` | When the user wants to conduct, analyze, or synthesize customer research. Use when the user mentions "customer research," "ICP research," "talk to customers," "analyze transcripts," "c…. |
| `directory-submissions` | When the user wants to submit their product to startup, SaaS, AI, agent, MCP, no-code, or review directories for backlinks, domain rating, and discovery. Also use when the user mention…. |
| `emails` | When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. Also use when the user mentions "email sequence," "drip ca…. |
| `free-tools` | When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or brand awareness. Also use when the user mentions "engineering as mar…. |
| `influencer-marketing` | When the user wants to run influencer, creator, or ambassador partnerships to promote their product — finding and vetting partners, structuring deals, briefing creators, disclosure com…. |
| `lead-magnets` | When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation. Also use when the user mentions "lead magnet," "gated content," "content upgrade,"…. |
| `marketing-plan` | When the user needs a comprehensive marketing plan for a client, a company they advise, or their own product. Also use when the user mentions "marketing plan," "growth plan," "GTM plan…. |
| `marketing-psychology` | When the user wants to apply psychological principles, mental models, or behavioral science to marketing. Also use when the user mentions 'psychology,' 'mental models,' 'cognitive bias…. |
| `offers` | When the user wants to design, construct, or improve an offer — the thing they actually sell — including value framing, bonus stacking, guarantee design, scarcity/urgency, naming, and…. |
| `onboarding` | When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. Also use when the user mentions "onboarding flow," "activation rate," "…. |
| `paywalls` | When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. Also use when the user mentions "paywall," "upgrade screen," "upgrade modal…. |
| `popups` | When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. Also use when the user mentions "exit intent," "popup conversions," "…. |
| `pricing` | When the user wants help with pricing decisions, packaging, or monetization strategy. Also use when the user mentions 'pricing,' 'pricing tiers,' 'freemium,' 'free trial,' 'packaging,'…. |
| `product-marketing` | When the user wants to create or update their product marketing context document. Also use when the user mentions 'product context,' 'marketing context,' 'set up context,' 'positioning…. |
| `programmatic-seo` | When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions "programmatic SEO," "template pages," "pages at scale," "directory pag…. |
| `prospecting` | When the user wants to find, qualify, and build a list of prospects to reach out to — across B2B SaaS, general B2B, or local small businesses. Also use when the user mentions "prospect…. |
| `public-relations` | When the user wants help with public relations, earned media, press coverage, journalist outreach, or media strategy (not pull requests). Also use when the user mentions 'PR,' 'public…. |
| `referrals` | When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy. Also use when the user mentions 'referral,' 'affiliate,' 'ambassad…. |
| `revops` | When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes. Also use when the user mentions 'RevOps,' 'revenue operations,' 'l…. |
| `sales-enablement` | When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts. Also use when the user mentions 'sales deck,' 'pitch deck,' 'one-page…. |
| `schema` | When the user wants to add, fix, or optimize schema markup and structured data on their site. Also use when the user mentions "schema markup," "structured data," "JSON-LD," "rich snipp…. |
| `seo-audit` | When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO audit," "technical SEO," "why am I not ranking," "SEO issues," "on-page…. |
| `signup` | When the user wants to optimize signup, registration, account creation, or trial activation flows. Also use when the user mentions "signup conversions," "registration friction," "signu…. |
| `site-architecture` | When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal linking. Also use when the user mentions "sitemap," "site map,"…. |
| `sms` | When the user wants to plan, build, or optimize SMS or MMS marketing — including welcome flows, abandoned cart texts, post-purchase, win-back, promotional sends, or transactional/auth…. |

### `content` — 16 skills

Social, newsletter, and short-form content production.

| Skill | What it does |
|---|---|
| `analytics-dashboard` | Turn a LinkedIn Analytics export into an interactive dark-themed React dashboard plus a written strategic analysis with 5 data-backed content recommendations. Reads every sheet in the…. |
| `content-matrix` | Generate 32+ LinkedIn post ideas in a single table by pairing the user's content pillars with 8 proven content formats. Based on the Justin Welsh content matrix. |
| `gemini-carousel` | Generate a branded slide-by-slide LinkedIn carousel using Gemini. Takes source content, builds a design brief, waits for approval, then outputs per-slide image generation prompts. 1080…. |
| `gemini-infographic` | Generate the hand-drawn whiteboard infographic prompt that pulled 480k impressions across 3 posts. Takes source content (a post, newsletter, blog, research note) and returns a complete…. |
| `graphic-designer` | Create LinkedIn post graphics. Decides between an HTML/CSS structured graphic or an AI-generated infographic based on the post content. |
| `hook-generator` | Generate 6 clickbait-style LinkedIn hook variations for any topic. Two-line hooks built on the formula: a 40-char opening line, a 40-char bold contrast line. Includes digits, "How I" o…. |
| `newsletter-voice` | Build newsletter writing instructions inside a Cowork project. Runs after voice-builder. Produces newsletter-voice.md, a single file Claude references when drafting newsletters in the…. |
| `niche-research` | Surface the 20 most relevant stories in a niche from the last 7 days using Claude for Chrome. Verified dates, real links, shareable angles. Claude drives the browser to scroll Reddit,…. |
| `post-formatter` | Turn a topic into a ready-to-publish LinkedIn post using PAS, AIDA, BAB, STAR, or SLAY frameworks. 200 to 250 words, 20 lines max, mobile-formatted with blank lines between sentences. |
| `post-scorer` | Score a LinkedIn post using real performance data. Pulls the user's own post history via Apify (or uses cached data) to identify what actually performs, then scores the draft against t…. |
| `post-writer` | Write LinkedIn posts that match the user's voice system (about-me.md and voice.md). |
| `profile-optimizer` | Rebuild a LinkedIn profile for maximum conversions. Produces new headline options, about section, experience section, featured section strategy, and 4 image generation prompts (banner,…. |
| `quote-post` | Two-step workflow for creating quote posts on LinkedIn. Claude generates viral motivational quotes to accompany a caption, then produces a Gemini prompt that recreates a reference imag…. |
| `reels-scripting` | Turn a reference Instagram Reel into a script for your own Reel, tuned to your voice and repurposed from your newsletter content. Takes a Reel URL or Notion reference link, uses Apify…. |
| `voice-builder` | Build a personalised voice profile inside a Cowork project from a short interview plus 3 to 5 sample pieces of writing. Works for any content format: LinkedIn posts, newsletters, essay…. |
| `youtube-thumbnail` | Generate a branded YouTube thumbnail from a video title. Uses a reference photo of the creator, high-CTR thumbnail principles, and brand colours to produce a ready-to-generate image pr…. |

### `design` — 16 skills

UI/UX design intelligence and frontend taste.

| Skill | What it does |
|---|---|
| `banner-design` | Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with AI-generated visuals. Actions: design, create, generate banner. Pl…. |
| `brand` | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of voice, marketing assets, brand compliance, style guides. |
| `brandkit` | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. Trained for minimalist, cinematic,…. |
| `design-system` | Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→component), CSS variables, spacing/typography scales, component specs, strate…. |
| `design-taste-frontend` | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Re…. |
| `design` | Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini AI), corporate identity program (50 deliverables, CIP mockups), HTML presentat…. |
| `high-end-visual-design` | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive. Blocks all the common de…. |
| `image-to-code` | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then implement the website to mat…. |
| `imagegen-frontend-mobile` | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobile products. Prioritizes clean hie…. |
| `imagegen-frontend-web` | Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate horizontal image FOR EVERY section…. |
| `industrial-brutalist-ui` | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, analog degradation effects. For…. |
| `minimalist-ui` | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows. |
| `redesign-existing-projects` | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality. Wor…. |
| `slides` | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies. |
| `ui-styling` | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based visual designs. Use when bui…. |
| `ui-ux-pro-max` | UI/UX design intelligence for web and mobile. Searchable local database with 84 styles, 192 color palettes, 74 font pairings, 192 product types, 98 UX guidelines, 104 icon entries, 16…. |

## Provenance

Every department skill is vendored verbatim from an MIT-licensed upstream collection. Upstream
licenses are kept alongside each department in `plugins/<dept>/licenses/`.

| Upstream | Author | Used by | Skills |
|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | Jesse Vincent | `engineering` (13) | 13 |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | Corey Haines | `marketing` (39) | 39 |
| [charliehills/social-media-skills](https://github.com/charliehills/social-media-skills) | Charlie Hills | `content` (16) | 16 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Next Level Builder | `design` (7) | 7 |
| [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) | Leon Lin | `design` (9) | 9 |

Six `taste-skill` directories were renamed to match the `name` their own frontmatter declares
(for example `taste-skill/` → `design-taste-frontend/`), which Claude Code requires. No skill
content was edited.

### What was left out

The five upstream collections hold 106 skills; 84 were taken. Skipped:

- **Duplicates of the core advisors** — `cro`, `content-strategy`, `social`, `launch`,
  `competitor-profiling`, `marketing-ideas`, already covered by `landing-page-cro-expert`,
  `chief-content-officer`, `marketing-campaign-planner`, `ai-research-analyst`, and
  `business-growth-consultant`.
- **Superseded or tool-locked variants** — `taste-skill-v1` (upstream marks it legacy),
  `gpt-tasteskill` (targets Codex), `stitch-skill` (Google Stitch only).
- **Author-personalized** — `pinned-comment`, written for its author's own LinkedIn voice.
- **Intrusive meta-skills** — `using-superpowers`, which demands invocation before every response.
- **Overlapping media helpers** — `image`, `video`, `marketing-loops`, `marketing-council`.

## Reaching the other orgs

A session can only attach repos from one owner, so `Keel-GRC` and `Drummond-IT` material cannot
be pushed here from a session rooted in those orgs, or pulled by attaching them from this one.
Public repos in those orgs are still readable here via anonymous clone; private and internal
ones need a session rooted in that org that hands results back as a file.

`docs/cross-org-sweep-prompt.md` has the prompt for that sweep and the details of the split.

## Adding a department

1. `mkdir -p plugins/<name>/{.claude-plugin,skills}`
2. Write `plugins/<name>/.claude-plugin/plugin.json` (copy an existing one).
3. Add the entry to `.claude-plugin/marketplace.json`.
4. Each skill is a directory holding `SKILL.md`, whose frontmatter `name` must equal the directory
   name and be lowercase-hyphenated.
