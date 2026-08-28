#!/usr/bin/env python3
"""Every SKILL.md must have a name matching its directory, and a usable description."""
import glob, os, re, sys, collections

problems, names = [], collections.defaultdict(list)
for path in sorted(glob.glob("plugins/*/skills/*/SKILL.md")):
    directory = os.path.basename(os.path.dirname(path))
    text = open(path, encoding="utf-8").read()
    front = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not front:
        problems.append(f"{path}: no frontmatter")
        continue
    name = re.search(r"^name:\s*(.+)$", front.group(1), re.M)
    desc = re.search(r"^description:\s*(.+)$", front.group(1), re.M)
    if not name or not desc:
        problems.append(f"{path}: missing name or description")
        continue
    name = name.group(1).strip()
    if name != directory:
        problems.append(f"{path}: name {name!r} != directory {directory!r}")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        problems.append(f"{path}: {name!r} is not lowercase-hyphenated")
    if len(desc.group(1).strip()) < 80:
        problems.append(f"{path}: description too thin to trigger reliably")
    names[name].append(path)

for name, paths in names.items():
    if len(paths) > 1:
        problems.append(f"duplicate skill name {name!r}: {', '.join(paths)}")

for problem in problems:
    print(f"  {problem}")
print(f"{len(names)} skills checked, {len(problems)} problems")
sys.exit(1 if problems else 0)
