---
name: detection-and-monitoring
description: Builds the capability to notice an attack in progress — deciding what to log and retain, centralizing it somewhere tamper-resistant, writing detections that fire on attacker behavior rather than on individual events, tuning out the noise that trains people to ignore alerts, and defining what happens when something fires. Use this to design or assess monitoring coverage, work out why an incident went unnoticed, cut alert volume without losing signal, or decide what a detection capability should cost.
---

# Detection and monitoring

Incident response assumes someone noticed. Most organizations that respond well to incidents found
out from a customer, a vendor, or an extortion note, and the gap between compromise and discovery
is where nearly all of the damage accumulates.

## Decide what to log by asking what you would need afterward

Work backwards from the questions an investigation asks: who authenticated, from where, and what
did they then do. That points at a short list that matters far more than volume.

- **Identity events** — authentication success and failure, MFA changes, privilege grants, new
  API keys and tokens, consent grants to applications.
- **Endpoint process activity** — what ran, what spawned it, what it connected to.
- **Administrative actions** in the platforms that hold your data, especially permission and
  sharing changes.
- **Network egress** where you have it, and DNS, which is cheap and unusually informative.

**Retention decides whether you can investigate at all.** Intrusions are commonly discovered months
after entry, so logs kept for thirty days answer none of the useful questions. Split it: a short
hot window you can search fast, and a longer cold archive you can still reach.

## Centralize, and make the copy hard to erase

Logs stored only on the system that produced them are logs the attacker controls. Ship them off the
host as they are written, to a destination with different credentials from the systems it collects
from — otherwise one compromised administrator account ends both the intrusion and the evidence of
it.

## Write detections for behavior, not for events

A single event is almost never an incident. What distinguishes an attacker is a sequence:
authentication from a new location, followed by a mailbox rule creation, followed by a bulk
download.

- **Start from the techniques that actually apply to you.** Coverage is a property of your own
  estate, not of a vendor's rule count.
- **Detect the steps an attacker cannot skip** — persistence, privilege escalation, credential
  access, and exfiltration — rather than the tools they might use, which change.
- **High-signal detections available cheaply**: inbox rules that forward or delete externally, new
  federation or identity-provider trust, disabled logging, impossible travel on administrative
  accounts, and mass file access by a single principal.

Every detection needs a documented response. A detection that fires with no defined next step
becomes noise on its second occurrence.

## Tune ruthlessly, because alert fatigue is the real failure mode

An alert that is wrong most of the time trains people to close it without reading. The team stops
noticing, and the eventual real one closes the same way.

Measure the proportion of alerts that are actually actioned. Anything consistently below roughly
half is a tuning problem, and the fix is narrowing or suppressing the rule rather than adding
another analyst. A smaller number of trustworthy detections beats broad coverage nobody believes.

## Decide who is watching, and when

Coverage hours are an explicit decision with a cost. Business-hours monitoring means an intrusion
starting on Friday evening runs unobserved for two days, which is exactly why attacks are timed
that way. If you cannot staff around the clock, say so, and choose a small number of detections
that page a human at any hour rather than pretending the queue is monitored.

Outsourcing detection is legitimate and does not outsource the decision. The provider escalates;
someone inside still has to be reachable and authorized to disconnect something.

## Test that it would actually fire

Detection coverage is assumed far more often than it is verified. Run the behavior — a benign
version of the technique — and confirm the alert arrives, reaches a person, and carries enough
context to act on. Coverage claimed from a configuration page is not coverage.

## Never

- Retain logs for a window shorter than the time it typically takes to discover an intrusion.
- Store the only copy of a log on the system it describes.
- Ship a detection with no defined response.
- Claim coverage for a technique nobody has tested end to end.
