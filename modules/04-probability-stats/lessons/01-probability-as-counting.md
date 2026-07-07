# 4.1 — Probability as Counting

*≤5 min read. Then straight to the worksheet.*

## Why this matters (the real reason)

An LLM never "knows" the next word. It outputs a **probability for every token in its vocabulary**,
then one gets picked. Stable Diffusion starts from pure random noise. Training itself is stochastic.
You cannot read a single page of modern ML without probabilities on it — and the good news is that
under the notation, probability is just **counting**.

## The one big idea

**Probability = favourable outcomes ÷ total outcomes** (when all outcomes are equally likely).

$$P(\text{event}) = \frac{\text{ways it can happen}}{\text{ways anything can happen}}$$

But here's the part school skips: that fraction isn't an abstract decree. It's a **prediction about
counts**. If you roll a die 6,000 times, you'll get close to 1,000 sixes — not exactly, but the
*fraction* of sixes settles toward $\frac{1}{6}$ as the rolls pile up.

> **Probability is what the count settles to.** Simulate first, formalise second — that's this
> whole module's method.

## Watch one get worked

*What's the probability two dice sum to 7?*

**Step 1 — LIST the equally likely outcomes.** Not the sums — the *(die 1, die 2)* pairs.
There are $6 \times 6 = 36$ pairs, each equally likely.

**Step 2 — COUNT the favourable ones.** Pairs summing to 7:
$(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$ — that's 6.

**Step 3 — DIVIDE.**

$$P(\text{sum} = 7) = \frac{6}{36} = \frac{1}{6}$$

The trap dodged in Step 1: the eleven possible *sums* (2 through 12) are **not** equally likely —
there's only one way to roll a 2 but six ways to roll a 7. Count at the level where things ARE
equally likely.

## The Python connection

You don't have to trust the counting — you can roll dice a million times:

```python
import numpy as np
rng = np.random.default_rng(42)          # a random-number generator (seeded — more in 4.4)

rolls = rng.integers(1, 7, size=(1_000_000, 2))   # a million pairs of dice
sums = rolls[:, 0] + rolls[:, 1]
print((sums == 7).mean())                # fraction of sevens ≈ 0.1666…
```

`(sums == 7)` makes an array of `True`/`False`; `.mean()` treats them as 1/0 — so it computes
exactly "favourable ÷ total". **The formula and the experiment are the same idea.**

## The classic traps

- **Counting unequal things as equal.** "Sum is 2 or not-2, so $P = \frac{1}{2}$" — no. Count the pairs.
- **The gambler's fallacy.** Five heads in a row doesn't make tails "due". The coin has no memory;
  the next flip is still 50/50.
- **Probabilities outside $[0, 1]$.** If you compute 1.3 or −0.2, a move broke somewhere upstream.

> **Deep-end question to hold during the worksheet:**
> $P(\text{sum}=7) = \frac{1}{6}$, yet a million simulated rolls almost never gives *exactly*
> $\frac{1}{6}$. So what exactly is the $\frac{1}{6}$ claiming? What would make the simulation
> get closer to it?

**Now: worksheet `01-probability-as-counting` — pen and paper. Then the notebook, where you watch the counts settle.**
