---
name: intellectual-property
description: Covers what the organization owns and what it is only borrowing — trademarks and clearance, copyright and work-for-hire, patents and trade secrets, open-source license obligations and copyleft reach, and IP terms in customer, contractor and AI-tool agreements. Use this to check whether a name is usable, establish that you own work you paid for, decide how to handle a license obligation in a dependency, or respond to an infringement claim.
---

# Intellectual property

Most IP damage is done quietly and early — by a name adopted without a search, a contractor
agreement missing an assignment clause, or a dependency added without reading its license. All
three are cheap to prevent and expensive to unwind.

**This structures the questions and the recurring failure patterns. IP rights are jurisdictional,
deadline-driven and fact-specific — get qualified counsel before adopting a name, filing anything,
or responding to a claim.**

## The four rights protect different things and are not interchangeable

- **Trademark** protects a name or mark as an indicator of source, within classes of goods and
  services and within territories. Rights come from use and are strengthened by registration.
- **Copyright** protects expression, not ideas. It arises automatically on creation; registration
  matters mainly for what you can recover in a dispute.
- **Patent** protects an invention, in exchange for publishing it, and is defeated by your own
  prior public disclosure in many regimes. If patenting is plausible, file before you present,
  publish, or demonstrate.
- **Trade secret** protects information whose value depends on being secret, for as long as you
  actually keep it secret — which requires demonstrable measures, not just intent.

## Clear a name before you build on it

A search is cheap; a rebrand after launch is not, and the cost lands after you have printed
material, bought domains, and built recognition. Search registered marks in the classes and
territories you will operate in, and check for confusingly similar marks rather than exact matches.

Domain availability tells you nothing about trademark risk. Neither does the absence of a company
with that exact name.

## Establish ownership of work you paid for, in writing, before it starts

This is the most common and most avoidable failure in the whole area.

- **Employee work** is often owned by the employer by default, but the default varies by
  jurisdiction and by whether the work relates to the job.
- **Contractor and agency work is usually owned by the contractor** unless the agreement assigns it.
  A paid invoice is not an assignment. Logos, code, photography, and copy commissioned without an
  assignment clause routinely turn out to be licensed rather than owned — discovered during
  diligence, at the worst possible time.
- **Get assignment plus a waiver of moral rights where they apply**, and confirm the contractor had
  the right to assign anything they incorporated.

## Open-source obligations are license terms, not etiquette

Every dependency carries a license with conditions, and the conditions attach to distribution.

- **Permissive licenses** mostly require attribution and notice retention. Cheap, but not zero —
  the notices have to actually ship.
- **Strong copyleft** can require you to offer source for the combined work you distribute. Whether
  it reaches your code depends on how you combine and whether you distribute, and that analysis is
  worth doing before adoption rather than before a release.
- **Network copyleft** treats providing the software as a service as triggering the obligation,
  which surprises teams who assumed a hosted product avoids distribution entirely.

Maintain an inventory of dependencies and their licenses, generated rather than maintained by hand,
and gate new licenses at the point of adoption. Removing a dependency after it is embedded is a
project.

## Read the IP terms in agreements you sign

In customer contracts, watch for ownership of deliverables and of anything developed during the
engagement, broad license grants back to the customer, and feedback clauses assigning your
improvements. In tooling agreements, including AI services, check what rights are claimed over your
inputs and outputs and whether your content trains anything.

## Responding to a claim

Do not reply substantively before counsel sees it, do not admit anything, and preserve everything —
a claim letter triggers a preservation obligation immediately. Check whether insurance responds,
and check the indemnity you may hold from a supplier whose component is the actual subject.

## Never

- Adopt a name on the strength of domain availability.
- Commission work without a written assignment signed before the work starts.
- Add a dependency without knowing its license and what it requires on distribution.
- Respond to an infringement claim before counsel has seen it.
