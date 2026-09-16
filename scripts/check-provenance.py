#!/usr/bin/env python3
"""All content here is original. This is a heuristic backstop, not proof: it catches the common
shapes of third-party license text and vendored assets. It cannot detect prose copied without a
notice, so it supplements review rather than replacing it."""
import fnmatch, glob, os, re, sys

# Markers for the licenses most likely to arrive with vendored material.
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
LICENSE_NAMES = re.compile(
    r"^(licen[cs]e|copying|notice|patents|authors|ofl)(\..*)?$|licen[cs]e", re.I
)
# Binary assets that are always third-party when present.
ASSET_EXTS = (".ttf", ".otf", ".woff", ".woff2", ".eot")

OWN_LICENSE = "LICENSE"  # ours, and the only one expected

# Naming our own license in our own documentation is expected and is not evidence of vendored
# material: the decision log records why MIT was chosen, and the other two tell contributors what
# they are agreeing to. Only the "MIT License" marker is waived, and only in these files — every
# other pattern still applies, so an actually pasted license is still caught by its body text
# ("Permission is hereby granted", "Copyright (c)"), which no real license lacks.
#
# This exemption exists because the check was previously passing these files by accident: they
# spelled the word the British way, which this American-spelled pattern never matched. Converting
# the prose to US English exposed the gap rather than creating it.
OWN_LICENSE_MENTION = {"CONTRIBUTING.md", "README.md", "docs/DECISION-LOG.md"}
OWN_LICENSE_PATTERN = r"\bMIT License\b"

# The source catalog classifies outside material by its license, so naming license families is its
# job rather than evidence of carrying any. The waiver is for the family *names* only, in the files
# that document the vocabulary and the agent that maintains it — every other pattern still applies,
# so actual license text remains caught by its body ("Permission is hereby granted", "Copyright
# (c)", "Redistribution and use..."), which no real license lacks. This is the same reasoning as the
# MIT waiver above: a name is a reference, a body is a copy.
#
# This originally excluded the catalog files themselves, on the reasoning that entries carry a short
# slug (`cc-by-sa`) and never a family's prose name. That stopped being true the moment a license
# became a *source*: a font license is the authority on whether a typeface may be embedded, so its
# title is the family name. The waiver now covers the catalog and what is generated from it.
LICENSE_FAMILY_MENTION_GLOBS = (
    "sources/*.toml",
    "sources/README.md",
    ".claude/agents/sources.md",
    "docs/SOURCES.md",
    "plugins/*/skills/*/references/sources.md",
)
LICENSE_FAMILY_PATTERNS = {r"\bCreative Commons Attribution\b", r"\bMIT License\b",
                           r"\bApache License\b", r"\bBSD \d-Clause\b",
                           r"\bMozilla Public License\b", r"\bSIL Open Font License\b"}

# Generated output and build byproducts are not this repository's content. `dist/` in particular
# is a copy of the tree already being checked, so scanning it doubles every finding.
SKIP_DIRS = (".git/", "dist/", "__pycache__/")


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
    if path == OWN_LICENSE:
        continue

    name = os.path.basename(path)
    if name.lower().endswith(ASSET_EXTS):
        problems.append(f"{path}: third-party font asset")
        continue
    if LICENSE_NAMES.match(name):
        problems.append(f"{path}: third-party license or notice file")
        continue

    # Every text file, whatever its extension — an extension allowlist is how a .txt slips past.
    if not is_probably_text(path):
        continue
    text = open(path, encoding="utf-8", errors="replace").read()
    waived = {OWN_LICENSE_PATTERN} if path in OWN_LICENSE_MENTION else set()
    if any(fnmatch.fnmatch(path.replace(os.sep, "/").lstrip("./"), g)
           for g in LICENSE_FAMILY_MENTION_GLOBS):
        waived |= LICENSE_FAMILY_PATTERNS
    for pattern in PATTERNS:
        if pattern in waived:
            continue
        if re.search(pattern, text):
            problems.append(f"{path}: matches {pattern!r}")
            break

for problem in problems:
    print(f"  {problem}")
print(f"provenance: {len(problems)} problems")
sys.exit(1 if problems else 0)
