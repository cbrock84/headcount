---
name: it-asset-management
description: Tracks hardware and software assets through their life — procurement, ownership, licensing, refresh, and disposal. Use this to build an asset register, prepare for a software audit, plan a refresh cycle, control license spend, or dispose of equipment safely.
---

# IT asset management

The register exists to answer operational questions: what do we have, who has it, is it supported, is
it licensed, and when does it need replacing. An inventory that answers none of those is an
accounting artifact.

## One register, reconciled against reality

A register maintained by hand diverges immediately. Feed it from discovery — what is actually on the
network and enrolled in management — and reconcile against procurement and finance records.

The valuable output is the **discrepancy list**: assets in the register that discovery cannot find,
and devices discovery finds that the register does not know about. The second category is the
security problem, since an unknown device is unmanaged by definition.

## Ownership, not just location

Every asset needs a named accountable person. "The engineering team" is not an owner; when the device
needs patching, returning or replacing, a team does not answer.

Track state through the lifecycle — ordered, in stock, assigned, in repair, retired, disposed — and
require the state change at the moment of handover. A register updated in batches is a register that
is wrong between batches, which is most of the time.

## Software licensing

Under-licensing is a financial and legal exposure that surfaces at audit; over-licensing is money
spent on nothing, and it is usually the larger number.

Reconcile entitlements against actual installs and actual use. Reclaiming licenses from people who
stopped using a tool typically funds a meaningful fraction of the next renewal, and the data for it
already exists.

Watch license models that change cost with infrastructure — per-core, per-socket, per-user in a
system that provisions freely. A routine infrastructure change can multiply a license bill with no
procurement decision anywhere in the path.

## Refresh and disposal

Plan refresh on a cycle and budget it as a steady cost through
`finance:budgeting-and-forecasting`. Refresh driven by failure produces an unpredictable expense and
a worse experience, and it always arrives at the wrong moment.

Disposal is where data escapes. Require certified destruction or verified wipe, keep the certificate,
and treat storage devices as data until proven otherwise. A drive in a cupboard nobody logged is a
breach with no date attached.

## Tooling

Discovery and hardware inventory: Lansweeper, Snipe-IT, ServiceNow ITAM, Device42, and similar;
the endpoint management platform already knows most of the fleet and is the cheapest starting
point.

Software licensing and SaaS spend: Flexera, Torii, Zylo, Productiv, and similar. The SaaS half is
where the money hides, and it is discovered through the expense system and single sign-on logs as
much as through any inventory tool.

Reconcile the register against the endpoint platform, the identity provider and the finance system
on a schedule. Three systems each holding a partial truth is the normal state, and the gaps between
them are the assets nobody is managing.

## Never

- Maintain a register by hand and trust it.
- Record a team as an asset owner.
- Renew licenses without reconciling against actual use.
- Dispose of storage without evidence of destruction or wipe.
