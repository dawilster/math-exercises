"""Wonder figures for the Interludes.

Run:  uv run python tools/figs/mod_interludes.py
Writes into modules/interludes/lessons/img/.

These are deliberately colourful 'wonder art' — the whole point of an interlude. They
preview what William builds himself in the notebook, so the beauty survives on the
e-reader too (where there is no notebook to run).
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(__file__)
sys.path.append(HERE)
sys.path.append(os.path.join(HERE, ".."))
from _style import INK, save  # noqa: E402

OUT = os.path.abspath(os.path.join(HERE, "..", "..",
                      "modules", "interludes", "lessons", "img"))
os.makedirs(OUT, exist_ok=True)

PURPLE = "#8e44ad"


def path(name):
    return os.path.join(OUT, name)


# ---- I.1 --------------------------------------------------------------------
def fig_golden_spiral():
    import matplotlib.pyplot as plt
    phi = (1 + np.sqrt(5)) / 2
    theta = np.linspace(0, 8 * np.pi, 2000)
    r = phi ** (theta / (np.pi / 2))
    fig, ax = plt.subplots(figsize=(6.5, 6.5))
    ax.plot(r * np.cos(theta), r * np.sin(theta), color=PURPLE, linewidth=2.5)
    ax.axis("equal")
    ax.axis("off")
    ax.set_title("The golden spiral — grow by φ every quarter turn")
    save(fig, path("01-golden-spiral.png"))


def fig_sunflower():
    import matplotlib.pyplot as plt
    n = np.arange(1, 2000)
    theta = n * np.deg2rad(137.5)
    r = np.sqrt(n)
    fig, ax = plt.subplots(figsize=(6.5, 6.5))
    ax.scatter(r * np.cos(theta), r * np.sin(theta), s=14, c=n, cmap="twilight", edgecolors="none")
    ax.axis("equal")
    ax.axis("off")
    ax.set_title("A sunflower seed head, grown from one rule: seed n at angle n × 137.5°")
    save(fig, path("01-sunflower.png"))


# ---- I.2 --------------------------------------------------------------------
def fig_bifurcation():
    import matplotlib.pyplot as plt
    r = np.linspace(2.5, 4.0, 2000)
    x = np.full_like(r, 0.2)
    for _ in range(500):
        x = r * x * (1 - x)
    fig, ax = plt.subplots(figsize=(10, 6.5))
    for _ in range(300):
        x = r * x * (1 - x)
        ax.plot(r, x, ",", color="#2d1e50", alpha=0.25)
    ax.set_xlabel("growth rate  r")
    ax.set_ylabel("long-term population")
    ax.set_title("The bifurcation diagram — one quadratic, iterated: calm splits to chaos")
    save(fig, path("02-bifurcation.png"))


def fig_butterfly():
    import matplotlib.pyplot as plt
    r = 3.9
    a, b = 0.2, 0.2 + 1e-9
    ha, hb = [], []
    for _ in range(60):
        a, b = r * a * (1 - a), r * b * (1 - b)
        ha.append(a)
        hb.append(b)
    fig, (top, bot) = plt.subplots(2, 1, figsize=(10, 5.6), sharex=True)
    top.plot(ha, linewidth=1.4, color=INK, label="starts at 0.2")
    top.plot(hb, linewidth=1.4, color="#c0392b", label="starts at 0.2 + one billionth")
    top.legend(frameon=False, fontsize=9)
    top.set_title("The butterfly effect: identical twins… for about 30 steps")
    diff = np.abs(np.array(ha) - np.array(hb))
    bot.semilogy(diff, color="#c0392b", linewidth=1.4)
    bot.set_title("gap between them (log scale) — a straight line means EXPONENTIAL divergence")
    bot.set_xlabel("step")
    for ax in (top, bot):
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    save(fig, path("02-butterfly.png"))


# ---- I.3 --------------------------------------------------------------------
def _mandelbrot(x0, x1, y0, y1, width=900, steps=100):
    height = int(width * (y1 - y0) / (x1 - x0))
    re = np.linspace(x0, x1, width)
    im = np.linspace(y0, y1, height)
    c = re[None, :] + 1j * im[:, None]
    z = np.zeros_like(c)
    escaped = np.zeros(c.shape)
    for step in range(1, steps + 1):
        alive = escaped == 0
        z[alive] = z[alive] ** 2 + c[alive]
        escaped[alive & (np.abs(z) > 2)] = step
    return escaped


def fig_mandelbrot_full():
    import matplotlib.pyplot as plt
    pic = _mandelbrot(-2.5, 1.0, -1.3125, 1.3125, width=900, steps=100)
    fig, ax = plt.subplots(figsize=(9, 6.8))
    ax.imshow(pic, cmap="twilight_shifted", origin="lower", extent=[-2.5, 1.0, -1.3125, 1.3125])
    ax.axis("off")
    ax.set_title("The Mandelbrot set — z → z² + c, nothing else")
    save(fig, path("03-mandelbrot.png"))


def fig_seahorse():
    import matplotlib.pyplot as plt
    zoom = _mandelbrot(-0.78, -0.72, 0.075, 0.12, width=900, steps=300)
    fig, ax = plt.subplots(figsize=(9, 6.8))
    ax.imshow(zoom, cmap="magma", origin="lower", extent=[-0.78, -0.72, 0.075, 0.12])
    ax.axis("off")
    ax.set_title("Seahorse valley — a zoom into the boundary, invisible in the whole-set view")
    save(fig, path("03-seahorse.png"))


# ---- I.4 --------------------------------------------------------------------
def fig_walkers():
    import matplotlib.pyplot as plt
    rng = np.random.default_rng(42)
    walks = np.cumsum(rng.choice([-1, 1], size=(200, 5_000)), axis=1)
    n = np.arange(1, 5_001)
    fig, ax = plt.subplots(figsize=(10, 5))
    for w, colour in zip(walks, plt.cm.viridis(np.linspace(0, 1, 200))):
        ax.plot(w, color=colour, linewidth=0.4, alpha=0.35)
    ax.plot(n, np.sqrt(n), color=INK, linewidth=2, label="±√n")
    ax.plot(n, -np.sqrt(n), color=INK, linewidth=2)
    ax.legend(frameon=False)
    ax.set_xlabel("step")
    ax.set_ylabel("position")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.set_title("200 random walkers — the cloud spreads exactly like √n")
    save(fig, path("04-walkers.png"))


def fig_brownian():
    import matplotlib.pyplot as plt
    rng = np.random.default_rng(7)
    xy = np.cumsum(rng.choice([-1, 1], size=(30_000, 2)), axis=0)
    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    ax.scatter(xy[:, 0], xy[:, 1], c=np.arange(len(xy)), cmap="twilight", s=0.5)
    ax.axis("equal")
    ax.axis("off")
    ax.set_title("Brownian motion — a 30,000-step 2-D walk, coloured by time")
    save(fig, path("04-brownian.png"))


# ---- I.5 --------------------------------------------------------------------
def fig_galton_emergence():
    import matplotlib.pyplot as plt
    rng = np.random.default_rng(42)
    slots = (rng.random((100_000, 12)) < 0.5).sum(axis=1)
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.8), sharey=True)
    for ax, n in zip(axes, [100, 2_000, 100_000]):
        ax.hist(slots[:n], bins=np.arange(14) - 0.5, density=True, color=PURPLE, edgecolor="white")
        ax.set_title(f"{n:,} balls")
        ax.set_xlabel("slot")
        for s in ("top", "right", "left"):
            ax.spines[s].set_visible(False)
        ax.set_yticks([])
    fig.suptitle("The same bell curve emerging from noise as the ball count grows", y=1.03, fontsize=12)
    save(fig, path("05-galton-emergence.png"))


def fig_galton_theory():
    import matplotlib.pyplot as plt
    rng = np.random.default_rng(42)
    n_rows = 12
    slots = (rng.random((100_000, n_rows)) < 0.5).sum(axis=1)
    mu = n_rows / 2
    sigma = np.sqrt(n_rows / 4)
    x = np.linspace(0, 12, 400)
    bell = np.exp(-((x - mu) ** 2) / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(slots, bins=np.arange(14) - 0.5, density=True, color=PURPLE, alpha=0.55,
            edgecolor="white", label="100,000 simulated balls")
    ax.plot(x, bell, color=INK, linewidth=2.5, label="the Gaussian — pen-and-paper theory")
    ax.legend(frameon=False)
    ax.set_xlabel("slot")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.set_title("Simulation meets theory: a formula written by hand lands on the simulated pile")
    save(fig, path("05-galton-theory.png"))


if __name__ == "__main__":
    fig_golden_spiral()
    fig_sunflower()
    fig_bifurcation()
    fig_butterfly()
    fig_mandelbrot_full()
    fig_seahorse()
    fig_walkers()
    fig_brownian()
    fig_galton_emergence()
    fig_galton_theory()
    print("\nInterlude figures done.")
