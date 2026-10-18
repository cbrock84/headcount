---
name: implementation-planning
description: Turns a spec or requirement into a written plan a separate session or agent can execute, then drives that plan through review checkpoints. Use this before touching code on any multi-step task, when work needs handing to someone else, when a task keeps sprawling mid-implementation, or when a plan exists and needs executing in order with verification between steps.
---

# Implementation planning

## When a plan is worth writing

More than about three steps, more than one file of consequence, or any work that will be handed off.
Below that, planning costs more than it saves.

## Writing the plan

A plan is executable when someone who was not in the conversation can follow it without guessing.
That means every step names:

- **The change** — the file or surface, and what it should do afterward.
- **The proof** — the command that shows it worked. "Run the tests" is not a step; the exact
  invocation is.
- **The checkpoint** — whether a human reviews before the next step starts.

Order steps so the system is working at the end of each one. A plan whose midpoint is a broken build
cannot be paused, and every plan gets paused.

State up front what is **out of scope**. Plans fail by accretion far more often than by being wrong.

## Executing

- One step at a time, in order. Finish and verify before starting the next.
- **Stop at checkpoints.** The point of a checkpoint is that continuing without it is a mistake.
- When reality contradicts the plan, stop and amend the plan. Do not improvise past it silently —
  the plan is the shared state, and a stale plan is worse than none.
- Track status *in* the plan as you go, so an interrupted run can resume.

## Never

- Start writing code because the plan felt obvious. If it was obvious, writing it costs a minute.
- Mark a step done without running its proof.
- Expand scope mid-execution. Note it, finish the plan, then decide.
