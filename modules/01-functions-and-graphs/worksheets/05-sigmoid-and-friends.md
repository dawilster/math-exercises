# Worksheet 1.5 — Sigmoid & Friends

*Pen and paper. Sketches first, matplotlib in Part E after scanning.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: run the activations

$\sigma(x) = \dfrac{1}{1 + e^{-x}} \qquad \mathrm{ReLU}(x) = \max(0, x)$

1. $\mathrm{ReLU}(5)$, $\mathrm{ReLU}(0)$, $\mathrm{ReLU}(-3)$

   ::: answer
   $5$, $0$, $0$ — move: $\max(0, x)$ keeps positives untouched and floors anything $\le 0$ to $0$.
   :::

2. $\sigma(0)$   *(show the two-line computation, not just the answer)*

   ::: answer
   $e^{0} = 1$, then $\sigma(0) = \dfrac{1}{1+1} = \dfrac{1}{2}$ — the two moves: evaluate the
   exponential, then add 1 and take the reciprocal.
   :::

3. Without computing exactly: is $\sigma(10)$ closest to $0$, $\frac{1}{2}$, or $1$?
   And $\sigma(-10)$? One line of reasoning each.

   ::: answer
   $\sigma(10)$ is closest to $1$: large positive $x$ makes $e^{-x}\to 0$, so the denominator
   $\to 1$. $\sigma(-10)$ is closest to $0$: large negative $x$ makes $e^{-x}$ huge, so the
   whole fraction shrinks toward $0$.
   :::

4. $\tanh(0)$, and the two values $\tanh(x)$ creeps toward as $x \to +\infty$ and $x \to -\infty$.

   ::: answer
   $\tanh(0) = 0$. As $x \to +\infty$, $\tanh(x) \to 1$. As $x \to -\infty$, $\tanh(x) \to -1$.
   :::

---

## Part B — Core: sketches and the linear collapse

5. Sketch $y = \sigma(x)$. Mark: the centre point $\left(0, \frac{1}{2}\right)$ and both
   asymptotes (dashed).

   ::: answer
   An S-curve rising left to right, passing exactly through $\left(0, \frac{1}{2}\right)$, with
   dashed horizontal asymptotes at $y = 0$ (as $x \to -\infty$) and $y = 1$ (as $x \to +\infty$).
   :::

6. Sketch $y = \tanh(x)$ on separate axes. Mark centre and asymptotes. In one line:
   the key difference from sigmoid.

   ::: answer
   Same S-shape, but centred at the origin $(0,0)$, with dashed asymptotes at $y = -1$ and
   $y = 1$. Key difference: tanh is zero-centred and spans $[-1, 1]$, while sigmoid spans
   $[0, 1]$ centred on $\frac{1}{2}$ (in fact $\tanh(x) = 2\sigma(2x) - 1$).
   :::

7. Sketch $y = \mathrm{ReLU}(x)$. Mark the kink. In one line: why isn't this machine linear,
   even though it's made of straight pieces?

   ::: answer
   A kink at the origin: slope $0$ for $x<0$, slope $1$ for $x>0$. That kink breaks additivity,
   the test a true linear machine must pass: $\mathrm{ReLU}(1 + (-1)) = \mathrm{ReLU}(0) = 0$,
   but $\mathrm{ReLU}(1) + \mathrm{ReLU}(-1) = 1 + 0 = 1$. Since $f(a+b) \ne f(a)+f(b)$, it's
   piecewise linear, not linear.
   :::

8. The collapse, by hand: $f(x) = 2x + 1$ and $g(x) = 3x - 2$. Expand $f(g(x))$ AND $g(f(x))$.
   Both should land in the same species — which one? What does this mean for a 100-layer network
   with no activations?

   ::: answer
   $f(g(x)) = 2(3x-2)+1 = 6x-3$. $g(f(x)) = 3(2x+1)-2 = 6x+1$. Same species: both are linear
   ($mx+b$) — composing two linear machines just builds another linear machine. Move that
   proves it: expand the bracket, then collect like terms. Consequence for the 100-layer
   network: however many linear layers you stack, the whole thing is mathematically equivalent
   to a single linear layer.
   :::

9. Decompose sigmoid (unit 1.4 skill): list the chain of zoo machines that turns
   $x$ into $\dfrac{1}{1 + e^{-x}}$, in firing order.

   ::: answer
   $x \to$ negate ($\times(-1)$) $\to$ exponentiate ($e^{\square}$) $\to$ add $1$ $\to$
   reciprocal ($1/\square$). Firing order: negate, exponential, $+1$, invert.
   :::

---

## Part C — Match & diagnose

