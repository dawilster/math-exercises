# Worksheet 4.2 — Mean, Variance, Standard Deviation

*Pen and paper. Use the five named steps: CENTRE → DEVIATIONS → SQUARE → AVERAGE → UNSQUARE.
Data is kept small so the arithmetic stays friendly. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up

1. Mean of $3, 7, 8, 10, 12$?

   ::: answer
   $\mu = 8$ — move: $\mu = \frac{\text{sum}}{n} = \frac{3+7+8+10+12}{5} = \frac{40}{5}$.
   :::

2. Data: $4, 4, 4, 4$. Without computing, what are the variance and std? Why?

   ::: answer
   $\sigma^2 = 0$, $\sigma = 0$ — move: every value already equals $\mu$, so every deviation is 0;
   squaring and averaging zeros still gives zero. No spread, no variance.
   :::

3. Deviations from the mean for the data in problem 1. Check they sum to 0.

   ::: answer
   $-5, -1, 0, 2, 4$ — move: $x_i - \mu$ for each point ($\mu = 8$). Sum: $-5-1+0+2+4 = 0$ ✓.
   :::

4. A dataset has $\sigma^2 = 25$. What's $\sigma$? If the data is in seconds, what units is each in?

   ::: answer
   $\sigma = 5$ — move: UNSQUARE, $\sigma = \sqrt{\sigma^2}$. $\sigma^2$ is in seconds² (squared units),
   $\sigma$ is back in the original units, seconds.
   :::

---

## Part B — Core

5. Full five steps on: $1, 2, 6, 7$. Give $\mu$, $\sigma^2$, $\sigma$.

   ::: answer
   $\mu = 4$; deviations $-3,-2,2,3$; squared $9,4,4,9$ (sum $26$); $\sigma^2 = \frac{26}{4} = 6.5$;
   $\sigma = \sqrt{6.5} \approx 2.55$ — move: CENTRE → DEVIATIONS → SQUARE → AVERAGE → UNSQUARE.
   :::

6. Full five steps on: $10, 20, 20, 30$. Give $\mu$, $\sigma^2$, $\sigma$.

   ::: answer
   $\mu = 20$; deviations $-10, 0, 0, 10$; squared $100, 0, 0, 100$ (sum $200$); $\sigma^2 = \frac{200}{4} = 50$;
   $\sigma = \sqrt{50} \approx 7.07$ — same five moves as problem 5.
   :::

7. Test scores have $\mu = 70$, $\sigma = 8$. Compute z-scores for marks of 86, 70 and 58.
   One phrase each: what does the z-score *say*?

   ::: answer
   $z_{86} = \frac{86-70}{8} = 2$ — "2 standard deviations above average" (unusually high).
   $z_{70} = \frac{70-70}{8} = 0$ — "bang on average."
   $z_{58} = \frac{58-70}{8} = -1.5$ — "1.5 standard deviations below average" (below par, not extreme).
   Move: $z = \frac{x-\mu}{\sigma}$.
   :::

8. Feature A (house price, \$): $\mu = 500{,}000$, $\sigma = 150{,}000$.
   Feature B (bedrooms): $\mu = 3$, $\sigma = 1$.
   A house costs \$650,000 and has 5 bedrooms. Which feature is more unusual for this house?
   Prove it with z-scores.

   ::: answer
   $z_A = \frac{650{,}000-500{,}000}{150{,}000} = 1$. $z_B = \frac{5-3}{1} = 2$. Move: $z = \frac{x-\mu}{\sigma}$
   on each feature to put them on the same scale. $z_B > z_A$, so the 5 bedrooms are *more* unusual for
   this house than the price is.
   :::

9. Two machines fill 500 g bags. Machine 1: $\mu = 500$, $\sigma = 2$.
   Machine 2: $\mu = 500$, $\sigma = 20$. Same mean — which machine do you want filling your
   bags, and what question does the mean alone fail to answer?

   ::: answer
   Machine 1 ($\sigma=2$ vs $\sigma=20$) — its bags cluster tightly around 500 g, while Machine 2's
   swing wildly even though it averages the same. Move: compare $\sigma$, not $\mu$ — the mean alone
   can't tell you about *consistency*.
   :::

---

## Part C — Spot the error

