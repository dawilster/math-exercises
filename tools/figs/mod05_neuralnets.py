"""Load-bearing figures for Module 5 (Math of Neural Nets) lessons.

Run:  uv run python tools/figs/mod05_neuralnets.py
Writes into modules/05-math-of-neural-nets/lessons/img/.

Module 5 is the payoff: this actually trains a tiny net on the two-moons task and
snapshots its decision boundary learning, and convolves a scene with real kernels.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(__file__)
sys.path.append(HERE)
sys.path.append(os.path.join(HERE, ".."))
from _style import INK, ACCENT, COOL, base, save  # noqa: E402

OUT = os.path.abspath(os.path.join(HERE, "..", "..",
                      "modules", "05-math-of-neural-nets", "lessons", "img"))
os.makedirs(OUT, exist_ok=True)

BLUE = "#2563eb"
RED = "#dc2626"


def path(name):
    return os.path.join(OUT, name)


# ---- 5.1 --------------------------------------------------------------------
def fig_untrained_surface():
    import matplotlib.pyplot as plt
    xs = np.linspace(-4, 4, 300)
    gx, gy = np.meshgrid(xs, xs)
    Z1a = 0.5 * gx - 1.0 * gy + 0.5
    Z1b = 1.0 * gx + 0.5 * gy - 1.0
    H1, H2 = np.maximum(0, Z1a), np.maximum(0, Z1b)
    out = 1 / (1 + np.exp(-(-1.0 * H1 + 2.0 * H2 - 2.0)))
    fig, ax = plt.subplots(figsize=(6.6, 5.6))
    m = ax.pcolormesh(gx, gy, out, cmap="RdBu_r", vmin=0, vmax=1, shading="auto")
    fig.colorbar(m, ax=ax, label="network output ŷ")
    ax.plot(1, 2, "k*", markersize=16, label="our input (1, 2)")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.legend(loc="lower right")
    ax.set_title("An untrained network's opinion of every point —\nthe creases are where each ReLU switches on/off")
    save(fig, path("01-untrained-surface.png"))


# ---- 5.2 --------------------------------------------------------------------
def fig_two_bills():
    fig, ax = base((8, 4.8))
    p = np.linspace(0.005, 0.999, 400)
    ax.plot(p, -np.log(p), color=ACCENT, linewidth=2.5, label="cross-entropy:  −ln ŷ")
    ax.plot(p, (p - 1) ** 2, color=COOL, linewidth=2.5, linestyle="--", label="MSE:  (ŷ − 1)²")
    ax.axhline(np.log(2), color=INK, linestyle=":", alpha=0.7)
    ax.annotate("0.693 — the coin-flip loss", (0.5, np.log(2) + 0.15), fontsize=10)
    ax.set_xlabel("prediction ŷ   (truth is y = 1)")
    ax.set_ylabel("loss")
    ax.legend(fontsize=10)
    ax.set_title("Two bills for the same wrongness: as ŷ→0, MSE tops out but cross-entropy → ∞")
    save(fig, path("02-two-bills.png"))


def fig_softmax():
    import matplotlib.pyplot as plt

    def softmax(s):
        e = np.exp(s)
        return e / e.sum()
    scores = np.array([2.0, 0.0, -1.0, 0.5])
    probs = softmax(scores)
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.6))
    axes[0].bar(range(4), scores, color=COOL)
    axes[0].set_title("raw scores (any numbers)")
    axes[1].bar(range(4), probs, color=ACCENT)
    axes[1].set_title("after softmax (positive, sum = 1)")
    for ax in axes:
        ax.set_xticks(range(4))
        ax.set_xticklabels(["A", "B", "C", "D"])
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    fig.suptitle("Softmax turns any scores into a probability distribution (e^x makes positive, ÷ total sums to 1)",
                 y=1.03, fontsize=11)
    save(fig, path("02-softmax.png"))


# ---- 5.3 --------------------------------------------------------------------
def fig_backprop_pipeline():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(11, 4.4))
    ax.axis("off")
    nodes = ["x", "z₁", "h", "z₂", "ŷ", "L"]
    xpos = np.linspace(0.5, 10.5, len(nodes))
    y = 2.0
    for xp, name in zip(xpos, nodes):
        ax.add_patch(plt.Circle((xp, y), 0.42, color=INK, fill=False, linewidth=2))
        ax.text(xp, y, name, ha="center", va="center", fontsize=15)
    fwd = ["W₁·+b₁", "ReLU", "W₂·+b₂", "sigmoid", "−ln ŷ"]
    bwd = ["δ₁", "gate", "δ₂ = ŷ−y", "σ'(z₂)", "−1/ŷ"]
    for i in range(len(nodes) - 1):
        x0, x1 = xpos[i] + 0.45, xpos[i + 1] - 0.45
        ax.annotate("", (x1, y + 0.25), (x0, y + 0.25),
                    arrowprops=dict(arrowstyle="->", color=BLUE, lw=2))
        ax.text((x0 + x1) / 2, y + 0.62, fwd[i], ha="center", color=BLUE, fontsize=10)
        ax.annotate("", (x0, y - 0.25), (x1, y - 0.25),
                    arrowprops=dict(arrowstyle="->", color=ACCENT, lw=2))
        ax.text((x0 + x1) / 2, y - 0.78, bwd[len(nodes) - 2 - i], ha="center", color=ACCENT, fontsize=10)
    ax.text(5.5, 3.3, "FORWARD PASS — compute the prediction  →", ha="center", color=BLUE, fontsize=12)
    ax.text(5.5, 0.5, "←  BACKWARD PASS — multiply local sensitivities, reusing each result",
            ha="center", color=ACCENT, fontsize=12)
    ax.set_xlim(-0.2, 11.2)
    ax.set_ylim(0, 3.7)
    ax.set_title("Backprop = the chain rule walked backwards through the forward pipeline", fontsize=13)
    save(fig, path("03-backprop-pipeline.png"))


# ---- 5.4 --------------------------------------------------------------------
def _moons(n=100, noise=0.1, seed=42):
    rng = np.random.default_rng(seed)
    t = np.linspace(0, np.pi, n)
    top = np.column_stack([np.cos(t), np.sin(t)])
    bottom = np.column_stack([1 - np.cos(t), 0.5 - np.sin(t)])
    X = np.vstack([top, bottom]) + rng.normal(0, noise, (2 * n, 2))
    y = np.vstack([np.zeros((n, 1)), np.ones((n, 1))])
    return X, y


def _train_moons():
    """A 2→8→1 ReLU/sigmoid net trained by hand-rolled backprop. Returns loss
    history and weight snapshots for plotting the decision boundary evolving."""
    X, y = _moons()
    rng = np.random.default_rng(0)
    W1 = rng.normal(0, 0.8, (2, 8))
    b1 = np.zeros((1, 8))
    W2 = rng.normal(0, 0.8, (8, 1))
    b2 = np.zeros((1, 1))
    lr = 0.3
    losses = []
    snaps = {}
    snap_at = [0, 200, 600, 1500, 3000, 6000]
    for step in range(6001):
        z1 = X @ W1 + b1
        h = np.maximum(0, z1)
        z2 = h @ W2 + b2
        yh = 1 / (1 + np.exp(-z2))
        eps = 1e-9
        loss = -np.mean(y * np.log(yh + eps) + (1 - y) * np.log(1 - yh + eps))
        losses.append(loss)
        if step in snap_at:
            snaps[step] = (W1.copy(), b1.copy(), W2.copy(), b2.copy())
        n = len(X)
        dz2 = (yh - y) / n
        dW2 = h.T @ dz2
        db2 = dz2.sum(0, keepdims=True)
        dh = dz2 @ W2.T
        dz1 = dh * (z1 > 0)
        dW1 = X.T @ dz1
        db1 = dz1.sum(0, keepdims=True)
        W1 -= lr * dW1
        b1 -= lr * db1
        W2 -= lr * dW2
        b2 -= lr * db2
    return X, y, losses, snaps, snap_at


def _predict_grid(gx, gy, params):
    W1, b1, W2, b2 = params
    grid = np.column_stack([gx.ravel(), gy.ravel()])
    h = np.maximum(0, grid @ W1 + b1)
    z2 = h @ W2 + b2
    return (1 / (1 + np.exp(-z2))).reshape(gx.shape)


def fig_moons_task():
    fig, ax = base((7, 5.4))
    X, y = _moons()
    ax.scatter(*X[y[:, 0] == 0].T, c=BLUE, s=22, alpha=0.85, label="class 0")
    ax.scatter(*X[y[:, 0] == 1].T, c=RED, s=22, alpha=0.85, label="class 1")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.legend()
    ax.set_aspect("equal")
    ax.set_title("The task: separate the two moons — no straight line can do it")
    save(fig, path("04-moons-task.png"))


def fig_moons_loss(losses):
    fig, ax = base((8, 4.4))
    ax.plot(losses, color=ACCENT, linewidth=2)
    ax.axhline(np.log(2), color=INK, linestyle="--", alpha=0.7)
    ax.annotate("0.693 — coin-flip ignorance, where every classifier is born",
                (len(losses) * 0.18, np.log(2) + 0.02), fontsize=9)
    ax.set_xlabel("training step")
    ax.set_ylabel("mean cross-entropy loss")
    ax.set_title("Your network earning its way down the hill (gradient descent, Module 3.5)")
    save(fig, path("04-moons-loss.png"))


def fig_moons_boundary(X, y, snaps, snap_at):
    import matplotlib.pyplot as plt
    gx, gy = np.meshgrid(np.linspace(-1.6, 2.6, 200), np.linspace(-1.1, 1.6, 200))
    fig, axes = plt.subplots(2, 3, figsize=(12, 7))
    for ax, step in zip(axes.ravel(), snap_at):
        p = _predict_grid(gx, gy, snaps[step])
        ax.contourf(gx, gy, p, levels=20, cmap="RdBu_r", vmin=0, vmax=1, alpha=0.85)
        ax.contour(gx, gy, p, levels=[0.5], colors="k", linewidths=2)
        ax.scatter(*X[y[:, 0] == 0].T, c=BLUE, s=7)
        ax.scatter(*X[y[:, 0] == 1].T, c=RED, s=7)
        ax.set_title(f"step {step}", fontsize=11)
        ax.set_xticks([])
        ax.set_yticks([])
    fig.suptitle("Your own math, learning: the black line (ŷ = 0.5) bends around the moons", fontsize=13)
    save(fig, path("04-moons-boundary.png"))


# ---- 5.5 --------------------------------------------------------------------
def _scene():
    h, w = 90, 120
    yy, xx = np.mgrid[0:h, 0:w]
    yy, xx = yy / h, xx / w
    scene = 0.15 + 0.35 * yy
    sun = (xx - 0.70) ** 2 + (yy - 0.28) ** 2 < 0.012
    scene[sun] = 1.0
    ridge = 0.62 + 0.10 * np.sin(xx * 2 * np.pi * 1.6)
    scene = np.where(yy > ridge, 0.06, scene)
    return scene


def _convolve(img, K):
    k = K.shape[0]
    out = np.zeros((img.shape[0] - k + 1, img.shape[1] - k + 1))
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            out[i, j] = np.sum(img[i:i + k, j:j + k] * K)
    return out


def fig_conv_gallery():
    import matplotlib.pyplot as plt
    scene = _scene()
    kernels = {
        "vertical edges": np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], float),
        "horizontal edges": np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], float),
        "blur (mean)": np.ones((3, 3)) / 9,
        "sharpen": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], float),
    }
    fig, axes = plt.subplots(1, 5, figsize=(15, 3.4))
    axes[0].imshow(scene, cmap="gray", vmin=0, vmax=1)
    axes[0].set_title("original")
    for ax, (name, K) in zip(axes[1:], kernels.items()):
        ax.imshow(_convolve(scene, K), cmap="gray")
        ax.set_title(name, fontsize=10)
    for ax in axes:
        ax.axis("off")
    fig.suptitle("One 3×3 kernel slid over the image = one feature detector, everywhere at once", y=1.04, fontsize=12)
    save(fig, path("05-conv-gallery.png"))


def fig_edge_magnitude():
    import matplotlib.pyplot as plt
    scene = _scene()
    Kv = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], float)
    Kh = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], float)
    mag = np.sqrt(_convolve(scene, Kv) ** 2 + _convolve(scene, Kh) ** 2)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
    axes[0].imshow(scene, cmap="gray", vmin=0, vmax=1)
    axes[0].set_title("what the camera sees")
    axes[1].imshow(mag, cmap="inferno")
    axes[1].set_title("what the edge detector sees (a CNN learns these kernels itself)")
    for ax in axes:
        ax.axis("off")
    save(fig, path("05-edge-magnitude.png"))


if __name__ == "__main__":
    fig_untrained_surface()
    fig_two_bills()
    fig_softmax()
    fig_backprop_pipeline()
    print("training moons net...")
    X, y, losses, snaps, snap_at = _train_moons()
    print(f"  final loss = {losses[-1]:.3f}")
    fig_moons_task()
    fig_moons_loss(losses)
    fig_moons_boundary(X, y, snaps, snap_at)
    fig_conv_gallery()
    fig_edge_magnitude()
    print("\nModule 5 figures done.")
