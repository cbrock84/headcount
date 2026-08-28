# agents-v1

A set of 12 Claude skills, each acting as a specialist agent. They live in
`.claude/skills/` so Claude Code picks them up automatically in this repo.

| # | Skill | Directory | What it does |
|---|---|---|---|
| 1 | Chief Content Officer | [`.claude/skills/chief-content-officer/`](.claude/skills/chief-content-officer/SKILL.md) | Acts as a strategic Head of Content who researches the market, analyzes competitors, and builds content strategies and production-ready assets optimized for business outcomes, not vanity metrics. |
| 2 | AI Research Analyst | [`.claude/skills/ai-research-analyst/`](.claude/skills/ai-research-analyst/SKILL.md) | Conducts executive-level market research, competitor analysis, trend discovery, and strategic business intelligence grounded in current, cited sources. |
| 3 | Landing Page CRO Expert | [`.claude/skills/landing-page-cro-expert/`](.claude/skills/landing-page-cro-expert/SKILL.md) | Audits, optimizes, and rewrites landing pages and sales pages using proven conversion-rate-optimization principles to increase signups, sales, and leads. |
| 4 | SaaS Idea Validator | [`.claude/skills/saas-idea-validator/`](.claude/skills/saas-idea-validator/SKILL.md) | Evaluates SaaS and startup ideas with brutal honesty across problem, market, competition, monetization, defensibility, and execution, and returns a clear verdict rather than encouragement. |
| 5 | AI Workflow Architect | [`.claude/skills/ai-workflow-architect/`](.claude/skills/ai-workflow-architect/SKILL.md) | Designs complete AI systems, automations, and agent workflows for businesses using tools like Claude, ChatGPT, MCP servers, APIs, and automation platforms. |
| 6 | UX & Product Auditor | [`.claude/skills/ux-product-auditor/`](.claude/skills/ux-product-auditor/SKILL.md) | Performs senior-level UX, conversion (CRO), usability, and product-strategy audits that tie every finding to a business outcome. |
| 7 | Newsletter Writer | [`.claude/skills/newsletter-writer/`](.claude/skills/newsletter-writer/SKILL.md) | Writes high-performing newsletters and marketing emails that people actually look forward to opening, built to educate, engage, and convert without sacrificing trust. |
| 8 | YouTube Producer | [`.claude/skills/youtube-producer/`](.claude/skills/youtube-producer/SKILL.md) | Plans, packages, scripts, and optimizes long-form YouTube videos for retention and channel growth. |
| 9 | Marketing Campaign Planner | [`.claude/skills/marketing-campaign-planner/`](.claude/skills/marketing-campaign-planner/SKILL.md) | Designs complete, coordinated multi-channel marketing campaigns and product launches built around one clear story, from strategy through timeline, content, and launch checklist. |
| 10 | Business Growth Consultant | [`.claude/skills/business-growth-consultant/`](.claude/skills/business-growth-consultant/SKILL.md) | Identifies the real constraint on a business's growth and the highest-leverage moves to increase revenue, profitability, and retention while scaling sustainably. |
| 11 | CEO Advisor | [`.claude/skills/ceo-advisor/`](.claude/skills/ceo-advisor/SKILL.md) | Acts as an experienced CEO coach and strategic advisor who helps founders make better decisions, prioritize ruthlessly, pressure-test plans, and lead with clarity. |
| 12 | Prompt Optimizer | [`.claude/skills/prompt-optimizer/`](.claude/skills/prompt-optimizer/SKILL.md) | Transforms rough ideas and weak prompts into production-quality prompts for Claude, ChatGPT, Gemini, and other AI models using real prompt-engineering technique, not superstition. |

## Usage

Claude Code loads every `SKILL.md` under `.claude/skills/` and invokes one when a
request matches its `description`. You can also call one by name, e.g. `/ceo-advisor`.

## Notes

Skill bodies are imported verbatim. The only edit is the frontmatter `name:` field,
which was changed from the display name to the directory slug (lowercase and
hyphenated) so the skills validate and load. The display name is preserved as the
`# Heading` at the top of each file.
