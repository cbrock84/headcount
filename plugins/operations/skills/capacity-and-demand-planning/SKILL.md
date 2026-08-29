---
name: capacity-and-demand-planning
description: Matches operational capacity to expected demand — forecasting load, sizing teams and systems, managing queues, and deciding when to add capacity. Use this to plan staffing for expected volume, diagnose a queue that keeps growing, size support or fulfilment capacity, or decide whether a bottleneck needs more capacity or better flow.
---

# Capacity and demand planning

This is operational throughput — how much work the organization can absorb. Allocating people
across projects is portfolio work, handled in `pmo:portfolio-governance`.

## Forecast demand honestly

Separate the three components, because they need different treatment:

- **Baseline** — the steady rate, best estimated from your own history rather than from a plan.
- **Trend** — the direction, measured over enough periods to distinguish it from noise.
- **Spikes** — launches, seasonality, campaigns, incidents. Known spikes are a planning input;
  unknown ones are what headroom is for.

Forecast in the unit the work actually arrives in — tickets, orders, shipments, minutes of handling
— not in revenue. Revenue divided by an average is a forecast of an average, and averages are where
capacity planning goes to die.

## Capacity is not headcount

Usable capacity is people multiplied by available hours multiplied by the fraction spent on the work
in question. The last term is the one everyone omits and it is rarely above 70%: meetings, training,
holiday, and the interruptions that come with the job are real.

Plan against realistic effective capacity. Planning at 100% guarantees the plan fails on its first
ordinary week.

## Queues tell you before the dashboard does

Utilisation above roughly 80% makes wait times rise sharply and non-linearly — a system at 95% is not
slightly slower than one at 85%, it is qualitatively worse. This is why "we have spare capacity on
paper" coexists with a queue that never clears.

Watch the **trend in queue age**, not the queue length. A stable-length queue whose oldest item keeps
getting older is a queue that is quietly failing its slowest customers.

## Add capacity or fix flow

Before adding capacity, establish which it is:

- **Genuine capacity shortfall** — arrival rate exceeds service rate at reasonable utilisation. Add
  capacity.
- **Flow problem** — rework, handoffs, waiting on another team, batching. Adding capacity here adds
  cost and often makes throughput worse by increasing coordination. Send this to
  `operations:process-design`.

The tell: if work spends most of its life waiting rather than being worked, it is a flow problem.

## Never

- Plan against nominal headcount rather than effective capacity.
- Run a critical queue at sustained high utilisation and treat the wait times as a mystery.
- Add capacity to a process you have not measured.
- Forecast in aggregate currency when work arrives in discrete units.
