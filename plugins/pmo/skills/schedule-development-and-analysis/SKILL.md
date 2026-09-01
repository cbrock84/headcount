---
name: schedule-development-and-analysis
description: Builds and interrogates a project schedule — logic-driven sequencing, dependency types and lags, float and the critical path, resource loading and leveling, schedule risk analysis, and measuring progress against a baseline rather than against optimism. Use this to construct a schedule, audit one you have inherited, find out why a plan keeps slipping, work out what a date change actually costs, or judge whether a reported percentage complete means anything.
---

# Schedule development and analysis

A schedule is a model of how work connects. Most schedules in circulation are a list of dates
someone typed, which looks the same in a status deck and behaves completely differently when
anything moves.

## Build it from logic, not from dates

Every task except the first and last should be connected to something. A task with a date and no
predecessor is an assertion; a task with a predecessor is a plan, because when the predecessor
moves the task moves with it and the schedule tells you so.

- **Finish-to-start** is the default and covers most real dependencies.
- **Start-to-start and finish-to-finish** describe overlapping work honestly and are worth using
  rather than faking the overlap with an earlier date.
- **Lags** should represent something real — curing time, a notice period, a review window. A lag
  used to make dates line up is a hidden assumption.

**Hard-coded date constraints are where schedules go to die.** Each one severs the logic at that
point, so slippage upstream stops propagating and the schedule keeps reporting a date it can no
longer support.

## Float is the information, and the critical path is the consequence

Float is how long a task can slip before it moves the end date. The critical path is the chain with
none. Attention belongs there and almost nowhere else — expediting work with three weeks of float
buys nothing and consumes the same management capacity.

Two readings worth taking regularly: **near-critical chains**, which become critical after one bad
week and are where surprises come from, and **negative float**, which means the schedule is already
telling you the date is impossible and someone has not looked.

## Load resources before you believe the dates

A schedule that assumes the same three people work on five parallel tasks is fiction that will
resolve itself as a delay. Load the named constraint — the one team, the one approver, the one
environment — and level it. Leveling extends the schedule; that extension was always there, it was
just unrecorded.

## Analyze schedule risk rather than adding a buffer at the end

Durations are ranges. Running the schedule with ranges rather than single durations shows something
a buffer cannot: paths that merge. Where several chains converge on one milestone, the milestone
waits for the latest of them, so the probability of hitting the date is far lower than the
probability of any single chain hitting its own — which is why plans with many parallel workstreams
slip even when no individual stream looks late.

A buffer at the end of the plan protects the end date. A buffer in front of each merge point
protects the plan.

## Measure progress against the baseline, not against effort

Keep a baseline and compare to it, or "we are 70% done" has nothing to be 70% of.

The useful comparison is three-way: what was planned to be complete by now, what is actually
complete, and what it cost to get there. Those three answer different questions — the first two
give you schedule performance, the last two give you cost performance, and a project can be ahead
on one and badly behind on the other.

**Percentage complete on in-progress work is where reporting rots.** A task reported at 90% for
three weeks is not 90% complete. Binary reporting — not started, in progress, done — with small
enough tasks that "done" arrives often is more honest and takes less time to maintain.

## Auditing a schedule you inherited

Look for these in order, because each one invalidates everything after it: tasks with no
predecessor or successor, hard date constraints, negative float, durations longer than a reporting
period, tasks that have been 90% complete for more than one period, and a baseline that has been
re-set so often it no longer means anything.

## Never

- Accept a date on a task with no logic behind it.
- Hard-code a constraint to make a date hold. It stops the schedule from telling you the truth.
- Report percentage complete on a task whose remaining work nobody has re-estimated.
- Re-baseline to make variance disappear. Re-baseline when scope genuinely changed, and say which.
