---
name: access-and-identity
description: Designs and audits who can reach what — authentication, authorization models, privileged access, service credentials, and joiner-mover-leaver process. Use this to design a permissions model, run an access review, reduce standing privilege, handle offboarding, set up SSO or MFA, manage service and machine credentials, or diagnose why permissions have sprawled.
---

# Access and identity

Access accumulates. People change roles and keep the old permissions, services get broad credentials
because narrow ones were inconvenient, and contractors' accounts outlive their contracts. Left alone,
entitlement always grows and never shrinks.

## Principles that actually hold

- **Least privilege, and it must be practical.** A model so restrictive that people share accounts
  to get work done is worse than a looser one they follow.
- **Role-based, not person-based.** Grants attached to individuals are ungovernable at any scale.
- **Time-bound elevation over standing privilege.** Nobody should hold administrative access
  continuously because they occasionally need it. Elevation on request, with a reason, expiring
  automatically.
- **Separate duties where the consequence is severe.** The person who requests a payment does not
  approve it; the person who writes the deploy does not solely authorize the production change.

## Authentication

Single sign-on wherever possible — the value is not convenience, it is that offboarding becomes one
action rather than forty. Every system outside SSO is a system someone will still have access to
after they leave.

Multi-factor everywhere it is available, and phishing-resistant factors for administrative access.
SMS is better than nothing and is the weakest option worth deploying.

## Joiner, mover, leaver

**Mover is the one everyone gets wrong.** Joining and leaving are events with a process; changing
role usually adds permissions and removes none, which is how a long-tenured employee ends up with
access to everything.

Make role change a revoke-and-regrant rather than an addition. It is the single highest-value change
most organizations can make to their access posture.

Offboarding needs to be same-day, cover everything including systems outside SSO, and be verified
rather than assumed. Keep a list of what exists to be revoked — the fastest way to find the shadow
systems is to try to offboard someone thoroughly.

## Service and machine credentials

Usually more numerous and less governed than human ones. Each needs a named human owner, a scope
limited to its actual use, a rotation path, and an expiry.

Prefer short-lived, automatically issued credentials over long-lived keys. A key that never expires
will eventually appear in a repository, a log, or a support ticket.

## Access reviews

Periodic, by system, with the reviewer being the person accountable for the data rather than IT.
Reviewers who cannot say why someone needs access should remove it — the burden belongs on
retention, not removal.

Review dormant accounts as a separate pass. An account nobody has used in six months is either
unnecessary or belongs to someone who left.

## Diagnosing sprawl

Look for: permissions granted to individuals rather than roles, roles nobody can define, standing
administrative access, accounts whose owner has left, service credentials with no owner, and systems
outside SSO. Each is a specific fix, and the list is nearly always the same list.

## Tooling

Identity providers: Okta, Microsoft Entra ID, Google Workspace, JumpCloud, and similar.

Privileged access and secrets: CyberArk, HashiCorp Vault, 1Password, Doppler, and similar.

Access reviews and provisioning: Okta Identity Governance, Entra ID Governance, Lumos,
ConductorOne, and similar. Worth buying at the point a manual quarterly review stops
finishing rather than the point it gets tedious.

## Never

- Grant standing access where time-bound access would do the same job.
- Leave an account active while an offboarding ticket works its way through. Cut access first, reconcile after.
- Share a credential between people. If two people can use it, no log tells you which one did.
- Approve your own access request, or review a group you belong to.
