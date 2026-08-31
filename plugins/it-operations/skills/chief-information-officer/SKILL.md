---
name: chief-information-officer
description: The CIO's remit — running the technology the company works on, service quality, IT spend, and the boundary with product engineering. Use this to set IT priorities, decide what IT owns versus engineering, structure IT spend or an IT roadmap, judge whether to build, buy or outsource, or work out why IT is seen as a cost center rather than an enabler.
---

# Chief Information Officer

The CIO runs the technology the company works *on*. The CTO runs the technology the company
*sells*. Confusing the two is why IT ends up owning a product roadmap it cannot resource, or why
engineering ends up running a help desk badly.

## What this department owns

The systems every employee depends on and nobody markets: identity, endpoints, network, corporate
applications, the service desk, and the backup and restore path. Its output is measured in
availability, time-to-resolution, and how little anyone has to think about it.

- `it-operations:service-desk` — the front door, and the honest measure of whether any of this works
- `it-operations:systems-administration` and `it-operations:network-administration` — the estate
- `it-operations:endpoint-management` — the most exposed surface, because it leaves the building
- `it-operations:identity-lifecycle-administration` — execution of joiner-mover-leaver
- `it-operations:it-asset-management` — what you have, who has it, what it costs
- `it-operations:backup-and-recovery` — the restore, tested rather than assumed
- `it-operations:virtualization-operations` — the hypervisor layer the servers actually run on
- `it-operations:cloud-administration` — the corporate cloud and SaaS estate, distinct from the product's
- `it-operations:telephony-and-conferencing` — voice, rooms, and the obligations they carry

## The boundaries that cause arguments

State them once, in writing, and the recurring turf disputes stop:

- **Security sets policy; IT executes it.** `security:access-and-identity` decides what a role should
  be entitled to; this department provisions it. `security:vulnerability-management` decides what is
  urgent; `it-operations:systems-administration` runs the cadence.
- **Engineering owns the product estate; IT owns the corporate estate.**
  `technology:cloud-infrastructure` designs the environment the product runs in. Where a corporate
  system runs in the same cloud, ownership follows who the users are, not where it is hosted.
- **Continuity objectives are the business's; the restore is IT's.**
  `operations:business-continuity-and-resilience` sets RTO and RPO with the process owners; this
  department has to deliver against them and should say plainly when it cannot.

## Build, buy, or outsource

Default to buy for anything that is not a differentiator. Building an internal tool that a mature
product already solves is a decision to maintain it forever, staffed by people who would rather be
doing something else.

Outsource where the work is commoditized and the failure is recoverable — first-line support out of
hours, hardware logistics. Keep in-house what needs institutional context or carries irreversible
risk: identity, data, and anything where a bad decision is discovered a year later.

## The recovery you have never tested is a plan, not a capability

Backups that have never been restored, failovers never exercised, and runbooks never followed under
pressure are all assertions. The characteristic discovery during a real incident is that one of them
was wrong in a way nobody could have known without trying.

Test on a schedule, with the person who would actually do it rather than the one who designed it,
and time the restore — recovery time is the number the business will ask for, and the only honest
answer comes from having done it. The same logic applies to the communication plan: its first real
exercise should not be its first real incident.

## Spend, and the cost-center trap

Attribute IT cost to the functions consuming it rather than reporting one aggregate. An
undifferentiated IT budget invites across-the-board cuts, because nobody can see what any of it buys.

The trap is real: a department judged only on cost is asked only to be cheaper, and the first
casualties are refresh cycles and patching, which surface as incidents two years later with no
visible cause. Report service outcomes alongside cost, and be specific about what a proposed cut
removes.

Track the split between running the estate and changing it, and defend it as a target rather than
letting it be the residue after everything else. An estate consuming everything on keeping the
lights on has no capacity to improve, and next year it will consume more — the ratio decays on its
own unless someone holds it.

## Never

- Accept a continuity objective you have not demonstrated you can meet.
- Let identity policy and identity execution sit with the same reviewer.
- Build an internal tool for a solved commodity problem.
- Report IT cost without reporting what it delivered.
- Count an untested restore as a recovery capability.
