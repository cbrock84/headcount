---
name: seo-strategy
description: Audits and improves organic search performance — technical health, site architecture, internal linking, structured data, and the content decisions that determine what can rank. Use this to run an SEO audit, diagnose why pages are not ranking or were deindexed, plan a site's URL and navigation structure, add structured data, or prioritize which SEO fixes are worth doing.
---

# SEO strategy

## Diagnose in this order

Skipping to content when the problem is technical wastes months. Work down; stop when you find the
break.

1. **Can it be crawled?** Robots directives, noindex left on after a launch, blocked resources,
   crawl budget wasted on parameter and filter URLs.
2. **Can it be indexed?** Check what is actually in the index versus what should be. Canonicals
   pointing at the wrong page and unintended duplicates are the two usual causes.
3. **Does the page deserve to rank?** Search intent match first. A page can be technically perfect
   and still lose because it answers a different question than the query asks.
4. **Does the site have the authority to rank for it?** Some terms are out of reach for now.
   Targeting them is a decision to spend without return.

## Architecture

Structure follows how people look for things, not how the company is organized.

- Anything important reachable within three clicks of the home page.
- Group related pages so internal linking is natural, not retrofitted.
- One URL per thing. Parameters, trailing-slash variants, and case differences that all resolve are
  duplicate content in the crawler's eyes.
- URLs readable and stable. Changing them costs equity even done correctly.

Internal linking is the most underused lever available: it is fully within your control, and it
directs authority to the pages you actually care about. Link with descriptive anchor text from your
strongest pages to the ones that need help.

## Performance and mobile

Speed and mobile usability are ranking inputs and, more importantly, conversion inputs. Audit them
as part of every SEO review rather than treating them as an engineering concern.

Measure on **field data** from real users where available, not only lab tools. Lab scores on a fast
connection routinely miss what mobile users experience.

The three that matter:

- **Loading** — how long until the largest visible element renders. Usually fixed by image sizing
  and format, render-blocking resources, and slow server response.
- **Interaction responsiveness** — how long the page takes to react to a tap or click. Usually
  fixed by reducing main-thread JavaScript work.
- **Layout stability** — how much content shifts while loading. Almost always fixed by reserving
  space for images, ads, and embeds before they load.

Mobile is the version that gets indexed. Check that mobile serves the same content as desktop —
content hidden or dropped on mobile is content that does not exist for ranking — and that tap
targets, font sizes, and viewport configuration do not make the page unusable.

Prioritize performance work by pages with traffic, not by worst score. A terrible score on a page
nobody visits is not a finding.

## Structured data

Mark up what genuinely exists on the page — the entity, its attributes, the relationships. It
clarifies meaning to the crawler and can earn richer results.

Use JSON-LD in the page head rather than inline microdata — it is easier to maintain and validate,
and it does not entangle markup with content.

The types worth implementing, in rough order of return: organization and site identity, breadcrumbs,
articles, products with offers and availability, frequently asked questions, events, local business
details, and job postings. Implement the properties each type actually requires plus the recommended
ones you can populate honestly; partial markup with missing required fields is usually ignored
entirely.

Validate after every template change. Structured data breaks silently when a template is edited, and
nothing tells you.

Never mark up content that is not visible on the page, and never mark up ratings, prices, or events
that are not real. Both are policy violations with penalties attached.

## Prioritizing

Rank fixes by traffic at risk against effort. In practice the order is almost always: indexation
problems, then intent mismatch on high-value pages, then internal linking, then structured data,
then everything else.

## Never

- Chase rankings for a term the page cannot satisfy. The click arrives, bounces, and teaches the engine the page was wrong.
- Restructure a site without a redirect map. Lost link equity does not come back on its own.
- Judge a change in the first fortnight. Search feedback is slow enough that early movement is usually noise.

## Return contract

Findings by severity with the evidence for each, the sequenced fix list, expected impact and when it
should be visible, and what you are choosing not to fix.
