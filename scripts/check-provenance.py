#!/usr/bin/env python3
"""All content here is original. This is a heuristic backstop, not proof: it catches the common
shapes of third-party licence text and vendored assets. It cannot detect prose copied without a
notice, so it supplements review rather than replacing it."""
import glob, os, re, sys

# Markers for the licences most likely to arrive with vendored material.
PATTERNS = [
    r"\bMIT License\b",
    r"\bApache License\b",
    r"\bGNU (?:GENERAL|LESSER|AFFERO)\b",
    r"\bBSD \d-Clause\b",
    r"\bMozilla Public License\b",
    r"\bSIL Open Font License\b",
    r"\bCreative Commons Attribution\b",
    r"Permission is hereby granted",
    r"Redistribution and use in source and binary forms",
    r"Copyright\s*(?:\(c\)|©)",
    r"\bSPDX-License-Identifier\b",
    r"\bAll rights reserved\b",
]

# Filenames that carry someone else's terms, whatever their extension.
LICENCE_NAMES = re.compile(
    r"^(licen[cs]e|copying|notice|patents|authors|ofl)(\..*)?$|licen[cs]e", re.I
)
# Binary assets that are always third-party when present.
ASSET_EXTS = (".ttf", ".otf", ".woff", ".woff2", ".eot")

OWN_LICENCE = "LICENSE"  # ours, and the only one expected
SKIP_DIRS = (".git/",)


def is_probably_text(path, sniff=4096):
    try:
        with open(path, "rb") as handle:
            chunk = handle.read(sniff)
    except OSError:
        return False
    if b"\0" in chunk:
        return False
    try:
        chunk.decode("utf-8")
    except UnicodeDecodeError:
        return False
    return True


problems = []
for path in glob.glob("**/*", recursive=True):
    if not os.path.isfile(path) or path.startswith(SKIP_DIRS):
        continue
    if os.path.abspath(path) == os.path.abspath(__file__):
        continue  # this file necessarily contains the patterns it searches for
    if path == OWN_LICENCE:
        continue

    name = os.path.basename(path)
    if name.lower().endswith(ASSET_EXTS):
        problems.append(f"{path}: third-party font asset")
        continue
    if LICENCE_NAMES.match(name):
        problems.append(f"{path}: third-party licence or notice file")
        continue

    # Every text file, whatever its extension — an extension allowlist is how a .txt slips past.
    if not is_probably_text(path):
        continue
    text = open(path, encoding="utf-8", errors="replace").read()
    for pattern in PATTERNS:
        if re.search(pattern, text):
            problems.append(f"{path}: matches {pattern!r}")
            break

for problem in problems:
    print(f"  {problem}")
print(f"provenance: {len(problems)} problems")
sys.exit(1 if problems else 0)
