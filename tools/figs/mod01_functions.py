"""Load-bearing figures for Module 1 (Functions & Graphs) lessons.

Run:  uv run python tools/figs/mod01_functions.py
Writes into modules/01-functions-and-graphs/lessons/img/.

This is the graph module, so the figures ARE the lesson. Multi-curve plots use a
grayscale-safe cycle (distinct linestyle + lightness) so they read on the e-reader.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(__file__)
sys.path.append(HERE)
sys.path.append(os.path.join(HERE, ".."))
from _style import INK, ACCENT, COOL, base, save  # noqa: E402
from plots import axes_through_origin  # noqa: E402

OUT = os.path.abspath(os.path.join(HERE, "..", "..",
                      "modules", "01-functions-and-graphs", "lessons", "img"))
os.makedirs(OUT, exist_ok=True)

# grayscale-safe cycle: (colour, linestyle)
CYCLE = [(INK, "-"), (ACCENT, "--"), (COOL, "-."), ("#7a5c9e", ":"), ("#2f8f6b", (0, (5, 1)))]


def path(name):
    return os.path.join(OUT, name)


def curves(items, xlim, ylim, title, n=800, legend="upper left", figsize=None):
    """items: list of (label, fn). Clips blow-ups. Returns the axis."""
    ax = axes_through_origin(xlim=xlim, ylim=ylim)
    if figsize:
        ax.figure.set_size_inches(*figsize)
    x = np.linspace(xlim[0], xlim[1], n)
    for i, (label, fn) in enumerate(items):
        colour, ls = CYCLE[i % len(CYCLE)]
        with np.errstate(all="ignore"):
            y = fn(x)
        y = np.where((y < ylim[0] - 1) | (y > ylim[1] + 1), np.nan, y)
        ax.plot(x, y, color=colour, linestyle=ls, linewidth=2, label=label)
    ax.legend(loc=legend, fontsize=9, frameon=True)
    ax.set_title(title, fontsize=11)
    return ax


# ---- 1.2 --------------------------------------------------------------------
def fig_zoo():
    ax = curves([
        ("linear: 2x − 1", lambda x: 2 * x - 1),
        ("quadratic: x² − 4", lambda x: x**2 - 4),
        ("exponential: 2^x", lambda x: 2.0**x),
        ("log: log₂ x", lambda x: np.log2(x)),
        ("reciprocal: 1/x", lambda x: 1 / x),
    ], xlim=(-6, 6), ylim=(-6, 8),
       title="The Shape Zoo — five species that cover almost all of ML")
    save(ax.figure, path("02-shape-zoo.png"))


def fig_exp_log_mirror():
    ax = curves([
        ("y = 2^x  (explodes)", lambda x: 2.0**x),
        ("y = log₂ x  (flattens)", lambda x: np.log2(x)),
        ("the mirror  y = x", lambda x: x),
    ], xlim=(-6, 6), ylim=(-6, 6),
       title="Exp and log are mirror images across y = x —\none explodes, the other tames it")
    save(ax.figure, path("02-exp-log-mirror.png"))


def fig_healthy_loss():
    # deterministic 'noise' so the figure is reproducible without Math.random-style calls
    fig, ax = base((8, 4.2))
    epochs = np.linspace(0, 10, 200)
    wobble = 0.03 * np.sin(epochs * 7.3) * np.cos(epochs * 2.1)
    loss = 2.5 * np.exp(-0.6 * epochs) + 0.1 + wobble
    ax.plot(epochs, loss, color=ACCENT, linewidth=1.6)
    ax.axhline(0.1, color=INK, linestyle="--", alpha=0.7, label="floor: as good as this model gets")
    ax.set_xlabel("epochs (passes through the data)")
    ax.set_ylabel("loss (how wrong the model is)")
    ax.legend(fontsize=10)
    ax.set_title("A healthy training run — exponential decay toward a floor. Learn it on sight.")
    save(fig, path("02-healthy-loss-curve.png"))


# ---- 1.3 --------------------------------------------------------------------
def fig_up_vs_left():
    f = lambda x: x**2
    ax = curves([
        ("f(x) = x²", f),
        ("f(x) + 3  → UP 3 (intuitive)", lambda x: f(x) + 3),
        ("f(x + 3)  → LEFT 3 (opposite day!)", lambda x: f(x + 3)),
    ], xlim=(-8, 8), ylim=(-2, 10),
       title="Outside the brackets shifts UP; inside the brackets shifts LEFT")
    save(ax.figure, path("03-up-vs-left.png"))


def fig_normalise():
    import matplotlib.pyplot as plt
    rng = np.random.default_rng(42)
    heights = rng.normal(175, 8, size=500)
    z = (heights - heights.mean()) / heights.std()
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
    axes[0].hist(heights, bins=30, color=COOL, alpha=0.85)
    axes[0].set_title(f"raw data: centre ≈ {heights.mean():.0f} cm, spread ≈ {heights.std():.1f}")
    axes[1].hist(z, bins=30, color=ACCENT, alpha=0.85)
    axes[1].set_title(f"normalised: centre ≈ {z.mean():.2f}, spread ≈ {z.std():.2f}")
    for ax in axes:
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    fig.suptitle("Normalising a dataset = shift (unit 1.3) so centre is 0, stretch so spread is 1",
                 fontsize=12, y=1.02)
    save(fig, path("03-normalise.png"))


# ---- 1.4 --------------------------------------------------------------------
def fig_order_matters():
    f = lambda x: x**2
    g = lambda x: x + 3
    ax = curves([
        ("f(g(x)) = (x+3)²  → valley at x = −3", lambda x: f(g(x))),
        ("g(f(x)) = x² + 3  → floats at y = 3", lambda x: g(f(x))),
    ], xlim=(-8, 5), ylim=(-1, 15),
       title="Order matters: 'add 3 then square' ≠ 'square then add 3'")
    save(ax.figure, path("04-order-matters.png"))


def fig_self_feeding():
    fig, ax = base((7.5, 3.8))
    f = lambda x: x / 2 + 1
    x = 0.0
    traj = [x]
    for _ in range(15):
        x = f(x)
        traj.append(x)
    ax.plot(traj, "o-", color=ACCENT, markersize=5)
    ax.axhline(2, color=INK, linestyle="--", label="fixed point x* = 2, where f(x*) = x*")
    ax.set_xlabel("iteration")
    ax.set_ylabel("x")
    ax.legend(fontsize=10)
    ax.set_title("A machine fed its own output: f(x) = x/2 + 1 settles onto 2 and stays")
    save(fig, path("04-self-feeding.png"))


def fig_chaos_glimpse():
    fig, ax = base((8.5, 4.2))
    logistic = lambda x: 3.9 * x * (1 - x)

    def run(x0, n=60):
        xs = [x0]
        for _ in range(n):
            xs.append(logistic(xs[-1]))
        return xs
    ax.plot(run(0.500000), color=INK, linewidth=1.3, label="start at 0.500000")
    ax.plot(run(0.500001), color=ACCENT, linewidth=1.3, linestyle="--",
            label="start at 0.500001 (a millionth apart)")
    ax.set_xlabel("iteration")
    ax.set_ylabel("x")
    ax.legend(fontsize=10)
    ax.set_title("The other kind of self-feeding: identical for ~30 steps, then total divergence — chaos")
    save(fig, path("04-chaos-glimpse.png"))


# ---- 1.5 --------------------------------------------------------------------
sigmoid = lambda x: 1 / (1 + np.exp(-x))
relu = lambda x: np.maximum(0, x)


def fig_activation_trio():
    import matplotlib.pyplot as plt
    ax = curves([
        ("sigmoid σ(x) → (0,1)", sigmoid),
        ("tanh(x) → (−1,1)", np.tanh),
        ("ReLU(x) → flat then ramp", relu),
    ], xlim=(-6, 6), ylim=(-2, 4),
       title="The three activation functions that run modern AI")
    for lvl in (0, 1, -1):
        ax.axhline(lvl, color="gray", linestyle=":", alpha=0.4, linewidth=1)
    save(ax.figure, path("05-activation-trio.png"))


def fig_linear_collapse():
    L1 = lambda x: 2 * x + 1
    L2 = lambda x: -0.5 * x + 3
    L3 = lambda x: 1.5 * x - 2
    L4 = lambda x: 0.8 * x + 0.3
    L5 = lambda x: -1.2 * x + 1
    tower = lambda x: L5(L4(L3(L2(L1(x)))))
    tower_relu = lambda x: L5(relu(L4(relu(L3(relu(L2(relu(L1(x)))))))))
    ax = curves([
        ("5 linear layers → still ONE straight line", tower),
        ("same 5 layers + ReLU between → structure!", tower_relu),
    ], xlim=(-6, 6), ylim=(-10, 10),
       title="Why activations exist: linear layers collapse to a ruler;\na kink between them buys real shape")
    save(ax.figure, path("05-linear-collapse.png"))


def fig_relu_approx():
    target = lambda x: x**2 / 8 - 1
    approx = lambda x: (-1 + 0.25 * relu(-x - 1) + 0.75 * relu(-x - 2.5)
                        + 0.25 * relu(x - 1) + 0.75 * relu(x - 2.5)
                        + 0.05 * relu(x) + 0.05 * relu(-x))
    ax = curves([
        ("target curve", target),
        ("six ReLUs, shifted / scaled / added", approx),
    ], xlim=(-5, 5), ylim=(-3, 3),
       title="Six kinks approximating a curve. Thousands of kinks + training = deep learning.")
    save(ax.figure, path("05-relu-approx.png"))


if __name__ == "__main__":
    fig_zoo()
    fig_exp_log_mirror()
    fig_healthy_loss()
    fig_up_vs_left()
    fig_normalise()
    fig_order_matters()
    fig_self_feeding()
    fig_chaos_glimpse()
    fig_activation_trio()
    fig_linear_collapse()
    fig_relu_approx()
    print("\nModule 1 figures done.")
