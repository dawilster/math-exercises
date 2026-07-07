"""Generate the load-bearing figures for Module 3 (Calculus) lessons.

Run:  uv run python tools/figs/mod03_calculus.py
Writes PNGs into modules/03-calculus/lessons/img/.

Each figure is the paper-and-e-reader version of a plot the notebook builds interactively.
The lesson embeds these; the notebook remains the place to *re-run and fiddle*.
"""
import os
import sys

import numpy as np

sys.path.append(os.path.dirname(__file__))
from _style import INK, ACCENT, COOL, base, save  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "..", "..",
                   "modules", "03-calculus", "lessons", "img")
OUT = os.path.abspath(OUT)
os.makedirs(OUT, exist_ok=True)


def path(name):
    return os.path.join(OUT, name)


def derivative(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h


# ---- 3.1 --------------------------------------------------------------------
def fig_secant_to_tangent():
    """Four panels: as h shrinks, the secant line pivots into the tangent."""
    import matplotlib.pyplot as plt
    x0 = 3.0
    hs = [2, 1, 0.5, 0.1]
    fig, axes = plt.subplots(1, 4, figsize=(12.5, 3.3), sharey=True)
    xs = np.linspace(0, 6, 200)
    for ax, h in zip(axes, hs):
        ax.plot(xs, xs**2, color=INK, linewidth=2)
        slope = ((x0 + h) ** 2 - x0**2) / h
        lx = np.linspace(1.2, 5.3, 2)
        ax.plot(lx, x0**2 + slope * (lx - x0), "--", color=ACCENT, linewidth=2)
        ax.plot([x0, x0 + h], [x0**2, (x0 + h) ** 2], "o", color=ACCENT, markersize=6)
        ax.set_title(f"h = {h}\nslope = {slope:.2f}", fontsize=11)
        ax.grid(True, alpha=0.25)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    axes[0].set_ylabel("f(x) = x²")
    fig.suptitle("Shrink the run h and the shortcut (secant) pivots onto the true slope 6",
                 fontsize=12, y=1.04)
    save(fig, path("01-secant-to-tangent.png"))


def fig_derivative_is_2x():
    """61 nudge-measured slopes of x² land exactly on the line 2x."""
    fig, ax = base((7, 4.4))
    xs = np.linspace(-3, 3, 400)
    ax.plot(xs, xs**2, color=INK, linewidth=2, label="f(x) = x²")
    ax.plot(xs, 2 * xs, color=COOL, linewidth=2, linestyle=":", label="y = 2x (the claim)")
    pts = np.linspace(-3, 3, 61)
    ax.plot(pts, [derivative(lambda t: t**2, x) for x in pts], "o",
            color=ACCENT, markersize=4, label="measured slope at each x")
    ax.set_ylim(-7, 10)
    ax.legend(loc="upper center", frameon=True, fontsize=10)
    ax.set_title("Every measured slope of x² lands on the line 2x — so f'(x) = 2x")
    save(fig, path("01-derivative-is-2x.png"))


def fig_sin_slope_is_cos():
    """The nudge-measured slope of sin is another wave — cos, a quarter-turn ahead."""
    fig, ax = base((8, 4.2))
    xs = np.linspace(0, 4 * np.pi, 300)
    ax.plot(xs, np.sin(xs), color=INK, linewidth=2, label="sin(x)")
    ax.plot(xs, [derivative(np.sin, v) for v in xs], color=ACCENT, linewidth=2,
            linestyle="--", label="its measured slope")
    ax.axhline(0, color="#888", linewidth=0.8)
    ax.legend(loc="upper right", frameon=True, fontsize=10)
    ax.set_title("The slope of a wave is another wave — sin's slope is cos, shifted a quarter-turn")
    save(fig, path("01-sin-slope-is-cos.png"))


# ---- 3.2 --------------------------------------------------------------------
def fig_exp_is_own_slope():
    """The measured slope curve of e^x lies exactly on e^x itself."""
    fig, ax = base((7, 4.4))
    xs = np.linspace(-2, 3, 200)
    ax.plot(xs, np.exp(xs), color=INK, linewidth=6, alpha=0.30, label="e^x")
    ax.plot(xs, [derivative(np.exp, v) for v in xs], color=ACCENT, linewidth=1.8,
            linestyle="--", label="measured slope of e^x")
    ax.legend(loc="upper left", frameon=True, fontsize=11)
    ax.set_title("e^x is its own derivative: the slope curve sits right on the function")
    save(fig, path("02-exp-is-own-slope.png"))


# ---- 3.3 --------------------------------------------------------------------
def fig_vanishing_exploding():
    """Multiplying one sensitivity down a deep pipe: vanish (<1) or explode (>1)."""
    fig, ax = base((8, 4.6))
    depths = np.arange(1, 51)
    styles = {0.8: ":", 0.95: "--", 1.0: "-", 1.05: "--", 1.25: ":"}
    for s, ls in styles.items():
        colour = INK if s == 1.0 else (COOL if s < 1 else ACCENT)
        ax.plot(depths, s**depths, linewidth=2, linestyle=ls, color=colour,
                label=f"each stage × {s}")
    ax.set_yscale("log")
    ax.set_xlabel("pipeline depth (number of stages)")
    ax.set_ylabel("end-to-end sensitivity (log scale)")
    ax.legend(fontsize=9, ncol=2)
    ax.set_title("Multiply 50 sensitivities: below 1 they vanish, above 1 they explode")
    save(fig, path("03-vanishing-exploding.png"))


# ---- 3.4 --------------------------------------------------------------------
def _gradient(f, x, y, h=1e-6):
    return (f(x + h, y) - f(x, y)) / h, (f(x, y + h) - f(x, y)) / h


def fig_gradient_uphill():
    """Contour map of x²+3xy with gradient arrows: each points straight uphill,
    perpendicular to the contour it stands on."""
    import matplotlib.pyplot as plt

    def f(x, y):
        return x**2 + 3 * x * y

    xs = np.linspace(-4, 4, 200)
    X, Y = np.meshgrid(xs, xs)
    fig, ax = plt.subplots(figsize=(6.4, 6.4))
    cs = ax.contour(X, Y, f(X, Y), levels=[-16, -9, -4, -1, 0, 1, 4, 9, 16],
                    colors=COOL, linewidths=1)
    ax.clabel(cs, fontsize=8)
    pts = np.linspace(-3, 3, 7)
    for px in pts:
        for py in pts:
            gx, gy = _gradient(f, px, py)
            ax.arrow(px, py, 0.05 * gx, 0.05 * gy, head_width=0.14,
                     color=ACCENT, alpha=0.9, length_includes_head=True)
    ax.plot(2, 1, "o", color=INK, markersize=7)
    ax.annotate("(2,1): ∇f = (7,6)", (2, 1), xytext=(2.2, 1.5), fontsize=10)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Gradient arrows point straight uphill —\nperpendicular to every contour")
    save(fig, path("04-gradient-uphill.png"))


def fig_saddle():
    """A saddle: x²−y². Arrows flee the origin along x, rush toward it along y —
    flat at the centre but no valley."""
    import matplotlib.pyplot as plt

    def s(x, y):
        return x**2 - y**2

    xs = np.linspace(-4, 4, 200)
    X, Y = np.meshgrid(xs, xs)
    fig, ax = plt.subplots(figsize=(6.4, 6.4))
    cs = ax.contour(X, Y, s(X, Y), levels=[-9, -4, -1, 0, 1, 4, 9],
                    colors=COOL, linewidths=1)
    ax.clabel(cs, fontsize=8)
    pts = np.linspace(-3, 3, 7)
    for px in pts:
        for py in pts:
            gx, gy = _gradient(s, px, py)
            ax.arrow(px, py, 0.05 * gx, 0.05 * gy, head_width=0.14,
                     color=ACCENT, alpha=0.9, length_includes_head=True)
    ax.plot(0, 0, "o", color=INK, markersize=8)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("A saddle point (x²−y²): flat at the centre, but no valley —\narrows flee along x, arrive along y")
    save(fig, path("04-saddle.png"))


# ---- 3.5 --------------------------------------------------------------------
def fig_descent_path():
    """Every footstep of gradient descent on f(x)=x², lr=0.1, from x=4."""
    fig, ax = base((7, 4.6))
    f = lambda x: x**2
    x = 4.0
    lr = 0.1
    trail = [x]
    for _ in range(15):
        x = x - lr * 2 * x
        trail.append(x)
    trail = np.array(trail)
    xs = np.linspace(-4.5, 4.5, 200)
    ax.plot(xs, f(xs), color=INK, linewidth=2)
    ax.plot(trail, f(trail), "o--", color=ACCENT, markersize=6,
            label="the descent, step by step")
    ax.annotate("start", (trail[0], f(trail[0])), xytext=(2.4, 17),
                arrowprops=dict(arrowstyle="->", color=INK))
    ax.legend(loc="upper left", fontsize=10)
    ax.set_title("Gradient descent gliding into the valley of f(x) = x²  (lr = 0.1)")
    save(fig, path("05-descent-path.png"))


def fig_learning_rates():
    """Four learning rates side by side, including the lr=1.05 divergence crash."""
    import matplotlib.pyplot as plt
    f = lambda x: x**2

    def descend(x0, lr, steps=15):
        trail = [x0]
        x = x0
        for _ in range(steps):
            x = x - lr * 2 * x
            trail.append(x)
        return np.array(trail)

    fig, axes = plt.subplots(1, 4, figsize=(13.5, 3.4), sharex=False)
    for ax, lr in zip(axes, [0.01, 0.1, 0.9, 1.05]):
        trail = descend(4.0, lr)
        span = max(4.5, np.abs(trail).max() * 1.1)
        gx = np.linspace(-span, span, 200)
        ax.plot(gx, f(gx), color=INK, linewidth=1.5)
        ax.plot(trail, f(trail), "o--", color=ACCENT, markersize=4)
        verdict = {0.01: "too slow", 0.1: "just right",
                   0.9: "bounces, shrinks", 1.05: "DIVERGES"}[lr]
        ax.set_title(f"lr = {lr}\n{verdict}", fontsize=11)
        ax.grid(True, alpha=0.25)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    fig.suptitle("The learning rate is everything: crawl, glide, bounce, or explode",
                 fontsize=12, y=1.05)
    save(fig, path("05-learning-rates.png"))


def fig_bowl_descent():
    """Descent across a 2-parameter bowl L(w,b), the path curving down the contours."""
    import matplotlib.pyplot as plt

    # an ELONGATED bowl (steeper in b than w). A circular bowl would give a
    # dead-straight path; the ellipse makes descent zig-zag and curve toward the
    # minimum, crossing each contour at a right angle — the interesting case.
    def L(w, b):
        return (w - 2) ** 2 + 6 * (b + 1) ** 2

    w, b = -4.0, 5.0
    lr, h = 0.12, 1e-6
    trail = [(w, b)]
    for _ in range(40):
        dw = (L(w + h, b) - L(w, b)) / h
        db = (L(w, b + h) - L(w, b)) / h
        w, b = w - lr * dw, b - lr * db
        trail.append((w, b))
    trail = np.array(trail)
    grid = np.linspace(-5, 8, 200)
    W, B = np.meshgrid(grid, grid)
    fig, ax = plt.subplots(figsize=(6.6, 6.6))
    cs = ax.contour(W, B, L(W, B), levels=[1, 4, 10, 20, 40, 70, 110, 160],
                    colors=COOL, linewidths=1)
    ax.clabel(cs, fontsize=8)
    ax.plot(trail[:, 0], trail[:, 1], "o-", color=ACCENT, markersize=4,
            label="descent path")
    ax.plot(2, -1, "*", color=INK, markersize=16, label="minimum (2, −1)")
    ax.legend(loc="upper right", fontsize=10)
    ax.set_aspect("equal")
    ax.set_xlabel("w")
    ax.set_ylabel("b")
    ax.set_title("Descending a 2-parameter bowl: the path zig-zags down toward the minimum")
    save(fig, path("05-bowl-descent.png"))


if __name__ == "__main__":
    fig_secant_to_tangent()
    fig_derivative_is_2x()
    fig_sin_slope_is_cos()
    fig_exp_is_own_slope()
    fig_saddle()
    fig_vanishing_exploding()
    fig_gradient_uphill()
    fig_descent_path()
    fig_learning_rates()
    fig_bowl_descent()
    print("\nModule 3 figures done.")
