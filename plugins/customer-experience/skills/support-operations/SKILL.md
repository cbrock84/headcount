---
name: support-operations
description: Designs and runs the support function — channels, queues, routing, staffing, service levels, quality, and the metrics that show whether it is working. Use this to set up or fix support operations, choose channels, size a team, set or renegotiate service levels, reduce cost per contact, diagnose long queues or poor quality, or decide what to automate.
---

# Support operations

## Understand demand before designing supply

Categorize a real sample of recent contacts — a few hundred, read individually, not a report. Almost
every support operation finds the same shape: a small number of causes generating most of the
volume, and most of those are preventable rather than answerable.

That analysis decides everything downstream. Staffing to demand you have not examined means staffing
to demand you could have eliminated.

## The hierarchy of handling

In order of cost, cheapest first. Push volume up this list rather than getting faster at the bottom:

1. **Eliminate** — fix the product defect or confusing flow generating the contact.
2. **Deflect** — answer it in the interface at the moment of confusion, not in a help center nobody
   visits.
3. **Self-serve** — findable documentation for people who go looking.
4. **Automate** — genuine resolution of routine requests, not a bot that stalls people before a
   human.
5. **Assist** — a person.

Most support improvement programs work on level 5 exclusively, because it is the visible one.

## Channels

Pick by what the work needs, not by what is fashionable. Asynchronous channels are cheaper and
better for anything requiring investigation. Synchronous channels are worth their cost for urgency,
high-value accounts, and anything where a customer is stuck mid-task.

Every channel you open must be staffed to its expectation. An unstaffed live-chat widget is worse
than no chat.

## Service levels

Set by severity and customer tier, published internally, and — this is the part usually missing —
**checked against actual capacity before being promised**. A commitment the staffing cannot meet is
a commitment to fail visibly.

Measure first response and time to resolution separately. They have different causes: first response
is a staffing problem, resolution is usually a product or escalation problem.

## Metrics that mean something

- **Contacts per active customer**, trending. The only metric that captures whether the product is
  getting better rather than the team getting faster.
- **First-contact resolution** — reopens are the honest signal.
- **Backlog age distribution**, not average age. Averages hide the tickets rotting at the back, and
  those are the ones that become complaints.
- **Customer-effort**, asked at resolution.

Be careful with time-to-close and volume handled. Both are easily gamed and both reward closing over
solving.

## Staffing

Size to peak-hour concurrency, not to daily volume — queues form in hours, not days. Model the
shrinkage honestly: training, breaks, meetings, leave. A plan assuming full utilization understaffs
by a wide margin and then blames the team.

## Quality

Review a sample of resolved contacts against a rubric agreed with the team, and coach against it.
Reviewing only escalations trains for defense rather than quality.

## Never

- Staff to average volume. Support arrives in peaks.
- Publish a service level you have not staffed to meet.
- Manage on handle time. It optimizes for closing tickets, not for solving problems.
- Let a repeat driver stay a support problem. Route it to whoever owns the cause.
