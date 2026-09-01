---
name: internal-controls-and-audit
description: Designs and tests controls over financial reporting — segregation of duties, approval limits, evidence, and preparing for audit. Use this to design controls for a process, prepare for an external audit, respond to an audit finding, set approval thresholds, or assess where a small team's segregation of duties is genuinely broken.
---

# Internal controls and audit

Controls exist because a single person who can initiate, approve and record a transaction can also
conceal one. Everything else is elaboration on that.

**This structures control design and audit readiness. Statutory audit requirements, and regimes such
as SOX where they apply, are matters for your auditors and qualified advisers.**

## The five components an auditor will assess

Segregation of duties is one control activity inside a much larger structure, and a team that has
only built control activities will still be told its control environment is weak. Auditors assess
five components, and a deficiency in any one undermines the others:

- **Control environment** — integrity and ethical values, oversight by whoever plays the board
  role, a structure with defined responsibility and authority, competence for the work assigned,
  and accountability actually enforced. This is the component small organizations skip and the one
  that determines whether every other control holds.
- **Risk assessment** — objectives defined clearly enough to have risks, risks identified and
  responded to, **fraud risk assessed explicitly** rather than assumed away, and change identified
  as it happens. New systems, new people, and rapid growth all invalidate control designs quietly.
- **Control activities** — the controls themselves, including those over the information systems
  the records depend on, and evidence that they were performed rather than merely designed.
- **Information and communication** — quality information available to the people who need it,
  communicated internally to those who act on it and externally to those who rely on it. A control
  nobody was told about does not operate.
- **Monitoring** — someone checks that controls still work, and identified deficiencies get
  remediated on a timetable rather than carried forward year after year.

Two of these are consistently the weak ones in organizations under a few hundred people: fraud risk
is never assessed on the reasoning that everyone is trusted, and monitoring never happens because
the people who would monitor are the people who perform the controls.

## Segregation of duties

Four capabilities should not sit with one person: **initiating** a transaction, **approving** it,
**recording** it, and **holding the asset**. Any two combined is a risk; three is an unmonitored
opportunity.

Small teams cannot always separate these. That is a normal constraint and pretending otherwise
produces a fictional control matrix. Where separation is impossible, compensate visibly:

- Review by someone outside the process, on a defined cadence rather than when convenient.
- Exception reporting that goes to someone who is not the preparer.
- Bank confirmations and reconciliations reviewed independently of whoever performs them.

Document the gap and the compensating control. An acknowledged, mitigated gap is a defensible
position; an unacknowledged one is a finding waiting to be written.

## Design controls that leave evidence

A control that happened but left no trace did not happen, as far as an auditor can determine. Each
control needs a stated owner, frequency, what is examined, and an artifact produced as a by-product
of doing the work — not assembled afterwards for the audit.

Prefer **preventive** controls, which stop the transaction, over **detective** ones, which find it
afterwards. Prefer automated over manual: system-enforced approval limits do not have busy weeks.

## Approval thresholds

Set limits by value and by risk, not value alone. A low-value payment to a new supplier deserves more
scrutiny than a large one to an established counterparty on contracted terms.

Watch for splitting — transactions repeatedly landing just under a threshold is the pattern the
threshold creates, and it is straightforward to monitor for.

## Audit findings

Treat a finding as information. Fix the cause rather than the instance, and be skeptical of
remediation that consists of more careful behavior: the same conditions will reproduce the finding
with different people.

Related but distinct: `legal-risk:corporate-governance` owns board and entity governance,
`legal-risk:enterprise-risk` owns the risk framework. This skill owns controls over financial
reporting.

## Never

- Sign a control matrix that describes separation the team does not actually have.
- Accept a control with no evidence produced in the ordinary course of performing it.
- Remediate a finding with a commitment to be more careful.
- Set approval limits on value alone and not monitor for splitting.
