# Worksheet 0.4 — Fractions, Ratios & Percentages

*Pen and paper. For every problem, write the **move you're making** next to each step, like
"× by 3/3 to match denominators" or "÷ by total to normalise". The moves are the point,
not the answers. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: costume changes

1. Write $\frac{3}{4}$ as a decimal and as a percentage.

   ::: answer
   $\frac{3}{4} = 0.75 = 75\%$ — move: divide numerator by denominator for the decimal,
   then $\times 100$ for the percentage.
   :::

2. Write $0.2$ as a fraction (simplest form) and as a percentage.

   ::: answer
   $0.2 = \frac{1}{5} = 20\%$ — move: write over $10$ ($\frac{2}{10}$), cancel the common
   factor $2$ to simplify, and $\times 100$ for the percentage.
   :::

3. Simplify $\frac{18}{24}$ by cancelling common factors. Name the factor(s) you cancel.

   ::: answer
   $\frac{18}{24} = \frac{3}{4}$ — move: cancel the common factor $6$ (top and bottom both $\div 6$).
   :::

4. What is $25\%$ of $80$?

   ::: answer
   $20$ — move: convert percentage to decimal ($25\% = 0.25$), multiply: $0.25 \times 80 = 20$.
   :::

---

## Part B — Core: the moves

Name every move.

5. $\frac{2}{3} \times \frac{9}{10}$   *(simplify before multiplying if you can — less arithmetic)*

   ::: answer
   $\frac{3}{5}$ — move: cancel the common factor $3$ between the $9$ and the $3$ first
   ($\frac{2}{1}\times\frac{3}{10}$), then multiply tops and bottoms: $\frac{6}{10}=\frac{3}{5}$.
   :::

6. $\frac{3}{4} \div \frac{1}{2}$   *(and sanity-check: should the answer be bigger or smaller than $\frac{3}{4}$?)*

   ::: answer
   $\frac{3}{4} \div \frac{1}{2} = \frac{3}{4}\times\frac{2}{1} = \frac{3}{2} = 1.5$ — move: flip
   the second fraction and multiply (keep, flip, change). Bigger than $\frac{3}{4}$, because
   dividing by a number less than $1$ grows the result.
   :::

7. $\frac{1}{4} + \frac{2}{3}$   *(matching pieces first)*

   ::: answer
   $\frac{11}{12}$ — move: common denominator $12$ ($\frac{1}{4}=\frac{3}{12}$,
   $\frac{2}{3}=\frac{8}{12}$), then add tops: $\frac{3+8}{12}=\frac{11}{12}$.
   :::

8. $\frac{5}{6} - \frac{1}{2}$

   ::: answer
   $\frac{1}{3}$ — move: common denominator $6$ ($\frac{1}{2}=\frac{3}{6}$), subtract tops:
   $\frac{5-3}{6}=\frac{2}{6}$, then cancel the common factor $2$ to get $\frac{1}{3}$.
   :::

9. A dataset has 1,200 images. You want an 80/20 train/test split.
   How many images in each part?

   ::: answer
   $960$ train, $240$ test — move: convert each percentage to a decimal, multiply by the total
   ($0.8\times1200=960$, $0.2\times1200=240$).
   :::

10. Normalise the scores $(6, 10, 4)$: divide each by the total, simplify each fraction,
    and confirm the three results sum to exactly 1.

    ::: answer
    $\frac{6}{20}=\frac{3}{10}$, $\frac{10}{20}=\frac{1}{2}$, $\frac{4}{20}=\frac{1}{5}$ — move:
    divide each by the shared total $20$, then cancel common factors. Check with a common
    denominator: $\frac{3}{10}+\frac{5}{10}+\frac{2}{10}=\frac{10}{10}=1$.
    :::

11. Solve for $x$ (balance moves on a fraction equation): $\;\frac{x}{5} = \frac{12}{20}$

    ::: answer
    $x=3$ — move: multiply both sides by $5$ (balance move): $x = 5\times\frac{12}{20} = \frac{60}{20}=3$.
    (Or spot directly that $\frac{12}{20}=\frac{3}{5}$.)
    :::

---

## Part C — Spot the illegal move

Circle the broken line and name the rule it broke.

12. Claimed addition:
    - line 1: $\frac{1}{2} + \frac{1}{3}$
    - line 2: $\frac{2}{5}$   *(added tops, added bottoms)*

    ::: answer
    Line 2 is broken. You can't add fractions by adding numerators and denominators
    separately — that only works once the denominators already match. Move needed: common
    denominator $6$ ($\frac{1}{2}=\frac{3}{6}$, $\frac{1}{3}=\frac{2}{6}$). Correct:
    $\frac{3}{6}+\frac{2}{6}=\frac{5}{6}$.
    :::

