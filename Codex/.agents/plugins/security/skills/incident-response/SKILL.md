---
name: incident-response
description: Runs a security incident from detection to closure — triage, containment, investigation, communication, and the review afterward. Use this when a compromise is suspected or confirmed, when preparing an incident response plan or running an exercise, when deciding whether something is an incident, or when a breach may trigger notification obligations.
---

# Incident response

> Breach notification runs on statutory clocks, measured in hours in several regimes. Involve Legal
> & Risk and qualified counsel as soon as personal data may be involved — not after the technical
> work is done.

## Decide it is an incident, and say so

The most expensive delay is the hour spent debating whether this is really an incident. Declare
early; standing down a declared incident is cheap, and discovering an hour late that it was real is
not.

Name an **incident commander** immediately. One person, coordinating, not doing the technical work.
Everyone else has a defined job. Incidents fail on coordination far more than on technical
capability.

## Order of operations

**1. Contain before investigating.** Stop the bleeding: isolate the host, revoke the credential,
disable the account, block the path. It is tempting to watch the attacker to learn more — do that
only with a deliberate decision, not by default.

**2. Preserve evidence while containing.** Snapshot before you rebuild. Capture volatile state —
memory, connections, running processes — before powering anything off. Rebuilding a compromised host
destroys the only record of how they got in, and you will need it.

**3. Establish scope.** What was accessed, what was taken, when it started, and whether it is still
happening. Assume the initial scope is understated; it usually is. Look for persistence and lateral
movement before declaring containment.

**4. Eradicate and recover.** Remove the access, close the path, then restore. Rebuild from known
good rather than cleaning in place — you cannot prove a cleaned host is clean.

Rotate every credential the attacker could have reached, not only the ones you know they used.

**5. Watch after recovery.** Re-entry is common. Monitor specifically for the path they used and its
neighbors.

## Communication

Keep one timeline as the single source of truth, updated as facts are established, with each entry
timestamped and attributed. Incidents generate contradictory information at speed, and the timeline
is what stops the same question being answered three ways.

Say what is known, what is not yet known, and when the next update comes. Never speculate on cause
or scope externally before it is established — a retracted statement extends the story and damages
credibility more than the incident did.

## Afterward

Blameless review, focused on the system rather than the person. The useful questions: how could this
have been detected sooner, what made containment slow, what did we not have that we needed, and what
made this possible in the first place.

Output actions with owners and dates. A review producing no committed changes is theatre, and the
same incident recurs.

## Preparation

The plan matters less than having run it. Exercise once a year at minimum: a tabletop against a
realistic scenario finds the gaps — who has authority out of hours, where the credentials are, who
calls counsel — at a time when finding them is free.
