# Worksheet 1.5 — Sigmoid & Friends

*Pen and paper. Sketches first, matplotlib in Part E after scanning.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: run the activations

$\sigma(x) = \dfrac{1}{1 + e^{-x}} \qquad \mathrm{ReLU}(x) = \max(0, x)$

1. $\mathrm{ReLU}(5)$, $\mathrm{ReLU}(0)$, $\mathrm{ReLU}(-3)$

2. $\sigma(0)$   *(show the two-line computation, not just the answer)*

3. Without computing exactly: is $\sigma(10)$ closest to $0$, $\frac{1}{2}$, or $1$?
   And $\sigma(-10)$? One line of reasoning each.

4. $\tanh(0)$, and the two values $\tanh(x)$ creeps toward as $x \to +\infty$ and $x \to -\infty$.

---

## Part B — Core: sketches and the linear collapse

5. Sketch $y = \sigma(x)$. Mark: the centre point $\left(0, \frac{1}{2}\right)$ and both
   asymptotes (dashed).

6. Sketch $y = \tanh(x)$ on separate axes. Mark centre and asymptotes. In one line:
   the key difference from sigmoid.

7. Sketch $y = \mathrm{ReLU}(x)$. Mark the kink. In one line: why isn't this machine linear,
   even though it's made of straight pieces?

8. The collapse, by hand: $f(x) = 2x + 1$ and $g(x) = 3x - 2$. Expand $f(g(x))$ AND $g(f(x))$.
   Both should land in the same species — which one? What does this mean for a 100-layer network
   with no activations?

9. Decompose sigmoid (unit 1.4 skill): list the chain of zoo machines that turns
   $x$ into $\dfrac{1}{1 + e^{-x}}$, in firing order.

---

## Part C — Match & diagnose

10. Match each job to the best activation (sigmoid / tanh / ReLU):

    a) "Output must be a probability for spam-or-not."

    b) "Hidden layers of a huge image model — needs to be dirt cheap to compute."

    c) "Outputs should be centred on zero, between −1 and 1."

11. Diagnose: a friend builds a 50-layer network using *only* linear layers ("more layers =
    smarter, right?"). It performs exactly as well as a 1-layer one. Explain why in
    two lines, citing problem 8.

12. Spot the error: "My sigmoid output is exactly 1.0, so the model is 100% certain."
    What's mathematically off about this claim, and what did floating point do?

---

## Part D — Deep end

*Beyond what was taught.*

13. The lesson's deep-end: compute $\mathrm{ReLU}(x) + \mathrm{ReLU}(-x)$ at $x = 3$, $x = -3$
    and $x = 0$. Sketch the result. What familiar machine have you built from two ReLUs?

14. Sketch $y = \mathrm{ReLU}(x) - \mathrm{ReLU}(x - 2)$. *(Compute it at
    $x = -1, 0, 1, 2, 3, 4$ first. Flat, ramp, flat — you've just built a feature detector.)*

15. Show, with Module 0 fraction moves, that $\sigma(-x) = 1 - \sigma(x)$.
    *(Start from $\sigma(-x) = \frac{1}{1+e^{x}}$ and make the two sides meet. Tough — attempt,
    name your moves.)* What does this symmetry mean for "probability of cat" vs
    "probability of not-cat"?

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
