# Starter rosters — mobile app portfolio, game portfolio, shared core

Concrete starting points, not prescriptions. Adapt the globs to your real trees; the
classes and the producer/auditor pairings are the parts worth keeping.

---

## Shared core repo (own repo, published + versioned)

Recommended shape for two consuming portfolios — see playbook §11(B). The core is a
**pinned published version** on each side; neither portfolio edits it in place.

```roster
# id                  class      status
core-owner            builder    planned
core-contracts        builder    planned
core-qa               reviewer   planned
security-deps         reviewer   planned
```

- **`core-owner`** — the shared runtime: state, persistence, networking, audio, input.
- **`core-contracts`** — the *published surface*: the public API, the save-file format, the
  analytics event schema, the version/compat policy. Sole agent permitted to change a
  contract, and it does so as a **coordinated pair** with a consumer PR.
- **`core-qa`** — tests the compat matrix: does version N read version N-1's save files.
- **`security-deps`** — sole reviewer for manifests, lockfiles, and third-party licences.

**The single most valuable rule here:** never remove a core export because it looks
unused. You cannot see the consumers from inside the core. Deprecate, announce, remove.

---

## Mobile app portfolio

```roster
# id                  class      status
app-builder           builder    planned
platform-ios          builder    planned
platform-android      builder    planned
design-system         builder    planned
data-layer            builder    planned
build-release         builder    planned
dependencies          builder    planned
store-presence        builder    planned
premerge-qc           reviewer   planned
store-compliance      reviewer   planned
security-deps         reviewer   planned
production-health     reviewer   planned
```

| Producer | Audited by |
|---|---|
| `app-builder`, `platform-*` | `premerge-qc`, `production-health` |
| `store-presence` | `store-compliance` |
| `data-layer`, `dependencies` | `security-deps` |
| `build-release` | `premerge-qc` |

- **`platform-ios` / `platform-android`** exist separately only if the native trees are
  genuinely separate. If you are on one cross-platform toolchain with a thin native shim,
  collapse them into `app-builder` and keep a single `platform-native` for the shims.
- **`store-presence`** owns listing copy, screenshots, and metadata *as repo files*.
  **Submission is class 3 — it stages, a human submits.**
- **`store-compliance`** is the reviewer that pays for itself: privacy-manifest / data-safety
  declarations, age ratings, permission justifications, and required disclosures, checked
  against what the code actually does. This is the class of mistake that costs you a
  rejection cycle, and it is exactly what a read-only auditor catches.

---

## Game portfolio

```roster
# id                  class      status
gameplay              builder    planned
content-pipeline      builder    planned
engine-integration    builder    planned
economy               builder    planned
build-release         builder    planned
dependencies          builder    planned
store-presence        builder    planned
premerge-qc           reviewer   planned
store-compliance      reviewer   planned
economy-integrity     reviewer   planned
security-deps         reviewer   planned
```

| Producer | Audited by |
|---|---|
| `gameplay`, `engine-integration` | `premerge-qc` |
| `economy` | `economy-integrity`, `security-deps` |
| `content-pipeline` | `premerge-qc` |
| `store-presence` | `store-compliance` |

- **`content-pipeline`** owns asset import, atlases, localization tables, and the
  generators that produce them. **A generator belongs with its output** — otherwise the
  output's owner cannot regenerate it.
- **`economy`** owns IAP catalogs, currency, progression curves, and reward tables.
- **`economy-integrity`** is the games analogue of a billing reviewer: it verifies that the
  price, the entitlement granted, the receipt validation path, and the store product
  actually agree end to end. **This is the one to install first.** Money and progression
  are where a silent disagreement between two files becomes a refund queue.
- Games accumulate **tuning constants** faster than anything else. Put every one in a
  source-of-truth registry (playbook §6) with a named owning file, or the same number ends
  up in four places with three values.

---

## Example map fragment (games)

````markdown
```surface:economy
config/economy/**
src/economy/**
!src/economy/receipts/**
```

```surface:security-deps
# read-only — no write surface
```

```surface:orchestrator
CLAUDE.md
docs/AGENT-SURFACES.md
docs/DECISION-LOG.md
.claude/**
scripts/agent-guard.mjs
```
````

Note `!src/economy/receipts/**` — receipt validation is an authentication boundary, so it
belongs to whichever agent owns auth, not to the agent that sets prices. That single
exclusion is the kind of carve-out the map exists to make visible.
