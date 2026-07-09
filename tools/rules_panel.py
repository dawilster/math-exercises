#!/usr/bin/env python3
"""Build the "Rules so far" panel injected into lesson/worksheet pages by render.py.

Parses every modules/*/rules.md (see modules/00-algebra-bootcamp/rules.md for the format:
"## <slug> — <Title>" sections, "- **Name**: description" bullets) and, for a given page
being rendered, computes the cumulative set of named moves taught up to and including that
page's position in the curriculum. One tab per module reached so far; within the current
module, only lessons up to the current one are included.
"""
import json
import re
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
MODULES_DIR = TOOLS_DIR.parent / "modules"
KATEX_DIR = TOOLS_DIR / "katex"

BULLET_RE = re.compile(r"^-\s+\*\*(.+?)\*\*:?\s*(.+)$")
MODULE_TITLE_RE = re.compile(r"^#\s*Module\s+\d+\s*—\s*(.+?)(?::.*)?$", re.MULTILINE)


def _fallback_title(dir_name: str) -> str:
    return dir_name.split("-", 1)[-1].replace("-", " ").title()


def parse_rules_md(path: Path):
    """Return (sections, module_title). sections is an ordered list of
    {"slug", "title", "rules": [{"name", "desc"}]}, in file order."""
    text = path.read_text()
    m = MODULE_TITLE_RE.search(text)
    module_title = m.group(1).strip() if m else _fallback_title(path.parent.name)

    sections = []
    for chunk in re.split(r"(?m)^##\s+", text)[1:]:
        lines = chunk.splitlines()
        heading = lines[0].strip()
        if "—" in heading:
            slug, title = (p.strip() for p in heading.split("—", 1))
        else:
            slug, title = heading, heading
        rules = []
        for line in lines[1:]:
            bm = BULLET_RE.match(line.strip())
            if bm:
                rules.append({"name": bm.group(1), "desc": bm.group(2)})
        sections.append({"slug": slug, "title": title, "rules": rules})
    return sections, module_title


def _discover_modules():
    """Sorted list of (module_dir, rules_md_or_None), skipping non-module dirs."""
    if not MODULES_DIR.exists():
        return []
    mods = []
    for d in sorted(MODULES_DIR.iterdir()):
        if not d.is_dir() or d.name.startswith(".") or d.name == "interludes":
            continue
        rules_md = d / "rules.md"
        mods.append((d, rules_md if rules_md.exists() else None))
    return mods


def build_panel_data(input_md: Path):
    """Cumulative rules-so-far data for the page at input_md, or None if not applicable
    (page isn't a module lesson/worksheet, or no rules.md files exist yet)."""
    input_md = input_md.resolve()
    modules = _discover_modules()
    if not any(rules_md for _, rules_md in modules):
        return None
    try:
        rel = input_md.relative_to(MODULES_DIR.resolve())
    except ValueError:
        return None
    parts = rel.parts
    if len(parts) < 3 or parts[1] not in ("lessons", "worksheets"):
        return None
    current_module_dir = parts[0]
    current_slug = Path(parts[-1]).stem

    tabs = []
    for mod_dir, rules_md in modules:
        if rules_md is None:
            continue
        if mod_dir.name > current_module_dir:
            break  # module not reached yet in curriculum order
        sections, module_title = parse_rules_md(rules_md)
        if mod_dir.name == current_module_dir:
            cutoff = next((i for i, s in enumerate(sections) if s["slug"] == current_slug), None)
            if cutoff is not None:
                sections = sections[: cutoff + 1]
        rules = [r for s in sections for r in s["rules"]]
        if rules:
            tabs.append({"id": mod_dir.name, "title": module_title, "rules": rules})

    if not tabs:
        return None
    return {"tabs": tabs, "currentModule": current_module_dir, "currentSlug": current_slug}


