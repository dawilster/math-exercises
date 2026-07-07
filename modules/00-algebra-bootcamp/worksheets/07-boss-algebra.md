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

   ::: answer
   $x = 7$ — move: $+7$ both sides ($4x = 28$), then $\div 4$.
   :::

2. Solve for $x$: $\;\frac{x}{5} + 3 = 9$

   ::: answer
   $x = 30$ — move: $-3$ both sides ($\frac{x}{5} = 6$), then $\times 5$.
   :::

3. Solve for $x$: $\;2x + 5 = 8x - 13$   *(mystery weights on both pans)*

   ::: answer
   $x = 3$ — move: $-2x$ both sides to herd the $x$-terms onto one pan ($5 = 6x - 13$),
   then $+13$ ($18 = 6x$), then $\div 6$.
   :::

4. Solve for $\mathbf{t}$ (symbols only): $\;v = u + at$

   ::: answer
   $t = \dfrac{v - u}{a}$ — move: $-u$ both sides ($v - u = at$), then $\div a$.
   :::

5. Solve for $\mathbf{r}$: $\;V = \frac{4}{3}\pi r^3$   *(a cube root is a legal move for the
    same reason a square root is)*

   ::: answer
   $r = \sqrt[3]{\dfrac{3V}{4\pi}}$ — move: $\times \frac{3}{4\pi}$ both sides to isolate
   $r^3$ ($r^3 = \frac{3V}{4\pi}$), then take the cube root of both sides.
   :::

---

## Part 2 — Reshaping *(0.3–0.4)*

6. Expand and simplify: $\;(2x + 3)(x - 4)$

   ::: answer
   $2x^2 - 5x - 12$ — move: distribute each term of the first bracket over the second
   ($2x \cdot x + 2x\cdot(-4) + 3\cdot x + 3\cdot(-4) = 2x^2 - 8x + 3x - 12$),
   then collect like terms ($-8x + 3x = -5x$).
   :::

