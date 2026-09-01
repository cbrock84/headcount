---
name: ai-workflow-architect
description: Designs AI systems, automations, and agent workflows for a business — identifying which manual work is worth automating, how to structure the system, which tools fit, and what could go wrong. Use this to automate part of an operation, design an agent or MCP workflow, reduce repetitive manual work, connect tools into a system, decide which automation to build first, or audit an automation that is not delivering.
---

# AI workflow architect

Most automation fails on selection, not implementation. The wrong process automated well is worse
than the right process left manual, because now it is faster and harder to change.

## What is worth automating

Score each candidate on four dimensions and require a real answer to each:

- **Frequency** — how often, honestly measured. Weekly is usually the floor.
- **Time cost** — per occurrence, times frequency. Most "huge time sinks" are twenty minutes a week.
- **Error rate and cost of error** — where mistakes are expensive, automation pays even at low
  volume.
- **Stability** — how often the process itself changes. A process that changes monthly will break
  monthly.

Then apply the disqualifiers. Do not automate a process that:

- **Nobody has documented.** Automating an unexamined process encodes its accidents permanently.
- **Requires judgment you cannot specify.** If you cannot write the rule, the system will produce
  confident wrong answers rather than stopping.
- **Fails silently.** An automation whose failure is invisible is worse than no automation — the
  work stops happening and nobody notices for a month.
- **Should be eliminated instead.** The best automation is deleting the step. Ask this before
  designing anything.

## Designing the system

Start with the smallest loop that delivers value end to end, not the full vision. Systems that must
be complete before they are useful usually never become either.

- **Deterministic where you can, model-driven where you must.** Use a model for judgment and
  language; use ordinary code for routing, validation, and anything with a correct answer. Models
  are the expensive, non-deterministic part — spend them deliberately.
- **Put a human at the consequential step**, not at every step. Approval on an irreversible action;
  no approval on a draft.
- **Make failure loud.** Every automation needs a defined failure mode, a place the failure surfaces,
  and someone who sees it.
- **Idempotence matters more than it seems.** Reruns happen. A workflow that double-sends on retry
  will eventually double-send.

## Designing specialized assistants

Where a workflow needs judgment repeatedly, define a role rather than writing a prompt each time.
A role carries: what it is accountable for, the inputs it can rely on, the output shape it must
produce, what it must escalate rather than decide, and what it must never do.

Keep roles narrow. A single assistant asked to research, decide, and write produces mediocre
versions of all three; three narrow ones with defined handoffs produce work you can inspect at each
stage.

Pair any role that produces work with something that checks it — a rule, a test, or a separate
reviewing role. A role that reviews its own output approves it.

## Scoring candidates

Score each automation candidate on frequency, time cost, error cost, and stability from one to five,
then multiply rather than average — multiplication makes a low score on any dimension disqualifying,
which is the correct behavior. A daily task that changes weekly should not survive on frequency
alone.

Rank by score ÷ build effort, and take the top item only. Automation programs fail by starting
four things.

## Choosing tools

Match to the constraint that actually binds — volume, latency, existing stack, who maintains it, and
what happens when the vendor changes terms. Prefer the boring option; a workflow platform your team
already uses beats a better tool nobody will maintain.

Where an agent needs access to systems, prefer a defined tool interface over screen-driving. Tools
fail explicitly; scrapers fail silently and at the worst time.

## Sequencing

Build in this order: highest frequency × lowest complexity first. Early wins fund attention for
harder ones, and the first automation teaches you what the second should look like.

## Risks to state before building

Data leaving your control, model output reaching customers unreviewed, a silent dependency on a
vendor's pricing, and the maintenance burden landing on one person. Name the owner of each before
building, not after.

## Never

- Automate a process nobody has written down. You will automate the exceptions along with the work.
- Build before you know what a wrong output costs and who is positioned to catch it.
- Put a model where a rule would do. Deterministic steps should stay deterministic.
- Ship without a human review point on any step that spends money, sends mail, or deletes data.
