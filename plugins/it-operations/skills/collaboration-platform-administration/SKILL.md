---
name: collaboration-platform-administration
description: Administers the email, chat, meeting and file-sharing platform the organization runs on — tenant and domain configuration, mail authentication and routing, phishing and spam controls, shared mailboxes and distribution groups, external sharing and guest access, permission sprawl in file storage, and retention and legal hold. Use this to configure a tenant, tighten sharing, investigate a mail delivery or phishing problem, or work out who can see a file and why.
---

# Collaboration platform administration

This platform holds most of the organization's unstructured information and nearly all of its
external communication. It is usually configured once during migration, by whoever ran the
migration, and then never revisited.

## Get mail authentication right, and keep it right

SPF, DKIM and DMARC together determine whether your mail is delivered and whether someone else can
send as you. All three need to exist and agree.

- **SPF** breaks quietly as third-party senders accumulate — marketing platforms, ticketing systems,
  invoicing tools — and has a hard limit on lookups that a growing list eventually crosses.
- **DKIM** has to be enabled per sending domain and per service, not once for the tenant.
- **DMARC** starts in monitoring and only protects once it moves to enforcement. A policy left at
  none for two years is a report nobody reads.

Every new tool that sends mail on your behalf is a change to this configuration. Route that through
the same process as any other change, or the first sign will be a customer saying your invoices go
to spam.

## Phishing controls are configuration, not awareness training

External sender warnings, impersonation and lookalike-domain protection, attachment and link
inspection, and blocking auto-forwarding to external addresses are settings. Auto-forward rules in
particular are the classic account-compromise persistence mechanism, and the account owner will not
notice.

Alert on inbox rule creation that forwards or deletes. It is one of the highest-signal detections
available and it comes free with the platform.

## Shared mailboxes, groups and the identities nobody owns

Shared mailboxes, distribution lists and team channels accumulate faster than anything else in the
tenant and are never cleaned up. Each needs a named owner and a review date, because a distribution
list nobody owns eventually mails the whole company by accident, and a shared mailbox with stale
access is a standing data exposure.

Never leave a shared mailbox with a sign-in-capable account. It is an unmonitored identity with a
password.

## External sharing is where file storage leaks

The defaults are usually more permissive than the organization would choose, and the settings sit
at several levels — tenant, site, folder, individual link — with the most permissive winning.

- **Anyone-with-the-link sharing** is the setting worth deciding on deliberately. If it is allowed,
  it needs an expiry.
- **Guest access** should expire and be reviewed. Guests from a project three years ago are still
  guests.
- **Permission inheritance is where sprawl comes from.** Someone grants access to a top-level
  folder to solve one request, and it propagates everywhere below.

Run a sharing report on a schedule. Nobody discovers over-sharing by browsing.

## Retention and legal hold are configured in advance or not at all

Retention policies decide what survives deletion and for how long, and they have to be set before
the data you will need is deleted. Legal hold suspends deletion for named custodians and must be
capable of being applied quickly.

The platform's own recycle bins are not a retention policy and not a backup — the retention windows
are short and administrator deletion can bypass them.

## Never

- Add a service that sends mail as your domain without updating authentication records.
- Leave DMARC in monitoring indefinitely and describe the domain as protected.
- Allow anyone-with-the-link sharing with no expiry.
- Treat the platform's recycle bin as either retention or backup.
