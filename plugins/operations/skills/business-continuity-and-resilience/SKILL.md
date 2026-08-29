---
name: business-continuity-and-resilience
description: Plans for operating through disruption — impact analysis, recovery objectives, continuity plans, and the exercises that prove they work. Use this to run a business impact analysis, set RTO and RPO, write or test a continuity plan, prepare for a supplier or site failure, or answer a customer's resilience questionnaire.
---

# Business continuity and resilience

Continuity is a business question wearing technical clothing. The technical restore is covered by
`it-operations:backup-and-recovery`; this is about which processes must keep running, for whom, and
how long you can survive without them.

## Start with impact, not systems

A business impact analysis asks, per process: what breaks downstream, how fast, and who notices.
Work outward from the customer-visible failure, not inward from the asset register — an inventory of
systems tells you what you own, never what matters.

For each critical process establish:

- **Maximum tolerable outage** — the point past which the damage is not recoverable by working harder
  afterwards. This is a business judgement, made by the process owner, not by IT.
- **RTO** — how quickly it must be back. Always shorter than someone wants to pay for.
- **RPO** — how much data you can afford to lose, measured in time. An RPO of zero is a claim about
  spending, not about intent.

RTO and RPO that were not signed by the person accountable for the process are aspirations.

## Plans people can follow badly

A continuity plan is read by a stressed person at 03:00 who did not write it. Optimise for that
reader: named roles rather than names, decision authority stated explicitly, and the first three
actions on the first page.

Include what to do when the plan's assumptions fail — the alternate site is also affected, the key
person is unreachable, the supplier is not answering. Plans that only handle the anticipated failure
handle almost nothing.

## Exercises

Untested plans are documents, not capabilities. Escalate the rigour:

1. **Walkthrough** — read it aloud together and find the steps nobody can actually perform.
2. **Tabletop** — inject a scenario and make the decisions under time pressure.
3. **Live failover** — actually run on the alternate path, in production, with the real people.

The exercise produces findings or it was theatre. Track them as work with owners and dates, and
re-run the scenario that failed rather than a fresh one, so improvement is demonstrable.

## Concentration risk

Resilience fails where dependencies converge invisibly: three suppliers who all sit on one cloud
region, redundant network paths in the same physical duct, a manual workaround that requires a
system you have just lost. Map dependencies to the point where they stop being yours, and check
whether the redundancy is real or just contractual.

## Never

- Set an RTO without the process owner agreeing to what it costs.
- Count a plan as tested because it was reviewed.
- Treat a backup as continuity — an unrestored backup is an untested assumption.
- Write a plan whose first step requires the system that has just failed.
