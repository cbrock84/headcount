---
name: service-desk
description: Runs the IT service desk — intake, triage, prioritization, escalation, knowledge, and the metrics that improve service rather than distort it. Use this to set up or fix a service desk, design ticket priority and escalation, reduce repeat contacts, structure a knowledge base, or work out why a desk hitting its targets still frustrates everyone.
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

Escalation should be time-based and automatic. Relying on someone to notice a ticket aging means the
tickets that age are the ones nobody is watching.

## Measure service, not activity

Tickets closed measures activity, and optimizing it produces premature closure and reopened tickets.
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

## Tiers are a design decision, not a headcount ladder

Most desks describe themselves in tiers without having decided what defines one. The useful
definition is not seniority — it is **what a tier is permitted to resolve without escalating**.
Tier 1 owns the known and the documented. Tier 2 owns diagnosis: problems with no article yet.
Tier 3 owns the systems themselves, and is the same people who build them.

Two failure modes, and they look opposite while sharing a cause:

- **Tiers drawn too high.** Tier 1 escalates anything unfamiliar, so it becomes a routing desk and
  the expensive people handle password resets. The tell is a high escalation rate on tickets that
  close with a documented fix.
- **Tiers drawn too low.** Tier 1 is expected to resolve things it has no access or training for,
  so it improvises, and the improvisations become the estate's undocumented configuration. The tell
  is repeat contacts on the same asset and fixes nobody can explain later.

Draw the boundary at access, not difficulty. A tier that cannot be granted the permission to fix a
class of problem should not be the tier that owns it, and granting the permission anyway to avoid
an escalation is how the least-experienced people end up with the most rights — see
`it-operations:identity-lifecycle-administration`.

Write the escalation criteria down as conditions rather than judgment: elapsed time, blast radius,
or a named system. "Escalate when you are stuck" produces wildly different behavior between two
people on the same shift, and the quieter one escalates later.

Each tier needs its own definition of done. Tier 1 closing a ticket by handing it upward has not
resolved anything, and counting that as a resolution is how a desk reports success while the
backlog grows one layer up.

## Never

- Run parallel unofficial intake channels and treat the ticket queue as the workload.
- Merge incidents and requests into one queue.
- Target individuals on ticket volume.
- Close a recurring issue repeatedly without escalating it as a problem to eliminate.
