# Worksheet 4.4 — Sampling & Randomness

*Pen and paper. Reasoning in sentences is the main product here — most answers are two lines,
not a number. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up

1. For each, name the **population** and the **sample**:
   a) tasting a spoonful of soup;
   b) a 1,000-person election poll;
   c) a minibatch of 32 images drawn from a 1.2-million-image dataset.

   ::: answer
   a) Population: the whole pot of soup; sample: the spoonful.
   b) Population: all eligible voters (or all voters in the election); sample: the 1,000 people polled.
   c) Population: the full 1.2-million-image dataset; sample: the 32-image minibatch.
   :::

2. A fair coin is flipped 10 times → 7 heads. Estimate of $P(\text{heads})$ from this sample?
   Is the coin necessarily unfair?

   ::: answer
   Estimate: $\hat p = 7/10 = 0.7$. Not necessarily unfair — with only $n=10$ flips the estimate
   wobbles a lot; 7 heads is well within normal sampling variation for a fair coin.
   :::

3. Same coin, 10,000 flips → 5,038 heads. New estimate? Which estimate deserves more trust, and why?

   ::: answer
   New estimate: $\hat p = 5038/10000 = 0.5038$. The 10,000-flip estimate deserves more trust —
   wobble shrinks like $1/\sqrt{n}$, so a 1000× bigger sample gives a far steadier estimate, and
   it lands much closer to the true $0.5$.
   :::

4. What does `np.random.default_rng(42)` guarantee that `np.random.default_rng()` (no seed)
   doesn't?

   ::: answer
   A fixed seed guarantees reproducibility: the exact same sequence of "random" draws every run.
   No seed pulls fresh entropy each run, so the sequence differs every time.
   :::

---

## Part B — Core

5. Estimate wobble shrinks like $\frac{1}{\sqrt{n}}$. Going from 100 samples to 10,000 samples
   makes an estimate roughly how many times steadier?

   ::: answer
   100× more data ($100 \to 10{,}000$) → wobble shrinks by $\sqrt{100} = 10$. Roughly 10× steadier.
   :::

6. To make an estimate 10× steadier, how many times more data do you need? One sentence on what
   this means for the cost of accuracy in ML.

   ::: answer
   Since wobble $\propto 1/\sqrt{n}$, making it $10\times$ steadier needs $10^2 = 100\times$ more
   data. Accuracy gets expensive fast — each extra digit of precision costs a quadratic amount of
   extra data/compute.
   :::

7. Poll A: 400 people, 55% support. Poll B: 40 people, 65% support. A friend says "B's number is
   higher, so support is probably around 65%." Better conclusion, using this unit's ideas?

   ::: answer
   Poll A ($n=400$) wobbles like $1/\sqrt{400} = 1/20$; Poll B ($n=40$) wobbles like
   $1/\sqrt{40} \approx 1/6.3$ — roughly $3\times$ more wobble. Poll A's estimate is far steadier,
   so the better conclusion is that support is closer to 55%, not 65% — the friend is trusting the
   noisier, smaller sample.
   :::

8. A dataset of pet photos is sorted: 10,000 cats first, then 10,000 dogs. Training reads it in
   order, 32 images per minibatch. Describe what each early minibatch looks like as a *sample of
   the dataset*, and what a single `rng.shuffle` fixes.

   ::: answer
   Each early minibatch is all cats — a badly biased sample of the dataset, not representative of
   the true 50/50 population. `rng.shuffle` fixes this by randomizing the order so every minibatch
   becomes a representative random sample of the whole dataset again.
   :::

9. Your training script crashes at step 40,000 with a weird loss spike. Why does having seeded
   the run with `default_rng(42)` change your debugging life?

   ::: answer
   A seed makes the "random" event sequence (data order, init weights, augmentations) exactly
   reproducible. You can rerun the identical trajectory to step 40,000 and inspect it with
   logging/breakpoints — without a seed, the crash might not even recur on the next run.
   :::

