#!/usr/bin/env node
/**
 * agent-guard — the executable half of the agent/subagent hierarchy.
 *
 * Two guards in one file, because prose rules do not execute. A surface map written
 * in Markdown and never checked is a suggestion; checked on every PR it is a control.
 *
 *   node agent-guard.mjs check          Is the map coherent?
 *   node agent-guard.mjs diff <agent>   Did this diff obey it?
 *
 * They are not redundant, and you need both. `check` proves no two agents claim the
 * same path and no path is unowned. It cannot prove a change respected the map — once
 * the work is committed by the orchestrator, the information about which agent authored
 * which hunk is gone. `diff` runs while that authorship is still known.
 *
 * No dependencies. Node 18+. Drop it anywhere and wire two scripts.
 */

import { execFileSync } from 'node:child_process';
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

/* ── Configure these three for your repo ──────────────────────────────────── */
const MAP_FILE = process.env.AGENT_MAP ?? 'docs/AGENT-SURFACES.md';
const AGENT_DIR = process.env.AGENT_DIR ?? '.claude/agents';
const DECISION_LOG = process.env.AGENT_DECISIONS ?? 'docs/DECISION-LOG.md';

/** The orchestrator is not an agent. It owns the context artifacts and commits everything. */
const ORCHESTRATOR = 'orchestrator';

/* ── Glob → RegExp ────────────────────────────────────────────────────────────
 * Hand-rolled on purpose. A matcher dependency here buys four metacharacters and
 * costs you a supply-chain review on the one file whose job is enforcing rules.
 *
 *   **\/   any number of leading segments, including none
 *   /**    this directory and everything below it
 *   *      any run of characters inside one segment; never crosses `/`
 *   ?      exactly one character inside one segment
 */
export function globToRegExp(glob) {
  let re = '';
  for (let i = 0; i < glob.length; i++) {
    const c = glob[i];
    if (c === '*') {
      if (glob[i + 1] === '*') {
        if (glob[i + 2] === '/') {
          re += '(?:[^/]*/)*';
          i += 2;
        } else if (glob[i - 1] === '/') {
          re = re.slice(0, -1) + '(?:/.*)?';
          i += 1;
        } else {
          re += '.*';
          i += 1;
        }
      } else {
        re += '[^/]*';
      }
    } else if (c === '?') {
      re += '[^/]';
    } else {
      re += c.replace(/[.+^${}()|[\]\\]/g, '\\$&');
    }
  }
  return new RegExp(`^${re}$`);
}

/** Owned when some pattern matches and no LATER `!pattern` un-matches. Order is meaningful. */
function claims(owner, file) {
  let owned = false;
  for (const p of owner.patterns) {
    if (!p.re.test(file)) continue;
    owned = !p.negated;
    p.hits++;
  }
  return owned;
}

const ownersOf = (owners, file) => owners.filter((o) => claims(o, file)).map((o) => o.id);

/* ── Parse the map ────────────────────────────────────────────────────────────
 * Two fenced-block kinds inside an ordinary Markdown file, so the map stays readable
 * as documentation and parseable as config. One file, not two that can disagree.
 *
 *   ```roster              <id> <builder|reviewer> <installed|planned>
 *   ```surface:<id>        one glob per line; `!` prefix excludes
 */
