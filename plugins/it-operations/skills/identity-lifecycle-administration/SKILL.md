---
name: identity-lifecycle-administration
description: Executes joiner, mover and leaver processes — provisioning, group membership, access changes on role change, and complete deprovisioning. Use this to set up or fix joiner-mover-leaver, deprovision someone completely, clean up accumulated access, audit group membership, or find accounts that outlived their owners.
---

# Identity lifecycle administration

This is execution: creating, changing and removing access as people arrive, move and leave.
**Policy — what a role should be entitled to, and least privilege — belongs to
`security:access-and-identity`.** This skill runs the process that policy defines, and the gap
between the two is where most access problems live.

## Joiners

Provision from the role, not by copying a colleague. Copying is the single largest source of
privilege accumulation: it inherits everything that person collected, including access they should
not have had, and it propagates that indefinitely.

Define role-based bundles for the common cases so a standard joiner is one action, and treat
anything outside them as an exception requiring approval. Exceptions are fine; unrecorded exceptions
are not.

Time provisioning to be complete before the start date — coordinated through
`people:onboarding-and-offboarding`.

## Movers are the neglected case

Leavers get attention because someone is going. Movers do not, and so access accrues: the person who
has worked in three departments has permissions from all three, and nobody ever removed the first
two.

Treat a role change as a **revoke and re-provision**, not an addition. This is the single highest-
value fix available in most organizations, and it is almost always skipped because the person is
still present and nothing appears broken.

## Leavers, completely

Disable promptly at the agreed time, then work a checklist that reaches past the directory: systems
outside single sign-on, local accounts, shared credentials the person knew, API keys and tokens they
created, external services procured on a personal login, and any mail or calendar delegation.

The gap is almost always the systems identity management does not reach. Maintain the list of them
explicitly rather than discovering it during an audit.

Preserve rather than delete where there is any prospect of investigation or legal hold — deletion is
irreversible and occasionally very expensive.

## Recertify, and act on it

Periodically, system owners confirm who should still have access. This is worth doing only if
non-response defaults to removal; where non-response means retain, recertification becomes a
formality that certifies whatever exists.

Hunt specifically for orphaned accounts — accounts with no owner, service accounts nobody claims,
and credentials that have not been used in months but still work.

## Never

- Provision by copying an existing user.
- Add access on a role change without removing the old.
- Consider a leaver deprovisioned when the directory account is disabled.
- Run recertification where non-response means retain.
