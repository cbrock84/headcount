---
name: branch-and-worktree-workflow
description: Isolates feature work in its own branch or worktree and integrates it cleanly when done. Use this when starting work that should not disturb the current workspace, when several efforts must proceed in parallel on one repository, or when implementation is finished and the change needs merging, rebasing, or splitting for review.
---

# Branch and worktree workflow

## Starting

Work that will take more than one sitting, or that runs alongside other work, gets its own isolated
workspace. A worktree gives you a second checkout of the same repository on a different branch — two
efforts, two directories, one object store, no stashing.

Branch from the current upstream default, not from whatever is checked out. Branching off a stale
local branch is how unrelated commits end up in a review.

## While working

- Commit at points where the tree is coherent, not at the end of the day.
- Keep the branch current with its base often. A merge conflict found on day one is a five-minute
  fix; the same conflict found on day ten is an afternoon.
- One concern per branch. If you find an unrelated bug, note it and leave it.

## Finishing

Before proposing the work:

1. Rerun the full check the project actually gates on, not the subset you have been running.
2. Read your own diff top to bottom. Remove debug output, stray files, and commented-out code.
3. Confirm the branch merges cleanly into its base.

Then decide how it integrates:

- **Small and coherent** — merge as is.
- **Several separable concerns** — split into stacked branches so each can be reviewed on its
  merits. A reviewer given three concerns in one diff reviews none of them well.
- **Exploratory** — keep the useful commits, drop the rest.

## Never

- Rewrite history on a branch someone else has checked out. Merge instead; a force-push breaks their
  working copy.
- Leave a worktree behind after merging — stale worktrees hold references and confuse later work.
- Merge your own change without the checks green on the final commit, not an earlier one.
