# Boss Worksheet — Module 4: Probability & Statistics

**Rules of the boss fight:**

- Parts A–D are **pen and paper, done cold** — no notes, no lessons, no Python.
- Show working and *name your steps* (LIST/COUNT/DIVIDE, CENTRE→…→UNSQUARE, PICK→LOG→NEGATE).
- Photograph everything into `scans/inbox/` for marking.
- **≥85% with sound reasoning unlocks Module 5** — where you build a neural net from scratch
  using everything in Modules 0–4. Gaps go on the review queue. Then: the Galton Board interlude.
- Part E is the simulation task — at the computer, after the paper parts are scanned.

*Log table (natural log):* $\ln 0.9 \approx -0.105$, $\ln 0.6 \approx -0.511$, $\ln 0.5 \approx -0.693$,
$\ln 0.25 \approx -1.386$, $\ln 0.1 \approx -2.303$, $\ln 0.02 \approx -3.912$.

---

## Part A — Probability puzzles

1. Two fair dice. $P(\text{sum} = 10)$? Show the pairs.

   ::: answer
   $\frac{3}{36} = \frac{1}{12}$ — move: LIST the pairs summing to 10 ($(4,6), (5,5), (6,4)$),
   COUNT 3, DIVIDE by 36.
   :::

2. Two fair dice. $P(\text{at least one even number})$? *(Count the complement.)*

   ::: answer
   $\frac{3}{4}$ — move: complement trick. $P(\text{both odd}) = \frac{3}{6}\times\frac{3}{6} = \frac14$,
   so $P(\text{at least one even}) = 1 - \frac14 = \frac34$.
   :::

3. A fair coin flipped 4 times. $P(\text{all four heads})$? And after 4 heads in a row, what is
   $P(\text{heads on flip 5})$ — and what fallacy says otherwise?

   ::: answer
   $P(\text{HHHH}) = \left(\frac12\right)^4 = \frac{1}{16}$ — move: independent events multiply.
   $P(\text{heads on flip 5}) = \frac12$ still — flips have no memory; claiming otherwise is the
   gambler's fallacy.
   :::

4. An LLM's next-token probabilities: "dog" 0.35, "cat" 0.30, "fox" 0.20, rest 0.15.
   $P(\text{the token is "dog" or "cat"})$? In 200 samples, roughly how many "fox"?

   ::: answer
   $P(\text{"dog" or "cat"}) = 0.35 + 0.30 = 0.65$ — move: addition rule for mutually exclusive
   outcomes. Expect roughly $200 \times 0.20 = 40$ "fox" tokens.
   :::

## Part B — Centre, spread, z-scores

5. Data: $3, 5, 5, 5, 6, 8, 8, 8$. Compute $\mu$, $\sigma^2$, $\sigma$ (all steps shown).

   ::: answer
   $\mu = 6$; deviations $-3,-1,-1,-1,0,2,2,2$ (sum $0$ ✓); squares $9,1,1,1,0,4,4,4$, sum $24$;
   $\sigma^2 = 24/8 = 3$; $\sigma = \sqrt3 \approx 1.73$ — move: CENTRE → DEVIATIONS → SQUARE →
   AVERAGE → UNSQUARE.
   :::

6. Features for one house: price \$800{,}000 where prices are $\mu = 650{,}000$, $\sigma = 100{,}000$;
   land 400 m² where land is $\mu = 550$, $\sigma = 75$. Compute both z-scores. Which feature is
   more unusual, and in which direction?

   ::: answer
   $z_{\text{price}} = \frac{800{,}000 - 650{,}000}{100{,}000} = 1.5$;
   $z_{\text{land}} = \frac{400-550}{75} = -2$ — move: $z = \dfrac{x-\mu}{\sigma}$. Land is the more
   unusual feature ($|{-2}| > |1.5|$), and it's unusual on the low side (smaller than typical).
   :::

7. Give the transformation that normalises the price feature to centre 0, spread 1, and state
   what a price of \$650,000 and a price of \$850,000 each become under it.

   ::: answer
   Move: $z = \dfrac{x-\mu}{\sigma}$ — subtract the mean, divide by the spread (shift to centre 0,
   stretch to spread 1). $\$650{,}000 \to z = 0$; $\$850{,}000 \to z = \frac{850{,}000-650{,}000}{100{,}000} = 2$.
   :::

## Part C — Interpret the distribution

8. IQ is $\mathcal{N}(100, 15)$. Sketch the bell; shade and compute the fraction of people
   between 70 and 115. From 10,000 people, how many above 130?

   ::: answer
   z-scores: $70 = \mu - 2\sigma$, $115 = \mu + \sigma$. Half-bands: $47.5\%$ ($-2\sigma$ to $\mu$,
   half of 95%) $+\ 34\%$ ($\mu$ to $+1\sigma$, half of 68%) $= 81.5\%$ between 70 and 115.
   $130 = \mu + 2\sigma$: the tail beyond $+2\sigma$ is $(100\% - 95\%)/2 = 2.5\%$, so
   $\approx 250$ of 10,000 people.
   :::

