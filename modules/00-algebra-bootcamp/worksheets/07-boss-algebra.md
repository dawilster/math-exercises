# Boss Worksheet — Module 0: Algebra Bootcamp

**The rules (this is the mastery gate):**

- **Cold.** Pen and paper, no notes, no lessons open, no Python until Part E says so.
- **Name every move** next to every step — the reasoning is what's being marked, not just answers.
- If stuck, write what you tried and where it jammed, then move on. Partial reasoning scores.
- When done, photograph everything into `scans/inbox/`.
- **≥ 85% with sound reasoning unlocks Module 1** (and the Fibonacci–golden-ratio interlude).
  Gaps go on the review queue — no shame, that's the system working.

---

## Part 1 — The moves, warmed up *(0.1–0.2)*

1. Solve for $x$, naming each move: $\;4x - 7 = 21$

2. Solve for $x$: $\;\frac{x}{5} + 3 = 9$

3. Solve for $x$: $\;2x + 5 = 8x - 13$   *(mystery weights on both pans)*

4. Solve for $\mathbf{t}$ (symbols only): $\;v = u + at$

5. Solve for $\mathbf{r}$: $\;V = \frac{4}{3}\pi r^3$   *(a cube root is a legal move for the
    same reason a square root is)*

---

## Part 2 — Reshaping *(0.3–0.4)*

6. Expand and simplify: $\;(2x + 3)(x - 4)$

7. Solve by factoring: $\;x^2 - 2x - 15 = 0$   *(name all three stages)*

8. Simplify fully, stating what may not be zero: $\;\frac{x^2 + 5x}{x}$

9. Compute by hand: $\;\frac{3}{8} + \frac{5}{6}$

10. A training run's loss drops from 2.4 to 1.8. By what percentage did it drop?
    Then: a second run's loss drops 25% and lands at 1.8 — where did it start?

---

## Part 3 — The hard rearrangements *(everything at once)*

*These are genuinely multi-step. Peel layers, reshape when stuck, name every move.*

11. Solve for $\mathbf{x}$: $\;y = \frac{2x + 3}{x - 1}$
    *(the target appears twice: clear the fraction, herd the $x$-terms, factor them out)*

12. Solve for $\mathbf{t}$: $\;L = L_0 \, e^{-kt} + c$
    *(a real loss-curve model: exponential decay down to a floor $c$)*

13. Solve for $\mathbf{n}$: $\;2^n = 8^{x}$ — give $n$ in terms of $x$ without any logs,
    by rewriting 8 as a power of 2. Then confirm the same answer using logs.

14. The sigmoid function (Module 1 preview) is $\;p = \dfrac{1}{1 + e^{-z}}$.
    Solve for $\mathbf{z}$. *(Full combo: basement, herding, logs. The answer —
    $z = \ln\frac{p}{1-p}$, the "log-odds" — is bread-and-butter ML. Earn it.)*

---

## Part 4 — Σ → Python *(0.6, on paper — you're the interpreter)*

15. Unroll and compute: $\;\displaystyle\sum_{i=1}^{4} (3i - 1)$

16. For $x = (4, 1, 7)$: compute $\;\bar{x} = \frac{1}{3}\sum_{i=1}^{3} x_i\;$ and then
    $\;\displaystyle\sum_{i=1}^{3} (x_i - \bar{x})^2$.

17. Translate into a Python loop (write the code on paper — exact, runnable syntax):
    $$S = \sum_{i=1}^{10} \frac{1}{i^2}$$

18. Translate this **nested** Σ into Python (paper again), for a grid `w` with 2 rows and
    3 columns:
    $$T = \sum_{i=1}^{2} \sum_{j=1}^{3} w_{ij}^2$$
    *(Careful with the two classic traps: inclusive limits, and paper counts from 1 while
    Python counts from 0.)*

19. Translate the other way — this code into Σ notation:
    ```python
    total = 0
    for i in range(1, 21):
        total = total + 2**i
    ```

---

## Part 5 — Python check (at the computer, LAST)

20. Only now: type your Part 4 code into Python and run it. Record what each prints.
    Then let sympy referee problems 11, 12 and 14, e.g.:

```python
import sympy as sp
x, y = sp.symbols("x y")
print(sp.solve(sp.Eq(y, (2*x + 3) / (x - 1)), x))     # problem 11

z, p = sp.symbols("z p")
print(sp.solve(sp.Eq(p, 1 / (1 + sp.exp(-z))), z))    # problem 14
```

Mark your own paper against the output — ✓ or ✗ per problem — *before* scanning.
Claude marks the reasoning; Python already marked the answers.

---

*Scan into `scans/inbox/`. Beat the gate and the golden ratio is waiting.*
