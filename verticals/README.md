# Verticals

A vertical is the core made specific to one industry. `scripts/build-vertical.py` reads a vertical's
config and emits a standalone repository from it — the whole core, plus what that industry adds.

```
python3 scripts/build-vertical.py industrial            → dist/headcount-industrial/
python3 scripts/build-vertical.py industrial --verify    emit to a temp dir, run its checks, keep nothing
python3 scripts/build-vertical.py --all --verify         the same for every vertical; this is what CI runs
```

## The rule

**Generation is one-way. Generated output is never hand-edited.** D8 chose a generator over overlays
because productization is planned, and this rule is the entire cost of that choice. An edit made
downstream is lost on the next emit, silently — which is worse than a fork, because the divergence
is invisible.

`dist/` is gitignored for the same reason. A committed copy of the output is a hand-editable copy in
front of every contributor. What replaces it is `--verify`, which emits into a temporary directory,
initializes it the way a consumer's clone would be, and runs the emitted repository's own checks
against it. CI runs that on every push, so the emit cannot rot unnoticed without anything being
stored (D36).

## Layout

```
verticals/<slug>/
  vertical.toml                              what the vertical is
  skills/<department>/<skill>/SKILL.md       industry-only skills, added to that department
  context/<department>/<skill>.md            extends a core skill of that name
```

Skills and fragments are **discovered on disk, never listed** in the config. A list is a second place
to forget, and a skill added to the directory but not the list would be silently dropped from every
emit — the failure `build-readme.py` already guards against for departments.

## What a vertical may do

| | |
|---|---|
| Add a skill | `skills/<department>/<skill>/SKILL.md`. Colliding with a core skill's name fails the emit. |
| Extend a core skill | `context/<department>/<skill>.md`, spliced in ahead of the skill's `## Never` block. |
| Add a department | A `[[department]]` entry in the config. |
| Drop a department | `[emit] exclude_departments` in the config. |

**A vertical may bring a department the core has no reason to carry.** Industrial does not: its
skills belong to `operations` and `people`, which already exist. Education does — a curriculum
function is not a thinner version of anything in a cross-industry core, and filing it under an
existing department to avoid the feature would misroute every request that reached it.

```toml
[[department]]
name = "education"
title = "Education"
description = "Standards alignment, learning-materials design, assessment construction."
keywords = ["curriculum", "standards"]
```

The generator does what the surface map requires of a new department, because nobody is there to do
it by hand: it writes the plugin manifest, adds the marketplace entry, inserts the roster row and
surface block into the emitted map, and generates the charter. It also drops the `verticals` and
`sources` rows from the emitted map — their inputs stay upstream, so downstream those rows would
claim paths that are not there.

It may **not** edit a core skill in place. A core skill that is wrong for every industry is wrong in
the core; fixing it there means every vertical gets the fix on its next emit, which is the whole
reason for generating rather than forking.

Fragments carry their own `##` heading and are spliced ahead of `## Never` rather than appended,
because every skill closes with its rules and material after them reads as an afterthought.

## Adding a vertical

1. `verticals/<slug>/vertical.toml` — `[vertical]` slug, title, tagline, description, rationale;
   `[repo]` url and upstream. The slug must equal the directory name.
2. Write the skills and fragments.
3. `python3 scripts/build-vertical.py <slug> --verify` until it passes.
4. `./scripts/check-all.sh` — the vertical check runs `--all --verify`, so a broken vertical fails
   the build for everything.

**Vertical content is checked through the emit, not directly.** The core checkers glob `plugins/**`,
which this directory is not, so a thin description, a British spelling, a mixed `## Never` block or
a dangling `department:skill` reference in a vertical skill surfaces when the emitted repository
runs those same checks against itself. It is caught before anything ships, and the failure names
the emitted path rather than the source — look for the same file under `verticals/<slug>/`.

Naming follows D22: each vertical is `headcount-<slug>`, which is what the emitted marketplace and
install strings use.

## Publishing

The emitted tree is a complete repository. Publishing it is a deliberate act rather than part of the
build: emit without `--verify`, then push `dist/headcount-<slug>/` to its own repository. It carries
its own README, its own `CONTRIBUTING.md` pointing contributions back here, and the checks that
still mean something downstream — the three that verify generated documents stay upstream, where the
generators that write them live.
