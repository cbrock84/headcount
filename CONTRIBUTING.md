# Contributing

Contributions are welcome. This document covers the license, the bar for a skill, and the checks.

## License

**By submitting a contribution you agree it is licensed under the [MIT License](LICENSE), the same
terms as the rest of this repository.**

Contribute only work you have the right to license this way. In particular, do not paste in skills,
prose, or reference material from another project unless you wrote it or its license permits
relocation — and if it does, say so in the pull request. Every line in this repository is original
to it.

`scripts/check-provenance.py` is a backstop, not a proof. It scans every text file in the tree for
license headers, copyright notices, and SPDX identifiers, flags files named like licenses
(`LICENSE`, `COPYING`, `NOTICE`, `PATENTS`, `AUTHORS`), and rejects bundled font assets. It cannot
detect prose lifted without a notice attached — which is the case that matters most. Review is what
catches that; the check only catches the obvious.

## What makes a good skill

A skill is judged twice: whether it loads at the right moment, and whether it helps once loaded.

**The description does the triggering.** It is the only part read when deciding whether to load. Lead
with what the skill does, then when to reach for it — in the words someone would actually use,
including the oblique ones. Vague descriptions fail twice over: they miss cases they should catch
and fire on cases they cannot help.

**The body does the work.** Write for someone competent who has not thought about this problem
today:

- **Method over exhortation.** "Be thorough" is noise; an ordered procedure is instruction.
- **State the failure behind each rule.** A rule with no failure attached gets optimized away by the
  next reader.
- **Be specific enough to be wrong.** Guidance too hedged to contradict is too vague to follow.
- **Long material goes in `references/`**, with the body saying when to read it.

**Where a skill touches regulated ground** — law, privacy, compensation, medical, financial, or
safety advice — say plainly what it structures and what needs qualified professional input. Skills
that sound authoritative and are subtly wrong in these areas cause real harm, because they get
trusted.

Read `technology:skill-authoring` for the full treatment, and `executive:agent-hierarchy` for why
departments are split by exclusive write surface rather than by topic.

## Before opening a pull request

```
./scripts/check-all.sh
```

Every check CI runs, in one script — the workflow calls this same file, so the two cannot drift:

| Check | What it enforces |
|---|---|
| Surface map | Every tracked path has exactly one owner |
| Skill frontmatter | `name` equals the directory name, lowercase-hyphenated, unique, description substantial |
| Provenance | No license headers, copyright notices, license-named files, or font assets |
| Generated docs | README, social card and org chart match the tree |
| Skill references | Every `department:skill` mentioned in the docs or in a skill body resolves |
| US English spelling | No British spellings, by exact word form |
| `## Never` blocks | Bullets inside one block agree on terminal punctuation |
| Manifests | The marketplace file and every `plugin.json` parse |

**Stage your files first.** The surface guard reads `git ls-files`, so an unstaged file is invisible
to it — the check will pass and then fail once committed. The script warns when untracked files are
present.

## Adding a skill

1. `plugins/<department>/skills/<skill-name>/SKILL.md`
2. Frontmatter `name` must equal the directory name.
3. Check nothing already covers the ground. Two skills whose descriptions both match a request means
   neither reliably wins — prefer extending an existing skill, or folding a family into one skill
   with references, over adding a near-neighbour.

## House style

**US English.** The author writes in US English and the catalog does too — *license*, *program*,
*catalog*, *behavior*, *prioritize*, *center*. `scripts/check-us-english.py` fails the build on
British spellings and `--fix` rewrites them.

The list is of exact word forms, not stems, because stems are a trap here: *analysis*, *analyst*,
*specialist* and *realistic* are already correct US English and must never be rewritten.

**A skill references only what it ships.** A skill is installed as part of its department plugin and
nothing else comes with it, so a pointer to `docs/SOMETHING.md` resolves for a reader of this
repository and dangles for everyone who installed the plugin. Say the thing inline instead. The
exception is `executive:agent-hierarchy`, whose `docs/` paths are instructions to create those files
in the reader's own repository, not references to files here.

**`## Never` bullets agree with each other.** Two styles are in use and both are fine — bare
imperatives ending in a period, or the chief-level `Never …` / `Do not …` lines without terminal
punctuation. Mixing them inside a single block is what a list spliced in from somewhere else looks
like, and it is how four skills ended up with a wrapped bullet's continuation stranded on an
unrelated rule. `scripts/check-never-blocks.py` fails the build on a block that mixes them.

## Adding a department

All five, in the same change, or the check fails:

1. `plugins/<name>/skills/` and `plugins/<name>/.claude-plugin/plugin.json`
2. A roster row and a `surface:` block in `docs/AGENT-SURFACES.md`
3. A charter at `.claude/agents/<name>.md`
4. An entry in `.claude-plugin/marketplace.json`
5. A `(rank, title, executive)` entry in `META` in `scripts/build-readme.py`, then regenerate with
   `python3 scripts/build-readme.py`

The generator reads the department list off disk and refuses to run until step 5 is done, so a new
department cannot end up missing from the README and the org chart while the checks still pass.

Give it a chief before any specialists — the department's remit should exist before things are added
to it.

## Adding a file outside `plugins/`

It needs an owner in `docs/AGENT-SURFACES.md`, or the surface check fails. Most such files belong to
`repo-meta`.

## Decisions

Choices with more than one defensible answer go in `docs/DECISION-LOG.md`, numbered. A number is
assigned when the question is raised, not when it is answered, and is never reused. Every entry
carries lettered options and an explicit recommendation.
