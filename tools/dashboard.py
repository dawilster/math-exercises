#!/usr/bin/env python3
"""Learning dashboard — progress at a glance, open lessons, mark units complete.

Usage:
    uv run python tools/dashboard.py         # → http://localhost:8123

- Modules/units are discovered from the filesystem (modules/NN-name/{lessons,worksheets,notebooks})
- Completion state lives in profile/dashboard-state.json (Claude reads this each session too)
- Lesson/worksheet links render markdown → HTML on demand (via tools/render.py) and cache it
- tools/build_site.py reuses PAGE/scan_modules/nav_bar to prerender the Vercel deployment
"""
import json
import subprocess
from datetime import date
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

from render import render as render_md  # same directory

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT / "profile" / "dashboard-state.json"
ICONS_DIR = Path(__file__).resolve().parent / "icons"
PORT = 8123

MODULE_ICONS = {
    "00": "scale", "01": "chart-line", "02": "grid-3x3", "03": "chart-spline",
    "04": "dices", "05": "brain", "06": "bot", "07": "file-text",
}

NAME_FIXES = {
    "Functions And Graphs": "Functions & Graphs",
    "Probability Stats": "Probability & Statistics",
    "Math Of Neural Nets": "The Math of a Neural Net",
    "Llms And Diffusion": "LLMs & Stable Diffusion",
    "Reading Papers": "Read a Breakthrough Paper",
}


def icon(name: str, cls: str = "ic") -> str:
    """Inline a vendored Lucide SVG, sized/coloured via CSS (stroke uses currentColor)."""
    svg = (ICONS_DIR / f"{name}.svg").read_text()
    return svg.replace("<svg ", f'<svg class="{cls}" ', 1)


# ---------- state ----------

def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"completed": {}}


def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n")


# ---------- structure discovery ----------

def title_of(md: Path) -> str:
    for line in md.read_text().splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return md.stem


def pretty_module_name(dirname: str) -> tuple[str, str]:
    """Returns (icon_name, display_name)."""
    if dirname == "interludes":
        return "shell", "Wonder Interludes"
    num, _, rest = dirname.partition("-")
    words = rest.replace("-", " ").title()
    words = NAME_FIXES.get(words, words)
    return MODULE_ICONS.get(num, "sigma"), f"Module {int(num)} — {words}"


def scan_modules() -> list[dict]:
    modules = []
    for mdir in sorted((ROOT / "modules").iterdir()):
        if not mdir.is_dir():
            continue
        units: dict[str, dict] = {}
        for kind, pattern in (("lesson", "lessons/*.md"), ("worksheet", "worksheets/*.md"),
                              ("notebook", "notebooks/*.ipynb")):
            for f in sorted(mdir.glob(pattern)):
                if ".ipynb_checkpoints" in f.parts:
                    continue
                units.setdefault(f.stem, {})[kind] = str(f.relative_to(ROOT))
        unit_list = []
        for stem in sorted(units):
            entry = units[stem]
            src = entry.get("lesson") or entry.get("worksheet")
            title = title_of(ROOT / src) if src else stem.replace("-", " ").title()
            unit_list.append({"id": f"{mdir.name}/{stem}", "title": title, **entry})
        icon_name, display = pretty_module_name(mdir.name)
        modules.append({"dir": mdir.name, "name": display, "icon": icon_name,
                        "interlude": mdir.name == "interludes", "units": unit_list})
    # interludes go last
    modules.sort(key=lambda m: (m["interlude"], m["dir"]))
    return modules


def study_sequence() -> list[dict]:
    """The natural study order: each unit's lesson, then its worksheet, module by module."""
    seq = []
    for m in scan_modules():
        for u in m["units"]:
            for kind in ("lesson", "worksheet"):
                if kind in u:
                    seq.append({"path": u[kind], "title": u["title"], "kind": kind})
    return seq


NAV_CSS = """<style>
/* Full-bleed sticky bar: escapes the centered body column via the 100vw trick */
body { overflow-x: hidden; }
.studynav { position: sticky; top: 0; z-index: 10; box-sizing: border-box;
  width: 100vw; margin: -2rem 0 1.5rem calc(50% - 50vw);
  display: flex; align-items: center; gap: .6rem;
  background: #ffffffee; backdrop-filter: blur(6px); border-bottom: 1px solid #e2e8f0;
  padding: .55rem 1.2rem; font-family: "Avenir Next","Segoe UI",system-ui,sans-serif;
  font-size: .85rem; line-height: 1.3; }
.studynav .zone { flex: 1 1 0; display: flex; min-width: 0; }
.studynav .zone.c { flex: 0 0 auto; }
.studynav .zone.r { justify-content: flex-end; }
.studynav a { color: #2563eb; text-decoration: none; border: 1px solid #dbeafe; background: #eff6ff;
  border-radius: 7px; padding: .3rem .7rem; white-space: nowrap; overflow: hidden;
  text-overflow: ellipsis; max-width: 100%; box-sizing: border-box;
  display: inline-flex; align-items: center; gap: .4rem; }
.studynav a:hover { background: #dbeafe; }
.studynav .ic { width: 1em; height: 1em; flex: none; }
@media print { .studynav { display: none; } }
</style>"""


