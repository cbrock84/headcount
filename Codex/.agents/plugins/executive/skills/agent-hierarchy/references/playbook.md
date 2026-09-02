# Agent hierarchy playbook

**What this is.** A portable, domain-neutral method for standing up an orchestrator →
specialist-subagent hierarchy in a Claude Code session, with guardrails that execute.
Extracted from a working implementation: ~24 agents across a 1,500-file monorepo,
machine-checked on every PR.

**Read the failures, not the rules.** Every section below names the thing that went wrong
before the rule existed. A rule with no failure attached is one somebody will optimize away.

---

## 0. The one-paragraph version

Split agents by **write surface, not by topic**. Two classes only: **builders**, which edit
inside exactly one exclusive surface and never commit, and **reviewers**, which are
permanently read-only and can always run in parallel. The orchestrator — your main chat —
is the sole committer. Write the surface map **before** any charters, put it in one
Markdown file, and enforce it with a script that runs in CI. Producer and auditor are never
the same agent. For each class of fact, exactly one file owns it and everyone else derives.

Everything else is detail.

---

## 1. Split by write surface, not by topic

A topic split is the intuitive one and it fails immediately.

> "One agent on SEO, one on UI." Both end up in `tokens.css`. Neither is wrong. The
> collision is silent, and it surfaces as a merge conflict or — worse — as one agent
> quietly reverting the other's work while believing it holds the full picture.

Parallel agents on one repo collide in three ways: they **edit the same files**, they
**re-litigate settled decisions**, and they **each believe they hold the full picture**.
A surface map fixes the first. A decision log (§7) fixes the second. A source-of-truth
registry (§6) fixes the third. They are three different problems and one mechanism does
not solve all three.

**The organizing question is never "what is this agent good at". It is "what files may
this agent write".** If you cannot answer the second, the agent does not exist yet.

---

## 2. Two classes, and the orchestrator is not one of them

| Class | May write | May commit | Parallel-safe |
|---|---|---|---|
| **builder** | inside its own surface, only | **never** | only with non-overlapping surfaces |
| **reviewer** | nothing, permanently | never | **always** |
| **orchestrator** (your chat) | everywhere | yes — sole committer | n/a |

**"Builders never commit" is the control that actually holds.** Not the charter text, not
the surface map — those are checked, but a check can be argued with. A builder that
physically cannot commit cannot land anything the orchestrator did not read. Everything
else is defense in depth behind that.

**A reviewer's read-only status has to be structural, not promised.** Give it
`tools: Read, Grep, Glob, Bash` and no `Edit`/`Write`. A charter that says "I am read-only"
inside an agent that holds `Write` is a comment claiming a guard — see §9.

**Reviewers are permanent.** Do not make an agent that reviews *and* fixes. The moment it
can fix, its incentive is to report what it can fix, and the findings it cannot fix stop
being reported.

---

## 3. The map file

One Markdown file, two kinds of fenced block. Readable as documentation, parseable as
config, and there is only one of it — two files that could disagree is the failure you are
trying to prevent.

````markdown
```roster
# id                class      status     authority
core-owner          builder    installed  proposes
ios-builder         builder    installed  autonomous
store-compliance    reviewer   installed  autonomous
telemetry           reviewer   planned    autonomous
```

```surface:ios-builder
apps/ios/**
!apps/ios/project.yml
!apps/ios/**/*.entitlements
```

```surface:store-compliance
# read-only — no write surface
```
````

**Semantics.** One glob per line. Leading `!` excludes. **Later lines win over earlier
ones.** A path may be claimed by exactly one owner.

**The fourth roster column is authority**, and it answers the question the surface cannot:
not *where* the agent may write, but whether that write may land without a decision.

| Authority | Meaning |
|---|---|
| `autonomous` | Dispatch it and take the result. The surface is the only gate needed. |
| `proposes` | It may do the work; the orchestrator surfaces the diff before landing it. |
| `escalates` | Do not dispatch it unasked. The work itself is the decision. |

Most rows are `autonomous` and should be — gate everything and the gate stops meaning
anything. Reserve it for surfaces where the blast radius escapes the surface: the build and
release path, dependency manifests, anything the other agents' checks run through. In the
example above `core-owner` is gated because every consumer compiles against what it changes.

Omitting the column means `autonomous`, so existing maps keep working; `check` reports which
rows defaulted, because a map that never asked the question should be distinguishable from
one that answered it.

