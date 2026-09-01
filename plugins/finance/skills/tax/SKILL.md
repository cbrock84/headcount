---
name: tax
description: Structures the tax questions a growing business faces — corporate income, sales and use, payroll, nexus, and the obligations created by hiring or selling somewhere new. Use this to work out what a new state or country obligates you to, prepare for a tax filing or audit, understand sales tax on your product, or check what a remote hire or new market triggers.
---

# Tax

Tax obligations are created by facts — where you sell, where people work, what you sell — not by
decisions anyone consciously makes. The characteristic failure is discovering an obligation years
after it began, with penalties and interest attached.

**This structures the question and tells you what to ask. Tax is technical, jurisdiction-specific,
and changes frequently. Positions on anything material belong with a qualified tax adviser or CPA,
not a checklist.**

## Nexus: the thing that creates obligations quietly

Nexus is the connection that gives a jurisdiction the right to tax you. It is established by
activities most companies do not think of as tax events:

- **An employee working somewhere.** One remote hire in a new state commonly creates payroll
  registration, income tax withholding, and often corporate income tax nexus.
- **Economic activity without physical presence.** Since *Wayfair*, US states set sales-tax nexus on
  revenue or transaction thresholds — a few hundred thousand dollars, or a couple of hundred
  transactions, with the numbers differing by state.
- **Inventory held somewhere**, including in a third-party fulfillment warehouse you never visit.
- **Contractors, or attending trade shows**, in some jurisdictions.

Review nexus whenever you hire in a new location, cross a revenue threshold, or change how you
distribute. Registering late costs more than registering early, and voluntary disclosure programs
exist precisely because this is so common.

## Sales tax is about what you sell, not what you charge

Taxability of software and services varies enormously by state: SaaS is taxable in some, exempt in
others, and treated differently again if delivered with implementation services. The classification
of your own product is a determination worth getting in writing and revisiting when packaging
changes — see `revenue:pricing-and-packaging`, because bundling can change the answer.

Exemption certificates for tax-exempt customers must be collected and kept current. In an audit,
missing certificates mean you owe the tax you did not collect.

## The calendar is most of the discipline

Tax failures are usually administrative, not technical: a missed registration, a late filing, an
estimated payment nobody scheduled. Maintain a calendar of every obligation by jurisdiction with an
owner, and treat it as part of `finance:financial-reporting-and-close`.

## Where it meets the rest of finance

- `finance:financial-reporting-and-close` — tax provision and the deferred position
- `finance:capital-allocation` — after-tax returns are the only ones that matter for a decision
- `people:workforce-planning` — every hire in a new jurisdiction is a tax question before it is a
  cost question
- `finance:revenue-recognition` — book and tax treatment diverge, and the difference is itself
  something to track

## Never

- Assume no obligation because there is no office in a jurisdiction.
- Treat your product's taxability as settled across states without a determination.
- Sell into exempt customers without current exemption certificates.
- Take a position on a material matter without a qualified adviser.
