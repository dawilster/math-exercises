# Worksheet 1.3 — Transforming Graphs

*Pen and paper. Sketch FIRST, verify with matplotlib only in Part E after scanning.
For every transformation, name the move — "shift left 2", "flip over x-axis" — the way you
named balance-scale moves in Module 0. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: name the move

$f$ is any machine. Describe in words what each does to the graph of $y = f(x)$:

1. $y = f(x) + 4$

   ::: answer
   Shifts **up** 4 — move: add 4 to the output.
   :::

2. $y = f(x - 2)$   *(careful — inside the brackets is opposite day)*

   ::: answer
   Shifts **right** 2 — move: $x \to x - 2$ is added to the *input*, and input moves run
   backwards: $-2$ inside pushes the graph right, not left.
   :::

3. $y = 3f(x)$

   ::: answer
   Vertical stretch ×3 — move: multiply the output by 3.
   :::

4. $y = -f(x)$

   ::: answer
   Flips upside down (reflects over the $x$-axis) — move: flip the output.
   :::

5. $y = f(-x)$

   ::: answer
   Flips left-right (reflects over the $y$-axis) — move: flip the input.
   :::

---

## Part B — Core: sketch by moves

Start from the zoo animal, list the moves in order, then sketch. Mark the key point that moved
(vertex, crossing, or asymptote).

6. $y = x^2 - 3$   *(from $y = x^2$)*

   ::: answer
   Move: subtract 3 from the output → shift **down** 3. Vertex $(0,0) \to (0,-3)$.
   :::

7. $y = (x + 2)^2$   *(from $y = x^2$ — which way does the vertex go?)*

   ::: answer
   Move: $x \to x + 2$ added to the input → shift **left** 2 (opposite day). Vertex
   $(0,0) \to (-2, 0)$.
   :::

8. $y = -(x - 1)^2 + 4$   *(from $y = x^2$, three moves — do them in blueprint order)*

   ::: answer
   Blueprint order, innermost first: (1) $x \to x - 1$ — shift **right** 1, vertex
   $(0,0) \to (1,0)$; (2) leading $-$ — flip upside down, valley becomes a hill, vertex
   stays $(1,0)$; (3) $+4$ — shift **up** 4, vertex $(1,0) \to (1,4)$. Result: a
   downward-opening hill peaking at $(1, 4)$.
   :::

9. $y = 2^x + 3$   *(from $y = 2^x$ — where is the asymptote now? Draw it dashed.)*

   ::: answer
   Move: add 3 to the output → shift **up** 3. The asymptote moves with it, from $y = 0$
   to $y = 3$.
   :::

10. $y = \dfrac{1}{x - 2}$   *(from $y = \frac{1}{x}$ — your worksheet 1.2 deep-end, now official)*

    ::: answer
    Move: $x \to x - 2$ added to the input → shift **right** 2 (opposite day). Vertical
    asymptote moves from $x = 0$ to $x = 2$; horizontal asymptote stays at $y = 0$.
    :::

---

## Part C — Spot the error

Each claim has exactly one mistake. Circle and correct it.

11. "$y = (x + 5)^2$ is $y = x^2$ shifted **right** 5, because the 5 is positive."

    ::: answer
    Wrong — it's shifted **left** 5. The $+5$ sits inside the brackets, added to the
    *input*, and input moves run backwards: opposite day.
    :::

12. "$y = 2^x + 3$ still has its asymptote at $y = 0$, because shifts don't affect asymptotes."

    ::: answer
    Wrong — the asymptote moves to $y = 3$. The $+3$ is added to the *output*, so it
    lifts the whole graph, floor included. Vertical shifts always drag the horizontal
    asymptote with them.
    :::

13. "$y = 2f(x) + 1$ and $y = 2(f(x) + 1)$ are the same graph, because both stretch by 2 and
    shift by 1."

    ::: answer
    Wrong — different graphs. $y = 2f(x) + 1$ stretches by 2, *then* shifts up 1.
    $y = 2(f(x) + 1) = 2f(x) + 2$ shifts up 1, *then* stretches by 2 — landing as $+2$
    overall, not $+1$. Brackets set the order, and order changes the result.
    :::

---

## Part D — Deep end

*Beyond what was taught.*

14. Normalisation, the ML ritual: $z = \dfrac{x - 5}{2}$. Describe it as two graph-moves applied
    to data. If the original data was centred at 5 with spread 2, where is $z$ centred and what's
    its spread?

    ::: answer
    Two moves: subtract 5 (shift by $-5$ → centres the data at 0), then divide by 2
    (squash by $\div 2$ → halves the spread). Result: $z$ is centred at $0$ with spread $1$.
    :::

15. The lesson's deep-end: show with an exponent rule (Module 0.5) that $e^{x+1} = e \cdot e^x$.
    So "shift left 1" and "stretch vertically by $e$" are the *same move* for this machine.
    Try the same trick on $y = x^2$: is $(x+1)^2$ a vertical stretch of $x^2$? Why not?

    ::: answer
    $e^{x+1} = e^x \cdot e^1 = e \cdot e^x$ (exponent rule $a^{m+n} = a^m a^n$) — confirms
    shift left 1 = stretch $\times e$ for this machine. For $x^2$: expand
    $(x+1)^2 = x^2 + 2x + 1$. That's not $a \cdot x^2$ for any constant $a$ — there's a
    leftover $2x + 1$ term — so it is **not** a vertical stretch. The trick only works for
    exponentials because $e^{x+c}$ factors into $e^c \cdot e^x$; polynomials don't factor
    that way under a shift.
    :::

16. Write the blueprint for: "$\frac{1}{x}$, flipped upside down, then shifted up 1."
    Then sketch it. Bonus: what are its two asymptotes?

    ::: answer
    Blueprint: $y = -\dfrac{1}{x} + 1$. Asymptotes: vertical $x = 0$ (unchanged by output
    moves), horizontal $y = 1$ (the flip keeps it at $y = 0$, then $+1$ lifts it to $y = 1$).
    :::

17. A machine's graph is a valley with vertex at $(-3, 7)$, opening downward… wait, valleys don't
    open downward. Fix the sentence, then write a blueprint whose graph is a *hill* with peak
    at $(-3, 7)$.

    ::: answer
    Fix: a valley (parabola) opens **upward**, not downward — a downward-opening parabola
    is a hill. Blueprint for a hill peaking at $(-3, 7)$: $y = -(x + 3)^2 + 7$.
    :::

---

## Part E — Python check (at the computer, after scanning)

18. Verify Part B by plotting each transformed machine **on the same axes as its zoo original**:

```python
import sys; sys.path.append("../../tools")
import numpy as np
import matplotlib.pyplot as plt
from plots import plot_functions

plot_functions({
    "y = x^2":          lambda x: x**2,
    "y = -(x-1)^2 + 4": lambda x: -(x - 1)**2 + 4,
}, xlim=(-6, 6), ylim=(-8, 8))
plt.show()
```

Do the rest of Part B the same way. ✓ or a miss-note next to each sketch.

> **Bonus thought:** plot problem 15's pair — `np.e * np.exp(x)` and `np.exp(x + 1)`.
> If the lesson is right, how many curves should you see on the screen?
