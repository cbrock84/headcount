#!/usr/bin/env python3
"""Generate the interactive org chart at docs/org-chart.html.

Every department, skill, count and description comes from the tree, so the chart cannot claim an
organization the repository does not have. `--check` compares the committed file against freshly
generated output, the same contract as the README and the social card.

  python3 scripts/build-org-chart.py           regenerate, then render the README screenshots
  python3 scripts/build-org-chart.py --check   fail if stale (CI)
  python3 scripts/build-org-chart.py --html    regenerate HTML only, skip rendering

The screenshots are a light and a dark crop of this same page, embedded in the README inside a
<picture> element so GitHub serves whichever matches the reader's theme. They are rendered from
the generated HTML in the same run, so they cannot describe a different organization than it does.
Rendering needs Chromium; without it the HTML is still written.
"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys

OUT = "docs/org-chart.html"
SHOT_LIGHT = "docs/assets/org-chart-light.png"
SHOT_DARK = "docs/assets/org-chart-dark.png"
SHOT_W, SHOT_H = 1280, 1010  # hero crop: masthead through the first full row of departments
REPO = "cbrock84/headcount"
BLOB = f"https://github.com/{REPO}/blob/main"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# META and REVIEWER live in build-readme.py, which is not importable under that filename.
# Read them out of it rather than keeping a second copy that can disagree.
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build-readme.py"),
            encoding="utf-8").read()
META = eval(re.search(r"^META = (\{.*?^\})", _src, re.S | re.M).group(1))
REVIEWER = eval(re.search(r"^REVIEWER = (\{.*?\})", _src, re.M).group(1))


def first_sentence(desc, limit=150):
    """The description's opening claim, before the 'Use this to ...' trigger list."""
    cut = re.split(r"(?:\.\s+)(?:Also )?[Uu]se (?:this|it)\b", desc)[0].rstrip(" .,—-")
    if len(cut) < 40:
        cut = desc
    return cut[: limit - 1].rstrip() + "…" if len(cut) > limit else cut


def collect():
    depts = []
    for slug in sorted(
        (os.path.basename(os.path.dirname(os.path.dirname(m)))
         for m in glob.glob("plugins/*/.claude-plugin/plugin.json")),
        key=lambda d: META[d][0],
    ):
        skills = []
        for path in sorted(glob.glob(f"plugins/{slug}/skills/*/SKILL.md")):
            text = open(path, encoding="utf-8").read()
            front = re.match(r"^---\s*\n(.*?)\n---", text, re.S).group(1)
            desc = re.search(r"^description:\s*(.*)$", front, re.M).group(1).strip()
            name = os.path.basename(os.path.dirname(path))
            skills.append({
                "name": name,
                "summary": first_sentence(desc),
                "trigger": desc,
                "url": f"{BLOB}/{path}",
            })
        _, title, exec_role = META[slug]
        depts.append({
            "slug": slug, "title": title, "exec": exec_role,
            "reviewer": slug in REVIEWER, "skills": skills,
        })
    return depts


