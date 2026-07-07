"""Load-bearing figures for Module 4 (Probability & Statistics) lessons.

Run:  uv run python tools/figs/mod04_probstats.py
Writes into modules/04-probability-stats/lessons/img/.
All randomness is seeded (default_rng(42)) so figures are reproducible.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(__file__)
sys.path.append(HERE)
sys.path.append(os.path.join(HERE, ".."))
from _style import INK, ACCENT, COOL, base, save  # noqa: E402

OUT = os.path.abspath(os.path.join(HERE, "..", "..",
                      "modules", "04-probability-stats", "lessons", "img"))
os.makedirs(OUT, exist_ok=True)


def path(name):
    return os.path.join(OUT, name)


def rng():
    return np.random.default_rng(42)


# ---- 4.1 --------------------------------------------------------------------
def fig_law_large_numbers():
    fig, ax = base((8, 4.2))
    flips = rng().integers(0, 2, size=10_000)
    frac = np.cumsum(flips) / np.arange(1, 10_001)
    ax.plot(frac, color=INK, linewidth=1)
    ax.axhline(0.5, color=ACCENT, linestyle="--", linewidth=2, label="0.5 — the claimed probability")
    ax.set_xscale("log")
    ax.set_xlabel("number of flips (log scale)")
    ax.set_ylabel("fraction of heads so far")
    ax.legend(fontsize=10)
    ax.set_title("Wild early, lawful later: the running fraction settles onto 0.5")
    save(fig, path("01-law-of-large-numbers.png"))


def fig_dice_sum():
    fig, ax = base((7.5, 4.2))
    r = rng().integers(1, 7, size=(1_000_000, 2))
    sums = r[:, 0] + r[:, 1]
    ax.hist(sums, bins=np.arange(1.5, 13.5), color=COOL, edgecolor="white")
    ax.set_xlabel("sum of two dice")
    ax.set_ylabel("count in a million rolls")
    ax.set_xticks(range(2, 13))
    ax.set_title("The 11 sums are NOT equally likely — seven has the most pairs (6 of them)")
    save(fig, path("01-dice-sum.png"))


# ---- 4.2 --------------------------------------------------------------------
def fig_normalise_scatter():
    import matplotlib.pyplot as plt
    r = rng()
    income = r.normal(70_000, 15_000, size=500)
    height = r.normal(178, 7, size=500)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4))
    ax1.scatter(income, height, s=8, color=COOL)
    ax1.set_xlabel("income ($)")
    ax1.set_ylabel("height (cm)")
    ax1.set_title("RAW: dollars dwarf centimetres")
    ax1.axis("equal")
    zi = (income - income.mean()) / income.std()
    zh = (height - height.mean()) / height.std()
    ax2.scatter(zi, zh, s=8, color=ACCENT)
    ax2.set_xlabel("income (z-score)")
    ax2.set_ylabel("height (z-score)")
    ax2.set_title("NORMALISED: both centre 0, spread 1")
    ax2.axis("equal")
    for ax in (ax1, ax2):
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    fig.suptitle("Normalising = give every feature its z-score, so a network sees them on equal terms",
                 y=1.02, fontsize=12)
    save(fig, path("02-normalise-scatter.png"))


# ---- 4.3 --------------------------------------------------------------------
def fig_clt():
    import matplotlib.pyplot as plt
    r = rng()
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.6))
    for ax, n_dice in zip(axes, [1, 2, 10]):
        rolls = r.integers(1, 7, size=(200_000, n_dice))
        sums = rolls.sum(axis=1)
        ax.hist(sums, bins=np.arange(n_dice - 0.5, 6 * n_dice + 1.5),
                color=COOL, edgecolor="white")
        ax.set_title(f"sum of {n_dice} {'die' if n_dice == 1 else 'dice'}", fontsize=11)
        ax.set_xlabel("total")
        for s in ("top", "right", "left"):
            ax.spines[s].set_visible(False)
        ax.set_yticks([])
    fig.suptitle("Flat → triangle → BELL: add up more small random things and a bell appears (the CLT)",
                 y=1.02, fontsize=12)
    save(fig, path("03-clt-emergence.png"))


def fig_68_95_997():
    fig, ax = base((8, 4.2))
    mu, sigma = 178, 7
    heights = rng().normal(mu, sigma, size=1_000_000)
    ax.hist(heights, bins=120, color=COOL, edgecolor="none")
    ax.axvline(mu, color=ACCENT, linewidth=2)
    for k in [-3, -2, -1, 1, 2, 3]:
        ax.axvline(mu + k * sigma, color=ACCENT, linestyle=":", linewidth=1)
    for k, lbl in [(1, "68%"), (2, "95%"), (3, "99.7%")]:
        ax.annotate(f"±{k}σ\n{lbl}", (mu + 0, 0), xytext=(mu - k * sigma + 0.3, 5000),
                    fontsize=8, color=INK)
    ax.set_xlabel("height (cm)")
    ax.set_yticks([])
    ax.set_title("One million heights, N(178, 7): the 68 / 95 / 99.7 rule, drawn")
    save(fig, path("03-68-95-997.png"))


def fig_dials():
    fig, ax = base((8.5, 4.4))
    z = rng().normal(0, 1, size=200_000)
    ax.hist(z, bins=120, density=True, alpha=0.55, color=INK, label="N(0, 1)  standard")
    ax.hist(3 + z, bins=120, density=True, alpha=0.55, color=ACCENT, label="N(3, 1)  μ shifts it →")
    ax.hist(2 * z, bins=120, density=True, alpha=0.55, color=COOL, label="N(0, 2)  σ widens it")
    ax.legend(fontsize=10)
    ax.set_yticks([])
    ax.set_title("Same bell, two dials: μ slides it left/right, σ widens it (and lowers the peak)")
    save(fig, path("03-mu-sigma-dials.png"))


# ---- 4.4 --------------------------------------------------------------------
def fig_sqrt_n():
    fig, ax = base((7.5, 4.4))
    r = rng()
    sizes = np.array([10, 100, 1_000, 10_000, 100_000])
    wobbles = []
    for n in sizes:
        flips = r.integers(0, 2, size=(2_000, n))
        wobbles.append(flips.mean(axis=1).std())
    ax.loglog(sizes, wobbles, "o-", color=ACCENT, label="measured wobble")
    ax.loglog(sizes, 0.5 / np.sqrt(sizes), "--", color=INK, label="the 1/√n prediction")
    ax.set_xlabel("sample size n")
    ax.set_ylabel("wobble of the estimate")
    ax.legend(fontsize=10)
    ax.set_title("10× the data → only √10 ≈ 3.16× steadier. More data helps, but slowly.")
    save(fig, path("04-sqrt-n.png"))


# ---- 4.5 --------------------------------------------------------------------
def fig_surprise():
    fig, ax = base((8, 4.4))
    p = np.linspace(0.01, 1, 500)
    ax.plot(p, -np.log(p), color=INK, linewidth=2)
    for prob, note in [(0.9, "expected → mild"), (0.5, "coin flip"),
                       (0.1, "rare → big"), (0.02, "'impossible' → huge")]:
        ax.plot(prob, -np.log(prob), "o", color=ACCENT)
        ax.annotate(f"p={prob}: {note}", (prob, -np.log(prob)),
                    xytext=(prob + 0.04, -np.log(prob) + 0.25), fontsize=9)
    ax.set_xlabel("probability the model gave the TRUE outcome")
    ax.set_ylabel("surprise = −ln p  (= the loss)")
    ax.set_title("Cross-entropy is surprise: certainty is free, 'impossible-but-it-happened' costs everything")
    save(fig, path("05-surprise.png"))


def fig_likelihood_scan():
    fig, ax = base((8, 4.4))
    r = rng()
    secret_p = 0.7
    flips = r.random(50) < secret_p
    heads = int(flips.sum())
    tails = 50 - heads
    grid = np.linspace(0.01, 0.99, 500)
    logL = heads * np.log(grid) + tails * np.log(1 - grid)
    best = grid[np.argmax(logL)]
    ax.plot(grid, logL, color=INK, linewidth=2)
    ax.axvline(best, color=ACCENT, linestyle="--", label=f"most likely model: p = {best:.2f}")
    ax.axvline(secret_p, color=COOL, linestyle=":", linewidth=2, label=f"the hidden truth: p = {secret_p}")
    ax.set_xlabel("candidate model's claimed P(heads)")
    ax.set_ylabel("log-likelihood of the observed flips")
    ax.legend(fontsize=10, loc="lower center")
    ax.set_title(f"Score every model against {heads} heads / {tails} tails → the data points at the truth")
    save(fig, path("05-likelihood-scan.png"))


if __name__ == "__main__":
    fig_law_large_numbers()
    fig_dice_sum()
    fig_normalise_scatter()
    fig_clt()
    fig_68_95_997()
    fig_dials()
    fig_sqrt_n()
    fig_surprise()
    fig_likelihood_scan()
    print("\nModule 4 figures done.")
