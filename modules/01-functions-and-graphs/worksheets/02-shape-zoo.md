# Worksheet 1.2 — The Shape Zoo

*Pen and paper. Sketch on paper FIRST — rough shape, key crossings, asymptotes as dashed lines.
Only after scanning do you verify with matplotlib (Part E). Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: name the species

For each blueprint, write the species (linear / quadratic / exponential / log / reciprocal)
and its one-word personality:

1. $y = 3^x$

2. $y = x^2 + 1$

3. $y = \dfrac{5}{x}$

4. $y = 4 - 2x$

5. $y = \log_2 x$

---

## Part B — Core: sketch from the blueprint

Sketch each on its own set of axes. Mark: axis crossings, asymptotes (dashed), and label one
concrete point you computed (e.g. "at $x=2$, $y=4$").

6. $y = 2x - 1$

7. $y = x^2 - 4$   *(where are the TWO x-axis crossings? Module 0.3 factoring finds them)*

8. $y = 2^x$   *(what's $2^0$? Where's the floor it never touches?)*

9. $y = \log_2 x$   *(what's its domain? Where does it cross the x-axis?)*

10. $y = \dfrac{1}{x}$   *(both branches. What happens just left and just right of $x = 0$?)*

---

## Part C — Match the description to the equation

Loss-curve triage. Match each description to exactly one equation from the list —
one equation is a decoy.

Equations: $\quad y = e^{-x} \qquad y = x^2 \qquad y = \log x \qquad y = 3x + 2 \qquad y = e^{x}$

11. "Training loss: drops steeply at first, then flattens, creeping toward zero but never
    reaching it." → ?

12. "Bug! The loss is *exploding* — each epoch it grows faster than the last." → ?

13. "Reward over time: shot up early, still improving, but each epoch buys less than the one
    before. Never actually stops growing." → ?

14. "Distance from the target as I overshoot past it: symmetric, with a single lowest point." → ?

15. Which equation was the decoy — and describe in one line what *its* graph looks like.

---

## Part D — Deep end

*Beyond what was taught.*

16. Sketch $y = 2^{-x}$. Which side is the explosion on now? Which side hugs the floor?

17. Who wins eventually, $x^2$ or $2^x$? Compute both at $x = 2, 4, 10$. Notice anything
    embarrassing for the quadratic at $x = 2$ and $4$ vs $10$?

18. Sketch $y = \dfrac{1}{x - 2}$. *(Same species as $\frac{1}{x}$ — but where has the crash
    site moved to? Next unit explains why.)*

19. The lesson's deep-end: an accuracy curve rises fast then levels off near 1.0.
    Propose a blueprint from the zoo (transformed however you like) with that shape.

---

## Part E — Python check (at the computer, after scanning)

20. Verify every Part B sketch:

```python
import sys; sys.path.append("../../tools")   # adjust if running from elsewhere
import numpy as np
import matplotlib.pyplot as plt
from plots import plot_functions

plot_functions({
    "y = 2x - 1":  lambda x: 2*x - 1,
    "y = x^2 - 4": lambda x: x**2 - 4,
}, xlim=(-5, 5), ylim=(-6, 10))
plt.show()
```

Add the other three yourself (`2**x`, `np.log2(x)`, `1/x`). Next to each Part B sketch write
✓ if your paper version had the right shape, crossings and asymptotes — or a note on what you missed.
