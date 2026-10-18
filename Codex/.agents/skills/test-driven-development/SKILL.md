---
name: test-driven-development
description: Drives implementation by writing a failing test first, then the smallest code that passes it. Use this before writing implementation code for any feature or bugfix, when a bug needs a regression test, when existing code is hard to change safely, or when someone asks whether a change is covered. Also use to decide what is worth testing and what is not.
---

# Test-driven development

## The loop

1. **Red** — write one test that fails for the right reason. Run it. A test that passes immediately
   is testing nothing; a test that errors instead of failing is testing the wrong thing.
2. **Green** — the smallest change that makes it pass. Ugly is fine here.
3. **Refactor** — clean up with the test green. If it goes red, you changed behavior, not structure.

Never skip step 1. Writing the test after the code produces a test shaped to the implementation,
which is the one shape that cannot catch the implementation being wrong.

## What to test

Test behavior at the boundary a caller actually depends on. For each unit ask: if this broke
silently, who notices and how? If the answer is nobody, delete the code rather than test it.

- **Test**: branching logic, boundary conditions, error paths, anything with a past bug, contracts
  between modules.
- **Do not test**: getters, framework behavior, private helpers reachable only through a public path
  already covered, exact wording of log lines.

## Bugs

Every bug gets a failing test *before* the fix, reproducing it at the smallest scope that shows it.
That test is the proof the bug existed and the guard that it stays fixed. A fix without one is a
claim.

## Rules

- One behavior per test. A test asserting five things tells you almost nothing when it fails.
- The test name states the behavior, not the method: `rejects_expired_token`, not `test_auth`.
- Never weaken an assertion to get green. If a test is inconvenient, the design is telling you
  something.
- Never mock what you own — mock the network and the clock, not your own modules. Mocking your own
  code tests the mock.

## Return contract

Report the tests added, what each pins down, what is deliberately untested and why, and the actual
command you ran with its output. "Tests pass" without the command output is not a result.
