# Worksheet 4.3 — The Normal Distribution

*Pen and paper. Sketch the bell for every problem in Parts B–D — the sketch IS the method:
z-score, sketch, split into half-bands, add. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up

1. For $\mathcal{N}(\mu = 100, \sigma = 15)$ (IQ scores), mark on a sketched bell:
   $\mu$, $\mu \pm 1\sigma$, $\mu \pm 2\sigma$, $\mu \pm 3\sigma$ (actual numbers).

   ::: answer
   $\mu = 100$; $\mu \pm 1\sigma = 85, 115$; $\mu \pm 2\sigma = 70, 130$; $\mu \pm 3\sigma = 55, 145$
   — move: each band is $\mu \pm n\sigma$, and here $\sigma = 15$.
   :::

2. What percentage of values fall within $1\sigma$ of the mean? Within $2\sigma$? Within $3\sigma$?

   ::: answer
   $\approx 68\%$ within $1\sigma$, $\approx 95\%$ within $2\sigma$, $\approx 99.7\%$ within $3\sigma$
   — move: the empirical (68/95/99.7) rule.
   :::

3. z-score of an IQ of 130? Of 85?

   ::: answer
   $z(130) = 2$, $z(85) = -1$ — move: $z = \dfrac{x - \mu}{\sigma}$.
   :::

4. Two curves: $\mathcal{N}(0, 1)$ and $\mathcal{N}(5, 1)$. Same paper, rough sketch of both.
   Which dial changed — shift or stretch?

   ::: answer
   Shift — move: $\mu$ changed ($0 \to 5$) but $\sigma = 1$ for both, so the width (stretch) is unchanged.
   :::

---

## Part B — Core

*(Use $\mathcal{N}(100, 15)$ throughout. Symmetry + 68/95/99.7 is all you need.)*

5. What fraction of people have IQ **above 100**?

   ::: answer
   $50\%$ — move: symmetry splits the bell exactly in half at the mean.
   :::

6. What fraction fall **between 85 and 115**?

   ::: answer
   $\approx 68\%$ — move: 85 to 115 is exactly $\mu \pm 1\sigma$.
   :::

7. What fraction fall **above 130**? *(Sketch: what's outside ±2σ, and what does symmetry
   say about just the right tail?)*

   ::: answer
   $\approx 2.5\%$ — move: 95% lies within $\pm 2\sigma$, leaving 5% split between the two tails;
   symmetry gives $2.5\%$ per tail.
   :::

8. What fraction fall **between 85 and 130**? Show the half-bands you added.

   ::: answer
   $\approx 81.5\%$ — move: half-bands added: $34\%$ (85 to 100, half of 68%) $+\ 47.5\%$
   (100 to 130, half of 95%) $= 81.5\%$.
   :::

9. Out of 1,000 people, roughly how many have IQ above 145?

   ::: answer
   $\approx 1$–$2$ people — move: 145 is $\mu + 3\sigma$; beyond $+3\sigma$ is
   $(100\% - 99.7\%)/2 = 0.15\%$ of the tail, and $0.15\%$ of 1,000 $\approx 1.5$.
   :::

10. Adult male heights are $\mathcal{N}(178, 7)$ cm. A doorway is 192 cm. What fraction of men
    must duck? *(z-score first.)*

    ::: answer
    $z = (192-178)/7 = 2$, so $\approx 2.5\%$ must duck — move: same reasoning as problem 7,
    the tail beyond $+2\sigma$.
    :::

---

## Part C — Diagnose the claim

11. "The bell curve for heights peaks at 178 cm with height 0.057 on the y-axis, so 5.7% of men
    are exactly 178 cm tall." What's the misread? Where does probability actually live on
    this graph?

    ::: answer
    The y-axis is **density**, not probability. For a continuous variable, probability lives in
    **area** under the curve over an interval — the height at a single point isn't a probability
    at all (in fact $P(X = 178)$ is exactly $0$).
    :::

12. "Household wealth has $\mu = \$400k$, so wealth is $\mathcal{N}(400k, \sigma)$ for some σ."
    Two sentences: why is wealth a bad candidate for a bell curve? (What does the curve assume
    that wealth violates? Think about what a billionaire does to symmetry.)

    ::: answer
    A normal curve assumes symmetric tails on both sides of the mean. Wealth violates this: it's
    bounded below (can't go far below \$0) but a handful of billionaires stretch the right tail
    enormously — the distribution is skewed, not symmetric.
    :::

13. "I generated noise with `rng.normal(0, 1, 100)` and got a value of 3.2. The generator must
    be broken — 99.7% of values are within 3σ." Is a 3.2 among 100 draws actually alarming?
    Roughly how often should a value beyond ±3σ show up?

    ::: answer
    Not alarming — move: beyond $\pm 3\sigma$ happens $100\% - 99.7\% = 0.3\%$ of the time, so in
    100 draws you'd *expect* about $0.3$ such values. Seeing one is unsurprising, not evidence
    the generator is broken.
    :::

---

## Part D — Deep end

14. $\mathcal{N}(0, 1)$ is the standard normal. Using Module 1.3 language, describe exactly what
    the transformation $x = 7z + 178$ does to it, and name the distribution you land on.

    ::: answer
    Move: a stretch by factor 7 (scales $\sigma$ from $1$ to $7$), then a shift by $+178$
    (moves $\mu$ from $0$ to $178$). Lands on $\mathcal{N}(178, 7)$.
    :::

15. Diffusion models add noise as $x_{\text{noisy}} = x + \varepsilon$, $\varepsilon \sim \mathcal{N}(0, \sigma)$,
    with σ growing each step. A pixel has true value 0.5. With $\sigma = 0.1$, between what two
    values will the noisy pixel land ~95% of the time? What about $\sigma = 0.5$? One sentence:
    why does big σ eventually destroy the image?

    ::: answer
    $\sigma = 0.1$: between $0.5 \pm 2(0.1) = 0.3$ and $0.7$. $\sigma = 0.5$: between
    $0.5 \pm 2(0.5) = -0.5$ and $1.5$ — move: 95% within $\mu \pm 2\sigma$. Big $\sigma$ eventually
    destroys the image because the noise spread swamps the true pixel value, drowning out the signal.
    :::

16. Sum of two dice: the possible totals 2–12 are not equally likely (4.1). Sketch the shape of
    the distribution of the sum of **ten** dice, mark its rough centre, and say what famous shape
    it's heading toward and *why* (which idea from the lesson?).

    ::: answer
    Centre $\approx 35$ ($10 \times 3.5$); it heads toward a **normal (bell)** shape — move: the
    Central Limit Theorem — sums of many independent random variables tend toward normal,
    regardless of the shape of what's being summed.
    :::

17. If 68% of values are within 1σ, what fraction of values are within 1σ *above* the mean but
    NOT within 1σ below it… trick question — untangle what that sentence even asks, then answer.

    ::: answer
    $34\%$ — untangled: "within 1σ above the mean" already excludes being below the mean, so
    the "NOT below it" clause adds nothing. It's just the upper half-band, $\mu$ to $\mu+1\sigma$,
    which is half of $68\%$.
    :::

---

## Part E — Python check (at the computer, after the pen work)

18. Verify problems 6, 7 and 10 by counting, e.g. for problem 7:

```python
import numpy as np
rng = np.random.default_rng(42)
iq = rng.normal(100, 15, size=1_000_000)
print((iq > 130).mean())      # compare with your Part B answer
```

19. Verify problem 13's intuition: `(np.abs(rng.normal(0, 1, 1_000_000)) > 3).mean()` —
    multiply by 100 draws. Were you right to be calm? ✓ each confirmed answer.
