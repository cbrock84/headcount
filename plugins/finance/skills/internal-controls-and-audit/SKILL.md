---
name: internal-controls-and-audit
description: Designs and tests controls over financial reporting — segregation of duties, approval limits, evidence, and preparing for audit. Use this to design controls for a process, prepare for an external audit, respond to an audit finding, set approval thresholds, or assess where a small team's segregation of duties is genuinely broken.
---

# Internal controls and audit

Controls exist because a single person who can initiate, approve and record a transaction can also
conceal one. Everything else is elaboration on that.

**This structures control design and audit readiness. Statutory audit requirements, and regimes such
as SOX where they apply, are matters for your auditors and qualified advisers.**

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
