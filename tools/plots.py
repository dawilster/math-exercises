"""Shared matplotlib helpers for lessons and notebooks.

Import in notebooks with:
    import sys; sys.path.append("../../../tools")   # from a module notebook dir
    from plots import axes_through_origin, plot_functions
"""
import matplotlib.pyplot as plt
import numpy as np


def axes_through_origin(ax=None, xlim=(-10, 10), ylim=(-10, 10), grid=True):
    """A school-style graph: axes crossing at the origin, arrows, grid.

    Makes plots look like the graphs in a math workbook instead of a science paper.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 6))
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if grid:
        ax.grid(True, alpha=0.3)
    ax.set_aspect("equal", adjustable="box")
    return ax


def plot_functions(funcs, xlim=(-10, 10), ylim=(-10, 10), n=1000, ax=None):
    """Plot one or more functions on school-style axes.

    funcs: dict of {label: python_function}, e.g. {"y = 2x + 1": lambda x: 2*x + 1}
    """
    ax = axes_through_origin(ax, xlim=xlim, ylim=ylim)
    x = np.linspace(*xlim, n)
    for label, f in funcs.items():
        y = f(x)
        y = np.where((y < ylim[0] - 1) | (y > ylim[1] + 1), np.nan, y)  # clip blow-ups
        ax.plot(x, y, linewidth=2, label=label)
    ax.legend(loc="upper left", frameon=True)
    return ax


def balance_scale(left: str, right: str, ax=None, title=""):
    """Draw a balance scale with expressions on each pan — the mental model for equations."""
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 3.2))
    ax.axis("off")
    # beam and stand
    ax.plot([1, 9], [2, 2], color="#1a1a2e", linewidth=3)          # beam
    ax.plot([5, 5], [0.4, 2], color="#1a1a2e", linewidth=4)        # post
    ax.plot([4.2, 5.8], [0.4, 0.4], color="#1a1a2e", linewidth=4)  # base
    for x in (1, 9):  # hangers + pans
        ax.plot([x, x], [1.55, 2], color="#1a1a2e", linewidth=2)
        ax.add_patch(plt.Rectangle((x - 1.1, 1.15), 2.2, 0.4, fill=True,
                                   color="#2563eb", alpha=0.15, ec="#2563eb"))
    ax.text(1, 1.35, f"${left}$", ha="center", va="center", fontsize=15)
    ax.text(9, 1.35, f"${right}$", ha="center", va="center", fontsize=15)
    ax.text(5, 2.35, "=", ha="center", fontsize=17, weight="bold")
    if title:
        ax.set_title(title, fontsize=12)
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(0, 3)
    return ax