7. Solve by factoring: $\;x^2 - 2x - 15 = 0$   *(name all three stages)*

   ::: answer
   $x = 5$ or $x = -3$. Stage 1 — factor: find two numbers multiplying to $-15$, adding to
   $-2$ (that's $-5$ and $3$) → $(x - 5)(x + 3) = 0$. Stage 2 — zero-product property: a
   product is zero only if a factor is zero, so $x - 5 = 0$ or $x + 3 = 0$. Stage 3 — solve
   each mini-equation.
   :::

8. Simplify fully, stating what may not be zero: $\;\frac{x^2 + 5x}{x}$

   ::: answer
   $x + 5$, provided $x \neq 0$. Move: factor the numerator ($x(x+5)$), then cancel the
   common factor $x$ top and bottom — legal only because $x \neq 0$ (can't divide by zero).
   :::

9. Compute by hand: $\;\frac{3}{8} + \frac{5}{6}$

   ::: answer
   $\frac{29}{24}$ (= $1\frac{5}{24}$) — move: common denominator $24$ (LCM of 8 and 6):
   $\frac{3}{8} = \frac{9}{24}$, $\frac{5}{6} = \frac{20}{24}$, add numerators.
   :::

10. A training run's loss drops from 2.4 to 1.8. By what percentage did it drop?
    Then: a second run's loss drops 25% and lands at 1.8 — where did it start?

    ::: answer
    First: drop $= 2.4 - 1.8 = 0.6$; percentage $= \frac{0.6}{2.4} = 25\%$ (move: change
    $\div$ original). Second: $1.8 = \text{start} \times (1 - 0.25) = 0.75 \times \text{start}$,
    so $\text{start} = \frac{1.8}{0.75} = 2.4$ (move: $\div 0.75$, not $\div 1.25$ — reversing
    a percentage drop means dividing by $(1 - \text{rate})$).
    :::

---

## Part 3 — The hard rearrangements *(everything at once)*

*These are genuinely multi-step. Peel layers, reshape when stuck, name every move.*

11. Solve for $\mathbf{x}$: $\;y = \frac{2x + 3}{x - 1}$
    *(the target appears twice: clear the fraction, herd the $x$-terms, factor them out)*

    ::: answer
    $x = \dfrac{y + 3}{y - 2}$ — move: $\times(x - 1)$ both sides to clear the fraction
    ($yx - y = 2x + 3$); herd $x$-terms onto one side ($-2x$ and $+y$ both sides:
    $yx - 2x = y + 3$); factor $x$ out ($x(y - 2) = y + 3$); $\div(y-2)$.
    :::

12. Solve for $\mathbf{t}$: $\;L = L_0 \, e^{-kt} + c$
    *(a real loss-curve model: exponential decay down to a floor $c$)*

    ::: answer
    $t = \dfrac{1}{k}\ln\!\left(\dfrac{L_0}{L - c}\right)$ — move: $-c$ both sides
    ($L - c = L_0 e^{-kt}$); $\div L_0$ ($\frac{L-c}{L_0} = e^{-kt}$); take $\ln$ of both
    sides to undo the exponential ($\ln\frac{L-c}{L_0} = -kt$); $\div(-k)$.
    :::

13. Solve for $\mathbf{n}$: $\;2^n = 8^{x}$ — give $n$ in terms of $x$ without any logs,
    by rewriting 8 as a power of 2. Then confirm the same answer using logs.

    ::: answer
    $n = 3x$ — move: rewrite $8 = 2^3$, so $8^x = 2^{3x}$; same base both sides means the
    exponents must match. With logs: take $\ln$ of both sides ($n\ln 2 = 3x\ln 2$), then
    $\div \ln 2$ — same answer.
    :::

14. The sigmoid function (Module 1 preview) is $\;p = \dfrac{1}{1 + e^{-z}}$.
    Solve for $\mathbf{z}$. *(Full combo: basement, herding, logs. The answer —
    $z = \ln\frac{p}{1-p}$, the "log-odds" — is bread-and-butter ML. Earn it.)*

    ::: answer
    $z = \ln\dfrac{p}{1-p}$ — move: take the reciprocal of both sides to lift $z$ out of the
    basement ($\frac{1}{p} = 1 + e^{-z}$); $-1$ ($\frac{1-p}{p} = e^{-z}$); $\ln$ both sides
    ($-z = \ln\frac{1-p}{p}$); $\times(-1)$, then use $-\ln(a) = \ln(1/a)$ to flip the fraction.
    :::

---

## Part 4 — Σ → Python *(0.6, on paper — you're the interpreter)*

15. Unroll and compute: $\;\displaystyle\sum_{i=1}^{4} (3i - 1)$

    ::: answer
    $26$ — unrolled: $(3\cdot1{-}1) + (3\cdot2{-}1) + (3\cdot3{-}1) + (3\cdot4{-}1)
    = 2+5+8+11 = 26$.
    :::

16. For $x = (4, 1, 7)$: compute $\;\bar{x} = \frac{1}{3}\sum_{i=1}^{3} x_i\;$ and then
    $\;\displaystyle\sum_{i=1}^{3} (x_i - \bar{x})^2$.

    ::: answer
    $\bar{x} = \frac{4+1+7}{3} = 4$. Then $\sum (x_i - \bar{x})^2 = (4-4)^2 + (1-4)^2 + (7-4)^2
    = 0 + 9 + 9 = 18$.
    :::

17. Translate into a Python loop (write the code on paper — exact, runnable syntax):
    $$S = \sum_{i=1}^{10} \frac{1}{i^2}$$

    ::: answer
    ```python
    S = 0
    for i in range(1, 11):
        S = S + 1 / i**2
    ```
    Move: Σ's upper limit $10$ is inclusive, but `range(1, 11)` stops one *short* of its
    second argument — so the stop value has to be $11$, not $10$.
    :::

18. Translate this **nested** Σ into Python (paper again), for a grid `w` with 2 rows and
    3 columns:
    $$T = \sum_{i=1}^{2} \sum_{j=1}^{3} w_{ij}^2$$
    *(Careful with the two classic traps: inclusive limits, and paper counts from 1 while
    Python counts from 0.)*

    ::: answer
    ```python
    T = 0
    for i in range(2):
        for j in range(3):
            T = T + w[i][j] ** 2
    ```
    Move: paper's $i = 1..2$, $j = 1..3$ (inclusive, counting from 1) become `range(2)` and
    `range(3)` (2 and 3 values each, but counting from 0) — index straight into `w[i][j]`,
    no extra shift needed since both schemes still visit every row/column exactly once.
    :::

19. Translate the other way — this code into Σ notation:
    ```python
    total = 0
    for i in range(1, 21):
        total = total + 2**i
    ```

    ::: answer
    $\displaystyle \text{total} = \sum_{i=1}^{20} 2^i$ — `range(1, 21)` produces
    $i = 1, 2, \dots, 20$ (Python stops one short of 21), matching an inclusive Σ upper
    limit of $20$.
    :::

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
