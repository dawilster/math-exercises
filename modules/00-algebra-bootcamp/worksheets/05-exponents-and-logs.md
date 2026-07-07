# Worksheet 0.5 — Exponents & Logarithms

*Pen and paper. For every problem, write the **move you're making** next to each step, like
"add exponents (same base multiplied)" or "log₂ both sides". The moves are the point, not
the answers. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: counting multiplications

Evaluate without a calculator. For 3–4, say *which pattern forces the answer*.

1. $2^5$

   ::: answer
   $2^5 = 32$ — move: repeated multiplication, $2\cdot2\cdot2\cdot2\cdot2$.
   :::

2. $3^2 \cdot 3^3$   *(rule first, then the number)*

   ::: answer
   $3^2 \cdot 3^3 = 3^5 = 243$ — move: $a^m \cdot a^n = a^{m+n}$ (same base multiplied → add exponents).
   :::

3. $7^0$

   ::: answer
   $7^0 = 1$ — move: $a^0 = 1$ for any nonzero base (the pattern $7^2,7^1,7^0$ each divides by 7: $49,7,1$).
   :::

4. $2^{-3}$

   ::: answer
   $2^{-3} = \frac{1}{8}$ — move: $a^{-n} = \frac{1}{a^n}$ (negative exponent flips to a reciprocal).
   :::

5. $9^{1/2}$

   ::: answer
   $9^{1/2} = 3$ — move: $a^{1/2} = \sqrt{a}$ (a fractional exponent of $\frac12$ means "square root").
   :::

---

## Part B — Core: rules and the "what exponent?" question

Name every move.

6. Simplify to a single power: $\;\frac{5^8}{5^6}$

   ::: answer
   $\frac{5^8}{5^6} = 5^2 = 25$ — move: $\frac{a^m}{a^n} = a^{m-n}$ (same base divided → subtract exponents).
   :::

7. Simplify to a single power: $\;(2^3)^4$

   ::: answer
   $(2^3)^4 = 2^{12} = 4096$ — move: $(a^m)^n = a^{mn}$ (a power of a power → multiply exponents).
   :::

8. Evaluate: $\log_2 32$   *("2 to the what makes 32?")*

   ::: answer
   $\log_2 32 = 5$ — move: a log asks "what exponent?"; $2^5 = 32$.
   :::

9. Evaluate: $\log_{10} 1000$ and $\log_{10} \frac{1}{100}$

   ::: answer
   $\log_{10} 1000 = 3$ (since $10^3 = 1000$) and $\log_{10}\frac{1}{100} = -2$ (since $10^{-2} = \frac{1}{100}$)
   — move: "10 to the what?" each time.
   :::

10. Rewrite as a sum of two logs: $\;\log(ab)$. Then rewrite $\log \frac{a}{b}$ as a difference.

    ::: answer
    $\log(ab) = \log a + \log b$ — move: product-inside-a-log rule.
    $\log\frac{a}{b} = \log a - \log b$ — move: quotient-inside-a-log rule.
    :::

11. Solve for $x$: $\;5 \cdot 2^x = 80$

    ::: answer
    $x = 4$ — move: $\div 5$ both sides first ($2^x = 16$), then ask "2 to the what makes 16?" ($2^4 = 16$).
    :::

12. Solve for $x$: $\;\log_2 x = 6$   *(the reverse direction — undo the log)*

    ::: answer
    $x = 64$ — move: undo the log by raising base 2 to both sides, $x = 2^6 = 64$.
    :::

---

## Part C — Spot the illegal move

Circle the broken line and name the rule it broke.

13. Claimed simplification:
    - line 1: $\log(x + y)$
    - line 2: $\log x + \log y$   *(split the log)*

    ::: answer
    Line 2 is broken. The log rule splits **products** into sums ($\log(ab) = \log a + \log b$) —
    there is no rule for splitting a **sum** inside a log. $\log(x+y)$ cannot be simplified further;
    it is *not* equal to $\log x + \log y$ in general.
    :::

14. Claimed evaluation:
    - line 1: $4^0$
    - line 2: $0$   *("anything times zero is zero")*

    ::: answer
    Line 2 is broken. It confuses the exponent $0$ with multiplying *by* zero — but $4^0$ means
    "no multiplications", not "times zero". Move: $a^0 = 1$ (pattern $4^2=16, 4^1=4, 4^0=1$,
    each step $\div 4$). Correct: $4^0 = 1$.
    :::

