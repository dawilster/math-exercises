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

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

13. Take the data from problem 5 and add 10 to every value. Recompute $\mu$ and $\sigma$
    (shortcut allowed if you can justify it). What changed, what didn't, and why?

    ::: rephrase
    You're **sliding the whole dataset** along the number line by $+10$ — every point moves the same
    distance. Before computing, predict: does the *centre* move? does the *spread* (how bunched the
    points are relative to each other) change? Picture problem 5's four points on a ruler, then shove
    the ruler 10 to the right: the balance point rides along, but do the gaps between points change?
    :::

    ::: hint
    The tool is the deviation $(x_i - \mu)$. Ask what happens to *one* deviation when both the point
    $x_i$ **and** the mean $\mu$ each go up by 10.
    :::

    ::: hint
    First move: find the new mean (old $\mu$ plus the shift), then write out the new deviations and
    watch the $+10$'s cancel.
    :::

    ::: steps
    1. **Shift the mean by the same constant.** $\mu_{\text{new}} = 4 + 10 = 14$
    2. **Recompute deviations — the shifts cancel.** $(x_i+10)-(\mu+10) = x_i - \mu$, still $-3,-2,2,3$
    3. **Spread is untouched.** $\sigma = \sqrt{6.5} \approx 2.55$, exactly as in problem 5
    :::

14. Now multiply every value in problem 5's data by 2. What happens to $\mu$, to $\sigma$,
    and to $\sigma^2$? *(Careful — one of these changes by more than you'd guess.)*

    ::: rephrase
    This is problem 13's twin, but instead of *sliding* you're **stretching** — every point $\times 2$,
    so the data fans out. Predict all three: $\mu$, $\sigma$, $\sigma^2$. The warning in the question
    points at $\sigma^2$: it's built from *squared* deviations, so a stretch hits it twice over.
    :::

    ::: hint
    The tool is again the deviation $(x_i - \mu)$. Ask what one deviation becomes when you double
    every value — then remember variance *squares* each deviation.
    :::

    ::: hint
    First move: doubling the data doubles each deviation; but squaring a doubled deviation multiplies
    it by $2^2 = 4$. That's where $\sigma^2$ grows faster than you'd guess.
    :::

    ::: steps
    1. **Double the mean.** $\mu_{\text{new}} = 2 \cdot 4 = 8$
    2. **Double every deviation.** $-6, -4, 4, 6$
    3. **Square them — each grows $\times 4$.** $36, 16, 16, 36$ (sum $104$)
    4. **Average → variance quadrupled.** $\sigma^2 = \frac{104}{4} = 26$ (was $6.5$; $\times 4$)
    5. **Unsquare → std merely doubled.** $\sigma = \sqrt{26} = 2\sqrt{6.5} \approx 5.10$
    :::

15. Using 13 and 14: your data has $\mu = 40$, $\sigma = 5$. Find $a$ and $b$ so that
    $x_{\text{new}} = a x + b$ has $\mu = 0$, $\sigma = 1$. What is this transformation called
    in ML, and where have you seen $\frac{x - \mu}{\sigma}$ before on this page?

    ::: rephrase
    You want to transform data with $\mu=40, \sigma=5$ so it lands at $\mu=0, \sigma=1$. That's
    combining both earlier moves: a **stretch** (problem 14: multiplying by $a$ scales $\sigma$ by
    $|a|$) to fix the spread, and a **shift** (problem 13: adding $b$ moves $\mu$) to fix the centre.
    You've already met the finished formula — it's the z-score $\frac{x-\mu}{\sigma}$ from problems 7–8.
    :::

    ::: hint
    Split the job: $a$ controls the spread, $b$ controls the centre. Pin down $a$ first — choose it so
    the new std equals 1.
    :::

    ::: hint
    First move: set $\sigma_{\text{new}} = |a|\cdot 5 = 1$ to get $a$. Then pick $b$ so the new mean
    $a\cdot 40 + b$ comes out to 0.
    :::

    ::: steps
    1. **Scale to fix the spread.** $a = \frac{1}{\sigma} = \frac{1}{5}$ (so new $\sigma = \frac{1}{5}\cdot 5 = 1$)
    2. **Shift to fix the centre.** $b = -\frac{\mu}{\sigma} = -\frac{40}{5} = -8$ (so new $\mu = \frac{40}{5} - 8 = 0$)
    3. **Recognise the result.** $x_{\text{new}} = \frac{x}{5} - 8 = \frac{x-40}{5}$ — the **z-score** $\frac{x-\mu}{\sigma}$; in ML this move is **standardisation**
    :::

16. Invent two different four-number datasets, both with $\mu = 5$ and both with $\sigma^2 = 8$.
    What does this tell you about how much two numbers can summarise?

    ::: rephrase
    Run the machine **backwards**: instead of computing $\sigma^2$ from given data, build data to hit
    a target $\sigma^2 = 8$. The easy trick is symmetry — a set like $\{5-d, 5, 5, 5+d\}$ is *guaranteed*
    to have $\mu = 5$, so you only have to tune $d$ to land the variance. Then make a second set with a
    different shape but the same two numbers. The point: many shapes, one summary.
    :::

    ::: hint
    Use symmetry to get $\mu = 5$ for free: pick $\{5-d, 5, 5, 5+d\}$. Now the only unknown is $d$ —
    choose it so the average squared deviation is 8.
    :::

    ::: hint
    First move: try $\{1,5,5,9\}$ ($d=4$) — deviations $-4,0,0,4$ give $\sigma^2 = \frac{32}{4} = 8$.
    Now cook a second, differently-shaped set that also averages a squared deviation of 8.
    :::

    ::: steps
    1. **First dataset — symmetric, tune $d$ to the variance.** $\{1,5,5,9\}$: deviations $-4,0,0,4$, so $\sigma^2 = \frac{32}{4} = 8$
    2. **Second dataset — different shape, same two numbers.** $\{5-2\sqrt2,\, 5-2\sqrt2,\, 5+2\sqrt2,\, 5+2\sqrt2\} \approx \{2.17, 2.17, 7.83, 7.83\}$: each deviation $\pm 2\sqrt2$, so $\sigma^2 = \frac{4\cdot 8}{4} = 8$
    3. **Conclude.** infinitely many shapes share one $\mu, \sigma^2$ — two numbers *summarise* but don't *reconstruct*; always ask what a statistic is hiding
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
