# Worksheet 1.2 — The Shape Zoo

*Pen and paper. Sketch on paper FIRST — rough shape, key crossings, asymptotes as dashed lines.
Only after scanning do you verify with matplotlib (Part E). Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: name the species

For each blueprint, write the species (linear / quadratic / exponential / log / reciprocal)
and its one-word personality:

1. $y = 3^x$

   ::: answer
   Exponential — personality: explosive growth. Hugs the floor $y = 0$ (never touches) as
   $x \to -\infty$, shoots upward as $x$ grows. Passes through $(0, 1)$.
   :::

2. $y = x^2 + 1$

   ::: answer
   Quadratic (parabola) — opens upward since the coefficient of $x^2$ is positive.
   Symmetric U-shape, vertex (minimum) at $(0, 1)$ — never touches or crosses the x-axis.
   :::

3. $y = \dfrac{5}{x}$

   ::: answer
   Reciprocal — personality: shy of both axes. Vertical asymptote at $x = 0$, horizontal
   asymptote at $y = 0$, two mirror-image branches (quadrants I and III since $5 > 0$).
   :::

4. $y = 4 - 2x$

   ::: answer
   Linear — personality: steady straight-line fall, slope $-2$. Crosses the y-axis at
   $(0, 4)$ and the x-axis at $(2, 0)$.
   :::

5. $y = \log_2 x$

   ::: answer
   Logarithmic — personality: slow, patient growth. Climbs fast near $x = 0^+$ then flattens.
   Vertical asymptote at $x = 0$, crosses the x-axis at $(1, 0)$.
   :::

---

## Part B — Core: sketch from the blueprint

Sketch each on its own set of axes. Mark: axis crossings, asymptotes (dashed), and label one
concrete point you computed (e.g. "at $x=2$, $y=4$").

6. $y = 2x - 1$

   ::: answer
   Linear, slope $2$. y-intercept $(0, -1)$; x-intercept at $x = \frac12$, so $(\frac12, 0)$.
   Concrete point: at $x = 2$, $y = 3$.
   :::

7. $y = x^2 - 4$   *(where are the TWO x-axis crossings? Module 0.3 factoring finds them)*

   ::: answer
   Parabola, opens upward, vertex (minimum) at $(0, -4)$. x-axis crossings at $x = \pm 2$
   (factors as $(x-2)(x+2) = 0$). Concrete point: at $x = 3$, $y = 5$.
   :::

8. $y = 2^x$   *(what's $2^0$? Where's the floor it never touches?)*

   ::: answer
   $2^0 = 1$, so y-intercept $(0, 1)$. Floor (horizontal asymptote) at $y = 0$, approached
   as $x \to -\infty$ but never touched. Concrete point: at $x = 3$, $y = 8$.
   :::

9. $y = \log_2 x$   *(what's its domain? Where does it cross the x-axis?)*

   ::: answer
   Domain: $x > 0$ (vertical asymptote at $x = 0$). Crosses the x-axis at $x = 1$
   (since $\log_2 1 = 0$). Concrete point: at $x = 4$, $y = 2$.
   :::

10. $y = \dfrac{1}{x}$   *(both branches. What happens just left and just right of $x = 0$?)*

    ::: answer
    Vertical asymptote $x = 0$, horizontal asymptote $y = 0$; two branches in quadrants I
    ($x>0, y>0$) and III ($x<0, y<0$). Just right of $0$ ($x \to 0^+$), $y \to +\infty$;
    just left ($x \to 0^-$), $y \to -\infty$.
    :::

---

## Part C — Match the description to the equation

Loss-curve triage. Match each description to exactly one equation from the list —
one equation is a decoy.

Equations: $\quad y = e^{-x} \qquad y = x^2 \qquad y = \log x \qquad y = 3x + 2 \qquad y = e^{x}$

11. "Training loss: drops steeply at first, then flattens, creeping toward zero but never
    reaching it." → ?

    ::: answer
    $y = e^{-x}$ — decaying exponential: starts high, falls fast, flattens toward the
    asymptote $y = 0$ without ever reaching it.
    :::

12. "Bug! The loss is *exploding* — each epoch it grows faster than the last." → ?

    ::: answer
    $y = e^{x}$ — growing exponential: increases faster and faster, no ceiling.
    :::

13. "Reward over time: shot up early, still improving, but each epoch buys less than the one
    before. Never actually stops growing." → ?

    ::: answer
    $y = \log x$ — logarithmic: keeps rising forever, but the rate of increase keeps
    shrinking (concave, decelerating growth).
    :::

14. "Distance from the target as I overshoot past it: symmetric, with a single lowest point." → ?

    ::: answer
    $y = x^2$ — parabola: symmetric about its vertex, a single minimum point.
    :::

15. Which equation was the decoy — and describe in one line what *its* graph looks like.

    ::: answer
    Decoy: $y = 3x + 2$ — a plain straight line, constant slope $3$, no curvature, no
    flattening or exploding, just climbs steadily forever.
    :::

---

## Part D — Deep end

*Beyond what was taught.*

16. Sketch $y = 2^{-x}$. Which side is the explosion on now? Which side hugs the floor?

    ::: answer
    $y = 2^{-x} = (1/2)^x$ is $2^x$ mirrored across the y-axis. The explosion is now on the
    LEFT (as $x \to -\infty$, $y \to \infty$); the floor-hugging ($y \to 0$) is on the RIGHT
    (as $x \to +\infty$).
    :::

17. Who wins eventually, $x^2$ or $2^x$? Compute both at $x = 2, 4, 10$. Notice anything
    embarrassing for the quadratic at $x = 2$ and $4$ vs $10$?

    ::: answer
    At $x=2$: $x^2=4$, $2^x=4$ — tied. At $x=4$: $x^2=16$, $2^x=16$ — tied again!
    At $x=10$: $x^2=100$, $2^x=1024$ — the exponential is already 10× bigger.
    Embarrassing bit: the quadratic manages to *tie* twice before the exponential
    permanently, and increasingly, dominates. $2^x$ wins eventually — always.
    :::

18. Sketch $y = \dfrac{1}{x - 2}$. *(Same species as $\frac{1}{x}$ — but where has the crash
    site moved to? Next unit explains why.)*

    ::: answer
    The crash site (vertical asymptote) moves from $x = 0$ to $x = 2$; the horizontal
    asymptote stays at $y = 0$. Same two-branch shape as $1/x$, just shifted 2 units right.
    :::

19. The lesson's deep-end: an accuracy curve rises fast then levels off near 1.0.
    Propose a blueprint from the zoo (transformed however you like) with that shape.

    ::: answer
    One valid choice: $y = 1 - 2^{-x}$ for $x \ge 0$. At $x=0$, $y=0$; as $x$ grows,
    $2^{-x} \to 0$ so $y \to 1$ — rising fast at first, then flattening near the ceiling
    $y = 1$. The key move: "1 minus a decaying exponential" (any decaying term works,
    e.g. $e^{-x}$).
    :::

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
