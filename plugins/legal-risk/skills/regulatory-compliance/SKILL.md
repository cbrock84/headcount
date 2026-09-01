---
name: regulatory-compliance
description: Identifies which regulations apply and builds the program that keeps you inside them — obligation mapping, controls, monitoring, and responding to regulators. Use this to work out what applies to your business, stand up a compliance program, prepare for a regulatory exam or certification, respond to a finding, or assess exposure before entering a new market.
---

# Regulatory compliance

Compliance failures are rarely defiance. They are almost always an obligation nobody knew applied,
in a jurisdiction nobody was watching, discovered by someone external.

**This structures the work and names what to ask. Which regulations apply, and what they require,
are legal determinations that vary by jurisdiction and change — they belong with qualified counsel.
Nothing here substitutes for that.**

## Start with an obligation map, not a framework

The first question is not "are we SOC 2 compliant" but "what are we actually obliged to do, by
whom, and what happens if we do not." Build the map from facts about the business:

- **What you sell, and to whom.** Selling to regulated customers pulls their obligations onto you
  through contract even when the regulation does not reach you directly.
- **What data you hold.** Personal data, health data, payment data and children's data each carry
  distinct regimes — see `legal-risk:privacy-and-data-protection`.
- **Where you operate and where your customers are.** Obligations follow the customer more often
  than companies expect.
- **How you are funded and structured.** Public, regulated, or government-adjacent adds regimes.

Distinguish three things that get conflated: **law** you must follow, **certifications** you choose
to obtain commercially, and **contractual commitments** you signed. Only the first carries state
enforcement; all three carry consequences.

## Certifications are evidence, not compliance

SOC 2, ISO 27001 and their equivalents demonstrate that controls exist and operate. They do not
establish that you meet any legal obligation, and a clean report is not a defense to a regulator.

Where they earn their cost is commercially — unblocking deals, as in the SOC 2 situation in
`docs/USE-CASES.md`. Scope them to what the market asks for rather than to everything, since scope
drives cost more than any other decision.

## The program is monitoring, not documentation

A compliance program that produces policies and stops is a shelf. What makes it real:

- **An owner per obligation** — a named person, not a department.
- **Controls that produce evidence as a by-product** of the work, rather than evidence assembled
  before an audit. See `finance:internal-controls-and-audit` for the control design pattern.
- **Monitoring that would detect failure** before an external party does, with the frequency matched
  to how fast the obligation can be breached.
- **Horizon scanning.** Regulation changes; a map built once is wrong within a year.

## When a regulator arrives

Respond promptly, accurately, and narrowly — answer what was asked. Route everything through counsel
before it goes out, preserve records from the moment you are aware, and never let an informal
conversation become an undocumented commitment.

Findings get root-caused like any other failure. A remediation that consists of retraining people on
a process that made the failure easy will produce the same finding next cycle.

## Tooling

Compliance automation — Vanta, Drata, Secureframe, Keel GRC, and similar — collects
evidence continuously and maps one control across several frameworks. It earns its cost on
the second audit far more often than the first.

Policy and attestation lives in those same tools, or in the HRIS, or in Confluence. What
matters is that a policy carries a version, an owner, and a record of who acknowledged it.

## Never

- Treat a certification as evidence of legal compliance.
- Build a compliance program without a named owner per obligation.
- Assemble control evidence retrospectively for an audit.
- Answer a regulator without counsel reviewing the response.
