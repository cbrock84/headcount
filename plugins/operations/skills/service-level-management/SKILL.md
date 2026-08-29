---
name: service-level-management
description: Defines and manages service levels — setting targets that reflect what customers need, measuring honestly, and handling breaches. Use this to write or negotiate an SLA, decide what to measure and at what threshold, respond to a missed service level, or work out why a service that meets its targets still has unhappy customers.
---

# Service level management

A service level is a promise with a number attached. The number is the easy part; choosing what to
measure is where these go wrong.

## Measure what the customer feels

The characteristic failure is a service meeting every target while customers are angry. It happens
when the measure is chosen for availability of data rather than relevance:

- **Uptime that excludes degraded operation.** Technically up and unusably slow is down.
- **Response time instead of resolution time.** An instant acknowledgement that resolves nothing
  measures the autoresponder.
- **Averages instead of percentiles.** A mean hides the tail, and the tail is who complains. Commit
  at p95 or p99, not the mean.
- **Measurement from inside your own perimeter**, which excludes the part of the path the customer
  actually traverses.

## Set targets you would fund

A target is a spending decision. Each added nine costs disproportionately more than the last, so the
question is never "what would be good?" but "what is the gap worth to the customer, and does it
exceed what closing it costs?"

Set the internal objective tighter than the external commitment. The gap between them is your
warning margin; without it, the first thing you learn about a breach is the breach.

## Write them so both sides can tell

An unmeasurable clause is a future dispute. Every service level needs: what is measured, where it is
measured from, how it is calculated, what is excluded, over what window, and what happens when it is
missed.

Exclusions are the substance — planned maintenance, force majeure, customer-caused failures,
dependencies outside your control. Vague exclusions get read narrowly when it matters. For anything
with contractual teeth, `legal-risk:contract-review` owns the remedy language; this skill owns
whether the number is achievable.

## When you breach

Say so before the customer does. A breach reported by the provider with a cause and a fix costs far
less trust than one the customer discovers and raises.

Then separate the incident from the pattern. One breach is an incident, handled by
`customer-experience:escalation-management`. Repeated breaches of the same target mean the target was
never fundable — renegotiate it honestly rather than continuing to miss it.

## Never

- Commit to a level you have not measured yourself achieving for a sustained period.
- Report availability on a mean when the customer experiences the tail.
- Agree an SLA whose exclusions are undefined.
- Let a target stand that you have missed repeatedly without either funding it or renegotiating it.