| Pattern | Matches |
|---|---|
| `**/` | any number of leading segments, including none |
| `dir/**` | `dir` itself and everything below it |
| `*` | any run of characters inside one segment, never crossing `/` |
| `?` | exactly one character inside one segment |

**Carve-outs are the load-bearing detail, not clutter.** Every `!` line is a collision a
naive tree split would have produced silently. Expect the map to be mostly exclusions once
it is honest. `apps/ios/**` and "every `project.yml`" both want
`apps/ios/project.yml`; only a written-down exclusion decides which gets it.

**No catch-all glob, anywhere.** A residual `docs/**` or `src/**` makes "every path has an
owner" unfalsifiable for exactly the directory where ownership is least obvious. Enumerate
instead. A new top-level file then *fails the guard until someone decides who owns it* —
that friction is the feature, not a bug to be smoothed.

**`git ls-files` cannot see a file you have not committed.** Add a path to a surface,
create the file, run the check locally, and it passes — because the file is untracked and
the sweep never reaches it. The overlap only appears in CI. **`git add` first, then run
the check.** This has bitten in production.

---

## 4. The guard is the entire point

Prose rules do not execute. The reference repo's top-level instructions said "framework
content must always be accurate" for **months** while a product surface shipped as
available with zero content behind it. Nothing failed, because nothing ran.

So: every claim in the map is checked against `git ls-files` on every PR.

`agent-guard.mjs check` asserts:

1. **No two surfaces overlap.**
2. **Every tracked file maps to exactly one owner.** Unowned means whoever touches it
   first becomes its de-facto owner, silently.
3. **Roster and charter files agree in both directions.** A charter with no roster row can
   write anywhere; a row still marked `planned` whose charter has landed is a lie about
   what is dispatchable.
4. **A reviewer declares no write surface.**
5. **Authority matches the surface the row holds.** A gated reviewer reads as governed while
   being the one row that never needed governing — it cannot write at all. A gated builder
   owning no surface has a checkpoint on an empty set. Both fail.
6. **Decision numbers are unique.** Two concurrent sessions both claiming `D14` merges
   cleanly in git and fails nothing — which is precisely why it needs a guard and not a
   convention. *(Tune this assertion's regex to your own log format; the shipped one
   matches `### D<number>` headings.)*

It also **reports patterns matching no tracked file** — a glob left behind by a rename
cannot sit silent. That is a note, not a failure: declaring a surface before the directory
exists is legitimate.

`agent-guard.mjs diff <agent>` answers the question the first one cannot: **did this diff
obey the map?** Run it before committing a builder's work. It fails on any changed path
outside that agent's surface, and **groups violations by who actually owns them**, because
that grouping is your handoff routing.

**The two are not redundant and you need both.** `check` proves the map is *coherent*. It
cannot prove a diff *respected* it — once the orchestrator commits, the information about
which agent authored which hunk is gone. Something has to check while authorship is still
known.

**Do not try to do path control with tool permissions.** Granting `Edit`/`Write` in
settings has no path scoping, and an allow-list would be a second, weaker copy of the map
that drifts from it. The frontmatter decides *whether* an agent can write; **the map
decides where, and `diff` enforces it.**

---

## 5. Producer and auditor are never the same agent

Pair every builder with a reviewer that did not write the thing.

| Producer | Audited by |
|---|---|
| whoever writes customer-facing copy | a claims/accuracy reviewer |
| whoever owns the data layer or dependencies | a security reviewer |
| whoever ships product code | a pre-merge gauntlet reviewer, a production-health reviewer |
| every builder, before merge | the gauntlet |

**A single reviewer's finding is a finding. The same finding from two independent
reviewers is the recommendation.** When reviewers genuinely split, surface both readings
and name the agent behind each — do not silently pick one and present it as settled.

Note the useful inversion: a support ticket alone is a *report*; a support ticket plus a
correlated error-monitoring issue is a **confirmed bug**. Pairing agents in the other
direction buys you evidence, not just review.

---

## 6. The source-of-truth registry

"Every agent believes it has the full picture" is a **read** problem. Write surfaces do
nothing for it.

So: **for each class of fact, exactly one file owns it and everyone else derives.**

| Fact | Owned by | Surface owner |
|---|---|---|
| e.g. pricing / tiers | `src/config/pricing.ts` | `config-owner` |
| e.g. color, type scale, spacing | `packages/ui/tokens.css` | `design-system` |
| e.g. shipped vs planned | `src/changelog.ts` | `content-owner` |

