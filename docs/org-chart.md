# Org chart

```
                              Chief Executive
                                     │
   ┌──────────┬──────────┬───────────┼───────────┬──────────┬──────────┐
   │          │          │           │           │          │          │
  CTO/CIO    CPO        CMO         CRO         CFO        COO        CHRO
Technology  Product   Marketing   Revenue     Finance   Operations   People
   │          │          │           │           │          │          │
   └──────────┴──────────┴─── Legal & Risk (CLO/CCO) ───────┴──────────┘
                                     │
                          Administration (CAO)
```

Legal & Risk sits across every function rather than under one: it reviews what the others commit
to. Administration owns what falls between functions.

## Departments

| Department | Executive | Population | Depth |
|---|---|---|---|
| `executive` | Chief Executive | 6 | staffed |
| `technology` | CTO / CIO | 16 | staffed |
| `product` | CPO | 15 | staffed |
| `marketing` | CMO | 46 | staffed |
| `revenue` | CRO | 12 | staffed |
| `finance` | CFO | 1 | **executive only** |
| `operations` | COO | 1 | **executive only** |
| `people` | CHRO | 1 | **executive only** |
| `legal-risk` | CLO / CCO | 1 | **executive only** |
| `administration` | CAO | 1 | **executive only** |

Five departments have an executive and no staff. That is the honest state: the skills inherited from
existing collections were all go-to-market, engineering, and design. The whole back half of a
company is missing.

## Gaps, ranked

### Tier 1 — a Fortune 500 cannot function without these

**Finance (CFO).** Zero skills. Nothing in this repo can build a budget, model a decision's cost,
compute unit economics, assess runway, or evaluate a spend request. `revenue:pricing` sets prices
without anyone checking the margin. Needed: `financial-modeling`, `budgeting-and-forecasting`,
`unit-economics`, `investment-analysis`, `procurement`.

**Legal & Risk (CLO/CCO).** Zero skills, and the highest-consequence gap. Nothing reviews a
contract, assesses privacy or regulatory exposure, checks an IP or licensing question, or maintains
a risk register. This repo's own licensing question is a live example of the gap. Needed:
`contract-review`, `privacy-and-data-protection`, `regulatory-compliance`, `ip-and-licensing`,
`enterprise-risk`, `audit-readiness`.

**People (CHRO).** Zero skills. No org design, hiring, leveling, compensation, performance, or
employee relations. Needed: `org-design`, `hiring-and-interviewing`, `compensation-and-leveling`,
`performance-management`, `onboarding-employees` (distinct from `revenue:onboarding`, which is
about users).

**Security (CISO).** Zero skills, and not merely a subset of Technology — at Fortune 500 scale the
CISO reports independently precisely so security can say no to engineering. Needed:
`threat-modeling`, `security-review`, `incident-response`, `vulnerability-management`,
`access-and-identity`.

### Tier 2 — structurally expected, currently absent

**Operations (COO).** One executive, no staff: no process design, program management, capacity
planning, vendor management, or supply chain. For a business with physical production this is a
first-tier gap, not a second.

**Data & Analytics (CDO).** `marketing:analytics` covers marketing measurement only. No data
governance, warehouse modeling, BI beyond marketing, or ML/AI governance.

**Customer Experience.** `revenue:churn-prevention` is the only retention-adjacent skill. No
support operations, escalation handling, voice-of-customer, or CSAT/NPS program.

**Corporate Strategy / Corp Dev.** `executive:ai-research-analyst` does market research;
nothing does M&A, partnership diligence, competitive war-gaming, or scenario planning.

**Communications / IR.** `marketing:public-relations` covers press. No internal communications,
executive communications, crisis communications, or investor relations.

### Tier 3 — real at Fortune 500 scale, defer until the business needs them

- **Chief Sustainability / ESG** — emissions reporting, supply-chain diligence, CSRD-style
  disclosure. Increasingly statutory rather than optional.
- **Corporate Secretary** — board minutes, entity governance, filings. Currently folded into
  Administration.
- **Internal Audit** — and a structural note: internal audit reports to the *audit committee*, not
  the CEO. Modeling it under `executive` would reproduce the exact independence failure it exists to
  prevent. If added, it needs a reviewer-class agent that no chief can overrule.
- **Chief Medical / Chief Scientific Officer** — industry-specific, not applicable here.

## Structural notes

**Marketing is oversized.** 46 of 100 skills. It should split into `marketing` (brand, content,
communications) and `demand-generation` (SEO, paid, lifecycle, analytics) once the empty departments
are staffed, or it will keep dominating whatever context it loads into.

**Producer and auditor should not be the same agent.** The `agent-hierarchy` skill in `executive`
makes this rule explicit, and the current chart violates it: every department reviews its own work.
Legal & Risk is the first genuine reviewer-class department. Security and Internal Audit are the
next two.

**Every department is one plugin.** Installing `finance` today gets a CFO charter and nothing
underneath. That is deliberate — the executive can reason about the function and say what is
missing, which is more useful than an empty directory.
