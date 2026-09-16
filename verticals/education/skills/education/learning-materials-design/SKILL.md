---
name: learning-materials-design
description: Designs worksheets, workbooks and practice material that actually teach — sequencing difficulty, managing cognitive load, writing instructions a child can follow unaided, and building answer keys that hold up. Use this to design or fix a worksheet or workbook, decide how much practice a skill needs, structure a page so it can be completed without an adult reading it aloud, or diagnose material that looks right and does not work.
---

# Learning materials design

Most bad worksheets are not wrong. They are unusable: the instruction assumes a reading level above
the skill being practiced, the page asks the student to hold three things in mind at once, or the
difficulty jumps in a place the author could not see because the author already knows the answer.

## The instruction is the hardest part of the page

A worksheet is used by a child, often without an adult reading it to them, and frequently by a
parent who did not see the lesson. The instruction has to survive that.

Two constraints that conflict and have to be resolved deliberately:

- **The instruction's reading level must sit below the skill being practiced.** A second-grade math
  page whose directions need third-grade reading is a reading test with numbers on it. The child who
  fails it may have no trouble with the math.
- **The instruction must be complete.** "Solve" does not say whether to show work, what form the
  answer takes, or what to do with the remainder.

Where the two cannot both be met, the answer is usually a worked example rather than more words. One
solved item at the top carries more instruction than a paragraph, and it is read.

## Cognitive load is the budget

Working memory is the scarce resource, and a page spends it on three things at once: the skill being
learned, the format it is presented in, and everything incidental — decoration, unfamiliar layout, a
font that makes a `9` look like a `g`.

Only the first is worth spending on. The practical consequences:

- **Change one thing at a time.** A page that introduces a new skill *and* a new answer format
  measures neither.
- **Keep the format stable across a section.** Familiarity with the layout is load the student stops
  paying after the first page, and resetting it is a cost with no return.
- **Decoration competes with content.** Illustration that carries meaning earns its space;
  illustration that fills it costs attention, most sharply for the students who have least to spare.

## Difficulty rises in steps somebody checked

The author knows the answer, which makes difficulty jumps invisible from the inside. The reliable
method is mechanical: list the sub-skills the final task requires, order them by dependency, and
confirm every item exercises only sub-skills already introduced.

Where practice sits in a sequence changes what it should look like:

1. **Acquisition** — heavily scaffolded, worked examples adjacent, immediate feedback possible.
   Errors here are information, so the page should make them visible rather than punish them.
2. **Fluency** — scaffolding removed, volume up, the same skill in the same form. This is the stage
   most commercial material skips, and the reason a student who "understands it" cannot do it in
   March.
3. **Generalization** — the skill in unfamiliar wrappers, mixed with earlier skills, in contexts the
   examples did not cover. This is where transfer is tested and where spaced review belongs.

Mixing stages on one page is common and usually a mistake: a generalization item among acquisition
items reads as unfair, and an acquisition item among fluency items reads as filler.

## The answer key is part of the product

An answer key that is wrong is worse than no key, because it is trusted. It is also where multiple
valid answers get discovered — the page that admits two readings, the drawing task with no
determinate result, the word problem whose units were never stated.

Build the key by solving the page cold, from the printed instruction, without reference to what was
intended. Every item that is ambiguous when solved that way is ambiguous to the student, and the fix
belongs on the page rather than in the key.

For anything open-ended, the key states what makes an answer acceptable rather than pretending there
is one answer. A parent needs that more than the child does.

## Print is a constraint, not a format

Material that will be printed or sold as a file has limits that a screen mockup hides: margin loss
on a home printer, greyscale rendering of a color-coded task, and the fact that nobody can zoom.

Design in black and white first and add color as reinforcement rather than as the carrier of
meaning. A task that requires distinguishing red from green fails in greyscale and fails for the
significant minority of readers who cannot make that distinction anyway.

`marketing:visual-content` covers the design craft; what is specific here is that the constraint is
a child's hand, a home printer and no adult present.

## Tooling

Layout for print material is a document problem before it is a design one. InDesign, Affinity
Publisher, Canva and similar all produce a usable page; what determines whether a hundred-page
workbook stays maintainable is whether the layout is driven by styles and templates rather than
placed by hand, because the correction always arrives after page sixty.

Generated material — the same task shape across many values — is worth scripting rather than
copying. A script that emits items from a parameter set makes the difficulty sequence explicit and
regenerable, and it is the only way a mistake in item construction gets fixed once rather than
eighty times.

For anything sold, keep the source and the output separate and treat the PDF as a build artifact.
The alternative is a product nobody can correct.

## Sources

`references/sources.md` in this skill lists the outside authorities that settle the questions
here — what each one is authoritative for, and what you may do with it. Check them before
answering on anything they cover, and cite what you used. Most are free to read and not free
to reproduce; the use note on each is binding.

## Never

- Write an instruction that reads above the level of the skill being practiced.
- Introduce a new skill and a new answer format on the same page.
- Build the answer key from what you intended rather than from what the page says.
- Carry meaning in color alone.
- Ship a difficulty sequence nobody walked through from the student's side.
