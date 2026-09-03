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

/* ── Authority ────────────────────────────────────────────────────────────────
 * The surface map answers *where* an agent may write. It has never answered whether
 * that write may land without a human seeing it, so in practice that was decided per
 * dispatch, from memory, by whoever was driving. Authority is the second axis, stated
 * once in the map and checked like everything else.
 *
 *   autonomous  dispatch it and take the result; the surface is the only gate needed
 *   proposes    it may do the work, but the orchestrator surfaces the diff before landing
 *   escalates   do not dispatch it without being asked to; the work itself is the decision
 *
 * Rows may omit the column. Omission means `autonomous` — the behavior every existing map
 * already had — and is reported as a note so a map that never considered the question is
 * distinguishable from one that answered it.
 */
const AUTHORITY = ['autonomous', 'proposes', 'escalates'];
const DEFAULT_AUTHORITY = 'autonomous';

/** Gated rows are the ones whose output the orchestrator may not simply take. */
const isGated = (row) => row.authority !== 'autonomous';

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
 *   ```roster              <id> <builder|reviewer> <installed|planned> [authority]
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
        const cols = line.split(/\s+/);
        const [id, klass, status, authority] = cols;
        if (!id || !klass || !status) { errors.push(`roster: cannot parse "${line}"`); continue; }
        if (cols.length > 4) { errors.push(`roster: ${id} has ${cols.length} columns, expected at most 4 (id, class, status, authority)`); continue; }
        if (klass !== 'builder' && klass !== 'reviewer') { errors.push(`roster: ${id} has unknown class "${klass}"`); continue; }
        if (status !== 'installed' && status !== 'planned') { errors.push(`roster: ${id} has unknown status "${status}"`); continue; }
        if (authority !== undefined && !AUTHORITY.includes(authority)) {
          errors.push(`roster: ${id} has unknown authority "${authority}" — one of ${AUTHORITY.join(', ')}`);
          continue;
        }
        if (roster.some((r) => r.id === id)) { errors.push(`roster: ${id} listed twice`); continue; }
        roster.push({
          id,
          klass,
          status,
          authority: authority ?? DEFAULT_AUTHORITY,
          authorityStated: authority !== undefined,
        });
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

  // 4. Authority is coherent with the surface the row actually holds.
  //    A reviewer holds no write surface, so gating its writes gates nothing — and a row
  //    reading `security-review reviewer installed proposes` looks governed while being
  //    the one row that never needed governing. Same failure in the other direction: a
  //    builder marked `proposes` that owns no surface has a checkpoint on an empty set.
  for (const r of roster) {
    const owned = owners.find((x) => x.id === r.id);
    const writes = owned ? owned.patterns.some((p) => !p.negated) : false;
    if (r.klass === 'reviewer' && isGated(r)) {
      problems.push(`reviewer ${r.id} declares authority "${r.authority}" — reviewers hold no write surface, so there is nothing to gate`);
    }
    if (r.klass === 'builder' && isGated(r) && !writes) {
      problems.push(`${r.id} declares authority "${r.authority}" but holds no write surface — the gate governs nothing`);
    }
  }

  // A row that never stated an authority is not wrong, but it did not answer the question
  // either. Say so once, the same way a stale glob is said.
  const unstated = roster.filter((r) => !r.authorityStated).map((r) => r.id);
  if (unstated.length) {
    notes.push(`authority not stated on ${unstated.length} row(s), defaulting to ${DEFAULT_AUTHORITY}: ${unstated.join(', ')}`);
  }

  // 5. Decision numbers are unique. Two concurrent sessions both claiming D14 merges
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
  const gated = roster.filter(isGated);
  for (const n of notes) console.log(`  ok  ${n}`);
  console.log(`  ok  Roster: ${builders} builder(s), ${reviewers} reviewer(s), ${charters.length} charter file(s).`);
  console.log(gated.length
    ? `  ok  Authority: ${roster.length - gated.length} autonomous, ${gated.length} gated — ${gated.map((r) => `${r.id} (${r.authority})`).join(', ')}.`
    : `  ok  Authority: all ${roster.length} row(s) autonomous.`);

  if (problems.length) {
    console.error(`\nAgent surfaces FAILED — ${problems.length} problem(s):`);
    for (const p of problems) console.error(`  ✗ ${p}`);
    process.exit(1);
  }
  console.log('\nAgent surfaces passed.');
}

/* ── diff ───────────────────────────────────────────────────────────────────── */
function changedPaths(base) {
  // `-z` on both commands. Without it git wraps any path containing a space in literal quotes
  // and octal-escapes non-ASCII bytes, so `plugins/finance/skills/a b.md` arrives as
  // `"plugins/finance/skills/a b.md"` and fails the prefix test below — the guard then reports
  // no violation for a file squarely inside another agent's surface. NUL-delimited output is
  // the raw byte path, and it also removes the need to guess where a ` -> ` is a rename arrow
  // rather than part of a filename.
  if (base) {
    return execFileSync('git', ['diff', '--name-only', '-z', `${base}...HEAD`], { encoding: 'utf8' })
      .split('\0').filter(Boolean);
  }
  // Default: the working tree, because a builder has not committed. That is the point
  // at which this is worth running.
  const records = execFileSync('git', ['status', '--porcelain', '-z'], { encoding: 'utf8' })
    .split('\0').filter(Boolean);
  const paths = [];
  for (let i = 0; i < records.length; i += 1) {
    const status = records[i].slice(0, 2);
    paths.push(records[i].slice(3));
    // A rename or copy writes the destination in this record and the source in the next one.
    if (status.includes('R') || status.includes('C')) i += 1;
  }
  return paths;
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
    // Clean is not the same as landable. This is the only moment the distinction is
    // actionable, so it is said here rather than left to whoever remembers the map.
    if (isGated(row)) {
      console.log(`  !!  ${agentId} authority is "${row.authority}" — surface this diff for a decision before committing it.`);
    }
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