---

## Part C — Diagnose the claim

10. "Our app-store survey of 2 million users shows 4.6★ average satisfaction." 2 million is huge —
    so what's still wrong? Who never appears in this sample?

    ::: answer
    Size doesn't fix bias — only wobble. This is a self-selected sample: only people motivated
    enough to leave a review appear (often the most delighted or most furious). The silent
    majority — happy-enough-to-not-comment users, and everyone who never uses the app at all —
    never appears, no matter how large $n$ gets.
    :::

11. "I rolled this die 12 times and got four 6s. That's double the expected two — the die is
    clearly loaded." Diagnose, using the vocabulary of this unit.

    ::: answer
    Expected count in 12 rolls is $12 \times \frac16 = 2$; the spread (SD) is
    $\sqrt{12 \cdot \frac16 \cdot \frac56} \approx 1.29$, so 4 sixes is only about 1.5 SDs from
    expectation — unremarkable noise at small $n$. Diagnosis: mistaking ordinary small-sample
    wobble for evidence of bias; $n=12$ is nowhere near enough to call the die loaded.
    :::

12. "Random shuffling can't matter — the model sees all the same data eventually either way."
    What does shuffling actually fix? (Problem 8 is your ammunition.)

    ::: answer
    Shuffling doesn't change the total data seen over an epoch, but it fixes what each individual
    minibatch looks like: instead of a biased run of cats-then-dogs (problem 8), every minibatch
    becomes a fair, representative sample of the whole dataset at each step, so gradient estimates
    aren't systematically skewed early in training.
    :::

13. "We set a seed, so our results are rigged, not random — reviewers shouldn't trust them."
    Untangle the two meanings of "random" being confused here.

    ::: answer
    Two different senses of "random": (1) *statistically random* — unpredictable, patternless, the
    property that makes sampling and inference valid; (2) *which pseudorandom sequence you use* —
    a seed just picks one specific (still statistically-random-looking) sequence. Fixing the seed
    doesn't cherry-pick a favourable outcome; it only makes the experiment replayable — the draws
    are exactly as "random" in sense (1) as an unseeded run.
    :::

---

## Part D — Deep end

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

