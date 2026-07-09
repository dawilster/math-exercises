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

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

16. Sketch $y = 2^{-x}$. Which side is the explosion on now? Which side hugs the floor?

    ::: rephrase
    Same species as $2^x$ (the $x$ is still up in the exponent), but the minus sign in $2^{-x}$
    runs it backwards — exactly the "predict before you plot" example from the lesson. "Which
    side explodes, which side hugs the floor?" just asks you to sketch it and read the two ends.
    A quick sanity test: plug in $x = -3$ vs $x = +3$ and see which one is huge.
    :::

    ::: hint
    A minus sign in the exponent is a **reflection**. Across which axis does it flip $2^x$?
    :::

    ::: hint
    Rewrite the exponent to make the shape obvious: $2^{-x} = (1/2)^x$ — a base *less than 1*,
    so it *decays* as $x$ grows.
    :::

    ::: steps
    1. **Rewrite the exponent** ($a^{-x} = (1/a)^x$). $2^{-x} = (1/2)^x$
    2. **Reflect $2^x$ across the y-axis** — same graph read right-to-left. $x=-3 \Rightarrow 8,\quad x=+3 \Rightarrow 1/8$
    3. **Read off the two ends.** explosion on the LEFT ($x \to -\infty,\; y \to \infty$); floor-hug on the RIGHT ($x \to +\infty,\; y \to 0$)
    :::

17. Who wins eventually, $x^2$ or $2^x$? Compute both at $x = 2, 4, 10$. Notice anything
    embarrassing for the quadratic at $x = 2$ and $4$ vs $10$?

    ::: rephrase
    This is the lesson's "species barrier" trap made concrete: $x^2$ (variable in the *base*)
    vs $2^x$ (variable in the *exponent*). No cleverness needed — just build a little table,
    plug in $x = 2, 4, 10$, and compare the two columns. "Who wins eventually" means: for big
    $x$, which grows bigger and stays bigger?
    :::

    ::: hint
    Make a two-column table — $x^2$ in one, $2^x$ in the other — and fill in $x = 2, 4, 10$.
    :::

    ::: hint
    Look hard at $x=2$ and $x=4$ before you decide who's stronger — the numbers *match*.
    Then let $x=10$ break the tie.
    :::

    ::: steps
    1. **Evaluate at $x=2$.** $x^2 = 4,\quad 2^x = 4$ — tied
    2. **Evaluate at $x=4$.** $x^2 = 16,\quad 2^x = 16$ — tied again
    3. **Evaluate at $x=10$.** $x^2 = 100,\quad 2^x = 1024$ — exponential already 10× bigger
    4. **Conclude.** the quadratic only ever manages to *tie* (at 2 and 4); past that $2^x$ dominates permanently and increasingly — $2^x$ wins eventually, always
    :::

18. Sketch $y = \dfrac{1}{x - 2}$. *(Same species as $\frac{1}{x}$ — but where has the crash
    site moved to? Next unit explains why.)*

    ::: rephrase
    Same reciprocal species as $\frac1x$ — two swooping branches, both axes as asymptotes. The
    only new question is: *where's the crash now?* $\frac1x$ crashed where its bottom hit zero
    ($x=0$); the bottom here is $x-2$, so find the input that makes *that* zero.
    :::

    ::: hint
    A reciprocal crashes (vertical asymptote) wherever the **denominator equals 0**. Which $x$
    makes $x - 2 = 0$?
    :::

    ::: hint
    The horizontal asymptote doesn't move — dividing 1 by something huge still gives ~0. So only
    the crash slides sideways; the whole picture shifts with it.
    :::

    ::: steps
    1. **Find the crash: set the denominator to 0.** $x - 2 = 0 \Rightarrow x = 2$ — vertical asymptote
    2. **Horizontal asymptote is unchanged.** $y = 0$
    3. **Describe the shape.** same two branches as $1/x$, shifted 2 units right
    :::

19. The lesson's deep-end: an accuracy curve rises fast then levels off near 1.0.
    Propose a blueprint from the zoo (transformed however you like) with that shape.

    ::: rephrase
    You're being asked to *invent* a curve with a target shape: rises fast, then flattens just
    under a ceiling of 1. This is the lesson's parting question — and you already met its mirror
    image in problem 16: $2^{-x}$ *falls* fast toward the floor 0. You need something that *rises*
    fast toward the ceiling 1. Turn one into the other.
    :::

    ::: hint
    You already own a curve that drops fast to 0: $2^{-x}$ (or $e^{-x}$). How do you turn a
    "falling to 0" curve into a "rising to 1" curve?
    :::

    ::: hint
    Subtract the decaying curve from 1. When the decaying part is big, $1 - (\text{big})$ is
    small; when it decays to 0, $1 - 0 = 1$ — the ceiling.
    :::

    ::: steps
    1. **Start with a decaying exponential.** $2^{-x} \to 0$ as $x$ grows
    2. **Flip it up under a ceiling of 1** — the key move, "1 minus a decaying term". $y = 1 - 2^{-x}$
    3. **Check the ends.** at $x=0$: $y = 1 - 1 = 0$; as $x \to \infty$: $2^{-x}\to 0$ so $y \to 1$ — rises fast, flattens near the ceiling (any decaying term works, e.g. $e^{-x}$)
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
