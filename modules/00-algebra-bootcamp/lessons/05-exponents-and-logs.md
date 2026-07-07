# 0.5 — Exponents & Logarithms

*≤5 min read. Then straight to the worksheet.*

## Why this matters (the real reason)

Two of ML's most-typed lines: a loss plotted on a **log scale** (because it falls so fast a
normal plot is useless), and a learning rate decayed **exponentially** ($\eta_t = \eta_0 e^{-kt}$).
Deeper still: classifiers are trained on **log-probabilities** — the "cross-entropy loss"
you'll meet in Module 4 is literally a logarithm. Why? Probabilities *multiply*
($0.9 \times 0.8 \times \dots$), and long products of small numbers underflow to zero and
are miserable to work with. Logs convert multiplication into addition — the one trick that
makes training the giant models possible. This unit is where you earn that trick.

## The one big idea

$a^n$ starts as a **count of multiplications**: $2^3 = 2 \times 2 \times 2$. Every rule
falls out of counting:

| Rule | Why (count the multiplications) |
|---|---|
| $a^m \cdot a^n = a^{m+n}$ | $m$ copies times $n$ copies = $m+n$ copies |
| $\frac{a^m}{a^n} = a^{m-n}$ | $n$ of the copies cancel |
| $(a^m)^n = a^{mn}$ | $n$ bundles of $m$ copies |

Then the pattern forces the weird cases. Walk $2^3, 2^2, 2^1, \dots$ — each step **divides
by 2**. Keep walking past the edge:

$$2^3 = 8,\quad 2^2 = 4,\quad 2^1 = 2,\quad 2^0 = 1,\quad 2^{-1} = \tfrac{1}{2},\quad 2^{-2} = \tfrac{1}{4}$$

$a^0 = 1$ and $a^{-n} = \frac{1}{a^n}$ aren't decrees — they're the only values that keep
the pattern unbroken. Same logic gives $a^{1/2} = \sqrt{a}$ (because
$a^{1/2} \cdot a^{1/2} = a^1$ — what times itself makes $a$?).

**A logarithm is just the question "what exponent?"**

$$\log_2 8 = 3 \quad\text{because}\quad 2^3 = 8$$

That's the entire definition. $\log_2 8$ is pronounced *"2 to the what makes 8?"*
And because logs *are* exponents, every exponent rule has a log twin:

$$a^m \cdot a^n = a^{m+n} \qquad\Longleftrightarrow\qquad \log(xy) = \log x + \log y$$

There it is — **multiplication becomes addition**. The trick ML lives on, in one line.

## Watch one game get played

Solve $10 \cdot 2^x = 640$ — the $x$ is upstairs, in the exponent. New territory, same game:

$$10 \cdot 2^x = 640$$
$$2^x = 64 \qquad \leftarrow \text{move: divide both pans by } 10$$
$$x = \log_2 64 \qquad \leftarrow \text{move: ask "2 to the what?" (take } \log_2 \text{ of both pans)}$$
$$x = 6 \qquad \leftarrow \text{because } 2^6 = 64$$

**Log-of-both-sides is a legal move** — same reason as ever: applied to both pans, balance holds.
It's the move that brings a variable *down from the exponent*.

## The Python connection

```python
import numpy as np

print(2 ** 10)            # ** is Python's "to the power of" → 1024
print(np.log2(1024))      # "2 to the what makes 1024?" → 10.0

# THE trick: a product of many small probabilities...
probs = [0.9, 0.8, 0.95, 0.7]
print(np.prod(probs))                     # np.prod multiplies a list → 0.4788
print(np.sum(np.log(probs)))              # sum of logs → -0.7364...
print(np.log(np.prod(probs)))             # log of product → the SAME -0.7364...
```

`log(product) == sum(of logs)` — with 10,000 probabilities the product underflows to `0.0`
and is useless, but the sum of logs stays a perfectly ordinary number. *That* is why every
loss function you'll ever meet has a log in it.

(Heads-up: `np.log` is $\log_e$ — base $e \approx 2.718$, called $\ln$. ML uses it by default.
Different base, same idea: "e to the what?")

## What breaks the balance (the classic traps)

- $\log(x + y) \neq \log x + \log y$. The log rule rewrites **products**, not sums.
  (It's $\log(xy)$ that splits.)
- $a^0 = 1$, not $0$. Zero multiplications leaves you at the multiplicative starting line, which is 1.
- $(a + b)^2 \neq a^2 + b^2$ — the freshman's dream from 0.3 wearing an exponent costume.
- Logs of zero or negatives don't exist: $2^{\text{anything}}$ is always positive,
  so "2 to the what makes $-4$?" has no answer.

> **Deep-end question to hold in your head during the worksheet:**
> your ears already do this. Musical octaves: A is 110 Hz, then 220, 440, 880 — each octave
> *doubles* the frequency, yet every octave sounds like the *same size step*.
> What does that say about the scale your hearing runs on?

**Now: worksheet `05-exponents-and-logs` — pen and paper. Photograph it into `scans/inbox/` when done.**
