#!/usr/bin/env python3
"""
Build a self-contained index.html from all markdown files in the repo.
All content is embedded as JSON so the page works on any host without auth.
"""

import json
import os
import glob
import re
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.join(ROOT, "site")

SECTIONS = [
    ("Portfolio",  "portfolio",  "portfolio/*.md"),
    ("Theses",     "theses",     "theses/*.md"),
    ("Tickers",    "tickers",    "tickers/*.md"),
    ("Macro",      "macro",      "macro/*.md"),
    ("Journal",    "journal",    "journal/*.md"),
    ("Watchlist",  "root",       "watchlist.md"),
]

EXCLUDE_PATTERNS = {"_template.md", "CLAUDE.md"}

def collect_files():
    nav = []
    files = {}
    for section_label, section_key, pattern in SECTIONS:
        full_pattern = os.path.join(ROOT, pattern)
        matches = sorted(glob.glob(full_pattern), reverse=True)
        items = []
        for fpath in matches:
            fname = os.path.basename(fpath)
            if fname in EXCLUDE_PATTERNS:
                continue
            rel = os.path.relpath(fpath, ROOT).replace("\\", "/")
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue
            title = fname.replace(".md", "").replace("-", " ").replace("_", " ").title()
            # Try to extract a better title from first H1
            h1 = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            if h1:
                title = h1.group(1).strip()
                # Shorten long titles for nav
                if len(title) > 40:
                    title = title[:37] + "..."
            files[rel] = content
            items.append({"key": rel, "title": title})
        if items:
            nav.append({"section": section_label, "items": items})
    return nav, files

def build_html(nav, files, build_time):
    nav_json = json.dumps(nav, ensure_ascii=False)
    files_json = json.dumps(files, ensure_ascii=False)

    # Pick the default file to show on load
    default_key = "portfolio/core-book.md" if "portfolio/core-book.md" in files else (list(files.keys())[0] if files else "")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Beyond the Noise — Investment Ops</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
:root {{
  --bg: #0d1117;
  --surface: #161b22;
  --surface2: #21262d;
  --border: #30363d;
  --text: #e6edf3;
  --muted: #8b949e;
  --accent: #58a6ff;
  --green: #3fb950;
  --red: #f85149;
  --yellow: #d29922;
  --sidebar-w: 280px;
  --header-h: 52px;
  --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  --mono: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: var(--bg); color: var(--text); font-family: var(--font); font-size: 14px; line-height: 1.6; display: flex; flex-direction: column; height: 100vh; overflow: hidden; }}

/* Header */
header {{
  height: var(--header-h);
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center; padding: 0 16px; gap: 12px;
  flex-shrink: 0; z-index: 100;
}}
header h1 {{ font-size: 15px; font-weight: 600; color: var(--text); white-space: nowrap; }}
header .subtitle {{ font-size: 12px; color: var(--muted); }}
header .spacer {{ flex: 1; }}
header .build-time {{ font-size: 11px; color: var(--muted); white-space: nowrap; }}
.hamburger {{ display: none; background: none; border: 1px solid var(--border); color: var(--text); padding: 4px 8px; border-radius: 6px; cursor: pointer; font-size: 16px; }}

/* Layout */
.layout {{ display: flex; flex: 1; overflow: hidden; }}

/* Sidebar */
nav.sidebar {{
  width: var(--sidebar-w);
  background: var(--surface);
  border-right: 1px solid var(--border);
  overflow-y: auto;
  flex-shrink: 0;
  padding: 8px 0;
}}
.section-header {{
  padding: 6px 16px 4px;
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin-top: 8px;
}}
.section-header:first-child {{ margin-top: 0; }}
nav.sidebar a {{
  display: block;
  padding: 5px 16px 5px 24px;
  color: var(--muted);
  text-decoration: none;
  font-size: 13px;
  border-left: 2px solid transparent;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  transition: color 0.1s, background 0.1s;
}}
nav.sidebar a:hover {{ background: var(--surface2); color: var(--text); }}
nav.sidebar a.active {{ color: var(--accent); border-left-color: var(--accent); background: var(--surface2); }}

/* Content */
main {{
  flex: 1;
  overflow-y: auto;
  padding: 32px;
}}
.md-body {{ max-width: 860px; margin: 0 auto; }}

/* Markdown styles */
.md-body h1 {{ font-size: 24px; font-weight: 700; color: var(--text); border-bottom: 1px solid var(--border); padding-bottom: 10px; margin-bottom: 16px; margin-top: 0; }}
.md-body h2 {{ font-size: 18px; font-weight: 600; color: var(--text); margin-top: 28px; margin-bottom: 10px; padding-bottom: 6px; border-bottom: 1px solid var(--border); }}
.md-body h3 {{ font-size: 15px; font-weight: 600; color: var(--text); margin-top: 20px; margin-bottom: 8px; }}
.md-body h4 {{ font-size: 13px; font-weight: 600; color: var(--muted); margin-top: 16px; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.05em; }}
.md-body p {{ margin-bottom: 12px; color: var(--text); }}
.md-body a {{ color: var(--accent); text-decoration: none; }}
.md-body a:hover {{ text-decoration: underline; }}
.md-body ul, .md-body ol {{ margin-bottom: 12px; padding-left: 24px; }}
.md-body li {{ margin-bottom: 4px; }}
.md-body strong {{ color: var(--text); font-weight: 600; }}
.md-body em {{ color: var(--muted); font-style: italic; }}
.md-body code {{ background: var(--surface2); border: 1px solid var(--border); border-radius: 4px; padding: 1px 5px; font-family: var(--mono); font-size: 12px; color: #ff7b72; }}
.md-body pre {{ background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; padding: 16px; overflow-x: auto; margin-bottom: 16px; }}
.md-body pre code {{ background: none; border: none; padding: 0; color: var(--text); }}
.md-body blockquote {{ border-left: 3px solid var(--accent); margin: 0 0 12px; padding: 8px 16px; background: var(--surface2); border-radius: 0 6px 6px 0; color: var(--muted); }}
.md-body hr {{ border: none; border-top: 1px solid var(--border); margin: 24px 0; }}

/* Tables */
.md-body table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 13px; }}
.md-body thead th {{ background: var(--surface2); color: var(--muted); font-weight: 600; text-transform: uppercase; font-size: 11px; letter-spacing: 0.05em; padding: 8px 12px; text-align: left; border-bottom: 2px solid var(--border); }}
.md-body tbody tr {{ border-bottom: 1px solid var(--border); transition: background 0.1s; }}
.md-body tbody tr:hover {{ background: var(--surface2); }}
.md-body tbody td {{ padding: 7px 12px; vertical-align: top; }}
/* Color-code P&L patterns in table cells */
.md-body td.green, .md-body td[data-sign="+"] {{ color: var(--green); }}
.md-body td.red {{ color: var(--red); }}

