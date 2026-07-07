# Worksheet 4.4 — Sampling & Randomness

*Pen and paper. Reasoning in sentences is the main product here — most answers are two lines,
not a number. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up

1. For each, name the **population** and the **sample**:
   a) tasting a spoonful of soup;
   b) a 1,000-person election poll;
   c) a minibatch of 32 images drawn from a 1.2-million-image dataset.

2. A fair coin is flipped 10 times → 7 heads. Estimate of $P(\text{heads})$ from this sample?
   Is the coin necessarily unfair?

3. Same coin, 10,000 flips → 5,038 heads. New estimate? Which estimate deserves more trust, and why?

4. What does `np.random.default_rng(42)` guarantee that `np.random.default_rng()` (no seed)
   doesn't?

---

## Part B — Core

5. Estimate wobble shrinks like $\frac{1}{\sqrt{n}}$. Going from 100 samples to 10,000 samples
   makes an estimate roughly how many times steadier?

6. To make an estimate 10× steadier, how many times more data do you need? One sentence on what
   this means for the cost of accuracy in ML.

7. Poll A: 400 people, 55% support. Poll B: 40 people, 65% support. A friend says "B's number is
   higher, so support is probably around 65%." Better conclusion, using this unit's ideas?

8. A dataset of pet photos is sorted: 10,000 cats first, then 10,000 dogs. Training reads it in
   order, 32 images per minibatch. Describe what each early minibatch looks like as a *sample of
   the dataset*, and what a single `rng.shuffle` fixes.

9. Your training script crashes at step 40,000 with a weird loss spike. Why does having seeded
   the run with `default_rng(42)` change your debugging life?

---

## Part C — Diagnose the claim

10. "Our app-store survey of 2 million users shows 4.6★ average satisfaction." 2 million is huge —
    so what's still wrong? Who never appears in this sample?

11. "I rolled this die 12 times and got four 6s. That's double the expected two — the die is
    clearly loaded." Diagnose, using the vocabulary of this unit.

12. "Random shuffling can't matter — the model sees all the same data eventually either way."
    What does shuffling actually fix? (Problem 8 is your ammunition.)

13. "We set a seed, so our results are rigged, not random — reviewers shouldn't trust them."
    Untangle the two meanings of "random" being confused here.

---

## Part D — Deep end

14. An LLM's next-token distribution is: "blue" 0.5, "grey" 0.3, "green" 0.15, "purple" 0.05.
    a) At temperature → 0 (always take the most likely token), what does it output, every time?
    b) At normal temperature (sample according to the probabilities), out of 100 generations,
       roughly how many of each?
    c) One sentence: why might you want each mode — a legal contract vs a poem?

15. You want to know the mean of a population with $\sigma = 20$. Sample means based on $n$ draws
    wobble with spread roughly $\frac{\sigma}{\sqrt{n}}$. How big must $n$ be for the sample mean
    to wobble by only ~1? By ~0.1?

16. A gradient computed on a minibatch of 32 is a *sample estimate* of the full-dataset gradient.
    Using problem 15's formula-shape: what does doubling the batch size buy you, and why do
    practitioners not just use the biggest batch that fits? (Recall the lesson's deep-end
    question. Speculate freely — a reasoned guess beats silence.)

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
