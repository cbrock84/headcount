---
name: cloud-administration
description: Administers the cloud the company runs on rather than the one it sells — tenant and subscription structure, the SaaS estate and who owns each app, identity as the real perimeter, cloud spend that arrives as a surprise, and what the provider does not do for you. Use this to structure subscriptions or tenants, get control of sprawling SaaS, cut a cloud bill, work out who owns an application nobody admits to buying, or decide what corporate workloads belong in cloud at all.
---

# Cloud administration

Corporate cloud is bought, not architected. Someone needed a tool, expensed it, and it entered the
estate without a review, an owner, or an offboarding path. The characteristic failure is not a bad
design — it is discovering the estate years later, one invoice at a time.

This is the cloud the business runs on. For the cloud a product is built on — environments,
infrastructure as code, scaling, region failure — see `technology:cloud-infrastructure`. The two
follow different rules and the boundary is worth keeping sharp.

## Structure the tenant before you need to

Subscription and account structure encodes what you can later separate: billing, access, policy,
and blast radius. Retrofitting it means moving live workloads, so the cheap moment is the first
one.

A workable default is to separate by what you would want to bill, govern, or lose independently —
production corporate services, non-production, and anything with a distinct compliance obligation.
Resist a subscription per team; teams reorganize, and the structure outlives them.

Tag at creation with owner, cost center, and environment, and enforce it with policy rather than
documentation. Untagged resources become unattributable spend within a quarter, and nobody
volunteers to claim them.

## The SaaS estate is the part nobody is managing

Most companies underestimate their application count by a wide margin, because the ones they know
about were bought by IT and the rest were bought by everyone else. The discovery methods that
actually work are financial, not technical: expense reports, corporate card statements, and the
identity provider's sign-in logs. Network monitoring finds less than the accounting system does.

Every application needs a named business owner, a renewal date, and a data classification. Without
the owner there is nobody to ask at renewal. Without the renewal date the negotiation happens after
auto-renewal. Without the classification, nobody knows which breach notification obligations apply
when the vendor is compromised.

An application that stores customer or employee data belongs in the review that
`legal-risk:privacy-and-data-protection` describes, and a departing employee's access to it is
`it-operations:identity-lifecycle-administration`'s problem — which it cannot solve for an
application it does not know exists.

## Identity is the perimeter, so treat it as infrastructure

Once the estate is cloud, network location protects nothing and the identity provider is the only
consistent control point. Single sign-on is therefore not a convenience feature; it is what makes
deprovisioning possible in one place instead of forty.

The practical rule is to refuse applications that cannot federate, or to accept them knowingly with
a documented manual offboarding step. Vendors that charge extra for SSO are charging for the
security baseline, and that cost belongs in the purchase decision rather than being discovered
later.

Conditional access, MFA, and privileged role activation are the controls worth the effort. See
`security:access-and-identity` for the design; this skill owns operating it across a real estate.

## Cloud spend surprises are structural

Cloud bills grow because nothing in the system stops them. Resources are easy to create, nobody is
billed personally, and consumption is invisible until the invoice.

Three habits catch most of it: a budget alert on every subscription before workloads land, a
monthly review of the largest movers rather than the whole bill, and a scheduled look at anything
running that nobody has logged into. Reserved and committed pricing is real money for steady
workloads, but it is a bet on a run rate — commit only where the load is genuinely predictable.

Non-production environments running overnight and at weekends are the most common single line of
waste, and shutting them on a schedule is a change nobody notices.

## Shared responsibility is narrower than people assume

The provider keeps the platform available. Almost everything else — configuration, access, and in
most cases the data itself — stays yours.

The one that catches organizations out is backup. A major SaaS suite protects itself against its
own failures, not against a user deleting a mailbox or a ransomware event propagating through
sync. Retention settings are not backups, and the recycle bin is not a recovery point. Decide
deliberately what needs independent protection under `it-operations:backup-and-recovery` rather
than assuming the vendor's durability promise covers your mistakes.

## Tooling

Platforms: AWS, Microsoft Azure, Google Cloud, and similar.

Infrastructure as code: Terraform, OpenTofu, Pulumi, Bicep, CloudFormation, and similar.

Cost visibility: the native cost tools, or CloudZero, Vantage, Finout, and similar.
Guardrails: AWS Control Tower, Azure Policy, Wiz, and similar.

Console changes nobody can reproduce in code become the outage you cannot rebuild from.

## Never

- Buy an application that cannot federate without recording the manual offboarding step.
- Let a resource exist without an owner tag and a cost center.
- Treat vendor retention settings as a backup.
- Structure subscriptions around the current org chart.
