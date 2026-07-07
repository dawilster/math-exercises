#!/usr/bin/env python3
"""Bundle markdown lessons/worksheets into an EPUB for the e-reader.

Math is converted to MathML (supported by most modern e-readers; falls back readably).

Usage:
    uv run python tools/make_epub.py modules/00-*/worksheets/01-*.md -o booklets/algebra-1.epub --title "Algebra Bootcamp 1"
    uv run python tools/make_epub.py a.md b.md c.md -o booklets/week1.epub --title "Week 1 Practice"
"""
import argparse
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def make_epub(inputs: list[Path], output: Path, title: str) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    # let pandoc find each lesson's img/ dir so figures get pulled into the EPUB,
    # even when inputs span several module directories.
    resource_dirs = [ROOT] + [p.resolve().parent for p in inputs]
    resource_path = ":".join(dict.fromkeys(str(d) for d in resource_dirs))
    cmd = [
        "pandoc",
        *[str(p) for p in inputs],
        "-o", str(output),
        "--mathml",
        "--toc",
        f"--resource-path={resource_path}",
        "--metadata", f"title={title}",
        "--metadata", "author=William's Math System",
        "--metadata", "lang=en-AU",
    ]
    subprocess.run(cmd, check=True)
    print(f"epub: {output}  ({output.stat().st_size // 1024} KB)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("inputs", nargs="+", type=Path)
    ap.add_argument("-o", "--output", type=Path, required=True)
    ap.add_argument("--title", required=True)
    args = ap.parse_args()
    make_epub(args.inputs, args.output, args.title)


if __name__ == "__main__":
    main()
