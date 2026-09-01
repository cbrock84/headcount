---
name: agent-hierarchy
description: Designs orchestrator-and-subagent hierarchies for a repository — splitting agents by exclusive write surface, pairing every producer with an independent auditor, and enforcing the split with a script that runs in CI. Use this whenever the user wants to set up, expand, audit, or fix a multi-agent or subagent structure for a codebase; asks how to divide work between agents; wants agent charters, roles, or a surface map written; or is hitting agents that collide on the same files, review their own work, or drift from their remit. Also use when sizing a roster or deciding whether a new agent is justified.
---

# Agent hierarchy

A method for standing up an orchestrator → specialist-subagent hierarchy, extracted from a
working implementation of ~24 agents over a 1,500-file monorepo, machine-checked on every PR.

## The whole method in one paragraph

Split agents by **write surface, not by topic**. Two classes only: **builders**, which edit
inside exactly one exclusive surface and never commit, and **reviewers**, which are permanently
read-only and can always run in parallel. The orchestrator — the main chat — is the sole
committer. Write the surface map **before** any charters, keep it in one Markdown file, and
enforce it with a script that runs in CI. Each row also carries an **authority** — `autonomous`,
`proposes`, or `escalates` — which answers the separate question of whether that agent's work may
land without a decision; most rows are `autonomous`, and gating everything makes the gate
meaningless. Producer and auditor are never the same agent. For
each class of fact, exactly one file owns it and everyone else derives.

## Why topic splits fail

"One agent on SEO, one on UI" is the intuitive split and it breaks immediately: both end up
editing `tokens.css`. Neither is wrong, and neither can be held responsible. A surface split
has no such overlap by construction — which is exactly what makes it checkable.

## Order of operations

Do not start writing charters early; the order is the method.

1. **Inventory the real tree** — `git ls-files | sed 's|/[^/]*$||' | sort -u`. Report what is
   actually there before proposing anything.
2. **Propose the roster** — the smallest set where no two agents share a file. Each needs an
   id, a class, a one-line remit, and its exact globs. An agent whose surface cannot be stated
   in globs is not an agent; fold it in.
3. **Write the surface map** — one Markdown file, one row per agent.
4. **Wire the guard** — `scripts/agent-guard.mjs check` proves the map is coherent (no path
   claimed twice, no path unowned); `agent-guard.mjs diff <agent>` proves a given diff obeyed
   it. Both are needed: once the orchestrator commits, the authorship that `diff` checks is
   gone, so it has to run while the work is still attributable.
5. **Write charters last**, in the format in the playbook: why the agent exists, what it must
   never do, the verification its surface implies, and a six-section return contract.

## Rules that carry a failure behind them

- **Producer and auditor are never the same agent.** An agent that reviews its own output
  reliably approves it.
- **The orchestrator is not one of the two classes.** It is the sole committer, and giving it
  a surface makes it a builder that can also merge.
- **One file owns each class of fact.** Everything else derives from it, or the two copies
  diverge and nobody notices which is stale.
- **Never remove a shared-core export because it looks unused.** You cannot see the consumers
  from inside the core. Deprecate, announce, then remove.

## This repository's own log

`docs/DECISION-LOG.md` is the live instance of the decision log described in the playbook. When a
decision is raised, assign it the next number immediately — before it is answered — and give it
lettered options with an explicit recommendation. Never renumber, never reuse a number, and record
resolutions in place rather than deleting them.

## Never

- Add an agent before the surface it will own exists. The map comes first, the agent second.
- Let two agents hold a write claim on the same path. Overlap resolves itself as a race.
- Hand-edit a generated artifact instead of the source it derives from.
- Skip the guard because the change is small. Small changes are how surfaces drift.

## References

- `references/playbook.md` — the full 415-line playbook: surface splitting, the guard, the
  registry, the decision log, anti-patterns with their failure modes, sizing, multi-repo and
  shared-core layouts, the charter format, and a day-one checklist.
- `references/starter-rosters.md` — concrete rosters for a mobile-app portfolio, a game
  portfolio, and a shared core, with producer/auditor pairings.
- `references/bootstrap-prompt.md` — a fill-in-the-blanks prompt for standing this up in a
  fresh session against a target repo.
- `scripts/agent-guard.mjs` — the executable guard. No dependencies, Node 18+.
