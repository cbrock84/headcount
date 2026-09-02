# Getting started

This is a library of expertise, packaged as sixteen independently installable departments for
[Claude Code](https://claude.com/claude-code). You install the ones you need, and the relevant
specialist loads itself when you ask something in its territory.

Nothing here changes your project. Installing a department adds skills to Claude Code — it does not
write to your repository, add dependencies, or run anything on its own.

## Install

Add the marketplace once:

```
/plugin marketplace add cbrock84/headcount
```

Then install departments one at a time:

```
/plugin install it-operations@headcount
/plugin install security@headcount
```

`/plugin` on its own opens the plugin menu, where installed plugins can be reviewed and managed.

**Install what you will use, not everything.** Sixteen departments is a lot of surface, and a
smaller set produces sharper triggering. You can add more at any point.

## Which departments to install first

Start from what you actually spend your week on rather than from the org chart.

| If you… | Start with |
|---|---|
| Run IT or infrastructure for a company | `it-operations`, `security`, `operations` |
| Run a small company or a whole function | `executive`, `finance`, `operations` |
| Own revenue or go-to-market | `revenue`, `marketing`, `demand-generation` |
| Build product | `product`, `technology`, `data-analytics` |
| Run delivery or a PMO | `pmo`, `operations` |
| Own people or hiring | `people`, `legal-risk` |
| Have customers to keep | `customer-experience`, `revenue` |

**Add `security` and `legal-risk` early regardless of what else you install.** They are the two
that tell you something you did not want to hear, which is the whole reason to have them.

## Three ways to use it

**1. Just ask.** Skills load themselves when a request matches. This is the normal path and the one
to reach for first.

> *"Our margins slipped this quarter and nobody can tell me why."*

**2. Name the skill** when you want a specific lens rather than the one that would trigger:

```
/finance:cost-accounting
```

Skills are addressed as `department:skill`, so names never collide across departments.

**3. Delegate a whole department.** Each department ships an agent charter in `.claude/agents/`,
so it can be handed a body of work as a subagent with its own exclusive write surface. See
`executive:agent-hierarchy` for the method, and why the split is by write surface rather than by
topic.

## What to expect back

A skill is not a template that fills itself in. Most will start by asking you the two or three
things that decide the answer — what the unit is, what the comparison is, who owns the consequence —
because those are the questions that get skipped and are the reason the usual answer is wrong.

Expect to be told what the library cannot determine. A skill that names its limits is doing the job;
one that answers everything confidently is the failure mode this catalog is built against.

## Reviewer-class departments behave differently

`security` and `legal-risk` review what other departments commit to. They hold no write surface,
they report to the chief executive rather than into the function they review, and **their blocking
findings are not overrulable by the department under review.**

In practice: when you ask a revenue question and the security review says the access model cannot
support the control the deal requires, that is not a trade-off to price against the deal. The date
moves or the control gets built. This is deliberate, and it is why those two are worth installing
even when they are not your job.

## What this is not

Several skills carry an explicit disclaimer, and it is not boilerplate. Employment classification,
tax, financing terms, contract positions, privacy obligations and regulatory filings are matters
where the facts and the jurisdiction decide the answer. These skills structure the question and
tell you what to ask — they are not a substitute for qualified counsel, and they say so.

## Seeing what is in it

The [live org chart](https://cbrock84.github.io/headcount/org-chart.html) is searchable across every
skill in every department, generated from the repository so it cannot drift from what actually
ships.

[Worked situations](USE-CASES.md) show what happens when a problem crosses departments — what
engages, in what order, what comes back, and where the library has nothing useful to say.

## Getting help

Questions, gaps and disagreements belong in
[Discussions](https://github.com/cbrock84/headcount/discussions). A situation the catalog handles
badly is the most useful thing you can report, more than a missing skill — the gap is usually that
a skill exists and fails to trigger, or triggers and answers the wrong question.
