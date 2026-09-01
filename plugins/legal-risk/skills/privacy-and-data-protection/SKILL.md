---
name: privacy-and-data-protection
description: Assesses and improves how personal data is collected, used, shared, and retained — data mapping, lawful basis, consent, processor agreements, subject rights, and breach obligations. Use this before launching anything that handles personal data, when adding a vendor that will process it, when a data subject request arrives, when assessing exposure under GDPR or US state privacy laws, or when preparing for a privacy review.
---

# Privacy and data protection

> Not legal advice. Regimes differ by jurisdiction and change; material questions need qualified
> counsel. This structures the assessment and identifies what to escalate.

## Start from the data map

You cannot assess what you have not inventoried. For each category of personal data:

- What is collected, from whom, and where it came from.
- Why — the specific purpose, and the lawful basis where one is required.
- Where it lives, who can reach it, and which vendors receive it.
- How long it is kept, and what deletes it. "Indefinitely" is a finding, not an answer.
- Whether it crosses a border, and under what mechanism.

Most privacy failures are inventory failures: data nobody remembered was being collected, in a
system nobody owned.

## Design decisions that prevent problems

- **Collect less.** Every field is a liability with a maintenance cost. The cheapest way to protect
  data is not to hold it.
- **Purpose limitation is real.** Data collected for one purpose is not automatically available for
  another — particularly for training models, which is where this most often goes wrong now.
- **Separate identifiers from behavior** where analysis does not require linkage.
- **Retention with an enforcing mechanism.** A policy with no deletion job is a statement of intent.

## Consent, where it applies

Specific, informed, freely given, and as easy to withdraw as to give. Pre-ticked boxes, bundled
consent, and cookie walls that offer no genuine choice fail on their face in the regimes that
require consent.

Note that consent is one lawful basis among several and often the weakest — it can be withdrawn,
and then the processing must stop.

## Vendors

Any third party processing personal data on your behalf needs a written agreement covering purpose,
security, sub-processors, deletion, and assistance with subject rights. Sending data to a vendor
without one is a common and easily avoided violation.

Assess the vendor's actual security, not their questionnaire answers, in proportion to the
sensitivity of what they will hold.

## Subject rights and breaches

Have a working process before the first request: how it arrives, how identity is verified, how the
data is located across systems, and the deadline. Locating the data is the part that fails.

For breaches, know your notification clock before you need it — several regimes measure it in hours
from awareness. Decide in advance who determines that awareness has occurred.

## Never

- Collect data because it may be useful later. Purpose first, then collection.
- Retain personal data past the period you published.
- Send personal data to a vendor before the contract terms and the transfer basis are in place.
- Load production personal data into a test environment.
