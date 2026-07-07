# Worksheet 0.4 — Fractions, Ratios & Percentages

*Pen and paper. For every problem, write the **move you're making** next to each step, like
"× by 3/3 to match denominators" or "÷ by total to normalise". The moves are the point,
not the answers. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: costume changes

1. Write $\frac{3}{4}$ as a decimal and as a percentage.

2. Write $0.2$ as a fraction (simplest form) and as a percentage.

3. Simplify $\frac{18}{24}$ by cancelling common factors. Name the factor(s) you cancel.

4. What is $25\%$ of $80$?

---

## Part B — Core: the moves

Name every move.

5. $\frac{2}{3} \times \frac{9}{10}$   *(simplify before multiplying if you can — less arithmetic)*

6. $\frac{3}{4} \div \frac{1}{2}$   *(and sanity-check: should the answer be bigger or smaller than $\frac{3}{4}$?)*

7. $\frac{1}{4} + \frac{2}{3}$   *(matching pieces first)*

8. $\frac{5}{6} - \frac{1}{2}$

9. A dataset has 1,200 images. You want an 80/20 train/test split.
   How many images in each part?

10. Normalise the scores $(6, 10, 4)$: divide each by the total, simplify each fraction,
    and confirm the three results sum to exactly 1.

11. Solve for $x$ (balance moves on a fraction equation): $\;\frac{x}{5} = \frac{12}{20}$

---

## Part C — Spot the illegal move

Circle the broken line and name the rule it broke.

12. Claimed addition:
    - line 1: $\frac{1}{2} + \frac{1}{3}$
    - line 2: $\frac{2}{5}$   *(added tops, added bottoms)*

13. Claimed simplification:
    - line 1: $\frac{x + 6}{6}$
    - line 2: $x$   *(cancelled the 6s)*

14. Claimed percentage logic:
    - line 1: a model's error rate rose from 10% to 15%
    - line 2: "so the error rate increased by 5%"
    *(Careful: 5 percentage POINTS, yes. But by what percentage did the error rate itself
    grow? Which claim would a headline print?)*

---

## Part D — Deep end

*Beyond what was taught. Struggle is the workout — attempt everything, name your moves.*

15. A jacket is discounted 30%, then the sale price gets 10% tax added.
    What single percentage of the original do you pay? Does the order
    (discount-then-tax vs tax-then-discount) matter? Test both.

16. Normalise the symbols $(a, b, c)$: what does each become, and — using 0.4's common-
    denominator move with pure symbols — prove the three results sum to exactly 1.

17. In one class of 20 students, 15 passed. In another class of 80 students, 44 passed.
    What percentage passed **overall**? Why is the answer NOT the average of 75% and 55%?
    *(This trap — averaging averages — corrupts real ML evaluations all the time.)*

18. Solve for $x$: $\;\frac{2}{x} + \frac{1}{3} = 1$
    *(A 0.2 basement problem wearing 0.4 clothes. Clear the clutter first.)*

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