**Never hardcode a value that could drift — derive it from the owning file.** The
right-hand column is the practical consequence: *reading* any of these is free, but
*changing* one is a handoff to the agent named there.

---

## 7. The decision log, and why numbers are addresses

Keep `docs/DECISION-LOG.md`. One heading per decision, numbered, never reused.

**A number is the address of a question, so it is assigned when the question is asked, not
when it is answered.** This matters in chat as much as in the file: an ad-hoc `1. 2. 3.`
list restarts every message, so the same digit means a different question three replies
later. The human answers `1a` against the list they are reading and you resolve it against
the list you last wrote. That produces exactly one mismapped answer before you stop doing it.

Every decision carries **lettered options and an explicit recommendation**. Never a bare
question, never options with no recommendation, never a recommendation with no
alternatives.

---

## 8. What is not a path

The write-surface model assumes every output is a repo file. Some are not, and each class
needs different handling.

| Class | Examples | Rule |
|---|---|---|
| **1 — Repo files** | everything in the map | Ordinary write surface. |
| **2 — App-mediated content** | anything authored in an admin UI and stored in a DB | Agents draft to a staging directory. **Never** a direct DB write. A human publishes. |
| **3 — External platforms** | app-store submission, `npm publish`, storefront metadata, ad campaigns, customer replies, social posts | Agents **stage and version**. The human performs the act. |

**No agent publishes.** It matters most where the failure modes hurt worst: a wrong number
in a draft is recoverable; the same number in a submitted store listing or a sent campaign
is not.

For an app/game portfolio this is the rule that saves you — **store submission, signing,
and release notes are class 3.** An agent prepares the build and writes the release notes;
it never submits.

---

## 9. Anti-patterns, each with its failure

- **A comment that claims a guard, shipped without the guard.** If a docblock says a value
  is "pinned", "verified", or "asserted by" some test, that assertion lands in the *same
  edit* as the sentence. A comment claiming a guard exists is why nobody goes looking for
  the guard — it makes an unprotected value read as protected, which is **worse than no
  comment**.
- **Counting agents in prose.** Any hardcoded roster count is wrong the week after it is
  typed. Print the live figure from the check. This has gone stale three separate times in
  the reference repo, including inside the file whose job was to be authoritative.
- **A topic-named agent with no surface.** "performance agent", "quality agent" — these
  cannot be given an exclusive write surface, which means they cannot be checked, which
  means they are a prompt, not an agent.
- **Letting a builder commit "just this once."** The one control that holds, gone.
- **A reviewer that also fixes.** See §2.
- **Writing charters before the map.** You will discover the collisions one at a time, in
  production, as conflicts. Writing the map first means the argument about who owns what
  is had exactly once — the reference repo wrote 19 charters in a single day only because
  every path was already owned on paper.
- **Splitting a test from the code it tests.** Forces a handoff on every change. Put them
  in the same surface, with a named exception where a test genuinely belongs to another
  agent's module.
- **Separating a generator from its output.** A generator belongs with what it writes, or
  the output's owner cannot regenerate it.

---

## 10. Sizing

Start with **the smallest roster where no two agents share a file**, not with a target
number. Add an agent when you can state its exclusive surface in globs; if you cannot, the
work belongs to an existing agent.

A useful shape at any size:

- **2–5 builders** covering the real code trees
- **2–3 reviewers**: one gauntlet (build/test/lint truth-teller), one security/dependency,
  one domain-correctness reviewer for whatever your product cannot afford to get wrong
- **1 orchestrator** — you

Grow the builder side as trees genuinely diverge. Grow the reviewer side when a class of
mistake has escaped twice.

---

## 11. Multi-repo and shared core

This is the case that breaks naive setups, and it is worth getting right up front.

**A guard sweeps one repository.** It cannot see the other chat, the other repo, or the
other portfolio. So a shared core edited by two sessions has *no mechanism at all* keeping
them apart — the map is silent by construction.

Two workable shapes:

**(A) Contract owner — one agent owns both sides.** Designate a single `core-owner` agent
that is the *only* agent permitted to change the shared core or its consumers' bindings to
it, and require both sides to move as **one coordinated pair of PRs**. No other agent
touches either side. This is what the reference repo does for three published contracts
(a REST API, a file-bundle format, a generated dataset), each consumed by a different
external repo.

