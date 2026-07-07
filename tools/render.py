#!/usr/bin/env python3
"""Render a markdown lesson/worksheet to a self-contained, print-friendly HTML file.

Math: $inline$ and $$display$$ (LaTeX), rendered offline via the vendored KaTeX
in tools/katex/ — no internet needed, safe for printing and Artifacts.

Usage:
    uv run python tools/render.py modules/00-algebra-bootcamp/worksheets/01-balance-game.md
    uv run python tools/render.py input.md -o output.html
"""
import argparse
import subprocess
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
KATEX_DIR = TOOLS_DIR / "katex"
CSS_FILE = TOOLS_DIR / "worksheet.css"
ANSWERS_JS = TOOLS_DIR / "answers.html"   # hover/tap-to-reveal answers + lock toggle


def render(input_md: Path, output_html: Path, katex_url: str | None = None,
           css_url: str | None = None) -> None:
    """Render md → HTML. Default: fully self-contained (embedded KaTeX, ~1.7MB, printable anywhere).
    With katex_url (e.g. "/katex/"): links KaTeX from that URL instead — tiny files for web deploys.
    css_url likewise swaps the embedded stylesheet for a linked one."""
    if not KATEX_DIR.exists():
        sys.exit(f"KaTeX not found at {KATEX_DIR} — re-vendor it (see CLAUDE.md).")
    cmd = [
        "pandoc",
        str(input_md),
        "-o", str(output_html),
        "--standalone",
        "--toc", "--toc-depth=2",     # contents at the top of every page
        "--css", css_url or str(CSS_FILE),
        "--metadata", f"pagetitle={input_md.stem.replace('-', ' ').title()}",  # browser-tab title only, no header block
        "--metadata", "lang=en-AU",
    ]
    if ANSWERS_JS.exists():
        cmd += [f"--include-after-body={ANSWERS_JS}"]  # self-activates only if the page has .answer
    if katex_url:
        cmd += [f"--katex={katex_url}"]
    else:
        cmd += ["--embed-resources", f"--katex={KATEX_DIR.as_uri()}/"]
    subprocess.run(cmd, check=True)
    print(f"rendered: {output_html}  ({output_html.stat().st_size // 1024} KB)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", type=Path)
    ap.add_argument("-o", "--output", type=Path, default=None)
    args = ap.parse_args()
    out = args.output or args.input.with_suffix(".html")
    render(args.input, out)


if __name__ == "__main__":
    main()
