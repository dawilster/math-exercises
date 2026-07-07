# Boss Worksheet — Module 1: Functions & Graphs

**The rules:**

- Done **cold**: pen and paper, no notes, no lessons open, no computer.
- Every sketch on paper, with axis crossings and asymptotes (dashed) marked.
- Photograph everything into `scans/inbox/` when done.
- **≥ 85% with sound reasoning unlocks Module 2 — Linear Algebra.** Gaps go on the review queue.
- **AFTER scanning:** verify every sketch yourself in matplotlib (`plot_functions`) and note which
  ones you'd already nailed. Marking your own predictions is half the training.

---

## Section 1 — Sketch from the blueprint

Sketch each on its own axes. Mark crossings, vertices/kinks, and asymptotes.

1. $y = 3x - 2$

2. $y = x^2 - 9$

3. $y = (x - 2)^2 - 3$

4. $y = 2^x + 1$

5. $y = -\dfrac{1}{x}$

6. $y = \mathrm{ReLU}(x) = \max(0, x)$

---

## Section 2 — Predict the shape (no full sketch needed)

For each: name the species, the direction it heads at both far ends, and any asymptotes or
forbidden inputs.

7. $y = e^{-x}$

8. $y = \log x$

9. $y = -(x + 1)^2$

10. $y = \dfrac{1}{x - 3}$

---

## Section 3 — Match the graph to the equation

Each description fits exactly one equation. Two equations are decoys.

Equations:
$$y = \sigma(x) = \tfrac{1}{1+e^{-x}} \quad\; y = x^2 + 2 \quad\; y = \log x \quad\; y = 2^{-x} \quad\; y = 2^{x} \quad\; y = \tanh x \quad\; y = \tfrac{1}{x}$$

11. "S-curve, climbs from a floor near $-1$ to a ceiling near $+1$, passes through the origin." → ?

12. "Decays toward zero as $x$ grows; explodes as $x$ goes negative; crosses the $y$-axis at 1." → ?

13. "Valley, symmetric about the $y$-axis, never dips below $y = 2$, no axis crossings at all." → ?

14. "Only exists for positive inputs; crosses the $x$-axis at 1; grows forever, ever more slowly." → ?

15. "S-curve squashed between 0 and 1, passing through $\left(0, \frac{1}{2}\right)$." → ?

16. Name both decoys and give each a one-line description of its graph.

---

## Section 4 — Composition

$f(x) = x^2 \qquad g(x) = x - 4 \qquad h(x) = 2x + 1$

17. Compute $f(g(6))$ and $g(f(6))$, showing the intermediate values.

18. Build and expand the blueprint $f(h(x))$.

19. Decompose $k(x) = \dfrac{1}{(x+5)^2}$ into a chain of machines in firing order.

20. Expand $h(h(x))$. What species is it? State, in two lines, why deep networks need
    nonlinear activations between layers — and what the kink in ReLU has to do with it.

21. Domain hunt: with $v(x) = \dfrac{1}{x}$, what is the domain of $v(g(x))$?
    *(Which input crashes the pipeline — and in which machine does the crash actually happen?)*

---

## Section 5 — Deep end

22. Predict the shape of $y = 2^{-x^2}$, then sketch it. Work like a machine-reader:
    inner machine first — what does $-x^2$ do to inputs on both sides of zero? Then feed that
    into $2^{(\;)}$. Mark the highest point and what happens at both far ends.
    *(You have never been taught this curve. You have been taught everything needed to derive it —
    and you'll meet it again wearing a lab coat in Module 4.)*

---

**After scanning:** open a notebook, plot all of Sections 1, 2 and 5 with `plot_functions`,
and mark your own predictions honestly. Then tell Claude the scan is in — Module 2 (and the
logistic-map interlude you glimpsed in unit 1.4) is waiting on the other side.