10. Match each job to the best activation (sigmoid / tanh / ReLU):

    a) "Output must be a probability for spam-or-not."

    b) "Hidden layers of a huge image model — needs to be dirt cheap to compute."

    c) "Outputs should be centred on zero, between −1 and 1."

    ::: answer
    a) sigmoid — squashes to $[0,1]$, readable as a probability.
    b) ReLU — cheapest to compute (no exponentials), the default for big hidden layers.
    c) tanh — zero-centred, range $(-1, 1)$.
    :::

11. Diagnose: a friend builds a 50-layer network using *only* linear layers ("more layers =
    smarter, right?"). It performs exactly as well as a 1-layer one. Explain why in
    two lines, citing problem 8.

    ::: answer
    Problem 8's move: composing linear machines always yields another linear machine, never
    anything richer. So 50 stacked linear layers collapse algebraically into one linear map —
    the same expressive power as a single layer. Only a nonlinear activation stops the collapse.
    :::

12. Spot the error: "My sigmoid output is exactly 1.0, so the model is 100% certain."
    What's mathematically off about this claim, and what did floating point do?

    ::: answer
    $y = 1$ is an asymptote of $\sigma$ — the curve gets arbitrarily close but never actually
    reaches it for any finite $x$, so "100% certain" isn't mathematically available. What
    happened: for large enough $x$, $e^{-x}$ underflows to $0.0$ in floating point, so
    $1+e^{-x}$ rounds to exactly $1.0$ and $1/1.0 = 1.0$ — that displayed $1.0$ is a rounding
    artifact of finite precision, not genuine certainty.
    :::

---

## Part D — Deep end

*Beyond what was taught.*

13. The lesson's deep-end: compute $\mathrm{ReLU}(x) + \mathrm{ReLU}(-x)$ at $x = 3$, $x = -3$
    and $x = 0$. Sketch the result. What familiar machine have you built from two ReLUs?

    ::: answer
    $x=3$: $\mathrm{ReLU}(3)+\mathrm{ReLU}(-3) = 3+0 = 3$. $x=-3$: $0+3 = 3$. $x=0$: $0+0 = 0$.
    That's $|x|$ — the absolute-value machine, built from two ReLUs (one keeps the positive
    side, the other, fed $-x$, keeps the negative side, and both land above the axis).
    :::

14. Sketch $y = \mathrm{ReLU}(x) - \mathrm{ReLU}(x - 2)$. *(Compute it at
    $x = -1, 0, 1, 2, 3, 4$ first. Flat, ramp, flat — you've just built a feature detector.)*

    ::: answer
    Values: $x=-1\to 0$, $x=0\to 0$, $x=1\to 1$, $x=2\to 2$, $x=3\to 2$, $x=4\to 2$. Flat at $0$
    up to $x=0$, ramps linearly up to $2$ across $0 \le x \le 2$, flat at $2$ after that — a
    "window" that only switches on for a specific input range: a feature detector.
    :::

15. Show, with Module 0 fraction moves, that $\sigma(-x) = 1 - \sigma(x)$.
    *(Start from $\sigma(-x) = \frac{1}{1+e^{x}}$ and make the two sides meet. Tough — attempt,
    name your moves.)* What does this symmetry mean for "probability of cat" vs
    "probability of not-cat"?

    ::: answer
    Start from $1 - \sigma(x)$ and write $1$ as $\frac{1+e^{-x}}{1+e^{-x}}$ (move: common
    denominator) to get $1-\sigma(x) = \frac{(1+e^{-x})-1}{1+e^{-x}} = \frac{e^{-x}}{1+e^{-x}}$.
    Multiply top and bottom by $e^{x}$ (move: $\times \frac{e^x}{e^x} = 1$) to clear the
    negative exponent: $\frac{1}{e^{x}+1} = \frac{1}{1+e^{x}} = \sigma(-x)$. So
    $\sigma(-x) = 1 - \sigma(x)$. Meaning: "probability of not-cat" is forced to be exactly
    $1$ minus "probability of cat" — the two outputs sum to $1$, as real probabilities must.
    :::

---

## Part E — Python check (at the computer, after scanning)

16. Verify your Part A values and Part B sketches:

```python
import sys; sys.path.append("../../tools")
import numpy as np
import matplotlib.pyplot as plt
from plots import plot_functions

sigmoid = lambda x: 1 / (1 + np.exp(-x))
relu    = lambda x: np.maximum(0, x)

print(sigmoid(0), relu(-3), np.tanh(0))

plot_functions({
    "sigmoid": sigmoid,
    "tanh":    np.tanh,
    "ReLU":    relu,
}, xlim=(-5, 5), ylim=(-2, 3))
plt.show()
```

17. Verify problem 13 by plotting `lambda x: relu(x) + relu(-x)`. Was your sketch right?

> **Bonus thought:** print `sigmoid(37)` and `sigmoid(38)`. At what point does Python give up
> on the asymptote and just say 1.0?