/* ⚠️ alert blocks */
.md-body h3 + p, .md-body h2 + p {{ }}
.alert-block {{ background: rgba(210, 153, 34, 0.1); border: 1px solid var(--yellow); border-radius: 8px; padding: 12px 16px; margin-bottom: 16px; }}

/* Responsive */
@media (max-width: 768px) {{
  .hamburger {{ display: block; }}
  nav.sidebar {{ position: fixed; top: var(--header-h); left: -100%; height: calc(100vh - var(--header-h)); z-index: 200; transition: left 0.2s; }}
  nav.sidebar.open {{ left: 0; }}
  main {{ padding: 16px; }}
  .md-body h1 {{ font-size: 20px; }}
  .md-body table {{ font-size: 12px; display: block; overflow-x: auto; }}
}}

/* Scrollbar */
::-webkit-scrollbar {{ width: 6px; height: 6px; }}
::-webkit-scrollbar-track {{ background: transparent; }}
::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 3px; }}
</style>
</head>
<body>
<header>
  <button class="hamburger" id="menuBtn" onclick="toggleMenu()">☰</button>
  <div>
    <h1>Beyond the Noise</h1>
    <div class="subtitle">Investment Operations</div>
  </div>
  <div class="spacer"></div>
  <div class="build-time">Built {build_time}</div>
</header>
<div class="layout">
  <nav class="sidebar" id="sidebar">
  </nav>
  <main>
    <div class="md-body" id="content">Loading…</div>
  </main>
</div>

<script>
const NAV = {nav_json};
const FILES = {files_json};
const DEFAULT = {json.dumps(default_key)};

// Build navigation
const sidebar = document.getElementById('sidebar');
NAV.forEach(section => {{
  const hdr = document.createElement('div');
  hdr.className = 'section-header';
  hdr.textContent = section.section;
  sidebar.appendChild(hdr);
  section.items.forEach(item => {{
    const a = document.createElement('a');
    a.href = '#' + encodeURIComponent(item.key);
    a.dataset.key = item.key;
    a.textContent = item.title;
    a.onclick = (e) => {{ e.preventDefault(); loadFile(item.key); closeMobile(); }};
    sidebar.appendChild(a);
  }});
}});

// Post-process P&L coloring in tables
function colorTables() {{
  document.querySelectorAll('.md-body td').forEach(td => {{
    const t = td.textContent.trim();
    if (/^[+]/.test(t) && /%|\\$/.test(t)) td.style.color = 'var(--green)';
    else if (/^[-]/.test(t) && /%|\\$/.test(t)) td.style.color = 'var(--red)';
  }});
  // Highlight ⚠️ headings
  document.querySelectorAll('.md-body h3').forEach(h => {{
    if (h.textContent.includes('⚠️') || h.textContent.includes('Alert') || h.textContent.includes('Flag')) {{
      h.style.color = 'var(--yellow)';
    }}
  }});
  document.querySelectorAll('.md-body h2').forEach(h => {{
    if (h.textContent.includes('⚠️')) h.style.color = 'var(--yellow)';
  }});
}}

// Render markdown
function loadFile(key) {{
  const content = FILES[key];
  if (!content) {{ document.getElementById('content').innerHTML = '<p>File not found.</p>'; return; }}
  document.getElementById('content').innerHTML = marked.parse(content);
  colorTables();
  // Update active link
  document.querySelectorAll('nav.sidebar a').forEach(a => {{
    a.classList.toggle('active', a.dataset.key === key);
  }});
  // Update hash
  history.replaceState(null, '', '#' + encodeURIComponent(key));
  // Scroll to top
  document.querySelector('main').scrollTop = 0;
}}

// Handle hash on load
function loadFromHash() {{
  const hash = decodeURIComponent(window.location.hash.slice(1));
  if (hash && FILES[hash]) loadFile(hash);
  else loadFile(DEFAULT);
}}

// Mobile menu
function toggleMenu() {{
  document.getElementById('sidebar').classList.toggle('open');
}}
function closeMobile() {{
  document.getElementById('sidebar').classList.remove('open');
}}

// Close sidebar on outside click (mobile)
document.querySelector('main').addEventListener('click', closeMobile);

window.addEventListener('hashchange', loadFromHash);
loadFromHash();
</script>
</body>
</html>"""
    return html

def main():
    os.makedirs(SITE_DIR, exist_ok=True)
    nav, files = collect_files()
    build_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    html = build_html(nav, files, build_time)
    out = os.path.join(SITE_DIR, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built {out} — {len(files)} files embedded, build time {build_time}")

if __name__ == "__main__":
    main()
