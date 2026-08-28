#!/usr/bin/env python3
"""All content here is original. Fail if third-party licence text or upstream names reappear."""
import glob, os, re, sys

PATTERNS = [
    r"\bMIT License\b",
    r"Permission is hereby granted",
    r"Copyright \(c\)",
    r"\bSPDX-License-Identifier\b",
    r"\bSIL Open Font License\b",
]
BANNED_FILES = ("licence", "license", "ofl", ".ttf", ".otf", ".woff")

problems = []
for path in glob.glob("**/*", recursive=True):
    if not os.path.isfile(path) or path.startswith(".git/"):
        continue
    if os.path.abspath(path) == os.path.abspath(__file__):
        continue  # this file necessarily contains the patterns it searches for
    if any(token in os.path.basename(path).lower() for token in BANNED_FILES):
        problems.append(f"{path}: third-party licence or font asset")
        continue
    if os.path.splitext(path)[1] not in (".md", ".json", ".mjs", ".py", ".yml"):
        continue
    text = open(path, encoding="utf-8", errors="replace").read()
    for pattern in PATTERNS:
        if re.search(pattern, text):
            problems.append(f"{path}: matches {pattern!r}")

for problem in problems:
    print(f"  {problem}")
print(f"provenance: {len(problems)} problems")
sys.exit(1 if problems else 0)
