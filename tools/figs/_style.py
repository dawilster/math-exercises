"""Shared style for lesson figures.

Lesson figures are embedded PNGs (the lesson is the source of truth), so they must read
clearly BOTH on the web dashboard and on William's grayscale e-reader. Two rules follow:

- distinguish series by *lightness* and *linestyle*, never by hue alone (survives e-ink);
- keep them small and high-DPI so text stays crisp when the e-reader scales them.

Colours: INK (near-black, the function), ACCENT (crimson, the "measured/derived" thing),
COOL (steel, secondary structure). Crimson-on-steel still separates in grayscale because
their lightness differs; linestyle backs it up.
"""
import matplotlib.pyplot as plt

INK = "#1a1a2e"      # the primary curve / the given function
ACCENT = "#c81e4a"   # the thing we compute or claim (slope, descent path)
COOL = "#3a6ea5"     # secondary structure (contours, comparison line)
GRID = 0.25          # grid alpha

DPI = 150


def base(figsize=(7, 4.2)):
    """A clean figure+axis with light grid, spines trimmed."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.grid(True, alpha=GRID)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    return fig, ax


def save(fig, path):
    fig.tight_layout()
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", path)
