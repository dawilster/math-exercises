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

## Part D — Deep end

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a
ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time
(each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take
the fewest rungs you can — the struggle before each tap is where the learning happens. Always
name your moves, even when guessing.*

13. Solve for $t$ (symbols only): $\;\eta = \eta_0 \, e^{-kt}$ — the exponential learning-rate
    decay from the lesson.

    ::: rephrase
    $t$ is trapped up in the exponent of $e$. "Solve for $t$" just means: make legal moves
    until the equation reads $t = (\text{stuff with no } t)$. It's problem 11 ($5\cdot2^x=80$)
    wearing symbols — same shape, with $e$ where the $2$ was and $\ln$ as the "what exponent?" tool.
    :::

    ::: hint
    $t$ is stuck in an exponent. What single tool pulls a variable *down* out of an exponent?
    (The base here is $e$, so its matching "what exponent?" log is $\ln$.)
    :::

    ::: hint
    Before $\ln$ does anything useful, get $e^{-kt}$ **alone** on one side first. What's
    multiplying it that you can divide away?
    :::

    ::: steps
    1. **Divide both sides by $\eta_0$** — isolates the exponential. $\dfrac{\eta}{\eta_0} = e^{-kt}$
    2. **Take $\ln$ of both sides** — undoes $e^{(\cdot)}$, pulling the exponent down. $\ln\dfrac{\eta}{\eta_0} = -kt$
    3. **Divide by $-k$** — unwraps $t$; flip the fraction to absorb the minus sign. $t = \dfrac{1}{k}\ln\dfrac{\eta_0}{\eta}$
    :::

14. Without a calculator, put these in size order: $\;\log_2 100$, $\;\log_{10} 100$, $\;\log_2 8$.

    ::: rephrase
    Each log asks "**what power?**" — $\log_2 100$ means "2 to the *what* is 100?". You don't
    need exact values, only which is biggest. Two of these land on exact whole numbers; only
    one needs bracketing between two whole numbers.
    :::

    ::: hint
    Nail the two easy ones first. $\log_{10} 100$: ten to the what is 100? $\log_2 8$: two to
    the what is 8? Both are exact.
    :::

    ::: hint
    For $\log_2 100$, trap it: find the power of 2 just *below* 100 and just *above* it.
    $2^6 = 64$, $2^7 = 128$ — so $\log_2 100$ sits between 6 and 7, already bigger than the other two.
    :::

    ::: steps
    1. **Evaluate the exact ones.** $\log_{10} 100 = 2$ (since $10^2=100$); $\log_2 8 = 3$ (since $2^3=8$).
    2. **Bracket the hard one.** $2^6 = 64 < 100 < 128 = 2^7$, so $\log_2 100 \approx 6.64$ — between 6 and 7.
    3. **Order smallest → largest.** $\log_{10}100 \;<\; \log_2 8 \;<\; \log_2 100$.
    :::

15. You fold a sheet of paper in half, then in half again, and again — thickness doubles
    each fold. Paper is about $0.1$ mm thick. Write the thickness after $n$ folds as a
    formula, then find how many folds reach the Moon ($384{,}000$ km). Express the exact
    answer with a log, then estimate it using $2^{10} \approx 10^3$.

    ::: rephrase
    "Doubles each fold" = repeated $\times 2$ = an exponent. Start at $0.1$ mm: after 1 fold
    $0.2$, after 2 folds $0.4$, … after $n$ folds → a formula in $n$. "How many folds reach the
    Moon" then means: set that formula equal to the Moon's distance and solve for $n$ — same
    finish as problem 11. **Watch the units** — get everything into mm before comparing.
    :::

    ::: hint
    Thickness after $n$ folds: start at $0.1$ mm and double $n$ times → $0.1 \times 2^n$ mm.
    :::

    ::: hint
    Convert the Moon's distance to mm ($384{,}000$ km $\times 1000$ for m $\times 1000$ for mm),
    set your formula equal to it, then it's a "solve $2^n = \text{big number}$" problem — finish with $\log_2$.
    :::

    ::: steps
    1. **Formula: double $n$ times from $0.1$ mm.** thickness $= 0.1 \cdot 2^n$ mm
    2. **Convert the Moon to mm and set equal.** $384{,}000\text{ km} = 3.84\times10^{11}$ mm, so $0.1 \cdot 2^n = 3.84\times10^{11}$
    3. **Isolate the power** ($\times 10$, i.e. $\div 0.1$). $2^n = 3.84\times10^{12}$
    4. **$\log_2$ both sides** — the exact answer. $n = \log_2(3.84\times10^{12}) \approx 41.8 \Rightarrow \textbf{42 folds}$
    5. **Estimate check with $2^{10}\approx10^3$.** so $2^{40}\approx10^{12}$, and $3.84\times10^{12}\approx2^2\cdot10^{12}\approx2^{42}$ — same ballpark, $n\approx42$. ✓
    :::

16. Prove the log rule from the exponent rule: if $x = a^m$ and $y = a^n$, show step by step
    why $\log_a(xy) = \log_a x + \log_a y$. *(Three lines. This is a real proof — your first.)*

    ::: rephrase
    A "proof" here just means: start from what you're *told* is true and make legal moves until
    the thing you want to show appears. You're given $x=a^m$ and $y=a^n$. The target has a log
    of a **product** $(xy)$ — and you already know a rule for multiplying same-base powers.
    Follow the exponents.
    :::

    ::: hint
    Multiply $x$ and $y$ using their $a^{(\cdots)}$ forms. Which exponent rule fires when you
    multiply same-base powers?
    :::

    ::: hint
    Once $xy = a^{(\text{something})}$, translate back into log language: $\log_a(xy)$ *is* that
    exponent. Then swap the exponents back for the logs you were given.
    :::

    ::: steps
    1. **Multiply the two forms** ($a^m\cdot a^n = a^{m+n}$). $xy = a^m \cdot a^n = a^{m+n}$
    2. **Read it as a log** — "what exponent gives $xy$?" is $m+n$. $\log_a(xy) = m + n$
    3. **Swap exponents back for logs** ($m=\log_a x,\; n=\log_a y$). $\log_a(xy) = \log_a x + \log_a y \;\blacksquare$
    :::

---

## Part E — Python check (at the computer, after the pen work)

17. Referee Parts A–B:

```python
import numpy as np

print(2**5, 3**2 * 3**3, 7**0, 2**-3, 9**0.5)   # Part A
print(np.log2(32), np.log10(1000))               # problems 8–9
print(np.log2(80 / 5))                           # problem 11 — should match your x
```

18. Watch THE trick fail and then get rescued (why logs run ML):

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
