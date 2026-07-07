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

   ::: answer
   Straight line, slope $3$, y-intercept $(0, -2)$, x-intercept $\left(\tfrac{2}{3}, 0\right)$
   (set $3x - 2 = 0$). No asymptotes — read straight off $y = mx + c$.
   :::

2. $y = x^2 - 9$

   ::: answer
   Upward parabola, vertex $(0, -9)$. x-intercepts at $x = \pm 3$ (move: $x^2 = 9$, then $\sqrt{\ }$
   both sides — two roots). y-intercept $-9$. No asymptotes.
   :::

3. $y = (x - 2)^2 - 3$

   ::: answer
   Upward parabola, vertex $(2, -3)$ (shift right 2, down 3 from $y = x^2$). x-intercepts at
   $x = 2 \pm \sqrt{3}$ (move: $(x-2)^2 = 3$, then $\sqrt{\ }$ both sides). y-intercept: $(0-2)^2 - 3 = 1$.
   :::

4. $y = 2^x + 1$

   ::: answer
   Exponential growth curve, horizontal asymptote $y = 1$ as $x \to -\infty$. y-intercept
   $2^0 + 1 = 2$. No x-intercept — $2^x > 0$ always, so $y > 1$ always. Grows without bound as
   $x \to \infty$.
   :::

5. $y = -\dfrac{1}{x}$

   ::: answer
   Reciprocal shape reflected in the x-axis. Vertical asymptote $x = 0$, horizontal asymptote
   $y = 0$. Branches in quadrant II ($x<0, y>0$) and quadrant IV ($x>0, y<0$). No intercepts.
   :::

6. $y = \mathrm{ReLU}(x) = \max(0, x)$

   ::: answer
   Flat along $y = 0$ for $x \le 0$, then the straight line $y = x$ for $x > 0$ — a kink
   (sharp corner, not smooth) at the origin. No asymptotes.
   :::

---

## Section 2 — Predict the shape (no full sketch needed)

For each: name the species, the direction it heads at both far ends, and any asymptotes or
forbidden inputs.

7. $y = e^{-x}$

   ::: answer
   Species: exponential decay. As $x \to -\infty$, $y \to \infty$; as $x \to \infty$, $y \to 0^+$
   (horizontal asymptote $y = 0$). Domain all reals — no forbidden inputs.
   :::

8. $y = \log x$

   ::: answer
   Species: logarithm. Vertical asymptote $x = 0$: as $x \to 0^+$, $y \to -\infty$. As
   $x \to \infty$, $y \to \infty$ ever more slowly. Forbidden inputs: $x \le 0$ (domain $x > 0$).
   :::

9. $y = -(x + 1)^2$

   ::: answer
   Species: downward parabola (leading coefficient negative). Vertex $(-1, 0)$ (shift left 1,
   then reflect). As $x \to \pm\infty$, $y \to -\infty$ at both ends. Touches the x-axis only at
   the vertex; no other asymptotes.
   :::

10. $y = \dfrac{1}{x - 3}$

    ::: answer
    Species: reciprocal (hyperbola), shifted right 3. Vertical asymptote $x = 3$ (forbidden
    input), horizontal asymptote $y = 0$. As $x \to \infty$, $y \to 0^+$; as $x \to -\infty$,
    $y \to 0^-$.
    :::

---

## Section 3 — Match the graph to the equation

Each description fits exactly one equation. Two equations are decoys.

Equations:
$$y = \sigma(x) = \tfrac{1}{1+e^{-x}} \quad\; y = x^2 + 2 \quad\; y = \log x \quad\; y = 2^{-x} \quad\; y = 2^{x} \quad\; y = \tanh x \quad\; y = \tfrac{1}{x}$$

11. "S-curve, climbs from a floor near $-1$ to a ceiling near $+1$, passes through the origin." → ?

    ::: answer
    $y = \tanh x$ — range $(-1, 1)$ and $\tanh 0 = 0$.
    :::

12. "Decays toward zero as $x$ grows; explodes as $x$ goes negative; crosses the $y$-axis at 1." → ?

    ::: answer
    $y = 2^{-x}$ — as $x \to \infty$, $2^{-x} \to 0^+$; as $x \to -\infty$, $2^{-x} \to \infty$;
    at $x=0$, $y = 2^0 = 1$.
    :::

13. "Valley, symmetric about the $y$-axis, never dips below $y = 2$, no axis crossings at all." → ?

    ::: answer
    $y = x^2 + 2$ — vertex (minimum) at $(0, 2)$, never reaches $y \le 2$ so it never touches
    either axis.
    :::