TEMPLATE = r"""<meta charset="utf-8">
<title>headcount org chart</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
  /* Palette inherited from the repository's existing identity — the badge row and the social
     preview card — rather than invented here. Light ground is a cool neutral: the accent is
     already terracotta, and a warm cream under it is the stock look. */
  :root {
    --ground:#F6F7F9; --surface:#FFFFFF; --surface-2:#EEF1F4;
    --line:#D8DEE6; --line-strong:#B9C3CE;
    --ink:#141A21; --ink-2:#4A5866; --ink-3:#78889A;
    --accent:#C2663F; --accent-ink:#FFFFFF; --accent-soft:rgba(194,102,63,.10);
    --shadow:0 1px 2px rgba(20,26,33,.06), 0 8px 24px -12px rgba(20,26,33,.18);
    --focus:#C2663F;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --ground:#0B0E14; --surface:#141A22; --surface-2:#1B222C;
      --line:#252E3A; --line-strong:#3A4553;
      --ink:#E6EDF3; --ink-2:#9FB0C3; --ink-3:#71818F;
      --accent:#D97757; --accent-ink:#1A1006; --accent-soft:rgba(217,119,87,.13);
      --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 30px -14px rgba(0,0,0,.7);
      --focus:#D97757;
    }
  }
  :root[data-theme="dark"] {
    --ground:#0B0E14; --surface:#141A22; --surface-2:#1B222C;
    --line:#252E3A; --line-strong:#3A4553;
    --ink:#E6EDF3; --ink-2:#9FB0C3; --ink-3:#71818F;
    --accent:#D97757; --accent-ink:#1A1006; --accent-soft:rgba(217,119,87,.13);
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 30px -14px rgba(0,0,0,.7);
    --focus:#D97757;
  }

  * { box-sizing:border-box; }
  body {
    margin:0; background:var(--ground); color:var(--ink);
    font-family:"IBM Plex Sans","Helvetica Neue",Arial,sans-serif;
    font-size:15px; line-height:1.5;
    -webkit-font-smoothing:antialiased;
  }
  .wrap { max-width:1180px; margin:0 auto; padding:52px 28px 80px; }

  /* ---- masthead ---- */
  .eyebrow {
    font-family:"IBM Plex Mono",monospace; font-size:12px; letter-spacing:.16em;
    text-transform:uppercase; color:var(--ink-3);
  }
  h1 {
    font-family:Archivo,"Helvetica Neue",sans-serif; font-weight:700;
    font-size:clamp(34px,5vw,50px); letter-spacing:-.03em; line-height:1.05;
    margin:12px 0 0; text-wrap:balance;
  }
  .lede { color:var(--ink-2); margin:12px 0 0; max-width:60ch; }
  .figures { display:flex; flex-wrap:wrap; gap:26px; margin-top:26px; }
  .figure b {
    display:block; font-family:Archivo,sans-serif; font-weight:700;
    font-size:27px; letter-spacing:-.02em; font-variant-numeric:tabular-nums;
  }
  .figure span {
    font-family:"IBM Plex Mono",monospace; font-size:11px; letter-spacing:.13em;
    text-transform:uppercase; color:var(--ink-3);
  }

  /* ---- controls ---- */
  .controls {
    display:flex; flex-wrap:wrap; gap:10px; align-items:center;
    margin:34px 0 8px; position:sticky; top:0; z-index:5;
    background:var(--ground); padding:12px 0; border-bottom:1px solid var(--line);
  }
  #q {
    flex:1 1 260px; min-width:0; padding:10px 13px;
    background:var(--surface); color:var(--ink);
    border:1px solid var(--line-strong); border-radius:8px;
    font-family:"IBM Plex Sans",sans-serif; font-size:14px;
  }
  #q::placeholder { color:var(--ink-3); }
  .btn {
    padding:10px 14px; background:var(--surface); color:var(--ink-2);
    border:1px solid var(--line-strong); border-radius:8px; cursor:pointer;
    font-family:"IBM Plex Sans",sans-serif; font-size:13px; font-weight:500;
  }
  .btn:hover { color:var(--ink); border-color:var(--ink-3); }
  .btn[aria-pressed="true"] {
    background:var(--accent-soft); border-color:var(--accent); color:var(--accent);
  }
  #count {
    font-family:"IBM Plex Mono",monospace; font-size:12px; color:var(--ink-3);
    font-variant-numeric:tabular-nums; white-space:nowrap;
  }
  :focus-visible { outline:2px solid var(--focus); outline-offset:2px; }

  /* ---- chief executive + reviewer rail ---- */
  .top { margin:38px 0 0; display:flex; flex-direction:column; align-items:center; }
  .ceo {
    background:var(--accent); color:var(--accent-ink);
    border-radius:11px; padding:13px 26px; text-align:center; box-shadow:var(--shadow);
  }
  .ceo b {
    font-family:Archivo,sans-serif; font-weight:700; font-size:17px; letter-spacing:-.01em;
    display:block;
  }
  .ceo span { font-family:"IBM Plex Mono",monospace; font-size:11px; opacity:.8; }
  .stem { width:2px; height:26px; background:var(--line-strong); }

  .rail {
    width:100%; border:1px dashed var(--accent); border-radius:12px;
    background:var(--accent-soft); padding:16px 18px;
    display:flex; flex-direction:column; gap:14px;
  }
  .rail-label {
    font-family:"IBM Plex Mono",monospace; font-size:11px; letter-spacing:.13em;
    text-transform:uppercase; color:var(--accent); text-align:center;
  }
  .rail-note {
    text-align:center; color:var(--ink-2); font-size:13px;
    max-width:66ch; margin:0 auto;
  }
  .rail-cards {
    display:grid; gap:14px; grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  }

  /* ---- department grid ---- */
  .grid {
    margin-top:26px; display:grid; gap:14px;
    grid-template-columns:repeat(auto-fill,minmax(290px,1fr));
  }
  .dept {
    background:var(--surface); border:1px solid var(--line); border-radius:12px;
    overflow:hidden; transition:border-color .12s ease;
  }
  .dept:hover { border-color:var(--line-strong); }
  .dept.rev { border-color:var(--accent); }
  .dept.open { border-color:var(--ink-3); box-shadow:var(--shadow); }
  .dept.hidden { display:none; }

  .head {
    width:100%; text-align:left; background:none; border:0; cursor:pointer;
    padding:15px 16px; display:flex; gap:12px; align-items:baseline; color:inherit;
    font-family:inherit;
  }
  .head h2 {
    margin:0; font-family:Archivo,sans-serif; font-weight:600; font-size:16px;
    letter-spacing:-.012em; flex:1;
  }
  .role {
    font-family:"IBM Plex Mono",monospace; font-size:11px; color:var(--ink-3);
    white-space:nowrap;
  }
  .n {
    font-family:"IBM Plex Mono",monospace; font-size:12px; color:var(--ink-2);
    font-variant-numeric:tabular-nums;
  }
  .slug {
    display:block; font-family:"IBM Plex Mono",monospace; font-size:11px;
    color:var(--ink-3); margin-top:3px; font-weight:400;
  }
  .revtag {
    font-family:"IBM Plex Mono",monospace; font-size:10px; letter-spacing:.1em;
    text-transform:uppercase; color:var(--accent);
    border:1px solid var(--accent); border-radius:4px; padding:1px 5px;
  }

  .body { display:none; border-top:1px solid var(--line); }
  .dept.open .body { display:block; }
  .install {
    display:flex; gap:8px; align-items:center; padding:11px 16px;
    background:var(--surface-2); border-bottom:1px solid var(--line);
  }
  .install code {
    font-family:"IBM Plex Mono",monospace; font-size:12px; color:var(--ink-2);
    overflow-x:auto; white-space:nowrap; flex:1; min-width:0;
  }
  .copy {
    border:1px solid var(--line-strong); background:var(--surface); color:var(--ink-2);
    border-radius:6px; padding:4px 9px; font-size:11px; cursor:pointer;
    font-family:"IBM Plex Mono",monospace; white-space:nowrap;
  }
  .copy:hover { color:var(--ink); }

  ul { list-style:none; margin:0; padding:0; }
  li { border-bottom:1px solid var(--line); }
  li:last-child { border-bottom:0; }
  li.hidden { display:none; }
  li a {
    display:block; padding:12px 16px; text-decoration:none; color:inherit;
  }
  li a:hover { background:var(--surface-2); }
  .sname {
    font-family:"IBM Plex Mono",monospace; font-size:13px; font-weight:500;
    color:var(--accent);
  }
  .sdesc { color:var(--ink-2); font-size:13.5px; margin-top:3px; }

  .empty {
    display:none; text-align:center; padding:56px 20px; color:var(--ink-3);
  }
  .empty.on { display:block; }
  footer {
    margin-top:52px; padding-top:20px; border-top:1px solid var(--line);
    color:var(--ink-3); font-size:13px;
    display:flex; flex-wrap:wrap; gap:10px; justify-content:space-between;
  }
  footer a { color:var(--ink-2); }
  mark { background:var(--accent-soft); color:inherit; border-radius:2px; }
  @media (prefers-reduced-motion:reduce) { * { transition:none !important; } }
</style>

<div class="wrap">
  <div class="eyebrow">cbrock84 / headcount</div>
  <h1>The org chart</h1>
  <p class="lede">
    An agent organization for Claude Code, structured as a company. Every department installs
    independently. Search across every skill, or open a department to see what it holds.
  </p>
  <div class="figures" id="figures"></div>

  <div class="controls">
    <input id="q" type="search" placeholder="Search 135 skills — try “threat”, “pricing”, “backup”…" autocomplete="off">
    <button class="btn" id="revonly" aria-pressed="false">Reviewer-class only</button>
    <button class="btn" id="expand">Expand all</button>
    <span id="count"></span>
  </div>

  <div class="top">
    <div class="ceo"><b>Chief Executive</b><span>executive</span></div>
    <div class="stem"></div>
    <div class="rail" id="rail">
      <div class="rail-label">Reviewer-class — reports to the chief executive</div>
      <p class="rail-note">
        Security and Legal&nbsp;&amp; Risk review what the other departments commit to, and their
        blocking findings are not overrulable by the department under review. That is why they report
        to the chief executive rather than into the function they oversee.
      </p>
      <div class="rail-cards" id="rail-cards"></div>
    </div>
  </div>

  <div class="grid" id="grid"></div>
  <div class="empty" id="empty">No skill or department matches that.</div>

  <footer>
    <span>Generated from the repository tree — <code>scripts/build-org-chart.py</code></span>
    <span><a href="https://github.com/cbrock84/headcount">github.com/cbrock84/headcount</a> · MIT</span>
  </footer>
</div>

<script>
const DEPTS = __DATA__;

const grid = document.getElementById('grid');
const q = document.getElementById('q');
const countEl = document.getElementById('count');
const emptyEl = document.getElementById('empty');
const revBtn = document.getElementById('revonly');
const expandBtn = document.getElementById('expand');

const totalSkills = DEPTS.reduce((n, d) => n + d.skills.length, 0);
const reviewers = DEPTS.filter(d => d.reviewer);

document.getElementById('figures').innerHTML = [
  [DEPTS.length, 'departments'],
  [totalSkills, 'skills'],
  [reviewers.length, 'reviewer-class'],
].map(([n, l]) => `<div class="figure"><b>${n}</b><span>${l}</span></div>`).join('');

const esc = s => s.replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

function card(d) {
  const el = document.createElement('section');
  el.className = 'dept' + (d.reviewer ? ' rev' : '');
  el.dataset.slug = d.slug;
  el.innerHTML = `
    <button class="head" aria-expanded="false">
      <span style="flex:1">
        <h2>${esc(d.title)}${d.reviewer ? ' <span class="revtag">reviewer</span>' : ''}</h2>
        <span class="slug">${esc(d.slug)}</span>
      </span>
      <span class="role">${esc(d.exec)}</span>
      <span class="n">${d.skills.length}</span>
    </button>
    <div class="body">
      <div class="install">
        <code>/plugin install ${esc(d.slug)}@headcount</code>
        <button class="copy">Copy</button>
      </div>
      <ul>${d.skills.map(s => `
        <li data-hay="${esc((s.name + ' ' + s.trigger).toLowerCase())}">
          <a href="${s.url}" target="_blank" rel="noopener">
            <span class="sname">${esc(d.slug)}:${esc(s.name)}</span>
            <div class="sdesc">${esc(s.summary)}.</div>
          </a>
        </li>`).join('')}</ul>
    </div>`;

  const head = el.querySelector('.head');
  head.addEventListener('click', () => {
    const open = el.classList.toggle('open');
    head.setAttribute('aria-expanded', String(open));
  });

  const copy = el.querySelector('.copy');
  copy.addEventListener('click', async e => {
    e.stopPropagation();
    try {
      await navigator.clipboard.writeText(`/plugin install ${d.slug}@headcount`);
      copy.textContent = 'Copied';
      setTimeout(() => { copy.textContent = 'Copy'; }, 1400);
    } catch { copy.textContent = 'Select it'; }
  });
  return el;
}

const railCards = document.getElementById('rail-cards');
DEPTS.forEach(d => (d.reviewer ? railCards : grid).appendChild(card(d)));

function apply() {
  const term = q.value.trim().toLowerCase();
  const revOnly = revBtn.getAttribute('aria-pressed') === 'true';
  let shown = 0, visibleDepts = 0;

  document.querySelectorAll('.dept').forEach(el => {
    const d = DEPTS.find(x => x.slug === el.dataset.slug);
    if (revOnly && !d.reviewer) { el.classList.add('hidden'); return; }

    let matches = 0;
    el.querySelectorAll('li').forEach(li => {
      const hit = !term || li.dataset.hay.includes(term);
      li.classList.toggle('hidden', !hit);
      if (hit) matches++;
    });

    const deptHit = !term
      || d.title.toLowerCase().includes(term)
      || d.slug.includes(term)
      || d.exec.toLowerCase().includes(term);

    if (matches === 0 && !deptHit) { el.classList.add('hidden'); return; }
    if (deptHit && matches === 0) {
      el.querySelectorAll('li').forEach(li => li.classList.remove('hidden'));
      matches = d.skills.length;
    }
    el.classList.remove('hidden');
    visibleDepts++;
    shown += matches;
    // A search is a request to see the hits, so open what matched.
    if (term) {
      el.classList.add('open');
      el.querySelector('.head').setAttribute('aria-expanded', 'true');
    }
  });

  // An empty dashed rail is a leftover, not a structure — hide it when neither reviewer matches.
  const railVisible = [...railCards.querySelectorAll('.dept')]
    .some(el => !el.classList.contains('hidden'));
  document.getElementById('rail').style.display = railVisible ? '' : 'none';
  document.querySelector('.stem').style.display = railVisible ? '' : 'none';

  countEl.textContent = term || revOnly
    ? `${shown} skill${shown === 1 ? '' : 's'} in ${visibleDepts} department${visibleDepts === 1 ? '' : 's'}`
    : `${totalSkills} skills in ${DEPTS.length} departments`;
  emptyEl.classList.toggle('on', visibleDepts === 0);
}

q.addEventListener('input', apply);
revBtn.addEventListener('click', () => {
  revBtn.setAttribute('aria-pressed', String(revBtn.getAttribute('aria-pressed') !== 'true'));
  apply();
});
expandBtn.addEventListener('click', () => {
  const anyClosed = [...document.querySelectorAll('.dept:not(.hidden)')]
    .some(el => !el.classList.contains('open'));
  document.querySelectorAll('.dept:not(.hidden)').forEach(el => {
    el.classList.toggle('open', anyClosed);
    el.querySelector('.head').setAttribute('aria-expanded', String(anyClosed));
  });
  expandBtn.textContent = anyClosed ? 'Collapse all' : 'Expand all';
});
apply();
</script>
"""


