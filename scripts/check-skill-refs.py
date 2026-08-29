#!/usr/bin/env python3
"""Verify that every `department:skill` reference in the documentation resolves.

Prose naming specific skills rots as skills are renamed or consolidated — and this repository
has already consolidated once, losing six capabilities in the process. A reference to a skill
that no longer exists is a broken promise to a reader, and nothing else in the tree catches it.

Only tokens whose prefix is a real department directory are checked, so ordinary prose with a
colon in it is ignored rather than guessed at.
"""
import glob
import os
import re
import sys

DOCS = ["README.md", "CONTRIBUTING.md"] + sorted(glob.glob("docs/**/*.md", recursive=True))
# `dept:skill` inside backticks — the convention this repository uses for addressing a skill.
REF = re.compile(r"`([a-z][a-z0-9-]*):([a-z][a-z0-9-]*)`")


def main():
    departments = {
        os.path.basename(os.path.dirname(os.path.dirname(m)))
        for m in glob.glob("plugins/*/.claude-plugin/plugin.json")
    }
    if not departments:
        print("  no departments found — run from the repository root")
        return 1

    problems = []
    checked = 0
    for path in DOCS:
        if not os.path.exists(path):
            continue
        for n, line in enumerate(open(path, encoding="utf-8"), 1):
            for dept, skill in REF.findall(line):
                if dept not in departments:
                    continue  # not a skill reference, just prose with a colon
                checked += 1
                if not os.path.exists(f"plugins/{dept}/skills/{skill}/SKILL.md"):
                    problems.append(f"{path}:{n}: `{dept}:{skill}` does not exist")

    for p in problems:
        print(f"  {p}")
    print(f"skill references: {checked} checked, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