def nav_bar(rel_path: str, href_for=None, home: str = "/") -> str:
    """Prev/dashboard/next bar. href_for maps a unit md path → link target
    (default: local /view/ route; the static build passes site-relative .html paths)."""
    href_for = href_for or (lambda p: f"/view/{p}")
    seq = study_sequence()
    idx = next((i for i, s in enumerate(seq) if s["path"] == rel_path), None)
    prev_link = next_link = ""
    if idx is not None and idx > 0:
        p = seq[idx - 1]
        prev_link = f'<a href="{href_for(p["path"])}">← {p["kind"]}: {p["title"]}</a>'
    if idx is not None and idx < len(seq) - 1:
        n = seq[idx + 1]
        next_link = f'<a href="{href_for(n["path"])}">{n["kind"]}: {n["title"]} →</a>'
    return (NAV_CSS + '<div class="studynav">'
            + f'<span class="zone">{prev_link}</span>'
            + f'<span class="zone c"><a href="{home}">{icon("house")} dashboard</a></span>'
            + f'<span class="zone r">{next_link}</span>'
            + "</div>")


# ---------- page ----------

PAGE = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Math — Dashboard</title>
<style>
  :root { --ink:#1a1a2e; --accent:#2563eb; --soft:#64748b; --bg:#f4f6fb; --card:#fff; --done:#16a34a; }
  * { box-sizing: border-box; }
  body { font-family:"Avenir Next","Segoe UI",system-ui,sans-serif; color:var(--ink);
         background:var(--bg); margin:0; padding:2rem 1rem; }
  .wrap { max-width: 60rem; margin: 0 auto; }
  h1 { font-size:1.5rem; margin:0 0 .3rem; display:flex; align-items:center; gap:.55rem; }
  h1 .ic { width:1.6rem; height:1.6rem; color:var(--accent); }
  .ic { width:1.05em; height:1.05em; vertical-align:-.18em; }
  .sub { color:var(--soft); margin-bottom:1.4rem; }
  .overall { background:var(--card); border-radius:14px; padding:1.1rem 1.3rem; margin-bottom:1.4rem;
             box-shadow:0 1px 4px rgba(26,26,46,.08); display:flex; align-items:center; gap:1.2rem; flex-wrap:wrap; }
  .bar { flex:1; min-width:180px; height:12px; background:#e2e8f0; border-radius:6px; overflow:hidden; }
  .bar > div { height:100%; background:linear-gradient(90deg,var(--accent),#7c3aed); transition:width .4s; }
  .pill { background:#eff6ff; color:var(--accent); border-radius:999px; padding:.25rem .8rem;
          font-size:.85rem; font-weight:600; white-space:nowrap; display:inline-flex; align-items:center; gap:.4rem; }
  .pill .ic { width:1em; height:1em; }
  .pill.warn { background:#fef3c7; color:#b45309; }
  .module { background:var(--card); border-radius:14px; padding:1rem 1.3rem; margin-bottom:1rem;
            box-shadow:0 1px 4px rgba(26,26,46,.08); }
  .module h2 { font-size:1.05rem; margin:.2rem 0 .7rem; display:flex; align-items:center; gap:.55rem; }
  .module h2 .ic { width:1.25rem; height:1.25rem; color:var(--accent); flex:none; }
  .module.interlude h2 .ic { color:#7c3aed; }
  .module h2 .mbar { flex:1; max-width:160px; height:7px; background:#e2e8f0; border-radius:4px; overflow:hidden; }
  .module h2 .mbar > div { height:100%; background:var(--done); }
  .module h2 .count { color:var(--soft); font-size:.8rem; font-weight:400; }
  .unit { display:flex; align-items:center; gap:.7rem; padding:.5rem .4rem; border-radius:9px; }
  .unit:hover { background:#f8fafc; }
  .unit.done .title { color:var(--soft); text-decoration:line-through; }
  .tick { width:1.45rem; height:1.45rem; border:2px solid #cbd5e1; border-radius:7px; cursor:pointer;
          flex:none; display:flex; align-items:center; justify-content:center;
          background:#fff; transition:all .15s; color:transparent; }
  .tick .ic { width:.95rem; height:.95rem; }
  .unit.done .tick { background:var(--done); border-color:var(--done); color:#fff; }
  .title { flex:1; font-size:.95rem; }
  .when { color:var(--soft); font-size:.75rem; white-space:nowrap; }
  .links { display:flex; gap:.35rem; }
  .links a, .links button { font-size:.75rem; text-decoration:none; color:var(--accent);
          border:1px solid #dbeafe; background:#eff6ff; border-radius:6px; padding:.22rem .55rem;
          cursor:pointer; font-family:inherit; display:inline-flex; align-items:center; gap:.35rem; }
  .links .ic { width:.95em; height:.95em; }
  .links a:hover, .links button:hover { background:#dbeafe; }
  .empty { color:var(--soft); font-size:.85rem; font-style:italic; padding:.3rem .4rem; }
  .next { border:2px solid var(--accent); }
  .nextlabel { font-size:.7rem; font-weight:700; color:var(--accent); letter-spacing:.05em; }
  footer { color:var(--soft); font-size:.8rem; text-align:center; margin-top:1.5rem; }
  .toast { position:fixed; bottom:1.2rem; left:50%; transform:translateX(-50%); background:var(--ink);
           color:#fff; padding:.5rem 1rem; border-radius:8px; font-size:.85rem; opacity:0; transition:opacity .3s; }
  .toast.show { opacity:1; }
  @media (max-width: 640px) { .links { flex-direction:column; } .unit { align-items:flex-start; } }
</style></head><body><div class="wrap">
<h1>__ICON_SIGMA__ William’s Math</h1>
<div class="sub">Year 10 → dangerous enough for deep learning</div>
<div class="overall">
  <strong id="pct">0%</strong>
  <div class="bar"><div id="obar" style="width:0%"></div></div>
  <span class="pill" id="counts"></span>
  <span class="pill warn" id="inbox" style="display:none"></span>
</div>
<div id="modules"></div>
<footer id="foot">Tick a unit when its worksheet is done &amp; scanned</footer>
<div class="toast" id="toast"></div>
</div>
<script>
const DATA = __DATA__;
const IC = DATA.icons;

async function init() {
  if (DATA.remote) {
    try {
      const r = await fetch("/api/state");
      if (!r.ok) throw new Error(r.status);
      DATA.state = await r.json();
    } catch (e) {
      DATA.deviceOnly = true;
      DATA.state = JSON.parse(localStorage.getItem("math-state") || '{"completed":{}}');
      document.getElementById("foot").textContent = "Progress is stored on this device only (state API unavailable)";
    }
  }
  render();
}

async function toggle(id) {
  if (DATA.deviceOnly) {
    const c = DATA.state.completed;
    if (c[id]) delete c[id]; else c[id] = new Date().toISOString().slice(0, 10);
    localStorage.setItem("math-state", JSON.stringify(DATA.state));
    return render();
  }
  try {
    const r = await fetch("/api/toggle", { method: "POST",
      headers: { "Content-Type": "application/json" }, body: JSON.stringify({ id }) });
    if (!r.ok) throw new Error(r.status);
    DATA.state = await r.json();
    render();
  } catch (e) { toast("Couldn’t save — is the server running?"); }
}

function render() {
  const { modules, state, inbox } = DATA;
  const completed = state.completed || {};
  const gradable = modules.filter(m => !m.interlude).flatMap(m => m.units);
  const doneCount = gradable.filter(u => completed[u.id]).length;
  const pct = gradable.length ? Math.round(100 * doneCount / gradable.length) : 0;
  document.getElementById("pct").textContent = pct + "%";
  document.getElementById("obar").style.width = pct + "%";
  document.getElementById("counts").textContent = doneCount + " / " + gradable.length + " units complete";
  if (inbox > 0) {
    const el = document.getElementById("inbox");
    el.style.display = "";
    el.innerHTML = IC.camera + " " + inbox + " scan" + (inbox > 1 ? "s" : "") + " waiting in inbox — tell Claude!";
  }
  let nextFound = false;
  const host = document.getElementById("modules");
  host.innerHTML = "";
  for (const m of modules) {
    const mDone = m.units.filter(u => completed[u.id]).length;
    const card = document.createElement("div");
    card.className = "module" + (m.interlude ? " interlude" : "");
    card.innerHTML = `<h2>${IC[m.icon]} ${m.name}
        <span class="mbar"><div style="width:${m.units.length ? 100 * mDone / m.units.length : 0}%"></div></span>
        <span class="count">${mDone}/${m.units.length}</span></h2>`;
    if (!m.units.length) {
      card.innerHTML += `<div class="empty">content appears here as we reach it — the curriculum has the roadmap</div>`;
    }
    for (const u of m.units) {
      const isDone = !!completed[u.id];
      const isNext = !isDone && !nextFound && !m.interlude;
      if (isNext) nextFound = true;
      const row = document.createElement("div");
      row.className = "unit" + (isDone ? " done" : "") + (isNext ? " next" : "");
      const nbLink = DATA.remote
        ? (u.notebook_html ? `<a href="${u.notebook_html}">${IC.notebook} notebook</a>` : "")
        : (u.notebook ? `<button data-nb="${u.notebook}">${IC.notebook} notebook</button>` : "");
      row.innerHTML = `
        <div class="tick" title="mark complete">${IC.check}</div>
        <span class="title">${u.title}${isNext ? ' <span class="nextlabel">← NEXT UP</span>' : ""}</span>
        ${isDone ? `<span class="when">${completed[u.id]}</span>` : ""}
        <span class="links">
          ${u.lesson ? `<a href="${link(u.lesson)}">${IC.lesson} lesson</a>` : ""}
          ${u.worksheet ? `<a href="${link(u.worksheet)}">${IC.worksheet} worksheet</a>` : ""}
          ${nbLink}
        </span>`;
      row.querySelector(".tick").onclick = () => toggle(u.id);
      const nb = row.querySelector("[data-nb]");
      if (nb) nb.onclick = async () => {
        await navigator.clipboard.writeText("uv run jupyter lab " + nb.dataset.nb);
        toast("Command copied — paste it in your terminal to open the notebook");
      };
      card.appendChild(row);
    }
    host.appendChild(card);
  }
}
function link(mdPath) {
  return DATA.remote ? "/" + mdPath.replace(/\\.md$/, ".html") : "/view/" + mdPath;
}
function toast(msg) {
  const t = document.getElementById("toast");
  t.textContent = msg; t.classList.add("show");
  setTimeout(() => t.classList.remove("show"), 2600);
}
init();
</script></body></html>"""


def page_icons() -> dict:
    return {"lesson": icon("book-open"), "worksheet": icon("pen-line"),
            "notebook": icon("notebook-pen"), "camera": icon("camera"), "check": icon("check"),
            **{m["icon"]: icon(m["icon"]) for m in scan_modules()}}


def dashboard_html() -> str:
    modules = scan_modules()
    data = {"modules": modules, "state": load_state(), "remote": False,
            "icons": page_icons(),
            "inbox": len([f for f in (ROOT / "scans" / "inbox").iterdir()
                          if f.is_file() and not f.name.startswith(".")])}
    return PAGE.replace("__DATA__", json.dumps(data)).replace("__ICON_SIGMA__", icon("sigma"))


# ---------- server ----------

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, *args):  # quiet
        pass

    def send_payload(self, body: str, ctype: str = "text/html; charset=utf-8") -> None:
        raw = body.encode()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/":
            return self.send_payload(dashboard_html())
        if path == "/api/state":
            return self.send_payload(json.dumps(load_state()), "application/json")
        if path.startswith("/view/"):
            rel = unquote(path[len("/view/"):])
            md = (ROOT / rel).resolve()
            if not md.is_relative_to(ROOT) or md.suffix != ".md" or not md.exists():
                return self.send_error(404)
            html = md.with_suffix(".html")
            if not html.exists() or html.stat().st_mtime < md.stat().st_mtime:
                render_md(md, html)  # render on demand, cache next to the md
            # inject the prev/next study-flow nav just after <body>
            page = html.read_text()
            page = page.replace("<body>", "<body>" + nav_bar(str(md.relative_to(ROOT))), 1)
            return self.send_payload(page)
        return super().do_GET()

    def do_POST(self):
        if urlparse(self.path).path == "/api/toggle":
            length = int(self.headers.get("Content-Length", 0))
            unit_id = json.loads(self.rfile.read(length))["id"]
            state = load_state()
            if unit_id in state["completed"]:
                del state["completed"][unit_id]
            else:
                state["completed"][unit_id] = date.today().isoformat()
            save_state(state)
            return self.send_payload(json.dumps(state), "application/json")
        return self.send_error(404)


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://localhost:{PORT}"
    print(f"Math dashboard → {url}   (Ctrl+C to stop)")
    try:
        subprocess.run(["open", url], check=False)
    except OSError:
        pass
    server.serve_forever()


if __name__ == "__main__":
    main()
