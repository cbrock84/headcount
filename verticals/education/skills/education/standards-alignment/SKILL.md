---
name: standards-alignment
description: Aligns learning material to the standard it claims — choosing the right framework for the grade and subject, citing standards by code rather than reproducing their text, and telling a real alignment from a decorative one. Use this to align a worksheet, lesson or workbook to Common Core, NGSS or a state framework, to check an alignment claim before publishing, or to decide what may lawfully be printed on the cover.
---

# Standards alignment

An alignment claim is a promise to a buyer who cannot verify it quickly. Most published alignment is
decorative — a code printed in a corner, chosen after the worksheet was written, that the task does
not actually assess. It survives because nobody checks, until a district curriculum reviewer does.

## Align to the verb, not the topic

A standard is written as a performance: what the student does, to what, under what conditions. The
topic is the least specific part of it and the part most alignment stops at.

`3.NF.A.1` is about fractions. It is specifically about *understanding a fraction as a quantity
formed by parts of a whole* — so a page of shaded-circle identification aligns, and a page of
fraction addition drills does not, however much both are "fractions in third grade."

The test to apply before printing a code: **could a student complete this task correctly without
doing what the standard describes?** If yes, the alignment is decorative. A word problem solvable by
guessing from the answer format assesses test-taking, and it is aligned to nothing.

## Know which framework applies

Grade and subject do not determine the framework on their own, and the mismatch is a common source
of wrong claims:

- **Common Core** covers mathematics and English language arts, K-12. It is adopted by most but not
  all states, and several adopting states have renamed and amended it — a "Common Core aligned"
  claim in a state that rewrote it is at best imprecise.
- **NGSS** covers science, and is organized as performance expectations that bundle a practice, a
  core idea and a crosscutting concept. Aligning to the disciplinary content alone misses two
  thirds of what the expectation asks for.
- **C3** covers social studies, and is an inquiry arc rather than a content list. It does not
  enumerate facts, so "aligned to C3" is a claim about the shape of the task, not its subject.
- **Pre-K has no Common Core.** Nothing below kindergarten is covered, and an alignment claim there
  is either to a state early learning standard, to Head Start's framework, or to nothing. Treat
  pre-K as its own problem — `education:early-childhood-practice` holds it.

State standards exist alongside all of these, and for a product sold into one state they are the
binding set. `education:learning-materials-design` covers what changes when the material is for a
named district rather than a general market.

## Cite the code, never the text

This is where alignment becomes a legal question rather than an editorial one, and the distinction
is sharper than most publishers treat it.

**Citing a standard by its code is not reproduction.** `4-PS3-2`, `RL.5.2`, `2.MD.C.7` are
identifiers. Using them to say what a page addresses is normal, expected, and safe.

**Reproducing the standard's wording is a different act**, and whether it is permitted depends on
the publisher:

- Common Core carries a public license that permits use **with its required attribution notice**.
  It is not public domain, and dropping the notice is the common failure.
- NGSS is copyrighted, and "Next Generation Science Standards" is a registered trademark — which
  constrains the alignment claim itself, not only the text.
- State frameworks vary. Many are state government works and freely usable; some are licensed from
  a vendor and are not.

Paraphrasing to avoid the question does not avoid it, and a paraphrase that stays close enough to be
useful is close enough to be a derivative. Write your own learning objective in your own words, and
cite the code beside it. That is both safer and clearer to a teacher.

`references/sources.md` carries the publisher and license class for each framework.

## An alignment document is the deliverable

For anything sold to a school, the alignment is an artifact, not an annotation. It lists, per page
or per lesson: the code, the text of *your* objective, the task that provides evidence, and where a
reviewer would look to verify it.

Building it after the material is written is what produces decorative alignment. Building it first
makes it a specification: each row is a task somebody then has to write.

## Tooling

Standards data is available as structured identifiers more often than publishers realize. Common
Core and NGSS codes are stable and enumerable, and a spreadsheet keyed on them beats prose in a
document — it makes coverage gaps visible, which is the question a reviewer asks first.

Curriculum mapping tools — Chalk, Atlas, Eduplanet21, Kiddom and similar — hold the alignment
document and the sequence together, and earn their place once the same material is sold into
several states with different frameworks. Below that, a maintained spreadsheet with one row per
standard and one column per unit is the same artifact without the subscription.

Whatever holds it, keep the standard's code and your objective in separate fields. Merging them is
how the standard's wording ends up in the product.

## Sources

`references/sources.md` in this skill lists the outside authorities that settle the questions
here — what each one is authoritative for, and what you may do with it. Check them before
answering on anything they cover, and cite what you used. Most are free to read and not free
to reproduce; the use note on each is binding.

## Never

- Print a standard code chosen after the task was written.
- Claim alignment to a framework the state in question does not use.
- Reproduce a standard's wording without the license notice its publisher requires.
- Align to the topic in the standard and ignore the performance it describes.
- Claim Common Core alignment for anything below kindergarten.