function fencedBlocks(src) {
  const out = [];
  for (const m of src.matchAll(/^```([^\n`]*)\n([\s\S]*?)^```$/gm)) {
    out.push({ info: (m[1] ?? '').trim(), body: m[2] ?? '' });
  }
  return out;
}

const significant = (body) =>
  body.split('\n').map((l) => l.trim()).filter((l) => l && !l.startsWith('#'));

export function parseSurfaceMap(src) {
  const roster = [];
  const owners = [];
  const errors = [];
  const seenSurface = new Set();

  for (const { info, body } of fencedBlocks(src)) {
    if (info === 'roster') {
      for (const line of significant(body)) {
        const [id, klass, status] = line.split(/\s+/);
        if (!id || !klass || !status) { errors.push(`roster: cannot parse "${line}"`); continue; }
        if (klass !== 'builder' && klass !== 'reviewer') { errors.push(`roster: ${id} has unknown class "${klass}"`); continue; }
        if (status !== 'installed' && status !== 'planned') { errors.push(`roster: ${id} has unknown status "${status}"`); continue; }
        if (roster.some((r) => r.id === id)) { errors.push(`roster: ${id} listed twice`); continue; }
        roster.push({ id, klass, status });
      }
    } else if (info.startsWith('surface:')) {
      const id = info.slice('surface:'.length).trim();
      if (seenSurface.has(id)) { errors.push(`surface: ${id} declared twice`); continue; }
      seenSurface.add(id);
      const patterns = significant(body).map((raw) => {
        const negated = raw.startsWith('!');
        const glob = negated ? raw.slice(1) : raw;
        return { glob, negated, re: globToRegExp(glob), hits: 0 };
      });
      owners.push({ id, patterns });
    }
  }
  return { roster, owners, errors };
}

const trackedFiles = () =>
  execFileSync('git', ['ls-files'], { encoding: 'utf8' }).split('\n').filter(Boolean);

function readMap(root = '.') {
  const path = join(root, MAP_FILE);
  if (!existsSync(path)) {
    console.error(`agent-guard: no map at ${MAP_FILE}. Write the map before the charters.`);
    process.exit(2);
  }
  return parseSurfaceMap(readFileSync(path, 'utf8'));
}

const charterIds = () =>
  existsSync(AGENT_DIR)
    ? readdirSync(AGENT_DIR).filter((f) => f.endsWith('.md')).map((f) => f.replace(/\.md$/, ''))
    : [];

/* ── check ──────────────────────────────────────────────────────────────────── */
function check() {
  const { roster, owners, errors } = readMap();
  const problems = [...errors];
  const notes = [];

  // 1. Every tracked file has EXACTLY ONE owner.
  //    Two owners is a future conflict: two agents, dispatched weeks apart, both
  //    correctly believing the path is theirs. Zero owners is worse — whoever touches
  //    it first becomes its de-facto owner and nobody decided that.
  const overlaps = new Map();
  const unowned = [];
  for (const file of trackedFiles()) {
    const os = ownersOf(owners, file);
    if (os.length === 0) unowned.push(file);
    else if (os.length > 1) {
      const key = os.sort().join(' + ');
      if (!overlaps.has(key)) overlaps.set(key, []);
      overlaps.get(key).push(file);
    }
  }
  for (const [pair, files] of overlaps) {
    problems.push(`overlap: ${pair} both claim ${files.length} path(s), e.g. ${files.slice(0, 3).join(', ')}`);
  }
  if (unowned.length) {
    problems.push(`unowned: ${unowned.length} tracked path(s) belong to nobody, e.g. ${unowned.slice(0, 5).join(', ')}`);
  }

  // 2. Roster and charters agree in BOTH directions.
  //    A charter with no map row can write anywhere. A row marked `planned` whose
  //    charter has landed is a lie about what is dispatchable.
  const charters = charterIds();
  const known = new Set([...roster.map((r) => r.id), ORCHESTRATOR]);
  for (const id of charters) {
    if (!known.has(id)) problems.push(`charter ${id}.md has no roster row`);
    const row = roster.find((r) => r.id === id);
    if (row && row.status === 'planned') problems.push(`${id} is marked planned but its charter exists`);
  }
  for (const r of roster) {
    if (r.status === 'installed' && !charters.includes(r.id)) {
      problems.push(`${r.id} is marked installed but ${AGENT_DIR}/${r.id}.md does not exist`);
    }
  }

  // 3. A reviewer holds NO write surface. Read-only has to be structural, not a promise
  //    made in prose inside the charter it would be violating.
  for (const r of roster.filter((x) => x.klass === 'reviewer')) {
    const o = owners.find((x) => x.id === r.id);
    if (o && o.patterns.some((p) => !p.negated)) {
      problems.push(`reviewer ${r.id} declares a write surface — reviewers are read-only`);
    }
  }

  // 4. Decision numbers are unique. Two concurrent sessions both claiming D14 merges
  //    cleanly in git and fails nothing, which is exactly why it needs a guard and not
  //    a convention.
  if (existsSync(DECISION_LOG)) {
    const nums = [...readFileSync(DECISION_LOG, 'utf8').matchAll(/^#{1,6}\s+D(\d+)\b/gm)].map((m) => m[1]);
    const dupes = nums.filter((n, i) => nums.indexOf(n) !== i);
    if (dupes.length) problems.push(`decision log: duplicate number(s) D${[...new Set(dupes)].join(', D')}`);
    notes.push(`decision log: ${nums.length} numbered entries, highest D${Math.max(...nums.map(Number), 0)}`);
  }

  // A pattern matching nothing is usually a rename left behind. A NOTE, not a failure —
  // declaring a surface before the directory exists is legitimate.
  for (const o of owners) {
    for (const p of o.patterns) {
      if (p.hits === 0) notes.push(`pattern matches no tracked file (reserved or stale): ${o.id}:${p.negated ? '!' : ''}${p.glob}`);
    }
  }

  const builders = roster.filter((r) => r.klass === 'builder').length;
  const reviewers = roster.filter((r) => r.klass === 'reviewer').length;
  for (const n of notes) console.log(`  ok  ${n}`);
  console.log(`  ok  Roster: ${builders} builder(s), ${reviewers} reviewer(s), ${charters.length} charter file(s).`);

  if (problems.length) {
    console.error(`\nAgent surfaces FAILED — ${problems.length} problem(s):`);
    for (const p of problems) console.error(`  ✗ ${p}`);
    process.exit(1);
  }
  console.log('\nAgent surfaces passed.');
}

/* ── diff ───────────────────────────────────────────────────────────────────── */
function changedPaths(base) {
  if (base) {
    return execFileSync('git', ['diff', '--name-only', `${base}...HEAD`], { encoding: 'utf8' })
      .split('\n').filter(Boolean);
  }
  // Default: the working tree, because a builder has not committed. That is the point
  // at which this is worth running.
  const porcelain = execFileSync('git', ['status', '--porcelain'], { encoding: 'utf8' });
  return porcelain.split('\n').filter(Boolean).map((l) => l.slice(3).split(' -> ').pop().trim());
}

function diff(agentId, base) {
  const { roster, owners } = readMap();
  const row = roster.find((r) => r.id === agentId);
  if (!row) {
    console.error(`agent-guard: "${agentId}" is not in the roster.`);
    process.exit(2);
  }
  if (agentId === ORCHESTRATOR) {
    console.error('agent-guard: the orchestrator is not an agent — it legitimately spans surfaces. Nothing to check.');
    process.exit(2);
  }

  const files = changedPaths(base);
  if (files.length === 0) { console.log('  ok  no changed paths.'); return; }

  const mine = owners.find((o) => o.id === agentId) ?? { id: agentId, patterns: [] };
  const violations = new Map();
  for (const f of files) {
    if (row.klass === 'builder' && claims(mine, f)) continue;
    // Group by who ACTUALLY owns it — that grouping is the handoff routing information.
    const real = ownersOf(owners, f);
    const key = real.length ? real.join(' + ') : '(unowned)';
    if (!violations.has(key)) violations.set(key, []);
    violations.get(key).push(f);
  }

  if (violations.size === 0) {
    console.log(`  ok  ${files.length} changed path(s), all inside ${agentId}'s surface.`);
    return;
  }
  console.error(`\nagents:diff FAILED — ${agentId} changed path(s) outside its surface:`);
  if (row.klass === 'reviewer') {
    console.error('  (this is a REVIEWER. It holds no write surface, so every changed path is a violation.)');
  }
  for (const [owner, fs] of violations) {
    console.error(`\n  → belongs to ${owner} — HANDOFF:`);
    for (const f of fs) console.error(`      ${f}`);
  }
  process.exit(1);
}

/* ── main ───────────────────────────────────────────────────────────────────── */
const [mode, ...rest] = process.argv.slice(2);
const baseIdx = rest.indexOf('--base');
const base = baseIdx === -1 ? null : rest[baseIdx + 1];
if (mode === 'check') check();
else if (mode === 'diff') diff(rest[0], base);
else {
  console.error('usage: agent-guard.mjs check | diff <agent-id> [--base <ref>]');
  process.exit(2);
}
