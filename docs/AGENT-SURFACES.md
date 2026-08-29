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

## Roster

```roster
# id                class      status
executive            builder    installed
technology           builder    installed
product              builder    installed
marketing            builder    installed
demand-generation    builder    installed
revenue              builder    installed
finance              builder    installed
operations           builder    installed
people               builder    installed
legal-risk           builder    installed
security             builder    installed
repo-meta            builder    installed
legal-risk-review    reviewer   installed
security-review      reviewer   installed
```

Charters live in `.claude/agents/`, one per installed row. A row marked `installed` without a
charter, or a charter without a row, fails the check — the two cannot drift apart silently.

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
```surface:security
plugins/security/**
```

```surface:repo-meta
docs/**
scripts/**
.github/**
.claude/**
.claude-plugin/**
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
