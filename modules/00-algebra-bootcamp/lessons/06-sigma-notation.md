# 0.6 — Σ Notation: It's Just a For-Loop

*≤5 min read. Then straight to the worksheet.*

## Why this matters (the real reason)

Open any ML paper and the scariest-looking equation is usually a $\Sigma$. The loss of an
entire neural network is one:

$$L = -\frac{1}{N}\sum_{i=1}^{N} \log p_i$$

Here's the demystifier: **you already read Σ fluently — in Python.** Σ is a for-loop with
an accumulator, wearing academic dress. This unit teaches the costume-change in both
directions, and after it, half of every ML paper stops being scary. (You'll also recognise
the pieces of that loss above: a fraction from 0.4, a log from 0.5. Module 0 assembling itself.)

## The one big idea

$$\sum_{i=1}^{4} i^2 \qquad\text{IS}\qquad \begin{array}{l}\texttt{total = 0}\\\texttt{for i in [1, 2, 3, 4]:}\\\qquad\texttt{total = total + i**2}\end{array}$$

Read the parts like code:

| Σ piece | For-loop piece | Meaning |
|---|---|---|
| $i = 1$ (below) | `for i in ...` starting at 1 | loop variable and where it starts |
| $4$ (above) | ...ending at 4 — **inclusive** | where it stops (Python's `range` stops early; Σ doesn't) |
| $i^2$ (body) | `total += i**2` | what gets added each pass |
| $\Sigma$ itself | `total = 0` + the loop | "add them all up" |

So $\sum_{i=1}^{4} i^2 = 1 + 4 + 9 + 16 = 30$. That's the whole notation.

Subscripts are just **indexing**: given a list $x = (x_1, x_2, \dots, x_n)$, the symbol
$x_i$ is Python's `x[i]`. Which makes the most famous formula in statistics readable:

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i \qquad\text{is just}\qquad \texttt{sum(x) / len(x)}$$

The **mean**. Add them up, divide by how many. You've known this since primary school —
now you can read it in paper-dress.

**Double subscripts** = 2D indexing: $w_{ij}$ is `w[i][j]` — row $i$, column $j$ of a grid.
Neural network weights are exactly this. And a double Σ is nested loops:
$\sum_{i}\sum_{j} w_{ij}$ means "loop over rows, loop over columns, add everything."

## Watch one game get played

Translate $\displaystyle\sum_{i=1}^{3} (2x_i + 1)$ where $x = (4, 7, 9)$:

$$\sum_{i=1}^{3}(2x_i + 1) = (2 \cdot 4 + 1) + (2 \cdot 7 + 1) + (2 \cdot 9 + 1) \qquad \leftarrow \text{move: unroll the loop}$$
$$= 9 + 15 + 19 = 43 \qquad \leftarrow \text{move: arithmetic}$$

Worth knowing: Σ obeys the balance-game laws you already own. Distributive law (0.3) says
constants factor out and sums split:

$$\sum_i (2x_i + 1) = 2\sum_i x_i + n \qquad \leftarrow 2(4{+}7{+}9) + 3 = 43. \text{ Same answer, reshaped.}$$

## The Python connection

```python
x = [4, 7, 9]

# the literal translation of the Σ:
total = 0
for xi in x:               # Python can loop over values directly — no index needed
    total = total + (2 * xi + 1)
print(total)               # 43

# the idiomatic one-liner (a generator inside sum()):
print(sum(2 * xi + 1 for xi in x))    # 43

# and the mean, three ways:
print(sum(x) / len(x))     # the Σ formula, verbatim
import numpy as np
print(np.mean(x))          # what you'll actually type in ML
```

From now on, when a paper shows you a Σ, your first move is: *write it as the loop.*
Ten seconds, and the fear is gone.

## What breaks the balance (the classic traps)

- **Off-by-one:** Σ's top limit is **inclusive**; Python's `range(1, n)` stops at $n-1$.
  You want `range(1, n + 1)` — the classic bug.
- **Index vs value:** $\sum_{i=1}^{3} i$ adds the *counters* $1+2+3$;
  $\sum_{i=1}^{3} x_i$ adds the *list entries*. Check what's in the body.
- **Squaring in the wrong place:** $\sum x_i^2 \neq \left(\sum x_i\right)^2$ —
  "add the squares" and "square the sum" are wildly different numbers.
  (For $x = (1,2,3)$: $14$ vs $36$.)

> **Deep-end question to hold in your head during the worksheet:**
> $\sum$ (sigma) repeats +. There's a twin, $\prod$ (capital pi), that repeats ×.
> Given what 0.5 taught you about logs, what would $\log$ of a $\prod$ turn into?
> (You've just derived the shape of every likelihood-based loss function.)

**Now: worksheet `06-sigma-notation` — pen and paper. Photograph it into `scans/inbox/` when done.**
