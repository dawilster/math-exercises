"""Load-bearing figures for Module 0 (Algebra Bootcamp) lessons.

Run:  uv run python tools/figs/mod00_algebra.py
Writes into modules/00-algebra-bootcamp/lessons/img/.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(__file__)
sys.path.append(HERE)
sys.path.append(os.path.join(HERE, ".."))   # for plots.py
from _style import INK, ACCENT, COOL, base, save  # noqa: E402
from plots import axes_through_origin, balance_scale  # noqa: E402

OUT = os.path.abspath(os.path.join(HERE, "..", "..",
                      "modules", "00-algebra-bootcamp", "lessons", "img"))
os.makedirs(OUT, exist_ok=True)


def path(name):
    return os.path.join(OUT, name)


# ---- 0.1 --------------------------------------------------------------------
def fig_balance():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    balance_scale("3x + 2", "14", ax=ax, title="An equation IS this picture: both pans weigh the same")
    save(fig, path("01-balance-scale.png"))


def fig_lines_meet():
    ax = axes_through_origin(xlim=(-2, 8), ylim=(-2, 20))
    xs = np.linspace(-2, 8, 200)
    ax.plot(xs, 3 * xs + 2, color=INK, linewidth=2, label="y = 3x + 2")
    ax.plot(xs, 0 * xs + 14, color=COOL, linewidth=2, linestyle="--", label="y = 14")
    ax.plot(4, 14, "o", color=ACCENT, markersize=10)
    ax.annotate("they meet at x = 4 — the solution!", (4, 14), xytext=(4.4, 7),
                fontsize=10, arrowprops=dict(arrowstyle="->", color=ACCENT))
    ax.legend(loc="upper left", fontsize=10)
    ax.set_title("Solving 3x + 2 = 14 = finding where the two lines cross")
    save(ax.figure, path("01-lines-meet.png"))


# ---- 0.2 --------------------------------------------------------------------
def fig_reflection():
    # honest: the real functions. A=πr² and r=√(A/π) are exact inverses, so they
    # ARE mirror images across y=x — no scaling fudge, or it wouldn't be true.
    ax = axes_through_origin(xlim=(0, 6), ylim=(0, 6))
    t = np.linspace(0, 6, 300)
    ax.plot(t, np.pi * t**2, color=INK, linewidth=2, label="A = πr²  (radius in → area out)")
    ax.plot(t, np.sqrt(t / np.pi), color=ACCENT, linewidth=2, linestyle="--",
            label="r = √(A/π)  (area in → radius out)")
    ax.plot(t, t, color=COOL, linewidth=1.2, linestyle=":", label="the mirror  y = x")
    ax.legend(loc="lower right", fontsize=9)
    ax.set_title("A rearrangement is a reflection —\nthe two forms are mirror images across y = x")
    save(ax.figure, path("02-rearrange-reflection.png"))


# ---- 0.3 --------------------------------------------------------------------
def fig_factor_roots():
    ax = axes_through_origin(xlim=(-7, 3), ylim=(-4, 12))
    xs = np.linspace(-7, 3, 300)
    ax.plot(xs, xs**2 + 6 * xs + 8, color=INK, linewidth=2)
    for root, lbl, xy in [(-2, "(x+2) → zero here", (-1.4, 4)),
                          (-4, "(x+4) → zero here", (-6.9, 6))]:
        ax.plot(root, 0, "o", color=ACCENT, markersize=9)
        ax.annotate(lbl, (root, 0), xytext=xy, fontsize=9,
                    arrowprops=dict(arrowstyle="->", color=ACCENT))
    ax.set_title("Factoring makes the roots visible:\nx² + 6x + 8 = (x+2)(x+4), crossing at −2 and −4")
    save(ax.figure, path("03-factor-roots.png"))


# ---- 0.4 --------------------------------------------------------------------
def fig_cake_series():
    fig, ax = base((7.5, 4.2))
    n = np.arange(1, 21)
    running = np.cumsum(1 / 2.0**n)
    ax.bar(n, running, color=COOL, alpha=0.75, label="running total")
    ax.axhline(1, color=ACCENT, linestyle="--", linewidth=2, label="the whole cake: 1")
    ax.set_xlabel("pieces taken")
    ax.set_ylim(0, 1.1)
    ax.legend(loc="lower right", fontsize=10)
    ax.set_title("½ + ¼ + ⅛ + … — infinitely many fractions creeping up on one whole cake")
    save(fig, path("04-cake-series.png"))


# ---- 0.5 --------------------------------------------------------------------
def fig_log_unmasks():
    import matplotlib.pyplot as plt
    steps = np.arange(0, 300)
    loss = 6.0 * np.exp(-0.03 * steps)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
    for ax in (ax1, ax2):
        ax.plot(steps, loss, color=ACCENT, linewidth=2)
        ax.set_xlabel("training step")
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        ax.grid(True, alpha=0.25)
    ax1.set_ylabel("loss")
    ax1.set_title("normal scale: a smear along the floor")
    ax2.set_yscale("log")
    ax2.set_title("log scale: the exponential unmasked — a straight line")
    fig.suptitle("Same training loss, two y-axes: why every loss curve is plotted on a log scale",
                 fontsize=12, y=1.03)
    save(fig, path("05-log-unmasks-exponential.png"))


# ---- 0.6 --------------------------------------------------------------------
def fig_sigma_square_wave():
    fig, ax = base((8.5, 4.6))
    xs = np.linspace(0, 4 * np.pi, 2000)
    for K, colour, lw, ls in [(1, COOL, 1.5, ":"), (3, "#7089b0", 1.8, "--"),
                              (30, INK, 2, "-")]:
        wave = np.zeros_like(xs)
        for k in range(1, K + 1):
            wave += np.sin((2 * k - 1) * xs) / (2 * k - 1)
        ax.plot(xs, wave, color=colour, linewidth=lw, linestyle=ls, label=f"K = {K} term(s)")
    ax.legend(loc="upper right", fontsize=10)
    ax.set_title("A Σ of smooth sine waves building a square wave — add more terms, sharper corners")
    save(fig, path("06-sigma-square-wave.png"))


if __name__ == "__main__":
    fig_balance()
    fig_lines_meet()
    fig_reflection()
    fig_factor_roots()
    fig_cake_series()
    fig_log_unmasks()
    fig_sigma_square_wave()
    print("\nModule 0 figures done.")
