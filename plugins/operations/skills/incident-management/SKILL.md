---
name: incident-management
description: Runs an operational incident from detection to closed action — declaring it and naming a commander, separating the people restoring service from the people communicating, keeping a timeline as it happens, deciding when it is over, and running a review that produces a small number of changes someone actually completes. Use this to set up an incident process, run one, work out why the same failure keeps recurring, or fix a review practice that generates findings nobody closes.
---

# Incident management

An incident is any unplanned disruption significant enough that normal work stops until it is
resolved. The discipline exists because the instincts that serve people well in ordinary work —
investigate thoroughly, decide carefully, keep everyone informed — all fail under time pressure
unless someone has structured them in advance.

This covers operational incidents generally. For security incidents, where evidence preservation
and disclosure obligations change the order of operations, see `security:incident-response`.

## Declare it, and say so out loud

The most expensive minutes are the ones spent deciding whether this is an incident. Set a low
threshold for declaring and accept that some declarations will be withdrawn — an incident stood
down after twenty minutes costs far less than one that ran for two hours as a conversation between
three people who each assumed someone else had it.

Severity should be defined in advance, in terms of customer impact rather than internal
inconvenience, with each level carrying a stated response: who is notified, how fast, and who can
be woken.

## Name a commander who does not fix anything

One person owns the incident: they decide, they sequence, they assign. **They should not be the
person with their hands in the system** — the moment the commander starts debugging, nobody is
running the incident and the timeline stops being kept.

Separate three roles even in a small response: the commander, the people restoring service, and
one person handling communication. Combining the first and third is survivable; combining the
first and second is how incidents run long without anyone noticing they have.

## Restore first, understand later

The goal during the incident is service restored, not cause understood. Roll back, fail over,
disable the feature, add capacity — whatever returns the customer to working. Diagnosis is
tomorrow's work, and pursuing it while people are affected is the most common way a thirty-minute
outage becomes a four-hour one.

**Preserve what you will need to diagnose before you destroy it.** Capture logs, a snapshot, the
current state — then restore. This is the one step where a minute spent now saves the entire
review.

## Keep a timeline while it is happening

Written as it happens, not reconstructed afterward. What was observed, what was changed, at what
time, by whom. Memory of an incident is unreliable within hours and the timeline is what makes the
review worth anything.

One channel, and everything in it. Side conversations produce a response where two people are
acting on different information.

## Communicate on a rhythm, including when there is nothing new

Say what is happening, what you are doing, what the impact is, and when you will next update — then
send that next update on time even if it says nothing has changed. Silence is read as absence, and
the update cost is trivial compared to the calls it prevents.

Do not speculate on cause while the incident is open. An early theory shared externally and later
withdrawn does more damage than the outage.

## Declare it over deliberately

Service restored is not the same as incident closed. Confirm recovery is holding, confirm the
backlog it created has been worked through, and say explicitly that it is over so people can stop.

## Run the review on the system, not the person

Within a few days, while memory is fresh. The question is what about the system made this failure
possible and made it take this long to resolve — not who typed the command. A review that produces
blame produces less information every subsequent time, because people stop volunteering what
actually happened.

**Produce one or two changes, not fifteen.** A short list that gets done beats a thorough list that
does not, and an unclosed action from a previous incident is the most common finding in the next
one. Track them to completion somewhere visible, with owners and dates.

## Never

- Debug while nobody is commanding.
- Destroy the state you will need to diagnose in order to restore a minute sooner.
- Skip a scheduled update because there is nothing new to say.
- Close a review with more actions than the organization will actually complete.
