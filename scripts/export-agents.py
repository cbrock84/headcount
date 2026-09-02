#!/usr/bin/env python3
"""Export headcount skills into a target project's `.agents/skills` directory.

Allows selective or full export of skills for Antigravity and Codex.

Examples:
  python scripts/export-agents.py --target "C:\\path\\to\\my-project"
  python scripts/export-agents.py --target "C:\\path\\to\\my-project" --departments technology security
  python scripts/export-agents.py --target "C:\\path\\to\\my-project" --skills code-review threat-modeling
"""
import argparse
import glob
import os
import shutil
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    parser = argparse.ArgumentParser(
        description="Export headcount skills to a target project's .agents directory."
    )
    parser.add_argument(
        "--target",
        required=True,
        help="Path to the target project root (where .agents will be created).",
    )
    parser.add_argument(
        "--departments",
        nargs="*",
        default=[],
        help="Specific department names to export (e.g. technology security).",
    )
    parser.add_argument(
        "--skills",
        nargs="*",
        default=[],
        help="Specific skill names to export (e.g. code-review threat-modeling).",
    )

    args = parser.parse_args()
    os.chdir(REPO_ROOT)

    target_root = os.path.abspath(args.target)
    target_skills_dir = os.path.join(target_root, ".agents", "skills")
    os.makedirs(target_skills_dir, exist_ok=True)

    skill_mds = sorted(glob.glob("plugins/*/skills/*/SKILL.md"))
    selected_skills = []

    dept_filter = set(args.departments) if args.departments else None
    skill_filter = set(args.skills) if args.skills else None

    for skill_md in skill_mds:
        # e.g., plugins/technology/skills/code-review/SKILL.md
        parts = os.path.normpath(skill_md).split(os.sep)
        dept = parts[1]
        skill_name = parts[3]

        if dept_filter and dept not in dept_filter:
            continue
        if skill_filter and skill_name not in skill_filter:
            continue

        selected_skills.append((os.path.dirname(skill_md), skill_name, dept))

    if not selected_skills:
        print("export-agents: no matching skills found for the given criteria.")
        return 1

    for src_dir, skill_name, _ in selected_skills:
        dst_dir = os.path.join(target_skills_dir, skill_name)
        if os.path.exists(dst_dir):
            shutil.rmtree(dst_dir)
        shutil.copytree(src_dir, dst_dir)

    print(
        f"export-agents: successfully exported {len(selected_skills)} skill(s) to {target_skills_dir}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
