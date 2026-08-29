# Use cases

A collection of skills answers a question. An organization answers a *situation* — several
functions engaging in order, with someone able to say no.

These are the situations this catalogue is shaped around. Every skill named here exists; a check
in CI fails if a reference stops resolving, so this page cannot rot as skills are renamed or
consolidated.

## Single asks

The fastest path is to just ask. Skills load themselves when a request matches.

| You ask | What loads |
|---|---|
| "why isn't this landing page converting?" | `demand-generation:landing-page-cro-expert` |
| "can we afford this hire?" | `finance:unit-economics` |
| "review this design before we build it" | `security:threat-modeling` |
| "our growth has stalled" | `executive:business-growth-consultant` |
| "is this contract term normal?" | `legal-risk:contract-review` |
| "how should we level this role?" | `people:compensation-and-leveling` |
| "what does the support queue tell us?" | `customer-experience:voice-of-customer` |
| "our data model is a mess" | `data-analytics:data-modeling` |

To force a specific lens, invoke by name: `/finance:financial-modeling`.

---

## Situations that cross departments

Each of these is one prompt, not seven. The point is what engages, in what order, and where it
stops.

### An enterprise prospect demands SOC 2

The deal is real, the certification is not, and sales wants a date.

1. `revenue:chief-revenue-officer` — what the deal is worth and what is genuinely blocked by it
2. `security:security-architecture-review` — the posture you actually have, not the one on the website
3. `security:access-and-identity` — least privilege and joiner-mover-leaver, the controls audits fail on most
4. `legal-risk:privacy-and-data-protection` — the data processing agreement and subprocessor chain
5. `operations:process-design` — evidence collection has to be repeatable, or year two is a fire drill
6. `finance:budgeting-and-forecasting` — auditor, tooling and the engineering time nobody costed

**Where it stops.** `security` is reviewer-class. A finding that the access model can't support the
control isn't a trade-off revenue gets to price against the deal — the date moves, or the control
gets built.

### You've had a security incident

The clock started before you knew.

1. `security:incident-response` — contain first, scope second
2. `legal-risk:privacy-and-data-protection` — which notification clocks are running, and from when
3. `customer-experience:escalation-management` — what affected customers are told, and by whom
4. `marketing:public-relations` — the external statement, if there is one
5. `executive:chief-executive` — who decides, and what is disclosed

**Where it stops.** Communications cannot outrun the legal position. `legal-risk` sets the
notification obligation; PR writes inside it, never ahead of it.

### Should we build this?

Everyone has an opinion and nobody has the number.

1. `product:chief-product-officer` — what problem, for whom, and how you'd know it worked
2. `data-analytics:business-intelligence` — whether the evidence exists or is being asserted
3. `finance:unit-economics` — what it costs to serve once it is real
4. `corporate-strategy:portfolio-strategy` — whether it fits the bets already placed
5. `security:threat-modeling` — before it is built, while changing the design is still cheap
6. `technology:implementation-planning` — what it actually takes

**Where it stops.** Threat modelling after the build is archaeology. It sits at step five
deliberately.

### Growth has stalled

Everyone is proposing a tactic. Nobody has agreed on the diagnosis.

1. `executive:business-growth-consultant` — diagnosis before remedy
2. `data-analytics:business-intelligence` — where the funnel actually leaks
3. `revenue:activation` and `revenue:retention` — whether it is a top or a bottom problem
4. `customer-experience:voice-of-customer` — what the people who stayed and left actually said
5. `demand-generation:experimentation` — how you'd test the fix rather than argue about it
6. `marketing:positioning-and-messaging` — if the leak is that nobody understands the product

**Why the order.** Reaching for `demand-generation:paid-advertising` first is the common failure:
buying traffic for a funnel that leaks makes the leak more expensive.

### Hiring your first real team

Ten offers will encode a structure you will live with for years.

1. `people:org-design` — the shape before the headcount
2. `people:compensation-and-leveling` — bands and levels, before the first offer sets a precedent
3. `finance:budgeting-and-forecasting` — fully loaded cost against runway
4. `people:hiring-and-interviewing` — a process that survives volume
5. `legal-risk:contract-review` — offer letters, IP assignment, classification

**Worth stating plainly.** Employment classification, compensation regulation and equity structuring
are legal and tax matters. These skills structure the decision and tell you what to ask; they are
not a substitute for qualified counsel.

### An enterprise contract lands on your desk

Signed as-is, it is a promise engineering has not seen.

1. `legal-risk:contract-review` — what is unusual, and what is expensive
2. `security:security-architecture-review` — the security addendum, against what you actually run
3. `revenue:pricing-and-packaging` — what the concessions do to the model
4. `finance:unit-economics` — whether the committed SLAs can be served profitably
5. `operations:vendor-management` — obligations that flow down to your subprocessors

**Where it stops.** `legal-risk` is reviewer-class. An uncapped indemnity is not a commercial
preference to be overridden by the revenue number attached to it.

### Preparing for diligence

A buyer's checklist reads your company back to you.

1. `corporate-strategy:mergers-and-acquisitions` — what the process demands and in what order
2. `finance:financial-modeling` — numbers that survive a stranger's questions
3. `legal-risk:corporate-governance` — cap table, board minutes, consents
4. `security:vulnerability-management` — the open findings you will be asked about
5. `data-analytics:data-governance` — what data you hold, under what basis
6. `technology:code-review` — what a technical reviewer will find first

---

## How the org behaves

**Reviewer-class departments** (`security`, `legal-risk`) report to the chief executive rather than
into the functions they review, and their blocking findings are not overrulable by the department
under review. That is why they appear as a stop in the situations above rather than as another
opinion.

**Departments install independently.** Nothing above requires the whole organization. Take the
three departments a situation touches:

```
/plugin install security@headcount
/plugin install legal-risk@headcount
/plugin install revenue@headcount
```

**Delegate a whole department.** Each ships an agent charter in `.claude/agents/`, so a department
can be handed work as a subagent with its own exclusive write surface — see
`executive:agent-hierarchy` for the method and why surfaces, not topics, are the split.
