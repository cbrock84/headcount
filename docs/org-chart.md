# Org chart

```
                              Chief Executive
                                     │
   ┌──────────┬──────────┬───────────┼───────────┬──────────┬──────────┐
   │          │          │           │           │          │          │
 CTO/CIO     CPO        CMO         CRO         CFO        COO        CHRO
Technology  Product  Marketing +   Revenue    Finance  Operations   People
                     Demand Gen
   │          │          │           │           │          │          │
   └──────────┴──────────┴─── Legal & Risk (CLO/CCO) ───────┴──────────┘
                                     │
                          Administration (CAO)
```

Legal & Risk sits across every function rather than under one: it reviews what the others commit
to. Administration owns what falls between functions.

## Departments

| Department | Executive | Skills |
|---|---|---|
| `executive` | Chief Executive | 6 |
| `technology` | CTO / CIO | 12 |
| `product` | CPO | 9 |
| `marketing` | CMO | 16 |
| `demand-generation` | CMO | 11 |
| `revenue` | CRO | 8 |
| `finance` | CFO | 4 |
| `operations` | COO | 4 |
| `people` | CHRO | 4 |
| `legal-risk` | CLO / CCO | 4 |
| `administration` | CAO | 1 |

Marketing was split: brand, content, and communications stay under `marketing`; acquisition,
conversion, and measurement moved to `demand-generation`. Both report to the CMO. The split keeps
specialization while halving what any one install loads.

## Remaining gaps, ranked

### Tier 1 — build next

**Security (CISO).** Still zero skills, and it should be its own department rather than living
under Technology: at scale the CISO reports independently so security can overrule engineering.
Needed: `threat-modeling`, `security-architecture-review`, `incident-response`,
`vulnerability-management`, `access-and-identity`. The `legal-risk` department covers governance and
audit readiness but not technical security work.

**Finance depth.** Four skills cover planning and analysis. Missing: `procurement`,
`investment-analysis`, `cash-management`, `revenue-recognition`, `financial-controls`.

**People depth.** Missing: `performance-management`, `employee-relations`, `learning-and-development`,
`workforce-planning`, `employee-onboarding` (distinct from `revenue:activation`, which is users).

**Legal depth.** Missing: `ip-and-licensing`, `regulatory-compliance`, `audit-readiness`,
`corporate-governance`.

### Tier 2

**Data & Analytics (CDO).** `demand-generation:marketing-analytics` covers marketing measurement
only. No data governance, warehouse modeling, BI beyond marketing, or AI/ML governance — the last
is increasingly a board-level obligation.

**Customer Experience.** `revenue:retention` is the only adjacent skill. No support operations,
escalation handling, or voice-of-customer program.

**Corporate Strategy / Corp Dev.** `executive:ai-research-analyst` does market research; nothing
covers M&A, diligence, or scenario planning.

**Operations depth.** Three skills. A business with physical production also needs
`supply-chain-planning`, `quality-management`, and `capacity-planning`.

### Tier 3 — when the business needs them

- **Chief Sustainability / ESG** — emissions reporting and supply-chain diligence, increasingly
  statutory rather than optional.
- **Corporate Secretary** — currently folded into Administration.
- **Internal Audit** — with a structural caveat: internal audit reports to the audit committee, not
  the CEO. Placing it under `executive` would reproduce the independence failure it exists to
  prevent. It needs a reviewer-class agent no chief can overrule.
- **Investor Relations** — only once there are investors to relate to.

## Structural notes

**Producer and auditor should not be the same agent.** The `executive:agent-hierarchy` skill makes
this explicit, and the chart still partly violates it: most departments review their own work.
`legal-risk` is the first genuine reviewer-class department. Security and Internal Audit are the
next two, and both need the authority to block.

**Administration is a placeholder.** One charter, no specialists. It exists so orphaned
responsibilities have somewhere to go rather than accumulating unowned.

**How gap skills were scoped.** The `finance`, `people`, `legal-risk`, and `operations` skills were
drafted against current senior job postings for those functions — FP&A leadership, commercial
counsel, cybersecurity GRC, and HR business partner roles — so each skill's remit reflects what the
role is actually accountable for rather than an assumption about it.
