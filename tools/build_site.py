#!/usr/bin/env python3
"""Prerender the whole learning site into web/public/ for Vercel deployment.

Vercel's build machines don't have pandoc, so everything is built locally:
- dashboard → index.html (remote mode: state via /api/state, localStorage fallback)
- every lesson/worksheet md → HTML with the prev/next study nav baked in
- every notebook → read-only HTML via nbconvert
- KaTeX served once from /katex/ (pages link it instead of embedding → tiny pages)

Usage: uv run python tools/build_site.py   then   cd web && vercel deploy --prod
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import dashboard as dash
from render import render as render_md

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "web" / "public"
KATEX = Path(__file__).resolve().parent / "katex"


def html_path(md_path: str) -> str:
    return md_path[: -len(".md")] + ".html"


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    # KaTeX once, shared by every page
    shutil.copytree(KATEX, OUT / "katex")

    modules = dash.scan_modules()
    seq = dash.study_sequence()

    # lessons + worksheets, with static nav
    for s in seq:
        md = ROOT / s["path"]
        out = OUT / html_path(s["path"])
        out.parent.mkdir(parents=True, exist_ok=True)
        render_md(md, out, katex_url="/katex/")
        nav = dash.nav_bar(s["path"], href_for=lambda p: "/" + html_path(p), home="/")
        page = out.read_text()
        out.write_text(page.replace("<body>", "<body>" + nav, 1))

    # notebooks → read-only HTML
    for m in modules:
        for u in m["units"]:
            if "notebook" not in u:
                continue
            nb = ROOT / u["notebook"]
            out = OUT / html_path(u["notebook"].replace(".ipynb", ".md"))  # .ipynb → .html
            out.parent.mkdir(parents=True, exist_ok=True)
            r = subprocess.run(
                ["uv", "run", "jupyter", "nbconvert", "--to", "html", str(nb),
                 "--output", out.stem, "--output-dir", str(out.parent)],
                capture_output=True, text=True, cwd=ROOT)
            if r.returncode != 0:
                print(f"nbconvert FAILED for {nb}:\n{r.stderr[-800:]}", file=sys.stderr)
                sys.exit(1)
            u["notebook_html"] = "/" + str(out.relative_to(OUT))

    # dashboard index — remote mode
    data = {"modules": modules, "state": {"completed": {}}, "remote": True,
            "icons": dash.page_icons(), "inbox": 0}
    index = dash.PAGE.replace("__DATA__", json.dumps(data)).replace(
        "__ICON_SIGMA__", dash.icon("sigma"))
    (OUT / "index.html").write_text(index)

    n_pages = len(list(OUT.rglob("*.html")))
    size_mb = sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file()) / 1e6
    print(f"built web/public: {n_pages} pages, {size_mb:.1f} MB")


if __name__ == "__main__":
    main()