10. "Data: $2, 4, 6, 8$. Mean is 5. Deviations are $-3, -1, 1, 3$, which average to 0 —
    so the variance is 0 and the data has no spread." Which step got skipped?

    ::: answer
    The **SQUARE** step. Raw deviations *always* average to 0 — that's a property of the mean, not
    evidence of "no spread". Squared deviations are $9,1,1,9$, summing to $20$, so
    $\sigma^2 = \frac{20}{4} = 5$, not 0.
    :::

11. "Salaries at our startup: $60k, 65k, 70k, 75k, 2{,}000k$ (the founder).
    Mean salary is \$454k — we pay brilliantly!" What's the diagnosis? Which single word in
    the claim does the mean not support?

    ::: answer
    The arithmetic is right ($\frac{60+65+70+75+2000}{5} = 454$k) but the mean is dragged up by one
    extreme outlier (the founder) — four of five employees earn $60$–$75$k. The word **"brilliantly"**
    isn't supported; the median ($70$k) tells the real story. Move: check for outliers before trusting
    the mean.
    :::

12. "Feature A has $\sigma = 150{,}000$ and feature B has $\sigma = 1$, so A carries
    150,000× more information and the network should focus on it." What's wrong, and what
    fix from this lesson makes A and B comparable?

    ::: answer
    $\sigma$ is measured in each feature's own units (dollars vs bedrooms), so raw spreads aren't
    comparable across scales — "150,000× more information" is meaningless. Move: standardise each
    feature with $z = \frac{x-\mu}{\sigma}$ first (centre 0, spread 1 for both), *then* compare.
    :::

---

## Part D — Deep end

13. Take the data from problem 5 and add 10 to every value. Recompute $\mu$ and $\sigma$
    (shortcut allowed if you can justify it). What changed, what didn't, and why?

    ::: answer
    New data $11,12,16,17$: $\mu = 14$ (shifted by $+10$, same as the shift), but $\sigma = \sqrt{6.5}
    \approx 2.55$ — **unchanged**. Move: shifting every value by a constant shifts $\mu$ by that
    constant, but every deviation $(x_i-\mu)$ stays exactly the same, so spread doesn't change.
    :::

14. Now multiply every value in problem 5's data by 2. What happens to $\mu$, to $\sigma$,
    and to $\sigma^2$? *(Careful — one of these changes by more than you'd guess.)*

    ::: answer
    New data $2,4,12,14$: $\mu = 8$ (doubled), $\sigma = 2\sqrt{6.5} = \sqrt{26} \approx 5.10$ (doubled
    too), but $\sigma^2 = 26$ — **quadrupled**, not doubled. Move: scaling by $k$ scales $\sigma$ by
    $|k|$, but scales $\sigma^2$ by $k^2$ (it's built from *squared* deviations).
    :::

15. Using 13 and 14: your data has $\mu = 40$, $\sigma = 5$. Find $a$ and $b$ so that
    $x_{\text{new}} = a x + b$ has $\mu = 0$, $\sigma = 1$. What is this transformation called
    in ML, and where have you seen $\frac{x - \mu}{\sigma}$ before on this page?

    ::: answer
    $a = \frac{1}{\sigma} = \frac{1}{5}$, $b = -\frac{\mu}{\sigma} = -8$, giving
    $x_{\text{new}} = \frac{x}{5} - 8 = \frac{x-40}{5}$ — that's the **z-score**, $\frac{x-\mu}{\sigma}$,
    from problems 7 and 8. In ML this shift-and-scale move is called **standardisation**.
    :::

16. Invent two different four-number datasets, both with $\mu = 5$ and both with $\sigma^2 = 8$.
    What does this tell you about how much two numbers can summarise?

    ::: answer
    E.g. $\{1,5,5,9\}$: $\mu=5$, deviations $-4,0,0,4$, $\sigma^2 = \frac{32}{4} = 8$. A totally
    different shape, $\{5-2\sqrt2,\ 5-2\sqrt2,\ 5+2\sqrt2,\ 5+2\sqrt2\} \approx \{2.17, 2.17, 7.83,
    7.83\}$, has the *same* $\mu=5,\ \sigma^2=8$ — infinitely many shapes share one mean and variance.
    Move: two numbers *summarise*, they don't *reconstruct* — always ask what a statistic is hiding.
    :::

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