9. Two loss-curve noise distributions: run 1's final losses across 20 seeds are
   $\mathcal{N}(2.1, 0.05)$; run 2's are $\mathcal{N}(2.0, 0.4)$. A single run of each is
   performed: run 1 scores 2.12, run 2 scores 1.75. A colleague concludes "run 2's setup is
   better." What do the σ's say about how much to trust that single 1.75? Which setup would you
   ship, and why?

   ::: answer
   z-scores against each run's own distribution: $z_{2.12} = \frac{2.12-2.1}{0.05} = 0.4$;
   $z_{1.75} = \frac{1.75-2.0}{0.4} = -0.625$. Both are completely unremarkable single draws
   (well under 1σ) — neither observed value is a surprising outlier, so one run each is weak
   evidence; run 2's σ is 8× run 1's, so its single number wobbles far more and shouldn't be
   trusted alone. Going by the actual population means (2.0 < 2.1), run 2 does look better on
   average — ship it, but demand more seeds before being confident, precisely because its high σ
   makes any one run unreliable.
   :::

10. "The pdf of $\mathcal{N}(0,1)$ has height ≈ 0.40 at 0, so $P(z = 0)$ is 40%." Correct the
    misread in one sentence, and state where probability lives on a pdf.

    ::: answer
    The pdf's height is a **density**, not a probability — $P(z=0)$ is exactly $0$ for a
    continuous variable (a single point has zero width). Probability lives in the **area** under
    the curve over an interval.
    :::

11. A histogram of household incomes has a long right tail (a few enormous values). Is the mean
    above or below the typical household? Would 68/95/99.7 reasoning be safe here? Why not?

    ::: answer
    The mean sits **above** the typical (median) household — the long right tail of rare huge
    incomes drags it up. 68/95/99.7 would not be safe: that rule assumes a symmetric bell curve,
    and a skewed distribution isn't one.
    :::

## Part D — Likelihood & cross-entropy

12. A model claims $P(\text{H}) = 0.6$ for a coin. You observe **H, T, H**.
    a) Likelihood. b) Negative log-likelihood via the table. c) Beat it: does $p = \frac{2}{3}$
    give higher likelihood? Show it.

    ::: answer
    a) $L = 0.6 \times 0.4 \times 0.6 = 0.144$.
    b) $\ln 0.4$ isn't listed directly, but $0.4 = \frac{4}{10}$, so $\ln 0.4 = \ln 4 - \ln 10 =
    1.386 - 2.303 = -0.917$ (both pieces from the table, since $\ln 0.25 \approx -1.386$ gives
    $\ln 4 = 1.386$ and $\ln 0.1 \approx -2.303$ gives $\ln 10 = 2.303$). NLL $=
    -[2\ln 0.6 + \ln 0.4] = -[2(-0.511) + (-0.917)] = 1.939$.
    c) $L\left(\frac23\right) = \left(\frac23\right)^2 \times \frac13 = \frac{4}{27} \approx 0.148 >
    0.144$ — yes, $p=\frac23$ (the observed frequency of heads) beats it.
    :::

13. Classifier output $[\text{cat: } 0.5,\ \text{dog: } 0.25,\ \text{bird: } 0.25]$; the truth is
    dog. Cross-entropy? Now the model "improves" to $[0.02, 0.9, 0.08]$ on a photo whose truth is
    **cat**: cross-entropy? One sentence: what behaviour is the loss punishing so hard?

    ::: answer
    $\text{CE}_1 = -\ln(0.25) \approx 1.386$ — move: PICK dog's probability (0.25), LOG, NEGATE.
    $\text{CE}_2 = -\ln(0.02) \approx 3.912$ — truth is cat, but the model now gives cat only 0.02.
    The loss punishes **confident wrong answers** brutally — being sure and wrong costs far more
    than being unsure ever earns back.
    :::

14. Why is an untrained 4-class classifier expected to start with loss near $\ln 4 \approx 1.386$,
    and what would a starting loss of 5 tell you?

    ::: answer
    With no learned signal the model outputs roughly uniform probabilities ($\frac14$ each), so
    $\text{CE} = -\ln\frac14 = \ln 4 \approx 1.386$ — move: shrug-loss $= \ln(\text{number of
    classes})$. A starting loss of 5 is *worse* than blind guessing (it means less than $\frac14$
    probability is going to the true class on average) — a sign something's broken (bad init,
    wrong labels, exploding weights), not just ordinary early training.
    :::

## Part E — Simulation task (at the computer, last)

15. **The wobble experiment.** Write a small script (fresh file or notebook cell), seeded with
    `np.random.default_rng(42)`:
    a) Simulate rolling a fair die $n$ times and estimating $P(6)$, for
       $n = 10, 100, 1{,}000, 10{,}000, 100{,}000$.
    b) For each $n$, repeat the estimate 200 times and print the standard deviation of the 200
       estimates (the *wobble*).
    c) On paper: does the wobble shrink like $\frac{1}{\sqrt{n}}$? Check one adjacent pair of
       $n$'s (×10 data → wobble ÷ ?) and write the verdict.
    d) Two-sentence conclusion connecting this to why bigger samples (and more training data)
       give steadier estimates — but at brutal cost.

*Scan Parts A–D into `scans/inbox/`, include your Part E code + output (screenshot is fine),
and tell Claude the boss fight is on.*
