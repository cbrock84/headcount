---
name: retention
description: Diagnoses and reduces churn — cancellation flows, save offers, failed-payment recovery, at-risk detection, and the product and service causes underneath. Use this when churn is rising or unexplained, to design a cancellation or win-back flow, to recover involuntary churn, to identify at-risk accounts before they leave, or to decide whether a retention problem is a product problem.
---

# Retention

## Separate the two churns first

They have nothing in common but the outcome, and conflating them wastes effort:

- **Involuntary** — payment failed. Often a large share of total churn, entirely mechanical, and the
  cheapest thing to fix in the whole business.
- **Voluntary** — they chose to leave.

Fix involuntary first. Card retries on a sensible schedule, dunning emails that reach a human,
pre-expiry notification, and a grace period that does not immediately cut off access. This is
recoverable revenue sitting untouched in most companies.

## Diagnosing voluntary churn

Ask when the decision was actually made. It is almost never at cancellation — it is weeks earlier,
at a failed expectation, an unresolved support issue, or a champion leaving.

Segment churn by tenure, plan, acquisition channel, and activation status. Concentrations tell you
the cause:

- **Early churn** — activation problem, not retention. Fix onboarding.
- **Churn at renewal** — value not visible enough to justify the line item.
- **Churn after a specific event** — find the event: a price change, an outage, a redesign, a
  champion departure.
- **Churn concentrated in one channel** — an acquisition problem. You are buying the wrong
  customers, and no retention work fixes that.

## Cancellation flow

Make cancelling straightforward. Obstruction generates chargebacks, public complaints, and in a
growing number of jurisdictions, regulatory exposure.

Do ask why, with specific options plus free text — this is the highest-quality product feedback you
will ever receive, from people with no reason to be polite.

Offer a save only where it addresses the stated reason. A discount offered to someone leaving
because a feature is missing confirms you were not listening. Pause is often the better offer and is
rarely available.

## At-risk detection

Build a simple signal from declining usage, a support escalation, a champion going quiet, or a seat
count dropping. Then act on it while intervention is still possible — a health score nobody works is
a dashboard, not a program.

## Never

- Count a saved cancellation as retained without checking whether they stayed a quarter later.
- Treat retention as a service problem when the data says it is a product or acquisition problem.
- Make cancellation require a phone call.