def render():
    depts = collect()
    total = sum(len(d["skills"]) for d in depts)
    html = TEMPLATE.replace("__DATA__", json.dumps(depts, ensure_ascii=False))
    return html.replace("Search 135 skills", f"Search {total} skills"), len(depts), total


def find_chromium():
    """Playwright's bundled Chromium first, then anything on PATH."""
    pw = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    candidates = [
        os.path.join(pw, "chromium"),
        *(shutil.which(n) for n in
          ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable")),
    ]
    return next((c for c in candidates if c and os.path.exists(c)), None)


def shoot(chrome, out, dark):
    subprocess.run(
        [chrome, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
         "--force-device-scale-factor=2", f"--window-size={SHOT_W},{SHOT_H}",
         "--virtual-time-budget=5000"]
        + (["--force-dark-mode"] if dark else [])
        + [f"--screenshot={out}", OUT],
        check=True, capture_output=True)
    return os.path.getsize(out) // 1024


def main():
    html, ndept, nskill = render()
    if "--check" in sys.argv:
        current = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if current != html:
            print(f"  {OUT} is stale — run: python3 scripts/build-org-chart.py")
            return 1
        print("org chart is current")
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"{OUT} regenerated — {ndept} departments, {nskill} skills")

    if "--html" in sys.argv:
        return 0
    chrome = find_chromium()
    if not chrome:
        print("  no Chromium found — HTML written, README screenshots not re-rendered.")
        return 0
    os.makedirs(os.path.dirname(SHOT_LIGHT), exist_ok=True)
    light = shoot(chrome, SHOT_LIGHT, dark=False)
    dark = shoot(chrome, SHOT_DARK, dark=True)
    print(f"{SHOT_LIGHT} {light} KB, {SHOT_DARK} {dark} KB "
          f"— {SHOT_W*2}x{SHOT_H*2}, embedded in the README as a <picture>")
    return 0


if __name__ == "__main__":
    sys.exit(main())
