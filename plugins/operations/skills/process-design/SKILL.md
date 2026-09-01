---
name: process-design
description: Designs, documents, and fixes operational processes — mapping the current state, finding where work actually stalls, redesigning the flow, and building controls that hold. Use this when the same failure keeps recurring, when a handoff between teams is unreliable, when onboarding a repeated task, when work takes far longer than the work itself, or when deciding whether to automate, standardize, or eliminate a process.
---

# Process design

## Map what happens, not what is supposed to happen

Follow a real instance end to end and record every step, handoff, wait, and rework loop. Talk to the
people doing it, who will describe several steps that exist nowhere in the documentation and one or
two that everyone has quietly stopped doing.

Then measure two things:

- **Touch time** — how long the work actually takes.
- **Elapsed time** — how long it takes to get through.

The gap between them is the process. In most broken processes, work is waiting more than ninety
percent of the time, which means speeding up the work changes almost nothing. Attack the waits.

## Find the real constraint

One step governs throughput. Improving anything else produces inventory in front of the constraint
and no more output. Find it: the step with a queue in front of it.

Common constraints that are not the obvious step: a single approver, a specialist everything routes
through, a system that only one team can access, and a batch cycle that makes everything wait for
the weekly run.

## Redesign

In this order, because the order is the leverage:

1. **Eliminate.** Does this step need to exist? Many exist to catch a failure that a different fix
   would prevent entirely.
2. **Simplify.** Fewer handoffs, fewer approvals, fewer systems. Every handoff is a place work
   stops.
3. **Standardize.** One way of doing it, written down, with the decision rules explicit.
4. **Automate.** Last. Automating an unexamined process makes a bad process faster and much harder
   to change.

Push approval to the lowest level that can be accountable, and set thresholds so routine cases do
not queue behind exceptional ones.

## Make it hold

A documented process that relies on discipline degrades within a quarter. Build the control into the
system: required fields, blocking gates, defaults that are correct, automated handoffs.

**Never fix a recurring failure with a reminder.** If people are forgetting a step, the system
permits forgetting it. Fix that.

## Never

- Redesign from the documented process. Map what people actually do first.
- Optimize a step that is not the constraint. Everything you speed up ahead of it just queues.
- Add an approval to prevent a failure that happened once.
- Hand over a process with no owner and no measure. It reverts within a quarter.

## Return contract

Current state with elapsed and touch time, the constraint and its evidence, the redesign, what it
costs to implement, and the measure that will show it worked.
