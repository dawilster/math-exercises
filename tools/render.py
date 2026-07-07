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


def render(input_md: Path, output_html: Path) -> None:
    if not KATEX_DIR.exists():
        sys.exit(f"KaTeX not found at {KATEX_DIR} — re-vendor it (see CLAUDE.md).")
    cmd = [
        "pandoc",
        str(input_md),
        "-o", str(output_html),
        "--standalone",
        "--embed-resources",          # inline KaTeX js/css/fonts → single file
        f"--katex={KATEX_DIR.as_uri()}/",
        "--css", str(CSS_FILE),
        "--metadata", f"pagetitle={input_md.stem.replace('-', ' ').title()}",  # browser-tab title only, no header block
        "--metadata", "lang=en-AU",
    ]
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
