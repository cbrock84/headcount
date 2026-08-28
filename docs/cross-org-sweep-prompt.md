# Cross-org sweep prompt

A Claude Code session can only attach repositories from **one owner**. A session rooted at
`cbrock84/agents-v1` cannot attach `Keel-GRC/*` or `Drummond-IT/*`, and a session rooted in
either of those cannot attach `agents-v1`. No single session sees both sides.

That restriction applies to **attaching** — which is what push access and the GitHub API need.
It does **not** apply to reading: the session's git proxy serves anonymous clones of any
**public** repo regardless of owner.

So the split is:

| Repos | How to reach them |
|---|---|
| Public `Keel-GRC/*` and `Drummond-IT/*` | Readable from the `agents-v1` session directly — no separate session needed |
| Private / internal `Keel-GRC/*` and `Drummond-IT/*` | Need a session rooted in that org, which then hands results back as a file |

Use the prompt below only for the second row.

---

## The prompt

Start a new Claude Code session with **`Keel-GRC/keelgrc-v1`** as its initial source (or
`Drummond-IT/Pace_API_v35_dev` for the Drummond sweep), then paste this:

---

Sweep this organization's **private and internal** repositories for Claude agent skills and
agent-definition material, and package what you find so it can be moved into another repo.

**Constraint, so you don't waste time on it:** this session is locked to this org's owner. You
cannot attach `cbrock84/agents-v1`, and you cannot push there. The deliverable is a file you
hand back, not a commit. Public repos in this org do not need you — they are readable from the
other session directly, so **skip anything public** and spend your budget on private/internal
repos only.

Do this in order:

1. **Enumerate.** Call `list_repos` and list every repo in this org whose visibility is
   `private` or `internal`. Report the list before doing anything else.

2. **Triage before cloning.** Cloning all of them is wasteful. Rank by likelihood of holding
   skills — names containing `skill`, `agent`, `claude`, `plugin`, `prompt`, `grc`, plus any
   repo you know to be a working knowledge base rather than an application. State your ranking
   and why, then clone the top candidates one at a time (`add_repo`, then a single
   `git clone --depth 1` inline with a ~10 minute timeout — parallel clones 429).

3. **Search each clone** for:
   - `SKILL.md` at any depth, and `.claude/skills/`, `skills/`, `agents/`, `.claude/agents/`
   - `.claude-plugin/plugin.json` or `marketplace.json`
   - `CLAUDE.md`, `AGENTS.md`, and any `*playbook*`, `*roster*`, `*charter*` markdown
   - loose system-prompt or persona markdown that is clearly an agent definition even without
     skill frontmatter

4. **For every hit, record:** repo, path, frontmatter `name` and `description` (watch for YAML
   block scalars — `description: >` puts the text on following indented lines), total size,
   whether it carries `scripts/` or large `references/`, and the repo's LICENSE.

5. **Flag anything that cannot leave this org.** These are private and internal business repos:
   customer names, credentials, internal hostnames, proprietary process detail, and
   client-identifying examples are all plausible. For each candidate skill say explicitly
   whether it is **portable** (generic method, safe to vendor into a personal repo) or
   **org-bound** (contains material specific to this business). Do not sanitize on your own
   judgment — flag it and let a human decide.

6. **Package the portable ones.** Build `sweep-export/` containing:
   - `manifest.json` — one entry per skill: `{name, description, source_repo, source_path,
     license, size_bytes, has_scripts, classification: "portable"|"org-bound", notes}`
   - `skills/<name>/` — verbatim copies of the portable skills, full directory including any
     `references/` and `scripts/`
   - `REPORT.md` — what you searched, what you found, what you classified as org-bound and why,
     and anything you could not reach

   Then `tar czf sweep-export.tar.gz sweep-export/` and send me both `REPORT.md` and the
   tarball with `SendUserFile`.

**Do not** commit the export to any repo in this org, and do not open a PR for it. Hand it back
as files.

---

## Bringing the results back

Attach the tarball (or paste `REPORT.md`) in the `agents-v1` session and say which departments
they should land in. Existing departments are `engineering`, `marketing`, `content`, `design`;
GRC material most likely wants a new `compliance` department, and Drummond print/prepress
material a `print-production` one.

Before anything lands, the receiving session should check each skill's frontmatter `name` is
lowercase-hyphenated and equal to its directory name, and that it does not collide with the 97
names already in this repo.
