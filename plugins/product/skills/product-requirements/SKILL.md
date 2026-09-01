---
name: product-requirements
description: Writes down what is being built so a team can build it and know when they are done — problem and success measure before solution, scope stated by exclusion, user-visible behavior including the states everyone forgets, acceptance criteria someone can test, and the open questions named rather than buried. Use this to write a specification, review one that is causing rework, or work out why a delivered feature technically matched the request and still was not what anyone wanted.
---

# Product requirements

A specification exists to prevent expensive rediscovery — of decisions already made, of scope
already agreed, and of the edge cases that are found either now on a page or later in production.

## Lead with the problem and the number, not the solution

Open with who has the problem, what it costs them today, and what you expect to change if this
ships — expressed as a measure with a target and a date. A document that starts with a solution
invites the team to optimize the wrong thing and gives you no way to tell afterward whether it
worked.

**Decide the success measure before building, not at launch.** A number chosen afterward is chosen
to be met.

## State scope by exclusion

Everyone reads what is in scope and assumes the rest is coming. An explicit "not in this" list is
the cheapest thing in the document and prevents most scope arguments — including the ones that
arrive as clarifications rather than as requests.

Say what is deferred versus what is rejected. Those are different, and conflating them means the
rejected thing comes back.

## Describe behavior, not implementation

Write what the user experiences and what the system guarantees. Leave the how to the people who
will own it — a specification that dictates implementation gets a worse implementation and blurs
who is accountable for it.

**The states nobody writes down are where the rework comes from.** Empty, loading, error,
partial, permission-denied, offline, and the first-run case with no data. Also: what happens to
records that already exist, what happens at the limits, and what happens when two people do it at
once. Most "that wasn't what I meant" traces back to one of these.

## Make acceptance criteria testable

Each one should be a statement someone can evaluate as true or false without asking you. "Fast" and
"intuitive" are not criteria; a response-time budget and a task someone completes unaided are.

If a criterion cannot be tested, it is either a principle — say so and move it — or it is not
finished being thought about.

## Name the open questions and who owns them

Every specification has unknowns. Listing them, with an owner and a date needed by, is what
separates a document that is honestly incomplete from one that is quietly wrong. Buried
uncertainty gets resolved by whoever hits it first, usually at the least convenient moment and
without anyone noticing a decision was made.

## Keep it alive, or state that it is frozen

A specification that diverges from what was built becomes a trap for the next person. Either update
it as decisions change, or mark it as-of-a-date and point at wherever the truth now lives. The
worst outcome is a document that looks current and is not.

## Never

- Open with a solution and leave the problem implied.
- Ship a specification with no explicit out-of-scope list.
- Write an acceptance criterion that requires asking you whether it passed.
- Leave an unresolved question inside the body where it reads as a decision.
