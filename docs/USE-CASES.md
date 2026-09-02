# Use cases

A collection of skills answers a question. An organization answers a *situation* — several
functions engaging in order, with someone able to say no.

These are the situations this catalog is shaped around. Every skill named here exists; a check
in CI fails if a reference stops resolving, so this page cannot rot as skills are renamed or
consolidated.

New here? [Getting started](GETTING-STARTED.md) covers installing, which departments to take first,
and the three ways to invoke a skill.

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

**Where it stops.** Threat modeling after the build is archaeology. It sits at step five
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

## Situations from an operating company

The situations above are shaped like a software business. These four are shaped like a company with
sites, contracts, staff and customers — and they are where the catalog's operations, IT and finance
depth actually shows. Each one names what comes back, not only what engages.

### Two sites, one lost its link at 6am, and nobody can say whether it is the carrier or us

The first hour goes to arguing about whose problem it is, which is the hour that matters.

1. `operations:incident-management` — declare it, name a commander whose hands stay out of the
   system, and start a timeline. The instinct to skip this because "it's just the link" is what
   turns a thirty-minute outage into a four-hour one.
2. `it-operations:network-administration` — diagnose in layers, from physical upward. The
   multi-site section is the relevant one: a second site multiplies the failure modes, not the work.
3. `operations:vendor-management` — the carrier is a supplier with a contract, and what you can
   demand of them is written down somewhere nobody has read this morning.
4. `operations:service-level-management` — whether their service level was breached, what the
   remedy is, and whether the credit is worth the claim.
5. `operations:business-continuity-and-resilience` — only if it runs long enough to matter, and
   the answer is usually that the impact analysis was never done for this site.

**What comes back.** A separation of two questions that get merged under pressure: *restore service*
and *establish whose fault it is*. The first is yours regardless. The second decides whether you get
a credit and whether you change carriers, and it is answered from the timeline you kept — not from
memory afterward, which is unreliable within hours.

**The hard part it will name.** You almost certainly cannot demonstrate the demarcation point from
your own monitoring, which is why the carrier conversation goes in circles. That is a gap to close
before the next outage, not during this one.

### A vendor renewal auto-renewed at a 22% increase because nobody owned the date

The increase is the symptom. The absence of an owner is the finding.

1. `operations:vendor-management` — the renewal was lost at the notice date, not at the price. Its
   Never list has this exact failure: reaching a renewal date without having started the renewal,
   because the auto-renew clause is the vendor's leverage and it is designed to be.
2. `legal-risk:contract-review` — what the notice period actually required, whether the increase is
   within a cap you already agreed, and what leaving now costs.
3. `finance:budgeting-and-forecasting` — the variance against plan, and whether this repeats across
   other contracts nobody is tracking either.
4. `it-operations:it-asset-management` — if it is software. The SaaS half of the estate is where
   spend hides, and it is found through the expense system and single sign-on logs as much as
   through any inventory.
5. `operations:operating-cadence` — the actual fix: a named owner and a date that surfaces before
   the notice window, rather than a resolution to be more careful.

**What comes back.** Two separate pieces of work. The immediate one is a negotiation you are
entering from a weak position, and it will tell you so plainly — the leverage was in the notice
period and it is spent. The structural one is a renewal register with owners and dates, because a
single renegotiated contract changes nothing about the next four.

**Worth stating.** The honest answer on the 22% may be that you pay it this year. What you can get
is a shorter term, a cap on the next increase, or a co-terminus date that makes the portfolio
manageable — which is `revenue:deal-negotiation` read from the buying side.

### Someone left and still had access to a shared mailbox three weeks later

Every part of this is a process failure, and one part may be an incident.

1. `it-operations:identity-lifecycle-administration` — the leaver path, completely. Shared mailboxes
   and group memberships are the two that survive an offboarding built around the primary account.
2. `it-operations:collaboration-platform-administration` — a shared mailbox with a sign-in-capable
   account is an unmonitored identity with a password, and that is the specific shape of what
   happened here.
3. `security:access-and-identity` — whether the access review would ever have caught it, and
   whether anything else is in the same state right now.
4. `people:onboarding-and-offboarding` — offboarding has to reach identity, devices and payroll on
   the same day, with one owner running the checklist end to end. Split ownership is exactly how
   accounts stay live.
5. `security:detection-and-monitoring` — the uncomfortable question: would you know whether the
   access was used? If the answer is no, that is a bigger finding than the access itself.

**Where it stops.** `security` is reviewer-class. If the mailbox held anything regulated and the
logs cannot rule out access, that becomes an incident with notification clocks attached, and
`legal-risk:privacy-and-data-protection` sets the obligation — a conclusion IT does not get to
overrule on the grounds that it was probably fine.

**What comes back.** A same-day containment step, a sweep for other accounts in the same condition,
and a rewritten leaver checklist. Also a question you may not want: how you found out, because
discovering it three weeks later by accident says the control that should have caught it does not
exist.

### Client rate cards have not been reviewed and now there is a margin problem

The margin moved for a reason, and it is rarely the one people reach for first.

1. `finance:cost-accounting` — decompose price, volume and mix before anything else. Without that,
   a shift toward lower-margin work gets reported as a pricing failure and priced accordingly.
2. `finance:financial-statement-analysis` — the trend and where it started, against prior period
   and against plan, which answer different questions.
3. `finance:unit-economics` — margin by client and by service rather than blended. Blended
   economics almost always conceal one account subsidizing another, and the average is the least
   useful number on the page.
4. `revenue:pricing-and-packaging` — whether the rate card structure is the problem, not just the
   levels. A metric clients cannot predict produces the disputes that erode realized rates.
5. `revenue:deal-negotiation` — repricing an existing client is a negotiation where you have less
   leverage than a new deal, and the concessions have to be traded rather than conceded.
6. `customer-experience:customer-success-management` — which accounts survive a price change and
   which are single-threaded on someone who will not defend it internally.

**What comes back.** Almost always the same finding: it is not one rate card. It is a mix shift,
an allocation basis that flatters some work and punishes other work, and two or three accounts
priced years ago that nobody revisited. Those are three different fixes and only one of them is a
conversation with clients.

**The order matters.** Going to the client with a rate increase before the cost decomposition is
done means arguing for a number you cannot defend, in a conversation you only get once.

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
