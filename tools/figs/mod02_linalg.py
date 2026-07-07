"""Load-bearing figures for Module 2 (Linear Algebra) lessons.

Run:  uv run python tools/figs/mod02_linalg.py
Writes into modules/02-linear-algebra/lessons/img/.
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
                      "modules", "02-linear-algebra", "lessons", "img"))
os.makedirs(OUT, exist_ok=True)


def path(name):
    return os.path.join(OUT, name)


def arrow(ax, v, color=INK, label=None, start=(0, 0), width=0.013, ls="solid"):
    ax.quiver(start[0], start[1], v[0], v[1], angles="xy", scale_units="xy",
              scale=1, color=color, width=width, linestyle=ls)
    if label:
        ax.annotate(label, (start[0] + v[0], start[1] + v[1]),
                    textcoords="offset points", xytext=(6, 6), color=color, fontsize=11)


# ---- 2.1 --------------------------------------------------------------------
def fig_magnitude():
    ax = axes_through_origin(xlim=(-1, 6), ylim=(-1, 6))
    arrow(ax, [3, 4], ACCENT, "(3, 4)")
    # the 3-4-5 triangle legs
    ax.plot([0, 3], [0, 0], color=COOL, linewidth=2, linestyle="--")
    ax.plot([3, 3], [0, 4], color=COOL, linewidth=2, linestyle="--")
    ax.annotate("3", (1.5, -0.4), color=COOL, fontsize=12, ha="center")
    ax.annotate("4", (3.3, 2), color=COOL, fontsize=12)
    ax.annotate("|v| = √(3²+4²) = 5", (1.2, 3.2), color=ACCENT, fontsize=11)
    ax.set_title("A vector's length is just Pythagoras: the arrow is the hypotenuse")
    save(ax.figure, path("01-magnitude-triangle.png"))


def fig_taste_space():
    users = {"Ana": [9, 1], "Raj": [8, 2], "Mei": [1, 8], "Drew": [4, 4]}
    colours = [ACCENT, "#e0693e", COOL, "#7a5c9e"]
    ax = axes_through_origin(xlim=(-1, 10), ylim=(-1, 10))
    for (name, vec), c in zip(users.items(), colours):
        arrow(ax, vec, c, name)
    ax.set_xlabel("sci-fi hours")
    ax.set_ylabel("comedy hours")
    ax.set_title("People as arrows in 'taste space' — Ana and Raj point almost the same way")
    save(ax.figure, path("01-taste-space.png"))


# ---- 2.2 --------------------------------------------------------------------
def fig_tip_to_tail():
    a = np.array([3, 1])
    b = np.array([1, 2])
    ax = axes_through_origin(xlim=(-1, 6), ylim=(-1, 6))
    arrow(ax, a, INK, "a")
    arrow(ax, b, COOL, "b  (from a's tip)", start=a)
    arrow(ax, a + b, ACCENT, "a + b")
    ax.set_title("Adding vectors = tip-to-tail = adding components. Always the same answer.")
    save(ax.figure, path("02-tip-to-tail.png"))


def fig_king_queen():
    # the four known words, labelled clear of each other
    words = {"king": ([9, 0], (6, -14)), "man": ([1, 0], (6, -14)),
             "woman": ([1, 1], (6, 6)), "queen": ([9, 1], (10, 6))}
    ax = axes_through_origin(xlim=(-1, 11.5), ylim=(-1, 3))
    for name, (vec, off) in words.items():
        ax.quiver(0, 0, vec[0], vec[1], angles="xy", scale_units="xy", scale=1,
                  color=COOL, width=0.011)
        ax.annotate(name, vec, textcoords="offset points", xytext=off, color=COOL, fontsize=11)
    res = np.array([9, 0]) - np.array([1, 0]) + np.array([1, 1])   # = (9, 1) = queen
    ax.quiver(0, 0, res[0], res[1], angles="xy", scale_units="xy", scale=1,
              color=ACCENT, width=0.017)
    ax.annotate("king − man + woman\n= queen ✓", (res[0], res[1]),
                textcoords="offset points", xytext=(-70, 18), color=ACCENT, fontsize=10)
    ax.set_title("king − man + woman lands exactly on queen — meaning becomes arithmetic")
    save(ax.figure, path("02-king-queen.png"))


# ---- 2.3 --------------------------------------------------------------------
def fig_dot_compass():
    import matplotlib.pyplot as plt
    fixed = np.array([2.0, 1.0])
    ax = axes_through_origin(xlim=(-3, 3), ylim=(-3, 3))
    for t in np.linspace(0, 2 * np.pi, 24, endpoint=False):
        v = 2 * np.array([np.cos(t), np.sin(t)])
        score = fixed @ v
        colour = plt.cm.coolwarm((score + 5) / 10)
        ax.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1,
                  color=colour, width=0.008)
    ax.quiver(0, 0, fixed[0], fixed[1], angles="xy", scale_units="xy", scale=1,
              color=INK, width=0.016)
    ax.set_title("Dot product with the black arrow:\nred = aligned (big +), pale = perpendicular (0), blue = opposite (−)")
    save(ax.figure, path("03-dot-compass.png"))


def fig_highdim_perp():
    fig, ax = base((7.5, 4.2))
    rng = np.random.default_rng(42)
    dims = [2, 10, 100, 768]
    means = []
    for dim in dims:
        sims = []
        for _ in range(400):
            u = rng.standard_normal(dim)
            v = rng.standard_normal(dim)
            sims.append(abs((u @ v) / (np.linalg.norm(u) * np.linalg.norm(v))))
        means.append(np.mean(sims))
    ax.bar([str(d) for d in dims], means, color=COOL, alpha=0.85)
    for i, m in enumerate(means):
        ax.annotate(f"{m:.2f}", (i, m), textcoords="offset points", xytext=(0, 4),
                    ha="center", fontsize=10)
    ax.set_xlabel("dimensions")
    ax.set_ylabel("avg |cosine| of random pairs")
    ax.set_title("In high dimensions, random arrows are nearly perpendicular —\nroom for every word to mean something different")
    save(fig, path("03-highdim-perpendicular.png"))


# ---- 2.4 --------------------------------------------------------------------
HOUSE = np.array([[0, 2, 2, 1, 0, 0], [0, 0, 2, 3, 2, 0]])


def fig_house_transforms():
    import matplotlib.pyplot as plt
    machines = {
        "stretch x by 2": np.array([[2, 0], [0, 1]]),
        "rotate 90°": np.array([[0, -1], [1, 0]]),
        "shear": np.array([[1, 0.5], [0, 1]]),
    }
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.2))
    for ax, (name, M) in zip(axes, machines.items()):
        new = M @ HOUSE
        ax.plot(HOUSE[0], HOUSE[1], "o-", color=COOL, label="before")
        ax.plot(new[0], new[1], "o-", color=ACCENT, label="after")
        ax.set_title(f"{name}\n{M.tolist()}", fontsize=10)
        ax.grid(alpha=0.3)
        ax.set_aspect("equal")
        ax.legend(fontsize=9)
        ax.set_xlim(-4, 5)
        ax.set_ylim(-1, 4)
    fig.suptitle("One matrix × every corner = the whole shape transformed at once", y=1.02, fontsize=12)
    save(fig, path("04-house-transforms.png"))


def fig_unit_decoder():
    M = np.array([[2, 0.5], [0, 1.0]])
    ax = axes_through_origin(xlim=(-1, 3), ylim=(-1, 3))
    arrow(ax, [1, 0], COOL, "unit x")
    arrow(ax, [0, 1], COOL, "unit y")
    arrow(ax, M @ np.array([1, 0]), ACCENT, "col 0 = where x lands")
    arrow(ax, M @ np.array([0, 1]), INK, "col 1 = where y lands")
    ax.set_title("The column decoder: a matrix IS the after-photo of the unit arrows")
    save(ax.figure, path("04-unit-decoder.png"))


# ---- 2.5 --------------------------------------------------------------------
def fig_matrix_order():
    import matplotlib.pyplot as plt
    R = np.array([[0, -1], [1, 0]])
    S = np.array([[2, 0], [0, 1]])
    panels = [("original", np.eye(2)),
              ("S @ R — rotate THEN stretch", S @ R),
              ("R @ S — stretch THEN rotate", R @ S)]
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.2))
    for ax, (title, M) in zip(axes, panels):
        new = M @ HOUSE
        ax.plot(HOUSE[0], HOUSE[1], "o-", color=COOL)
        ax.plot(new[0], new[1], "o-", color=ACCENT)
        ax.set_title(title, fontsize=10)
        ax.grid(alpha=0.3)
        ax.set_aspect("equal")
        ax.set_xlim(-7, 7)
        ax.set_ylim(-4, 4)
    fig.suptitle("AB ≠ BA: same two machines, different order, visibly different house", y=1.02, fontsize=12)
    save(fig, path("05-matrix-order.png"))


# ---- 2.6 --------------------------------------------------------------------
def _show(ax, img, title):
    if img.ndim == 2:
        ax.imshow(img, cmap="gray", vmin=0, vmax=1)
    else:
        ax.imshow(np.clip(img, 0, 1))
    ax.set_title(title, fontsize=10)
    ax.axis("off")


def _smiley():
    face = np.zeros((12, 12))
    face[2:4, 3:5] = 1.0
    face[2:4, 7:9] = 1.0
    face[7, 3:9] = 1.0
    face[6, 2] = 1.0
    face[6, 9] = 1.0
    return face


def fig_image_basics():
    import matplotlib.pyplot as plt
    row = np.linspace(0, 1, 100)
    gradient = np.tile(row, (100, 1))
    board = np.zeros((8, 8))
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.6))
    _show(axes[0], gradient, "a fade: one row, stacked")
    _show(axes[1], board, "a checkerboard: two lines of code")
    _show(axes[2], _smiley(), "a smile, specified numerically")
    fig.suptitle("An image IS a matrix of brightness numbers (0 = black, 1 = white)", y=1.04, fontsize=12)
    save(fig, path("06-image-basics.png"))


def fig_edits_gallery():
    import matplotlib.pyplot as plt
    face = _smiley()
    edits = {
        "original": face,
        "dimmed (×0.4)": face * 0.4,
        "negative (1−img)": 1 - face,
        "flipped [::-1]": face[::-1],
        "mirrored [:, ::-1]": face[:, ::-1],
    }
    fig, axes = plt.subplots(1, 5, figsize=(12, 3))
    for ax, (title, img) in zip(axes, edits.items()):
        _show(ax, img, title)
    fig.suptitle("Every photo edit is arithmetic you already own", y=1.05, fontsize=12)
    save(fig, path("06-edits-gallery.png"))


def fig_rgb_stack():
    import matplotlib.pyplot as plt
    row = np.linspace(0, 1, 100)
    gradient = np.tile(row, (100, 1))
    r, g, b = gradient, gradient.T, 1 - gradient
    sunset = np.stack([r, g, b], axis=-1)
    fig, axes = plt.subplots(1, 4, figsize=(12, 3.2))
    _show(axes[0], r, "R channel")
    _show(axes[1], g, "G channel")
    _show(axes[2], b, "B channel")
    _show(axes[3], sunset, "stacked → colour!")
    fig.suptitle("Colour = three grayscale matrices stacked: shape (height, width, 3)", y=1.04, fontsize=12)
    save(fig, path("06-rgb-stack.png"))


if __name__ == "__main__":
    fig_magnitude()
    fig_taste_space()
    fig_tip_to_tail()
    fig_king_queen()
    fig_dot_compass()
    fig_highdim_perp()
    fig_house_transforms()
    fig_unit_decoder()
    fig_matrix_order()
    fig_image_basics()
    fig_edits_gallery()
    fig_rgb_stack()
    print("\nModule 2 figures done.")