15. Claimed simplification:
    - line 1: $2^3 \cdot 2^4$
    - line 2: $2^{12}$   *(multiplied the exponents)*

    ::: answer
    Line 2 is broken. Multiplying exponents is the move for a **power of a power**, $(a^m)^n = a^{mn}$
    — but this is a **product of same-base powers**, which means $a^m \cdot a^n = a^{m+n}$ (add them).
    Correct: $2^3 \cdot 2^4 = 2^7 = 128$.
    :::

16. Claimed solution of $2^x = 10$:
    - line 1: $2^x = 10$
    - line 2: $x = 5$   *(divided 10 by 2)*

    ::: answer
    Line 2 is broken. Dividing undoes multiplication, not an exponent — $x$ is stuck in the
    exponent's seat, so the move needed is $\log_2$ both sides, not $\div 2$. Correct:
    $x = \log_2 10 \approx 3.32$.
    :::

---

## Part D — Deep end

*Beyond what was taught. Struggle is the workout — name your moves even when guessing.*

17. Solve for $t$ (symbols only): $\;\eta = \eta_0 \, e^{-kt}$ — the exponential learning-rate
    decay from the lesson. *(Use $\ln$, the base-$e$ log, as your "what exponent?" move.
    Expect a minus sign to deal with.)*

    ::: answer
    $t = \dfrac{1}{k}\ln\!\dfrac{\eta_0}{\eta}$ — moves: $\div \eta_0$ both sides ($\frac{\eta}{\eta_0} = e^{-kt}$),
    then $\ln$ both sides to undo the $e^{(\cdot)}$ ($\ln\frac{\eta}{\eta_0} = -kt$), then $\div(-k)$.
    :::

18. Without a calculator, put these in size order: $\;\log_2 100$, $\;\log_{10} 100$, $\;\log_2 8$.
    *(Bracket each between two whole numbers first, e.g. "2⁶ = 64 < 100 < 128 = 2⁷, so…")*

    ::: answer
    $\log_{10} 100 = 2$ (exact) < $\log_2 8 = 3$ (exact) < $\log_2 100 \approx 6.64$
    (bracket: $2^6 = 64 < 100 < 128 = 2^7$, so it's between 6 and 7).
    Order: $\log_{10}100 < \log_2 8 < \log_2 100$.
    :::

19. You fold a sheet of paper in half, then in half again, and again — thickness doubles
    each fold. Paper is about $0.1$ mm thick. Write the thickness after $n$ folds as a
    formula, then find how many folds reach the Moon ($384{,}000$ km). Use logs — express
    the exact answer, then estimate it with $2^{10} \approx 10^3$.

    ::: answer
    Thickness after $n$ folds: $0.1 \cdot 2^n$ mm. The Moon is $384{,}000$ km $= 3.84\times10^{11}$ mm,
    so $0.1 \cdot 2^n = 3.84\times10^{11} \Rightarrow 2^n = 3.84\times10^{12}$, giving the exact answer
    $n = \log_2(3.84\times10^{12}) \approx 41.8$ — so $42$ folds. Estimate check: $2^{10}\approx10^3$
    means $2^{40}\approx10^{12}$, and $3.84\times10^{12}\approx4\times10^{12}=2^2\cdot10^{12}\approx2^{42}$
    — same ballpark, $n\approx42$.
    :::

20. Prove the log rule from the exponent rule: if $x = a^m$ and $y = a^n$, show step by step
    why $\log_a(xy) = \log_a x + \log_a y$. *(Three lines. This is a real proof — your first.)*

    ::: answer
    Line 1: $xy = a^m \cdot a^n = a^{m+n}$ (move: $a^m\cdot a^n = a^{m+n}$).
    Line 2: by definition, $\log_a(xy)$ is "what exponent gives $xy$?" — and line 1 shows that's $m+n$,
    so $\log_a(xy) = m + n$.
    Line 3: but $m = \log_a x$ and $n = \log_a y$ (given), so $\log_a(xy) = \log_a x + \log_a y$. $\blacksquare$
    :::

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
