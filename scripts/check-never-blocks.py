#!/usr/bin/env python3
"""Verify that each `## Never` block is internally consistent in its bullet punctuation.

This catches a specific authoring accident. When a second list of rules is spliced into an
existing `## Never` block, the splice can land in the middle of a wrapped bullet and orphan
its continuation line onto an unrelated rule. Four skills shipped that way, and a fifth
carried the same off-style appendage without the orphaning. Nothing in the tree saw it.

The tell is not "a bullet without a full stop" — two styles are in use across the repository
and both are deliberate: most blocks are bare imperatives ending in a period, while the
chief-level blocks are `Never …` / `Do not …` lines without terminal punctuation. Either is
fine. What is never fine is *both inside one block*, because that is what a splice from
somewhere else looks like. Checking consistency rather than a single house style is what
makes this precise: on the tree as it stood it flagged all five affected files and nothing
else, where a flat terminal-punctuation rule produced fifty-nine hits, mostly style.

Wrapped bullets are joined before the check, so a continuation line is judged as part of the
bullet it belongs to rather than as a bullet of its own.
"""
import glob
import re
import sys

# A period, question mark or exclamation, optionally inside a closing quote or bracket.
TERMINAL = re.compile(r'[.!?]["”)]?$')


def logical_bullets(lines):
    """Bullets with their wrapped continuation lines folded back in."""
    bullets = []
    for line in lines:
        if line.startswith("- "):
            bullets.append(line[2:].strip())
        elif re.match(r"^\s+\S", line) and bullets:
            bullets[-1] += " " + line.strip()
    return bullets


def never_blocks(path):
    """Every `## Never` block in a file, as a list of its raw lines."""
    blocks, block, inside = [], [], False
    for line in open(path, encoding="utf-8").read().split("\n"):
        if line.startswith("## Never"):
            inside, block = True, []
            continue
        if inside and line.startswith("## "):
            blocks.append(block)
            inside = False
            continue
        if inside:
            block.append(line)
    if inside:
        blocks.append(block)
    return blocks


def main():
    problems = []
    checked = 0
    for path in sorted(glob.glob("plugins/**/SKILL.md", recursive=True)):
        for block in never_blocks(path):
            bullets = logical_bullets(block)
            if not bullets:
                continue
            checked += 1
            closed = [b for b in bullets if TERMINAL.search(b)]
            open_ = [b for b in bullets if not TERMINAL.search(b)]
            if closed and open_:
                minority = open_ if len(open_) <= len(closed) else closed
                problems.append(
                    f"{path}: `## Never` mixes {len(closed)} bullet(s) ending in punctuation "
                    f"with {len(open_)} that do not — usually a list spliced in from elsewhere"
                )
                for b in minority:
                    problems.append(f"    odd one out: {b[:88]}")

    for p in problems:
        print(f"  {p}")
    inconsistent = sum(1 for p in problems if not p.startswith("    "))
    print(f"never blocks: {checked} checked, {inconsistent} inconsistent")
    return 1 if inconsistent else 0


if __name__ == "__main__":
    sys.exit(main())
