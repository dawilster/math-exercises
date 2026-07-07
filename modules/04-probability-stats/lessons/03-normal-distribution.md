# 4.3 — The Normal Distribution

*≤5 min read. Then straight to the worksheet.*

## Why this matters (the real reason)

Stable Diffusion generates an image by starting with **pure Gaussian noise** — every pixel drawn
from the bell curve — and denoising step by step. Neural nets are *initialised* with Gaussian
random weights. When a paper writes $\varepsilon \sim \mathcal{N}(0, 1)$, it's naming today's
curve. This is THE distribution of deep learning, and of nature.

## The one big idea

**Add up many small independent random things, and the total is bell-shaped. Always.**

Each die roll is flat — 1 through 6, equally likely. But the *sum of ten dice* piles up around 35
and thins out symmetrically into tails. Heights, measurement errors, coin-flip totals: anything
built from many small random contributions comes out bell-curved. Randomness in, law out.
(This is the central limit theorem — you'll *watch it happen* in the notebook.)

The bell curve is a family with two dials, and you already own them from Module 1.3:

$$\mathcal{N}(\mu, \sigma) \quad \begin{cases} \mu \text{ — SHIFTS the curve left/right (where's the peak?)} \\ \sigma \text{ — STRETCHES it wide or squeezes it narrow} \end{cases}$$

Same shape every time; only shifted and stretched. And the stretch obeys a rule worth memorising:

**68 / 95 / 99.7** — about 68% of values land within $1\sigma$ of $\mu$, 95% within $2\sigma$,
99.7% within $3\sigma$.

## Watch one get worked

*Adult male heights: roughly $\mathcal{N}(\mu = 178\text{ cm}, \sigma = 7\text{ cm})$.
What fraction of men are between 171 cm and 192 cm?*

**Step 1 — Z-SCORE the boundaries** (4.2's move):
$$z_{171} = \frac{171 - 178}{7} = -1 \qquad z_{192} = \frac{192 - 178}{7} = +2$$

**Step 2 — SKETCH and shade.** Draw the bell, mark $-1\sigma$ and $+2\sigma$, shade between.

**Step 3 — READ the rule, piece by piece.** By symmetry, halve the bands:
- from $-1\sigma$ to $\mu$: half of 68% = 34%
- from $\mu$ to $+2\sigma$: half of 95% = 47.5%

**Step 4 — ADD.** $34\% + 47.5\% = 81.5\%$.

Every 68/95/99.7 problem is these four moves: z-score, sketch, split into half-bands, add.

## The Python connection

```python
import numpy as np
rng = np.random.default_rng(42)

heights = rng.normal(178, 7, size=100_000)   # rng.normal(mu, sigma, size) — bell-curve samples
inside = (heights > 171) & (heights < 192)   # & combines two True/False arrays
print(inside.mean())                          # ≈ 0.815 — the experiment agrees with the rule
```

Same superpower as 4.1: the rule is checkable by counting. And `rng.normal(0, 1, ...)` — the
**standard normal** — is literally the noise source inside diffusion models.

## The classic traps

- **Reading pdf height as probability.** The curve's height at 178 is *not* $P(\text{height}=178)$.
  Probability lives in **area under the curve** between two values, never in the height of one point.
  (Lightly held rule of thumb: heights compare likeliness, areas give probability.)
- **Assuming everything is normal.** Wealth, city sizes, word frequencies — heavily skewed, not
  bells. The theorem needs *many small independent* contributions; one dominating cause breaks it.
- **Mixing the dials.** $\mathcal{N}(0, 1)$ shifted by 178 and stretched by 7 gives
  $\mathcal{N}(178, 7)$: that's why $x = \mu + \sigma z$ works, and it's Module 1.3's
  shift-and-stretch, back for its starring role.

> **Deep-end question to hold during the worksheet:**
> the 68/95/99.7 rule means a $6\sigma$ event is absurdly rare (≈ 1 in 500 million). Yet stock-market
> crashes — supposedly $6\sigma$-plus — happen every few decades. What assumption of the bell curve
> is the market breaking?

**Now: worksheet `03-normal-distribution` — pen and paper. Then the notebook, where the bell
emerges out of chaos in front of you.**
