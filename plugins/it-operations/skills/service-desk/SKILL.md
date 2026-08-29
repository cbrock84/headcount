---
name: service-desk
description: Runs the IT service desk — intake, triage, prioritisation, escalation, knowledge, and the metrics that improve service rather than distort it. Use this to set up or fix a service desk, design ticket priority and escalation, reduce repeat contacts, structure a knowledge base, or work out why a desk hitting its targets still frustrates everyone.
---

# Service desk

The service desk is where the whole IT organization is judged, usually by people having a bad day.
Most of what makes it good is intake discipline and honest measurement.

## Intake determines everything downstream

Capture enough at first contact to route correctly and act without a second exchange: who, what
they were doing, what happened, what they expected, and how blocked they are.

Give the requester a single channel that works. Multiple half-supported channels — a queue, a chat, a
shoulder tap, a manager's direct message — mean the loudest request wins rather than the most urgent,
and the desk's workload becomes unmeasurable because most of it is invisible.

## Priority is impact against urgency

Priority is not a feeling. Define it on two axes — how many people are affected and how blocked they
are — and publish the matrix so it can be applied consistently rather than argued each time.

Keep **incidents** (something broken) separate from **requests** (something wanted). They have
different clocks, different queues, and different success conditions, and merging them lets routine
requests bury outages.

Escalation should be time-based and automatic. Relying on someone to notice a ticket ageing means the
tickets that age are the ones nobody is watching.

## Measure service, not activity

Tickets closed measures activity, and optimising it produces premature closure and reopened tickets.
Better:

- **First-contact resolution** — resolved without a handoff.
- **Time to resolution at the percentile users feel**, not the mean.
- **Reopen rate** — the direct check on premature closure.
- **Repeat contacts for the same underlying cause** — the number that points at problems worth
  eliminating.

Never target an individual on volume. It reliably produces cherry-picking of easy tickets and quiet
avoidance of hard ones.

## Eliminate demand rather than absorbing it

A desk that handles the same failure two hundred times has done two hundred units of work and solved
nothing. Cluster tickets by underlying cause and feed the top few into permanent fixes — a
configuration change, a fix at source, or self-service that genuinely resolves.

Knowledge articles should be written for the person with the problem, not the person who fixed it:
the symptom as experienced, then the steps. An article filed under the internal cause is not
findable by anyone who does not already know the answer.

## Never

- Run parallel unofficial intake channels and treat the ticket queue as the workload.
- Merge incidents and requests into one queue.
- Target individuals on ticket volume.
- Close a recurring issue repeatedly without escalating it as a problem to eliminate.
