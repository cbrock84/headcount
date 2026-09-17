---
name: parallel-agent-delivery
description: Splits work across multiple agents or sessions running at once, keeping their surfaces disjoint so results merge cleanly. Use this when facing several independent tasks with no shared state, when a plan has parallelizable steps, when a broad search or audit would be faster fanned out, or when deciding whether work can safely be split at all.
---

# Parallel agent delivery

Parallelism is a property of the work, not a preference. Establish it before dispatching.

## When it is safe

All three must hold:

1. **Disjoint write surfaces** — no two agents touch the same file. Not "unlikely to conflict";
   provably disjoint.
2. **No sequential dependency** — none needs another's output to start.
3. **Independently verifiable** — each result can be judged on its own.

Fail any one and run sequentially. Two agents editing one file produces a merge conflict at best and
a silent lost update at worst.

## Dispatching

Each agent gets a self-contained brief: the goal, its exclusive surface, the context it cannot see
for itself, and the shape of the answer expected. Agents share no memory — anything you leave out is
gone.

Ask for a **structured return**, the same shape from each, so results can be compared rather than
re-read.

## Read-only fan-out is the easy case

Searching, auditing, and reviewing have no write surface at all, so they parallelize without risk.
Reach for parallelism here first and freely.

## Integrating

- Review each result against its brief before merging any of them.
- Where two disagree on a shared fact, neither is authoritative — resolve it yourself.
- One agent returning nothing useful is a normal outcome, not a failure to retry blindly.

## Never

- Split work to look faster when the steps are actually sequential.
- Let two agents write to one surface because "they probably won't collide."
- Merge a result you have not read.
