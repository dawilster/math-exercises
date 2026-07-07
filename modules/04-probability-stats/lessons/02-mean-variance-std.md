# 4.2 — Mean, Variance, Standard Deviation

*≤5 min read. Then straight to the worksheet.*

## Why this matters (the real reason)

Feed a neural net one feature measured in dollars (0 to 1,000,000) and another in metres (0 to 2),
and training breaks: the dollar feature's huge numbers swamp everything, gradients go wild, learning
stalls. The fix — used in nearly every real ML pipeline, and built into batch norm — is to shift and
rescale every feature to **centre 0, spread 1**. To do that, you need exactly two numbers per
feature: its *centre* and its *spread*. That's this lesson.

## The one big idea

A pile of numbers can be summarised by two questions:

- **Where is it?** → the **mean** $\mu$ — the balance point:
$$\mu = \frac{1}{n}\sum_{i=1}^{n} x_i \qquad \text{(a Σ! Module 0.6: just a for-loop)}$$
- **How wide is it?** → the **variance** — the average *squared* distance from the mean:
$$\sigma^2 = \frac{1}{n}\sum_{i=1}^{n} (x_i - \mu)^2$$
and its square root, the **standard deviation** $\sigma$ — spread in the *original units*.

Why square the distances? Try averaging the raw deviations $(x_i - \mu)$: the positives and
negatives cancel to **exactly zero, every time** (the mean is the balance point — that's what
balancing means). Squaring makes every deviation count.

## Watch one get worked

Data: $2, 4, 4, 4, 5, 5, 7, 9$ (eight numbers).

**Step 1 — CENTRE.** $\mu = \frac{2+4+4+4+5+5+7+9}{8} = \frac{40}{8} = 5$

**Step 2 — DEVIATIONS.** Subtract $\mu$ from each: $-3, -1, -1, -1, 0, 0, 2, 4$ (check: they sum to 0 ✓)

**Step 3 — SQUARE.** $9, 1, 1, 1, 0, 0, 4, 16$

**Step 4 — AVERAGE.** $\sigma^2 = \frac{9+1+1+1+0+0+4+16}{8} = \frac{32}{8} = 4$

**Step 5 — UNSQUARE.** $\sigma = \sqrt{4} = 2$

Bonus move — the **z-score**: how unusual is the 9?
$$z = \frac{x - \mu}{\sigma} = \frac{9 - 5}{2} = 2$$
"Two spreads above centre." z-scores are unit-free, so a z of 2 in dollars and a z of 2 in metres
are *equally unusual* — that's why normalising features makes them comparable. Normalising = giving
every data point its z-score.

## The Python connection

```python
import numpy as np
x = np.array([2, 4, 4, 4, 5, 5, 7, 9])

print(x.mean())            # 5.0  — Step 1 in one call
print(x.var())             # 4.0  — Steps 2–4
print(x.std())             # 2.0  — Step 5
z = (x - x.mean()) / x.std()   # normalise: every value becomes its z-score
print(z.mean(), z.std())       # 0.0 and 1.0 — centre 0, spread 1. Job done.
```

`(x - x.mean())` subtracts the mean from *every element at once* — numpy applies operations
across whole arrays. That one line is what "normalise your inputs" actually is.

## The classic traps

- **Skipping the squares.** Average of raw deviations = 0 always. It tells you nothing.
- **Mixing up variance and std.** Variance is in *squared* units (dollars²!). When talking about
  spread in real units, you want $\sigma$.
- **Mean ≠ typical.** One billionaire walks into a bar and the mean wealth is millions.
  The mean chases outliers; keep an eye out for them.
- (You may meet $n-1$ instead of $n$ in the variance — that's a small correction for *samples*,
  coming in 4.4. Not today's problem.)

> **Deep-end question to hold during the worksheet:**
> add 100 to every data point — what happens to $\mu$? To $\sigma$? Now instead *multiply* every
> point by 3 — what happens to each? (This is shift vs stretch, and it's about to matter a lot.)

**Now: worksheet `02-mean-variance-std` — pen and paper. Then the notebook to do it at ML scale.**
