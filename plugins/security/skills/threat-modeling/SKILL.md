---
name: threat-modeling
description: Identifies what could go wrong in a system before it is built or changed — the assets worth attacking, the entry points, the trust boundaries, and the controls that actually address the realistic threats. Use this when designing a feature or system, when a change touches authentication, data handling, payments, or external input, before a security review, or when deciding which security work is worth doing at all.
---

# Threat modeling

Done at design time this is cheap and changes the design. Done after launch it produces a list of
things that are expensive to fix, so the timing is most of the value.

## Four questions, in order

**1. What are we building?** A diagram of the actual data flow — not the org chart, not the
marketing architecture. Components, the data moving between them, and where each store lives. If
nobody can draw it, that is the first finding.

Mark the **trust boundaries**: every point where data crosses from something you control to
something you do not, or from one privilege level to another. Almost every real vulnerability lives
on a boundary.

**2. What can go wrong?** Walk each boundary and each asset. A usable prompt set:

- **Spoofing** — can someone claim to be another user, service, or system?
- **Tampering** — can data be modified in transit, at rest, or in the client?
- **Repudiation** — can someone deny an action, and would we be able to show otherwise?
- **Information disclosure** — what leaks: to other users, to logs, to error messages, to the
  client bundle?
- **Denial of service** — what is unbounded? Uploads, queries, retries, fan-out.
- **Elevation of privilege** — can a user reach data or actions belonging to another tenant, role,
  or account?

Two that catch more real bugs than the classic list: **what does the client enforce that the server
does not**, and **what happens on the second attempt** — replay, race, and double-submit.

**3. What are we going to do about it?** For each realistic threat: mitigate, transfer, avoid, or
accept. Accepting is legitimate; accepting silently is not.

Prioritize by attacker effort against impact, not by how alarming it sounds. A trivially exploitable
tenant-isolation bug outranks a theoretical timing attack every time.

**4. Did we do a good job?** Re-check the model when the design changes. A threat model that
describes last quarter's architecture is worse than none, because it produces false confidence.

## Scoping

Model per feature or per boundary, not per system. A whole-system model is too big to finish and too
vague to act on.

Timebox it. An hour on a specific feature with the engineers who will build it beats a week-long
exercise producing a document nobody reads.

## Never

- Model the system as designed rather than as built. Ask what actually got shipped.
- Assume internal traffic is trusted. That assumption is what turns one compromised service into
  an incident.
- Accept "the framework handles that" without checking that it is configured to.
