---
name: code-review
description: Conducts and responds to code review — reviewing a change for correctness, design, and risk, and evaluating review feedback received on your own work. Use this before merging, when asked to review a diff or pull request, when review feedback has arrived and needs acting on, or when feedback seems wrong and needs a reasoned response rather than compliance.
---

# Code review

Two directions, one skill: reviewing, and being reviewed.

## Reviewing

Read the diff against what the change is *for*, not against your preferences. Order matters — spend
attention where damage is expensive:

1. **Correctness** — does it do what it claims, including at the boundaries and on the error path?
2. **Blast radius** — what else consumes this? Signature and schema changes are the ones that break
   things far away.
3. **Security and data** — untrusted input, authorization, anything logged or persisted.
4. **Tests** — do they pin the new behavior, or do they pass regardless?
5. **Design** — will this shape hold under the next change?
6. **Style** — last, and only where a linter cannot.

Say which category each comment is, and whether it blocks. A review that mixes a data-loss bug with
a naming preference in one undifferentiated list wastes the author's judgment.

## Receiving

Feedback is a report of a reader's experience, and that part is always valid — if the reviewer
misread it, the code is misleading. The proposed remedy is a separate thing and may be wrong.

- **Verify before implementing.** A suggestion that would break behavior gets a reply, not a commit.
- **Disagreeing is fine; ignoring is not.** Answer every comment: changed, or why not.
- **Do not batch-accept.** Applying every suggestion without judgment is how good code becomes
  incoherent.
- Where a reviewer is factually wrong, show the evidence — the test, the spec, the failing case —
  rather than asserting.

## Never

- Approve your own work, or a change you authored under another name.
- Leave a blocking comment without saying what would unblock it.
- Rewrite the author's approach in a review comment. Propose it, and let them decide.
