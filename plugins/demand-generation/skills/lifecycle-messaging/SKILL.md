---
name: lifecycle-messaging
description: Designs automated email and SMS programs — welcome and onboarding sequences, nurture, re-engagement, transactional messaging, and the timing and segmentation behind them. Use this to build or fix an email sequence, plan lifecycle automation, improve open or click performance, set up SMS flows, or decide what messages a customer should receive and when.
---

# Lifecycle messaging

## Map the lifecycle before writing any message

For each stage, name what the person is trying to do and what would move them forward. Messages
written without that answer become announcements, and announcements get unsubscribed from.

The stages that matter: just signed up, activated but not habitual, habitual, at risk, lapsed.
Most programs over-invest in the first and neglect at-risk entirely, which is where the money is.

## The welcome sequence

The highest-engagement messages you will ever send. Do not waste them on company history.

1. **Immediate** — deliver whatever was promised, plus the single next action.
2. **Within days** — the fastest route to first value, one step.
3. **After that** — the use case most people miss, or the objection most people have.

Set expectations early: what you send, how often. It reduces unsubscribes more than any subject-line
technique.

## Timing and cadence

Trigger on behavior, not the calendar, wherever possible. A message sent because someone did
something is many times more relevant than one sent because it is Tuesday.

Cadence sustainable at your worst week. Every message should be one the recipient would miss.

## SMS is a different medium

Higher consent bar, higher intrusion, higher cost. Reserve it for time-sensitive and transactional
messages — delivery, appointment, security, an expiring window. Marketing SMS at any volume trains
people to opt out.

Explicit opt-in, honored opt-out, sending hours respected in the recipient's timezone. These are
legal requirements in most jurisdictions, not preferences.

## SMS compliance is not optional

> Consult qualified counsel before launching an SMS program. The exposure here is statutory damages
> per message, which is how these become class actions.

In the US, marketing SMS requires **express written consent** obtained before sending — implied
consent, an existing customer relationship, or a phone number collected for another purpose does not
qualify. The consent record must show what the person agreed to receive and when, and it must be
retained.

The operational requirements that follow:

- Disclose program purpose, frequency, and that message rates may apply, at the point of consent.
- Honor opt-out immediately, on every standard keyword, with a single confirmation message and
  nothing after it.
- Respect quiet hours in the **recipient's** timezone, not yours.
- Keep consent and opt-out records for as long as the retention rules require — these records are
  the entire defense if challenged.
- Never buy or rent SMS lists. Purchased consent is not consent.

Other jurisdictions impose their own rules, and several are stricter. Determine which apply by where
recipients are, not where you are.

## Subject lines and preview text

They are one unit and get read together. A subject line that works with the preview repeating it
wastes the second-most-read text in the message — use the preview to extend the subject, not echo
it, and never leave it to default to the first line of the body.

## Diagnosing

- **Low open** — subject line, sender reputation, or list quality. Check deliverability before
  rewriting subject lines; a reputation problem looks exactly like a copy problem.
- **Open but no click** — the message did not deliver on the subject, or has no single clear action.
- **Click but no conversion** — the destination, not the email.
- **Rising unsubscribes** — frequency or relevance. Usually frequency.

## Tooling

Lifecycle automation: Customer.io, Braze, Iterable, Klaviyo for commerce, HubSpot or
Marketo for B2B, and similar.

Transactional sending is a separate job with separate reputation: Postmark, SendGrid,
Resend, and similar. Keep it off the marketing domain.

In-product messaging: Intercom, Appcues, Pendo, and similar. An email that should have been
an in-app prompt reaches half the audience at best.

## Never

- Send to a list that did not opt in.
- Bury the unsubscribe.
- Run a re-engagement program without a plan to actually remove the people who do not re-engage. An
  unengaged list damages delivery for everyone else.