_PANEL_TEMPLATE = """
<script>window.__RULES_PANEL_DATA__ = {data_json};</script>
<script>{katex_js}</script>
<script>{auto_render_js}</script>
<div id="rules-panel-root"></div>
<script>
(function () {{
  var DATA = window.__RULES_PANEL_DATA__;
  if (!DATA || !DATA.tabs || !DATA.tabs.length) return;

  var POS_KEY = "rules-panel-pos";
  var OPEN_KEY = "rules-panel-open";

  var root = document.getElementById("rules-panel-root");

  var toggle = document.createElement("button");
  toggle.type = "button";
  toggle.className = "rules-toggle";
  toggle.textContent = "\\ud83d\\udcd6 Rules";
  toggle.setAttribute("aria-label", "Show rules learned so far");

  var panel = document.createElement("div");
  panel.className = "rules-panel";

  var header = document.createElement("div");
  header.className = "rules-panel-header";
  var headerTitle = document.createElement("span");
  headerTitle.textContent = "\\ud83d\\udcd6 Rules so far";
  var closeBtn = document.createElement("button");
  closeBtn.type = "button";
  closeBtn.className = "rules-panel-close";
  closeBtn.textContent = "\\u2715";
  closeBtn.setAttribute("aria-label", "Close rules panel");
  header.appendChild(headerTitle);
  header.appendChild(closeBtn);

  var tabsRow = document.createElement("div");
  tabsRow.className = "rules-panel-tabs";

  var body = document.createElement("div");
  body.className = "rules-panel-body";

  panel.appendChild(header);
  panel.appendChild(tabsRow);
  panel.appendChild(body);
  root.appendChild(toggle);
  root.appendChild(panel);

  function renderTab(tab) {{
    body.innerHTML = "";
    var ul = document.createElement("ul");
    ul.className = "rules-list";
    tab.rules.forEach(function (r) {{
      var li = document.createElement("li");
      var name = document.createElement("strong");
      name.textContent = r.name;
      var desc = document.createElement("span");
      desc.textContent = " \\u2014 " + r.desc;
      li.appendChild(name);
      li.appendChild(desc);
      ul.appendChild(li);
    }});
    body.appendChild(ul);
    if (window.renderMathInElement) {{
      window.renderMathInElement(body, {{
        delimiters: [
          {{ left: "$$", right: "$$", display: true }},
          {{ left: "$", right: "$", display: false }}
        ],
        throwOnError: false
      }});
    }}
  }}

  function selectTab(id) {{
    tabsRow.querySelectorAll(".rules-tab-btn").forEach(function (b) {{
      b.classList.toggle("active", b.dataset.id === id);
    }});
    var tab = DATA.tabs.filter(function (t) {{ return t.id === id; }})[0];
    if (tab) renderTab(tab);
  }}

  DATA.tabs.forEach(function (tab) {{
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "rules-tab-btn";
    btn.dataset.id = tab.id;
    btn.textContent = tab.title;
    btn.addEventListener("click", function () {{ selectTab(tab.id); }});
    tabsRow.appendChild(btn);
  }});
  selectTab(DATA.currentModule);

  function setOpen(open) {{
    panel.classList.toggle("open", open);
    localStorage.setItem(OPEN_KEY, open ? "1" : "0");
  }}
  toggle.addEventListener("click", function () {{ setOpen(true); }});
  closeBtn.addEventListener("click", function () {{ setOpen(false); }});
  setOpen(localStorage.getItem(OPEN_KEY) === "1");

  // restore a dragged position
  var savedPos = null;
  try {{ savedPos = JSON.parse(localStorage.getItem(POS_KEY)); }} catch (e) {{}}
  if (savedPos && typeof savedPos.left === "number") {{
    panel.style.left = savedPos.left + "px";
    panel.style.top = savedPos.top + "px";
    panel.style.right = "auto";
    panel.style.bottom = "auto";
  }}

  // drag-to-reposition, mouse + touch
  var dragging = false, offX = 0, offY = 0;
  function startDrag(x, y) {{
    var rect = panel.getBoundingClientRect();
    dragging = true;
    offX = x - rect.left;
    offY = y - rect.top;
    panel.style.right = "auto";
    panel.style.bottom = "auto";
  }}
  function moveDrag(x, y) {{
    if (!dragging) return;
    var left = Math.min(Math.max(0, x - offX), window.innerWidth - panel.offsetWidth);
    var top = Math.min(Math.max(0, y - offY), window.innerHeight - panel.offsetHeight);
    panel.style.left = left + "px";
    panel.style.top = top + "px";
  }}
  function endDrag() {{
    if (!dragging) return;
    dragging = false;
    var rect = panel.getBoundingClientRect();
    localStorage.setItem(POS_KEY, JSON.stringify({{ left: rect.left, top: rect.top }}));
  }}
  header.addEventListener("mousedown", function (e) {{
    if (e.target === closeBtn) return;
    startDrag(e.clientX, e.clientY);
  }});
  window.addEventListener("mousemove", function (e) {{ moveDrag(e.clientX, e.clientY); }});
  window.addEventListener("mouseup", endDrag);
  header.addEventListener("touchstart", function (e) {{
    if (e.target === closeBtn) return;
    var t = e.touches[0];
    startDrag(t.clientX, t.clientY);
  }}, {{ passive: true }});
  window.addEventListener("touchmove", function (e) {{
    if (!dragging) return;
    var t = e.touches[0];
    moveDrag(t.clientX, t.clientY);
  }}, {{ passive: true }});
  window.addEventListener("touchend", endDrag);
}})();
</script>
"""


def render_panel_html(input_md: Path) -> str | None:
    """Full <script>/<div> block to inject via pandoc --include-after-body, or None if
    this page has no applicable rules (not a module page, or no rules.md yet)."""
    data = build_panel_data(input_md)
    if data is None:
        return None
    katex_js = (KATEX_DIR / "katex.min.js").read_text()
    auto_render_js = (KATEX_DIR / "contrib" / "auto-render.min.js").read_text()
    return _PANEL_TEMPLATE.format(
        data_json=json.dumps(data),
        katex_js=katex_js,
        auto_render_js=auto_render_js,
    )
