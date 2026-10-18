# Bootstrap prompt

Paste this into a fresh Claude Code session in the target repo. Fill the four bracketed
fields first; leave everything else alone.

---

Set up an orchestrator → specialist-subagent hierarchy in this repository, following
`references/playbook.md` (read it first, in full, before doing anything else).

**Context:**
- What this repo builds: **[e.g. a portfolio of iOS/Android/Amazon casual games]**
- Shared code it depends on or provides: **[e.g. packages/core, consumed by the apps portfolio too — or "none"]**
- What this codebase cannot afford to get wrong: **[e.g. store-policy compliance, IAP/receipt validation, save-file compatibility across versions]**
- Non-repo outputs: **[e.g. App Store / Play / Amazon submissions, store listing copy, ad creative]**

**Do these in order. Do not reorder them, and do not start writing agent charters early —
the order is the whole method.**

1. **Inventory the real trees.** Run `git ls-files | sed 's|/[^/]*$||' | sort -u` and read
   the actual directory structure. Report what you found before proposing anything.

2. **Propose a roster.** Smallest set of agents where no two share a file. For each:
   id, class (`builder` or `reviewer`), one-line remit, and **the exact globs it would
   own**. If you cannot state an agent's surface in globs, it is not an agent — fold it
   into a neighbor and say so. Pair every builder with a reviewer that did not write the
   thing. Number this proposal as a decision with lettered options and give me an explicit
   recommendation. **Stop here and wait for my answer.**

3. **Write `docs/AGENT-SURFACES.md`** in the playbook's format — a `roster` block plus one
   `surface:<id>` block per agent, every agent starting at `planned`. Assign **every**
   tracked path. No catch-all globs. Expect the exclusions to outnumber the inclusions;
   that is correct. Add the orchestrator's own surface for the context artifacts and the
   guard scripts themselves.

4. **Install `agent-guard.mjs`**, wire two scripts (`agents:check`, `agents:diff`), and
   iterate on the map until `check` passes. Paste the real passing output. **Do not write
   a single charter until this passes** — you now have a working control before any agent
   exists, which is the point.

5. **Wire the guard into CI** and into whatever pre-merge script this repo has. Show me the
   diff of the workflow file.

6. **Write the charters**, one per roster row, using the playbook's §12 format. Every
   builder charter must contain the words "You never commit, push, or open a PR" and the
   six-section return contract verbatim. Reviewers get `tools: Read, Grep, Glob, Bash` and
   no write tools. Flip each roster row `planned` → `installed` in the same commit as its
   charter; the guard checks both directions.

7. **Create `docs/DECISION-LOG.md`** with the numbering discipline from playbook §7.

8. **Write the orchestrator instructions** (`CLAUDE.md`): which agents exist, when to
   dispatch each, that builders never commit and the orchestrator is the sole committer,
   and that the live agent count comes from `agents:check` and is **never** written into
   prose.

9. **Prove it.** Dispatch one builder on a small real task, run `agents:diff <agent>` on
   its output before committing, and show me the result. If it fails, that is the system
   working — report the failure rather than fixing the map to accommodate it.

**Rules for you while doing this:**

- **Write the map before the charters.** Every path owned on paper before any agent exists
  to fight over it.
- **No claim without output.** When you say a check passes, paste the line it printed.
  "I could not verify X" and "X is clean" are different answers and must never be blurred.
- **Never write an agent count into prose** — not in `CLAUDE.md`, not in the map, not in a
  comment. Print it from the check.
- **A comment claiming a guard ships with the guard**, in the same edit. Never "next pass".
- Surface decisions to me as numbered items with lettered options and a bold
  recommendation. Never a bare question; never options with no recommendation.
- If the playbook and this repo's existing conventions conflict, say so and ask — do not
  silently pick one.

---

## Follow-up prompt: dispatching work afterwards

Once the hierarchy exists, use this shape for every task:

> Dispatch `<agent-id>` to `<task>`. It writes inside its own surface and does not commit.
> When it returns, run `agents:diff <agent-id>` before you commit anything, and show me the
> `VERIFIED` section of its report. If it touched a path outside its surface, that is a bug
> in the dispatch or the map — tell me which, do not just fix the file.

And for anything customer-visible or irreversible:

> Before this merges, run `<gauntlet-reviewer>` and `<domain-reviewer>` in parallel. If they
> disagree, give me both readings and name the agent behind each — do not pick one.