13. Claimed simplification:
    - line 1: $\frac{x + 6}{6}$
    - line 2: $x$   *(cancelled the 6s)*

    ::: answer
    Line 2 is broken. You can only cancel a common **factor** that multiplies the whole top
    and bottom — here the $6$ in the numerator is added, not multiplied, so it can't be
    cancelled against the $6$ on the bottom. Correct: $\frac{x+6}{6} = \frac{x}{6}+1$, which
    doesn't simplify further to $x$.
    :::

14. Claimed percentage logic:
    - line 1: a model's error rate rose from 10% to 15%
    - line 2: "so the error rate increased by 5%"
    *(Careful: 5 percentage POINTS, yes. But by what percentage did the error rate itself
    grow? Which claim would a headline print?)*

    ::: answer
    Line 2 is broken. Going from $10\%$ to $15\%$ is a rise of $5$ **percentage points**, not
    a $5\%$ increase. The percentage *increase* in the error rate itself is
    $\frac{15-10}{10}=0.5=50\%$ — a much bigger jump than "5%" suggests. A headline chasing
    drama would print "$50\%$ worse", which is technically the correct relative-change figure
    but easy to conflate with the $5$-point rise.
    :::

---

## Part D — Deep end

*Beyond what was taught. Struggle is the workout — attempt everything, name your moves.*

15. A jacket is discounted 30%, then the sale price gets 10% tax added.
    What single percentage of the original do you pay? Does the order
    (discount-then-tax vs tax-then-discount) matter? Test both.

    ::: answer
    $77\%$ of the original — and the order does **not** matter. Discount then tax:
    $0.7\times1.1 = 0.77$. Tax then discount: $1.1\times0.7=0.77$. Move: chained percentages
    are just multiplied factors, and multiplication commutes ($0.7\times1.1=1.1\times0.7$).
    :::

16. Normalise the symbols $(a, b, c)$: what does each become, and — using 0.4's common-
    denominator move with pure symbols — prove the three results sum to exactly 1.

    ::: answer
    $\frac{a}{a+b+c}$, $\frac{b}{a+b+c}$, $\frac{c}{a+b+c}$ — move: divide each by the shared
    total $a+b+c$, which is already a common denominator. Sum:
    $\frac{a+b+c}{a+b+c}=1$.
    :::

17. In one class of 20 students, 15 passed. In another class of 80 students, 44 passed.
    What percentage passed **overall**? Why is the answer NOT the average of 75% and 55%?
    *(This trap — averaging averages — corrupts real ML evaluations all the time.)*

    ::: answer
    $59\%$ overall ($\frac{15+44}{20+80}=\frac{59}{100}$). It's **not** the average of $75\%$
    and $55\%$ (which gives $65\%$) because the classes are different sizes — you need a
    size-weighted average, not a simple average of the two rates.
    :::

18. Solve for $x$: $\;\frac{2}{x} + \frac{1}{3} = 1$
    *(A 0.2 basement problem wearing 0.4 clothes. Clear the clutter first.)*

    ::: answer
    $x=3$ — move: multiply every term by the LCD $3x$ to clear both basements:
    $2(3) + x(1) = 1(3x) \Rightarrow 6+x=3x \Rightarrow 6=2x \Rightarrow x=3$.
    Check: $\frac{2}{3}+\frac{1}{3}=1$. ✓
    :::

---

## Part E — Python check (at the computer, after the pen work)

19. Python has exact fractions — let them referee Part B:

```python
from fractions import Fraction         # exact fractions, no decimal fuzz

print(Fraction(2, 3) * Fraction(9, 10))    # problem 5 — Fraction(a, b) means a/b
print(Fraction(3, 4) / Fraction(1, 2))     # problem 6
print(Fraction(1, 4) + Fraction(2, 3))     # problem 7
```

20. Check your normalisation (problem 10) the ML way:

```python
scores = [6, 10, 4]
props = [s / sum(scores) for s in scores]   # divide each by the total
print(props, sum(props))                    # must end in 1.0
```

Write ✓ next to each problem Python confirms.

> **Bonus thought:** run `print(0.1 + 0.2)`. Surprised? Now
> `print(Fraction(1, 10) + Fraction(2, 10))`. This is why `Fraction` exists —
> and why ML code (which uses fast decimals anyway) never tests floats with `==`.