14. An LLM's next-token distribution is: "blue" 0.5, "grey" 0.3, "green" 0.15, "purple" 0.05.
    a) At temperature → 0 (always take the most likely token), what does it output, every time?
    b) At normal temperature (sample according to the probabilities), out of 100 generations,
       roughly how many of each?
    c) One sentence: why might you want each mode — a legal contract vs a poem?

    ::: rephrase
    This distribution is a weighted bag of marbles: 50 blue, 30 grey, 15 green, 5 purple out of
    every 100. **Temperature → 0** means "always reach for the heaviest option"; **normal
    temperature** means "actually draw from the bag by its weights". This is the lesson's
    *temperature dial* — the same shuffling-vs-sampling randomness — made concrete. Part (c) just
    asks: when do you want the reliable grab vs the varied draw?
    :::

    ::: hint
    Temperature is the sampling dial from the lesson. Temp → 0 collapses it to "always pick the
    top token" (greedy / argmax) — which single token has the highest probability here?
    :::

    ::: hint
    For (b), "sample according to the probabilities" over many tries means the long-run counts
    *match* the probabilities (law of large numbers, problem 3's idea). Multiply each probability
    by the 100 generations.
    :::

    ::: steps
    1. **Temp → 0: take the argmax.** The single highest probability is "blue" (0.5), so it outputs "blue" every time.
    2. **Normal temp: counts follow the probabilities.** $100 \times$ each prob $\Rightarrow$ roughly 50 "blue", 30 "grey", 15 "green", 5 "purple".
    3. **Match the mode to the need.** Greedy = reliable, no surprises (a legal contract); sampling = variety and surprise (a poem).
    :::

15. You want to know the mean of a population with $\sigma = 20$. Sample means based on $n$ draws
    wobble with spread roughly $\frac{\sigma}{\sqrt{n}}$. How big must $n$ be for the sample mean
    to wobble by only ~1? By ~0.1?

    ::: rephrase
    This is problem 6's idea wearing a formula. The spread $\sigma = 20$ is fixed; you get to
    choose $n$ to make the sample mean's wobble as small as you want. "How big must $n$ be" just
    means: set the wobble formula equal to your target and solve for $n$ — like solving
    $20/\sqrt{n} = 1$. Same finish as any "isolate, then undo" problem.
    :::

    ::: hint
    Write the wobble as $\dfrac{20}{\sqrt{n}}$ and set it equal to your target ($1$, then $0.1$).
    The thing you're isolating is $\sqrt{n}$.
    :::

    ::: hint
    Get $\sqrt{n}$ alone on one side, then **square both sides** to turn $\sqrt{n}$ into $n$.
    :::

    ::: steps
    1. **Set wobble = target.** $\dfrac{20}{\sqrt{n}} = 1$
    2. **Isolate $\sqrt{n}$** (multiply both sides by $\sqrt{n}$). $\sqrt{n} = 20$
    3. **Square both sides** — undoes the root. $n = 400$
    4. **Repeat for target $0.1$.** $\dfrac{20}{\sqrt{n}} = 0.1 \Rightarrow \sqrt{n} = 200 \Rightarrow n = 40{,}000$
    :::

16. A gradient computed on a minibatch of 32 is a *sample estimate* of the full-dataset gradient.
    Using problem 15's formula-shape: what does doubling the batch size buy you, and why do
    practitioners not just use the biggest batch that fits? (Recall the lesson's deep-end
    question. Speculate freely — a reasoned guess beats silence.)

    ::: rephrase
    A minibatch gradient is a *sample estimate* of the true gradient, so it obeys the same
    $1/\sqrt{n}$ wobble law as everything else this unit. "What does doubling the batch buy" =
    plug $n \to 2n$ into that law and read off the steadiness factor. Then the judgment half:
    weigh that gain against what a bigger batch *costs*. A reasoned guess beats silence here.
    :::

    ::: hint
    Use the same $1/\sqrt{n}$ rule (problem 5). Doubling $n$ multiplies the wobble by
    $1/\sqrt{2}$ — what steadiness factor is that?
    :::

    ::: hint
    For "why not the biggest batch", invert the square-root law: how much *more* batch would it
    take to halve the noise? Then add the per-step compute/memory cost of a huge batch.
    :::

    ::: steps
    1. **Apply $1/\sqrt{n}$ to $n \to 2n$.** wobble shrinks by $\sqrt{2} \approx 1.41\times$ — noticeably but not dramatically steadier.
    2. **Invert the law for the real cost.** halving the noise needs $4\times$ the batch (and $4\times$ the compute/memory per step).
    3. **Name the trade-off.** square-root returns plus higher per-step cost (and worse generalization at very large batches) → the trade-off stops being worth it long before "the biggest that fits."
    :::

---

## Part E — Python check (at the computer, after the pen work)

17. Test problem 5's claim:

```python
import numpy as np
rng = np.random.default_rng(42)
for n in [100, 10_000]:
    estimates = [rng.integers(0, 2, size=n).mean() for _ in range(1_000)]
    print(n, np.std(estimates))     # wobble of the estimate — ratio ≈ 10?
```

18. Run `np.random.default_rng(42).integers(1, 7, size=5)` twice in a row (fresh generator each
    time). Then twice with no seed. One sentence in the margin: what did you see, and which
    behaviour do you want in an experiment you might need to replay?

    ::: answer
    Two seeded runs print the *identical* sequence both times; two unseeded runs each print a
    *different* sequence. For an experiment you might need to replay, you want the seeded
    behaviour — reproducibility beats "fresh" randomness.
    :::
