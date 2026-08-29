# Contributing

Contributions are welcome. This document covers the licence, the bar for a skill, and the checks.

## Licence

**By submitting a contribution you agree it is licensed under the [MIT Licence](LICENSE), the same
terms as the rest of this repository.**

Contribute only work you have the right to license this way. In particular, do not paste in skills,
prose, or reference material from another project unless you wrote it or its licence permits
relocation — and if it does, say so in the pull request. Every line in this repository is original
to it, and `scripts/check-provenance.py` fails the build if third-party licence text, copyright
notices, or font assets appear.

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

Four checks, the same ones CI runs:

| Check | What it enforces |
|---|---|
| Surface map | Every tracked path has exactly one owner |
| Skill frontmatter | `name` equals the directory name, lowercase-hyphenated, unique, description substantial |
| Provenance | No third-party licence text, copyright notices, or font assets |
| Generated docs | README and org-chart tables match the tree |

**Stage your files first.** The surface guard reads `git ls-files`, so an unstaged file is invisible
to it — the check will pass and then fail once committed. The script warns when untracked files are
present.

## Adding a skill

1. `plugins/<department>/skills/<skill-name>/SKILL.md`
2. Frontmatter `name` must equal the directory name.
3. Check nothing already covers the ground. Two skills whose descriptions both match a request means
   neither reliably wins — prefer extending an existing skill, or folding a family into one skill
   with references, over adding a near-neighbour.

## Adding a department

All four, in the same change, or the check fails:

1. `plugins/<name>/skills/` and `plugins/<name>/.claude-plugin/plugin.json`
2. A roster row and a `surface:` block in `docs/AGENT-SURFACES.md`
3. A charter at `.claude/agents/<name>.md`
4. An entry in `.claude-plugin/marketplace.json`

Give it a chief before any specialists — the department's remit should exist before things are added
to it.

## Adding a file outside `plugins/`

It needs an owner in `docs/AGENT-SURFACES.md`, or the surface check fails. Most such files belong to
`repo-meta`.

## Decisions

Choices with more than one defensible answer go in `docs/DECISION-LOG.md`, numbered. A number is
assigned when the question is raised, not when it is answered, and is never reused. Every entry
carries lettered options and an explicit recommendation.
