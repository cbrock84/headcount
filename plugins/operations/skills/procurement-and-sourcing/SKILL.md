---
name: procurement-and-sourcing
description: Buys well — specifying need, running competitive sourcing, negotiating, and category strategy before a contract exists. Use this to run an RFP or vendor selection, negotiate a purchase, consolidate spend across a category, decide between single and multiple suppliers, or bring uncontrolled spending under management.
---

# Procurement and sourcing

This is everything before signature: deciding what to buy, from whom, and on what terms.
`operations:vendor-management` takes over afterward — performance, renewals, exit.

## Specify the need, not the product

Most bad purchases are decided before any supplier is contacted, when a requirement is written as a
product someone already wanted. Specify the outcome and the constraints; let suppliers propose how.

Separate genuine requirements from preferences, and be honest about which is which. A requirements
list that only one supplier satisfies is a purchase order with extra steps, and everyone involved
knows it.

Involve the people who will live with the choice. Procurement that optimizes price against a
specification the users did not agree to produces a cheap thing nobody uses.

## Competition is the leverage

Price is set by the credible presence of an alternative, not by negotiating skill. The single most
effective act in sourcing is having a real second option — and being willing to take it.

Run a fair process: same information to every bidder, same questions answered for all, scoring
agreed before responses arrive. Scoring invented afterward reliably rediscovers the preferred
supplier.

Where genuine competition is impossible — an incumbent with switching costs, a sole source —
acknowledge it rather than staging a process. Then negotiate on the things still open: term length,
renewal caps, service levels, exit assistance.

## Total cost, not price

The quoted figure is a fraction of what you will spend. Model implementation, integration, training,
the internal effort to run it, and what leaving costs.

Watch for cost that arrives later by design: per-seat pricing that grows with headcount, usage
pricing with no cap, renewal uplifts, and support tiers that turn out to be mandatory. Ask what this
costs in year three, and get the answer in the contract.

## Category strategy

Aggregate spend before negotiating it. The same category bought independently by four teams is four
weak negotiating positions and usually four overlapping tools.

Segment by leverage: high-spend commodity categories reward consolidation and hard negotiation;
low-spend specialist ones are not worth the process cost. Concentrating everything on one supplier
buys a discount and sells an exit — see `operations:business-continuity-and-resilience` before
deciding that trade.

Route the resulting terms through `legal-risk:contract-review`, and anything touching customer data
through `legal-risk:privacy-and-data-protection` before signature rather than after.

## Tooling

Procure-to-pay: Coupa, SAP Ariba, Zip, Precoro, and similar. At smaller scale a request
form plus the accounting system's purchase orders does the same work.

Spend visibility: Ramp, Brex, Vertice, and similar, read against the ledger.

Vendor risk lives in the GRC tooling, not here — but the intake form is where the security
and privacy review has to be triggered, or it never happens.

## Never

- Write a requirement that only the preferred supplier can meet.
- Agree scoring criteria after responses arrive.
- Negotiate on price without modeling year-three total cost.
- Consolidate a critical category onto one supplier without pricing the exit.
