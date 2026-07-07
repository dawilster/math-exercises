# Worksheet 0.5 — Exponents & Logarithms

*Pen and paper. For every problem, write the **move you're making** next to each step, like
"add exponents (same base multiplied)" or "log₂ both sides". The moves are the point, not
the answers. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: counting multiplications

Evaluate without a calculator. For 3–4, say *which pattern forces the answer*.

1. $2^5$

2. $3^2 \cdot 3^3$   *(rule first, then the number)*

3. $7^0$

4. $2^{-3}$

5. $9^{1/2}$

---

## Part B — Core: rules and the "what exponent?" question

Name every move.

6. Simplify to a single power: $\;\frac{5^8}{5^6}$

7. Simplify to a single power: $\;(2^3)^4$

8. Evaluate: $\log_2 32$   *("2 to the what makes 32?")*

9. Evaluate: $\log_{10} 1000$ and $\log_{10} \frac{1}{100}$

10. Rewrite as a sum of two logs: $\;\log(ab)$. Then rewrite $\log \frac{a}{b}$ as a difference.

11. Solve for $x$: $\;5 \cdot 2^x = 80$

12. Solve for $x$: $\;\log_2 x = 6$   *(the reverse direction — undo the log)*

---

## Part C — Spot the illegal move

Circle the broken line and name the rule it broke.

13. Claimed simplification:
    - line 1: $\log(x + y)$
    - line 2: $\log x + \log y$   *(split the log)*

14. Claimed evaluation:
    - line 1: $4^0$
    - line 2: $0$   *("anything times zero is zero")*

15. Claimed simplification:
    - line 1: $2^3 \cdot 2^4$
    - line 2: $2^{12}$   *(multiplied the exponents)*

16. Claimed solution of $2^x = 10$:
    - line 1: $2^x = 10$
    - line 2: $x = 5$   *(divided 10 by 2)*

---

## Part D — Deep end

*Beyond what was taught. Struggle is the workout — name your moves even when guessing.*

17. Solve for $t$ (symbols only): $\;\eta = \eta_0 \, e^{-kt}$ — the exponential learning-rate
    decay from the lesson. *(Use $\ln$, the base-$e$ log, as your "what exponent?" move.
    Expect a minus sign to deal with.)*

18. Without a calculator, put these in size order: $\;\log_2 100$, $\;\log_{10} 100$, $\;\log_2 8$.
    *(Bracket each between two whole numbers first, e.g. "2⁶ = 64 < 100 < 128 = 2⁷, so…")*

19. You fold a sheet of paper in half, then in half again, and again — thickness doubles
    each fold. Paper is about $0.1$ mm thick. Write the thickness after $n$ folds as a
    formula, then find how many folds reach the Moon ($384{,}000$ km). Use logs — express
    the exact answer, then estimate it with $2^{10} \approx 10^3$.

20. Prove the log rule from the exponent rule: if $x = a^m$ and $y = a^n$, show step by step
    why $\log_a(xy) = \log_a x + \log_a y$. *(Three lines. This is a real proof — your first.)*

---

## Part E — Python check (at the computer, after the pen work)

21. Referee Parts A–B:

```python
import numpy as np

print(2**5, 3**2 * 3**3, 7**0, 2**-3, 9**0.5)   # Part A
print(np.log2(32), np.log10(1000))               # problems 8–9
print(np.log2(80 / 5))                           # problem 11 — should match your x
```

22. Watch THE trick fail and then get rescued (why logs run ML):

```python
import numpy as np
rng = np.random.default_rng(42)
probs = rng.uniform(0.1, 0.9, size=10_000)   # 10,000 random probabilities

print(np.prod(probs))            # the product underflows to 0.0 — information destroyed
print(np.sum(np.log(probs)))     # the log-sum: a perfectly healthy number
```

Write ✓ next to each problem Python confirms.

> **Bonus thought:** plot your paper-folding formula with matplotlib on a normal scale,
> then call `plt.yscale("log")` and look again. Which plot lets you actually *read* the
> early folds? That's why loss curves are plotted on log axes.