**(B) Publish and consume.** The shared core is its own repo/package with its own version.
The app portfolio and the game portfolio consume a **pinned published version** and never
edit it in place. Changing the core is a separate, deliberate piece of work with its own
release.

**Recommendation for a two-chat apps + games portfolio: (B), with (A) inside the core
repo.** Reason: (A) alone assumes one session at a time, and you have explicitly said two
chats. A pinned version is the only thing that makes "two sessions, one core" safe without
a cross-repo guard that does not exist. (A) then governs how the core repo itself changes.

Whichever you pick, **write the contract table into the map** so it is visible:

```markdown
| Contract | Core side | Consumer |
|---|---|---|
| Save-file format | `packages/core/src/save/**` | both portfolios |
| Analytics event schema | `packages/core/src/events/**` | both portfolios |
```

**Never remove a shared-core export because it looks unused.** You cannot see the consumers
from inside the core. Deprecate, announce, then remove.

---

## 12. Charter format

One file per agent at `.claude/agents/<id>.md`.

```markdown
---
name: ios-builder
description: One sentence on what it owns, one on what it explicitly does NOT own
  (naming the agent that does), and the sentence "Writes inside its own surface and
  never commits."
tools: Read, Grep, Glob, Bash, Edit, Write
---

You own <surface>, in one sentence.

**You never commit, push, or open a PR.** You edit and report a diff; the orchestrator
commits.

## Why this agent exists at all
The collision or failure that made it necessary. Without this, someone folds it back
into a neighbor in three months.

## What you must never do
The specific traps. Name them concretely — "never hand-edit generated output, change
the generator" beats "be careful with generated files".

## Verification your surface implies
The exact commands, and the requirement to paste real output.

## Return contract — end every report with these six sections
```

**The return contract is the highest-leverage 6 lines in the whole system.** Require it
verbatim in every charter:

```
SCOPE         What I was asked to do, and what I actually did. Name anything I skipped.
CHANGED       Every path I edited, plus the agents:diff output. Outside my surface is a BUG.
VERIFIED      Command → the actual output line it printed. No claim without a line.
NOT VERIFIED  What I could not check, and why.
HANDOFFS      Work found outside my remit, naming the path and the owning agent.
DECISIONS     Proposed decision-log entries, or blockers that need a human.
```

`VERIFIED` is the one that changes behavior most: **no claim without a line of real
output.** It converts "tests pass" into a pasted line, and it makes "I could not look" and
"I looked and it was clean" into visibly different answers — which is the distinction that
most often gets blurred.

`HANDOFFS` is what makes the whole thing composable: an agent that finds work outside its
surface does not do it and does not drop it. It routes it.

---

## 13. Scaffold procedure

Do these in order. The order is the point.

1. **Inventory.** `git ls-files | sed 's|/[^/]*$||' | sort -u` — look at the real trees,
   not the intended ones.
2. **Draft the surface map first, with no agents.** Assign every tracked path. Expect this
   to be the longest step and to surface real ownership questions.
3. **Install the guard** and run `check`. Iterate on the map until it passes. **You now
   have a working control before a single agent exists.**
4. **Wire it into CI** and into your pre-merge script. A guard that only runs when
   remembered is a guard that stops running.
5. **Write the charters**, one per roster row, using §12. Flip `planned` → `installed` as
   each lands — the guard enforces both directions.
6. **Add the decision log** with the numbering discipline from §7.
7. **Write the orchestrator's own instructions file** (`CLAUDE.md` / `AGENTS.md`): which
   agents exist, when to dispatch each, that builders never commit, and that the live
   agent count comes from the check and is never written in prose.
8. **Dispatch one builder on a real task** and run `diff` on its output before committing.
   Expect it to fail the first time. That failure is the system working.

---

## 14. Day-one checklist

- [ ] Every tracked path has exactly one owner; `check` passes
- [ ] No catch-all glob anywhere in the map
- [ ] Guard runs in CI, not just locally
- [ ] Reviewers hold no `Edit`/`Write` in frontmatter
- [ ] Every builder charter contains "never commit" and the six-section return contract
- [ ] Producer/auditor pairs written down
- [ ] Source-of-truth registry filled in for every fact that could drift
- [ ] Class-2 and class-3 outputs identified, with "no agent publishes" stated
- [ ] Shared core: contract table written, and (A) or (B) from §11 chosen deliberately
- [ ] No agent count written in prose anywhere
