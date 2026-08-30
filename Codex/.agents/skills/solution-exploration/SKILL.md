---
name: solution-exploration
description: Explores the problem and the range of possible approaches before any code is written — clarifying what is actually being asked, surfacing options with their tradeoffs, and converging on one. Use this at the start of any feature, component, or behavior change, when a request is ambiguous, when the first idea is the only idea on the table, or when a design decision needs pressure-testing before commitment.
---

# Solution exploration

The most expensive bugs are decisions, not defects. This runs before implementation, not instead of
it.

## Establish what is actually wanted

The stated request is a proposed solution wearing the clothes of a requirement. Get underneath it:

- What outcome does the person want? What breaks today without it?
- Who else touches this, and what do they assume about it now?
- What is explicitly **not** being asked for?
- How will we know it worked — the observable difference.

If the answers conflict, stop and resolve that first. Building the average of two requirements
satisfies neither.

## Generate genuinely different options

Two variations of the same idea are one option. Force real range:

- The smallest thing that could work.
- The version that assumes this doubles in scope next quarter.
- The version that requires no new moving parts.
- Buy, borrow, or do nothing.

For each: what it costs, what it forecloses, and what has to be true for it to be right.

## Converge

Recommend one and say why the others lost. A comparison that ends without a recommendation has
moved the work, not done it.

Name the assumption the recommendation rests on most heavily — that is where the plan will break if
it breaks.

## Never

- Present options you would not accept as padding around the one you want.
- Skip this because the task "is simple." Simple tasks take five minutes here.
- Let a preference stand in for a reason.
