#!/usr/bin/env bash
# Every check CI runs, runnable locally. CI calls this too, so the two cannot drift.
set -uo pipefail
cd "$(dirname "$0")/.."

fail=0

# The surface guard reads `git ls-files`, so a new file that has not been staged is invisible to
# it and the check passes locally then fails in CI. Warn rather than guess.
untracked=$(git ls-files --others --exclude-standard 2>/dev/null | head -5)
if [ -n "$untracked" ]; then
  printf '\033[33mwarning: untracked files are not seen by the surface check — stage them first:\033[0m\n'
  printf '%s\n' "$untracked" | sed 's/^/  /'
fi
run() {
  printf '\n\033[1m%s\033[0m\n' "$1"; shift
  if "$@"; then :; else fail=1; printf '  FAILED\n'; fi
}

run "Surface map is coherent" \
  node plugins/executive/skills/agent-hierarchy/scripts/agent-guard.mjs check
run "Skill frontmatter is valid" \
  python3 scripts/validate-skills.py
run "No third-party licence text" \
  python3 scripts/check-provenance.py
run "README is current" \
  python3 scripts/build-readme.py --check
run "Social card is current" \
  python3 scripts/build-social-card.py --check
run "Manifests parse" \
  python3 -c "
import json,glob,sys
bad=[]
for f in ['.claude-plugin/marketplace.json']+glob.glob('plugins/*/.claude-plugin/plugin.json'):
    try: json.load(open(f))
    except Exception as e: bad.append(f'{f}: {e}')
for b in bad: print(' ',b)
print(f'manifests: {len(bad)} problems')
sys.exit(1 if bad else 0)
"

printf '\n'
if [ "$fail" -eq 0 ]; then printf '\033[32mAll checks passed.\033[0m\n'; else printf '\033[31mChecks failed.\033[0m\n'; fi
exit "$fail"
