# Agent surfaces

The write-surface map for this repository. Every tracked path has exactly one owner and no two
owners claim the same path. `agent-guard check` verifies both, and CI runs it on every push.

Read `executive:agent-hierarchy` for the method. The short version: split by exclusive write
surface, not by topic, because a topic split has no checkable boundary — two agents working on "SEO"
and "UI" both end up in the same token file, and neither is wrong.

## Classes

- **builder** — edits inside exactly one exclusive surface, never commits.
- **reviewer** — permanently read-only, holds no write surface, can always run in parallel.

The orchestrator is neither: it owns no surface and is the sole committer.

## Authority

The class and the surface together answer *where* an agent may write. They have never answered
whether that write may land without a decision, so in practice that was settled per dispatch, from
memory, by whoever was driving. Authority states it once, in the same row, and `check` verifies it.

- **autonomous** — dispatch it and take the result. The surface is the only gate needed.
- **proposes** — it may do the work; the orchestrator surfaces the diff before landing it.
- **escalates** — do not dispatch it unasked. The work itself is the decision.

Two things the check enforces, both because the row would otherwise read as governed while
governing nothing: a reviewer may not be gated, because it holds no write surface to gate; and a
gated builder must actually own a surface.

Almost every row here is `autonomous`, and that is the honest answer rather than a placeholder — a
department writes only inside its own plugin directory, where the worst case is a bad skill in one
department. The column exists because the one exception is real, and because a repository adopting
this map will have more of them than this one does.

## Roster

```roster
# id                class      status     authority
executive            builder    installed  autonomous
technology           builder    installed  autonomous
product              builder    installed  autonomous
marketing            builder    installed  autonomous
demand-generation    builder    installed  autonomous
revenue              builder    installed  autonomous
finance              builder    installed  autonomous
operations           builder    installed  autonomous
people               builder    installed  autonomous
legal-risk           builder    installed  autonomous
customer-experience  builder    installed  autonomous
data-analytics       builder    installed  autonomous
corporate-strategy   builder    installed  autonomous
security             builder    installed  autonomous
it-operations        builder    installed  autonomous
pmo                  builder    installed  autonomous
repo-meta            builder    installed  proposes
legal-risk-review    reviewer   installed  autonomous
security-review      reviewer   installed  autonomous
```

`repo-meta` is the exception because of what it owns: the CI workflows, the check scripts, the
generators every document is built from, and this map. A change inside `plugins/finance/**` is
wrong in one department. A change to `scripts/check-all.sh` can make every other check stop
reporting, and nothing downstream would fail to say so.

Charters live in `.claude/agents/`, one per installed row. A row marked `installed` without a
charter, or a charter without a row, fails the check — the two cannot drift apart silently.

The column may be omitted; an omitted authority means `autonomous`, and `check` reports which rows
defaulted so that a map which never considered the question is distinguishable from one that
answered it.

## Surfaces

```surface:executive
plugins/executive/**
```

```surface:technology
plugins/technology/**
```

```surface:product
plugins/product/**
```

```surface:marketing
plugins/marketing/**
```

```surface:demand-generation
plugins/demand-generation/**
```

```surface:revenue
plugins/revenue/**
```

```surface:finance
plugins/finance/**
```

```surface:operations
plugins/operations/**
```

```surface:people
plugins/people/**
```

```surface:legal-risk
plugins/legal-risk/**
```
```surface:customer-experience
plugins/customer-experience/**
```

```surface:data-analytics
plugins/data-analytics/**
```

```surface:corporate-strategy
plugins/corporate-strategy/**
```

```surface:it-operations
plugins/it-operations/**
```

```surface:pmo
plugins/pmo/**
```

```surface:security
plugins/security/**
```

```surface:repo-meta
LICENSE
.gitignore
CONTRIBUTING.md
.gitattributes
docs/**
scripts/**
.github/**
.claude/**
.claude-plugin/**
Codex/**
README.md
```

Reviewers declare no surface. That is structural rather than a promise: `check` fails if a reviewer
claims one.

## Reviewer independence

`legal-risk` appears twice on purpose. As a **department** it owns `plugins/legal-risk/**` like any
other builder. As **`legal-risk-review`** it is reviewer-class: it reviews what other departments
commit to, holds no surface in that capacity, and its findings are not overrulable by the department
under review. Disagreement escalates to the Chief Executive rather than resolving inside the
reviewed department. See D13.

`security` mirrors `legal-risk`: a builder owning `plugins/security/**`, and separately
`security-review`, reviewer-class over what other departments build. Its blocking findings are not
overrulable by the department under review, which is why the CISO reports independently rather than
under the CTO (D9, D13).

## Rules

- **One owner per path.** A new department adds its roster row, its surface block, and its charter
  in the same change, or the check fails.
- **Never remove a surface because it looks unused.** Deprecate, announce, then remove.
- **Cross-surface work moves as one coordinated change**, never as two independent ones.