14. "Only exists for positive inputs; crosses the $x$-axis at 1; grows forever, ever more slowly." → ?

    ::: answer
    $y = \log x$ — domain $x > 0$, $\log 1 = 0$.
    :::

15. "S-curve squashed between 0 and 1, passing through $\left(0, \frac{1}{2}\right)$." → ?

    ::: answer
    $y = \sigma(x)$ — the sigmoid, range $(0,1)$, $\sigma(0) = \frac{1}{1+e^0} = \frac{1}{2}$.
    :::

16. Name both decoys and give each a one-line description of its graph.

    ::: answer
    Decoys (unused above): $y = 2^{x}$ — exponential growth, horizontal asymptote $y=0$ as
    $x\to-\infty$, passes through $(0,1)$. $y = \dfrac{1}{x}$ — hyperbola with asymptotes
    $x = 0$ and $y = 0$, branches in quadrants I and III.
    :::

---

## Section 4 — Composition

$f(x) = x^2 \qquad g(x) = x - 4 \qquad h(x) = 2x + 1$

17. Compute $f(g(6))$ and $g(f(6))$, showing the intermediate values.

    ::: answer
    $f(g(6))$: $g(6) = 6-4 = 2$, then $f(2) = 2^2 = 4$. $g(f(6))$: $f(6) = 6^2 = 36$, then
    $g(36) = 36-4 = 32$. Different answers — composition order matters, $f(g(x)) \ne g(f(x))$
    in general.
    :::

18. Build and expand the blueprint $f(h(x))$.

    ::: answer
    $f(h(x)) = (2x+1)^2 = 4x^2 + 4x + 1$ — move: square the whole binomial ($(a+b)^2 = a^2+2ab+b^2$
    with $a=2x, b=1$), don't just square each term.
    :::

19. Decompose $k(x) = \dfrac{1}{(x+5)^2}$ into a chain of machines in firing order.

    ::: answer
    $a(x) = x+5$ fires first, $b(x) = x^2$ fires second, $c(x) = \dfrac{1}{x}$ fires last:
    $k = c \circ b \circ a$, i.e. $k(x) = c(b(a(x)))$. Check: $c(b(x+5)) = c\left((x+5)^2\right)
    = \dfrac{1}{(x+5)^2}$. ✓
    :::

20. Expand $h(h(x))$. What species is it? State, in two lines, why deep networks need
    nonlinear activations between layers — and what the kink in ReLU has to do with it.

    ::: answer
    $h(h(x)) = 2(2x+1)+1 = 4x+3$ — still linear (a straight line). Composing linear machines
    always gives another linear machine, so stacking pure linear layers collapses to one
    equivalent layer no matter how deep. ReLU's kink makes it non-linear (it isn't $ax+b$
    anywhere near 0), so stacking it actually builds new, bent shapes layer by layer — that's
    the entire point of an activation function.
    :::

21. Domain hunt: with $v(x) = \dfrac{1}{x}$, what is the domain of $v(g(x))$?
    *(Which input crashes the pipeline — and in which machine does the crash actually happen?)*

    ::: answer
    $v(g(x)) = \dfrac{1}{x-4}$, domain: all reals except $x = 4$. $g$ itself never crashes
    (defined everywhere); the crash happens inside $v$ (division by zero) when $g$ hands it a $0$,
    which occurs when $x-4=0 \Rightarrow x=4$.
    :::

---

## Section 5 — Deep end

22. Predict the shape of $y = 2^{-x^2}$, then sketch it. Work like a machine-reader:
    inner machine first — what does $-x^2$ do to inputs on both sides of zero? Then feed that
    into $2^{(\;)}$. Mark the highest point and what happens at both far ends.
    *(You have never been taught this curve. You have been taught everything needed to derive it —
    and you'll meet it again wearing a lab coat in Module 4.)*

    ::: answer
    Inner machine $-x^2$ is symmetric (even) and always $\le 0$: it peaks at $0$ when $x=0$ and
    plunges to $-\infty$ as $x \to \pm\infty$ either direction. Feeding that into $2^{(\;)}$
    (always positive, increasing) turns the inner peak $0$ into the outer peak $2^0 = 1$ at
    $x=0$, and turns $-\infty$ into $\to 0^+$ at both far ends. Result: a symmetric bell-shaped
    bump, highest point $(0,1)$, horizontal asymptote $y=0$ as $x \to \pm\infty$ — the Gaussian
    shape behind the normal distribution.
    :::

---

**After scanning:** open a notebook, plot all of Sections 1, 2 and 5 with `plot_functions`,
and mark your own predictions honestly. Then tell Claude the scan is in — Module 2 (and the
logistic-map interlude you glimpsed in unit 1.4) is waiting on the other side.
