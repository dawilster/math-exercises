# Worksheet 4.2 — Mean, Variance, Standard Deviation

*Pen and paper. Use the five named steps: CENTRE → DEVIATIONS → SQUARE → AVERAGE → UNSQUARE.
Data is kept small so the arithmetic stays friendly. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up

1. Mean of $3, 7, 8, 10, 12$?

2. Data: $4, 4, 4, 4$. Without computing, what are the variance and std? Why?

3. Deviations from the mean for the data in problem 1. Check they sum to 0.

4. A dataset has $\sigma^2 = 25$. What's $\sigma$? If the data is in seconds, what units is each in?

---

## Part B — Core

5. Full five steps on: $1, 2, 6, 7$. Give $\mu$, $\sigma^2$, $\sigma$.

6. Full five steps on: $10, 20, 20, 30$. Give $\mu$, $\sigma^2$, $\sigma$.

7. Test scores have $\mu = 70$, $\sigma = 8$. Compute z-scores for marks of 86, 70 and 58.
   One phrase each: what does the z-score *say*?

8. Feature A (house price, \$): $\mu = 500{,}000$, $\sigma = 150{,}000$.
   Feature B (bedrooms): $\mu = 3$, $\sigma = 1$.
   A house costs \$650,000 and has 5 bedrooms. Which feature is more unusual for this house?
   Prove it with z-scores.

9. Two machines fill 500 g bags. Machine 1: $\mu = 500$, $\sigma = 2$.
   Machine 2: $\mu = 500$, $\sigma = 20$. Same mean — which machine do you want filling your
   bags, and what question does the mean alone fail to answer?

---

## Part C — Spot the error

10. "Data: $2, 4, 6, 8$. Mean is 5. Deviations are $-3, -1, 1, 3$, which average to 0 —
    so the variance is 0 and the data has no spread." Which step got skipped?

11. "Salaries at our startup: $60k, 65k, 70k, 75k, 2{,}000k$ (the founder).
    Mean salary is \$454k — we pay brilliantly!" What's the diagnosis? Which single word in
    the claim does the mean not support?

12. "Feature A has $\sigma = 150{,}000$ and feature B has $\sigma = 1$, so A carries
    150,000× more information and the network should focus on it." What's wrong, and what
    fix from this lesson makes A and B comparable?

---

## Part D — Deep end

13. Take the data from problem 5 and add 10 to every value. Recompute $\mu$ and $\sigma$
    (shortcut allowed if you can justify it). What changed, what didn't, and why?

14. Now multiply every value in problem 5's data by 2. What happens to $\mu$, to $\sigma$,
    and to $\sigma^2$? *(Careful — one of these changes by more than you'd guess.)*

15. Using 13 and 14: your data has $\mu = 40$, $\sigma = 5$. Find $a$ and $b$ so that
    $x_{\text{new}} = a x + b$ has $\mu = 0$, $\sigma = 1$. What is this transformation called
    in ML, and where have you seen $\frac{x - \mu}{\sigma}$ before on this page?

16. Invent two different four-number datasets, both with $\mu = 5$ and both with $\sigma^2 = 8$.
    What does this tell you about how much two numbers can summarise?

---

## Part E — Python check (at the computer, after the pen work)

17. Check problems 5 and 6:

```python
import numpy as np
x = np.array([1, 2, 6, 7])
print(x.mean(), x.var(), x.std())   # match your hand results?
```

18. Check problem 15: build `x = np.array([35., 35., 45., 45.])` (mean 40, std 5 — verify that
    first!), apply your $a$ and $b$,
    and print the new mean and std. You should see (near enough) `0.0` and `1.0`.
    ✓ each problem Python confirmed.
