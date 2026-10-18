---
name: completion-verification
description: Verifies that work is actually complete before it is claimed to be — running the checks, reading the output, and confirming the original request was satisfied rather than approximated. Use this before saying something is done, fixed, or passing; before committing or opening a pull request; and whenever a claim of success has not been backed by command output.
---

# Completion verification

The gap between "should work" and "does work" is where most wasted cycles live. This closes it.

## Before claiming done

1. **Run the real check**, not a subset. The command the project gates on, on the current state of
   the tree.
2. **Read the output.** An exit code of zero with skipped tests, or a build with new warnings, is
   not what it looks like at a glance.
3. **Re-read the original request.** Not your interpretation of it several steps ago — the actual
   words. Confirm each part was addressed, and name any part that was not.
4. **Check for collateral damage.** What else consumes what you changed? Did anything else move?
5. **Confirm nothing was left behind** — debug statements, a skipped test, a TODO standing in for
   the hard case.

## What a claim must carry

Say what you ran and what it said. "Tests pass" is an assertion; the command and its output is
evidence. If you could not run something, say that explicitly rather than omitting it — an unstated
gap reads as a covered one.

## Honest incompleteness

Partial work reported accurately is useful. Partial work reported as complete costs someone else the
time to discover otherwise, plus the trust. If a part is blocked, unverified, or deliberately
skipped, name it in the same breath as the parts that are done.

## Never

- Claim a fix works without having reproduced the failure first.
- Report success from a stale run.
- Weaken, skip, or delete a failing test in order to claim green.
