# Worksheet 1.3 — Transforming Graphs

*Pen and paper. Sketch FIRST, verify with matplotlib only in Part E after scanning.
For every transformation, name the move — "shift left 2", "flip over x-axis" — the way you
named balance-scale moves in Module 0. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: name the move

$f$ is any machine. Describe in words what each does to the graph of $y = f(x)$:

1. $y = f(x) + 4$

2. $y = f(x - 2)$   *(careful — inside the brackets is opposite day)*

3. $y = 3f(x)$

4. $y = -f(x)$

5. $y = f(-x)$

---

## Part B — Core: sketch by moves

Start from the zoo animal, list the moves in order, then sketch. Mark the key point that moved
(vertex, crossing, or asymptote).

6. $y = x^2 - 3$   *(from $y = x^2$)*

7. $y = (x + 2)^2$   *(from $y = x^2$ — which way does the vertex go?)*

8. $y = -(x - 1)^2 + 4$   *(from $y = x^2$, three moves — do them in blueprint order)*

9. $y = 2^x + 3$   *(from $y = 2^x$ — where is the asymptote now? Draw it dashed.)*

10. $y = \dfrac{1}{x - 2}$   *(from $y = \frac{1}{x}$ — your worksheet 1.2 deep-end, now official)*

---

## Part C — Spot the error

Each claim has exactly one mistake. Circle and correct it.

11. "$y = (x + 5)^2$ is $y = x^2$ shifted **right** 5, because the 5 is positive."

12. "$y = 2^x + 3$ still has its asymptote at $y = 0$, because shifts don't affect asymptotes."

13. "$y = 2f(x) + 1$ and $y = 2(f(x) + 1)$ are the same graph, because both stretch by 2 and
    shift by 1."

---

## Part D — Deep end

*Beyond what was taught.*

14. Normalisation, the ML ritual: $z = \dfrac{x - 5}{2}$. Describe it as two graph-moves applied
    to data. If the original data was centred at 5 with spread 2, where is $z$ centred and what's
    its spread?

15. The lesson's deep-end: show with an exponent rule (Module 0.5) that $e^{x+1} = e \cdot e^x$.
    So "shift left 1" and "stretch vertically by $e$" are the *same move* for this machine.
    Try the same trick on $y = x^2$: is $(x+1)^2$ a vertical stretch of $x^2$? Why not?

16. Write the blueprint for: "$\frac{1}{x}$, flipped upside down, then shifted up 1."
    Then sketch it. Bonus: what are its two asymptotes?

17. A machine's graph is a valley with vertex at $(-3, 7)$, opening downward… wait, valleys don't
    open downward. Fix the sentence, then write a blueprint whose graph is a *hill* with peak
    at $(-3, 7)$.

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
