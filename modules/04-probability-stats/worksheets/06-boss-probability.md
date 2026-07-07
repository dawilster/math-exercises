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

2. Two fair dice. $P(\text{at least one even number})$? *(Count the complement.)*

3. A fair coin flipped 4 times. $P(\text{all four heads})$? And after 4 heads in a row, what is
   $P(\text{heads on flip 5})$ — and what fallacy says otherwise?

4. An LLM's next-token probabilities: "dog" 0.35, "cat" 0.30, "fox" 0.20, rest 0.15.
   $P(\text{the token is "dog" or "cat"})$? In 200 samples, roughly how many "fox"?

## Part B — Centre, spread, z-scores

5. Data: $3, 5, 5, 5, 6, 8, 8, 8$. Compute $\mu$, $\sigma^2$, $\sigma$ (all steps shown).

6. Features for one house: price \$800{,}000 where prices are $\mu = 650{,}000$, $\sigma = 100{,}000$;
   land 400 m² where land is $\mu = 550$, $\sigma = 75$. Compute both z-scores. Which feature is
   more unusual, and in which direction?

7. Give the transformation that normalises the price feature to centre 0, spread 1, and state
   what a price of \$650,000 and a price of \$850,000 each become under it.

## Part C — Interpret the distribution

8. IQ is $\mathcal{N}(100, 15)$. Sketch the bell; shade and compute the fraction of people
   between 70 and 115. From 10,000 people, how many above 130?

9. Two loss-curve noise distributions: run 1's final losses across 20 seeds are
   $\mathcal{N}(2.1, 0.05)$; run 2's are $\mathcal{N}(2.0, 0.4)$. A single run of each is
   performed: run 1 scores 2.12, run 2 scores 1.75. A colleague concludes "run 2's setup is
   better." What do the σ's say about how much to trust that single 1.75? Which setup would you
   ship, and why?

10. "The pdf of $\mathcal{N}(0,1)$ has height ≈ 0.40 at 0, so $P(z = 0)$ is 40%." Correct the
    misread in one sentence, and state where probability lives on a pdf.

11. A histogram of household incomes has a long right tail (a few enormous values). Is the mean
    above or below the typical household? Would 68/95/99.7 reasoning be safe here? Why not?

## Part D — Likelihood & cross-entropy

12. A model claims $P(\text{H}) = 0.6$ for a coin. You observe **H, T, H**.
    a) Likelihood. b) Negative log-likelihood via the table. c) Beat it: does $p = \frac{2}{3}$
    give higher likelihood? Show it.

13. Classifier output $[\text{cat: } 0.5,\ \text{dog: } 0.25,\ \text{bird: } 0.25]$; the truth is
    dog. Cross-entropy? Now the model "improves" to $[0.02, 0.9, 0.08]$ on a photo whose truth is
    **cat**: cross-entropy? One sentence: what behaviour is the loss punishing so hard?

14. Why is an untrained 4-class classifier expected to start with loss near $\ln 4 \approx 1.386$,
    and what would a starting loss of 5 tell you?

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
