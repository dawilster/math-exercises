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

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

14. $\mathcal{N}(0, 1)$ is the standard normal. Using Module 1.3 language, describe exactly what
    the transformation $x = 7z + 178$ does to it, and name the distribution you land on.

    ::: rephrase
    It's asking you to read a formula as two dial-turns from Module 1.3. Here $z$ is the
    standard bell $\mathcal{N}(0,1)$, and the formula builds a new bell out of it: multiplying
    $z$ by a number is the **stretch** dial ($\sigma$), and adding a number is the **shift**
    dial ($\mu$). So read $7z + 178$ as "which dial does each piece turn, and to what?" — the
    exact shift-and-stretch the lesson used to build the height bell from the standard one.
    :::

    ::: hint
    The number *multiplying* $z$ controls the width (stretch → $\sigma$); the number *added*
    controls the centre (shift → $\mu$). Which is which here?
    :::

    ::: hint
    So the $\times 7$ makes $\sigma = 7$ and the $+178$ makes $\mu = 178$. Drop both into
    $\mathcal{N}(\mu, \sigma)$.
    :::

    ::: steps
    1. **Read the multiplier as the stretch dial.** scales $\sigma$ from $1$ to $7$
    2. **Read the added constant as the shift dial.** moves $\mu$ from $0$ to $178$
    3. **Name the landed distribution.** $\mathcal{N}(178, 7)$
    :::

15. Diffusion models add noise as $x_{\text{noisy}} = x + \varepsilon$, $\varepsilon \sim \mathcal{N}(0, \sigma)$,
    with σ growing each step. A pixel has true value 0.5. With $\sigma = 0.1$, between what two
    values will the noisy pixel land ~95% of the time? What about $\sigma = 0.5$? One sentence:
    why does big σ eventually destroy the image?

    ::: rephrase
    "95% of the time" is the flag for the middle band of 68/95/99.7: 95% of a bell's values sit
    within $\mu \pm 2\sigma$. Here the pixel's true value $0.5$ is the centre $\mu$, and $\sigma$
    is the noise size. So "between what two values 95% of the time" just means: compute
    $\mu \pm 2\sigma$ — the very band you sketched in Part A. Do it once for each $\sigma$.
    :::

    ::: hint
    The noisy pixel is centred on its true value, so $\mu = 0.5$. Which of 68/95/99.7 pairs with
    "95% of the time," and how many $\sigma$ does that band reach out?
    :::

    ::: hint
    95% ↔ within $\mu \pm 2\sigma$. So the two edges are $0.5 - 2\sigma$ and $0.5 + 2\sigma$ —
    substitute each $\sigma$ in turn.
    :::

    ::: steps
    1. **95% ↔ the $\pm 2\sigma$ band, centred on the true pixel.** interval $= 0.5 \pm 2\sigma$
    2. **Substitute $\sigma = 0.1$.** $0.5 \pm 2(0.1) = 0.3$ to $0.7$
    3. **Substitute $\sigma = 0.5$.** $0.5 \pm 2(0.5) = -0.5$ to $1.5$
    4. **Say why big $\sigma$ destroys the image.** the noise spread swamps the true pixel value, drowning out the signal
    :::

16. Sum of two dice: the possible totals 2–12 are not equally likely (4.1). Sketch the shape of
    the distribution of the sum of **ten** dice, mark its rough centre, and say what famous shape
    it's heading toward and *why* (which idea from the lesson?).

    ::: rephrase
    This is the lesson's opening picture run in reverse: one die is flat, ten dice pile into a
    bell. Three things are wanted — (1) the rough centre of the pile, (2) the shape it approaches,
    (3) which lesson idea forces that shape. The centre is just the *average roll* stacked ten
    times; the shape and the "why" are the one big idea from the very top of the lesson.
    :::

    ::: hint
    One die averages $3.5$ per roll. Ten independent dice — what's the typical total, and so
    where does the pile centre?
    :::

    ::: hint
    For the shape and the reason, recall the lesson's headline: add up many small independent
    random things and the total is always ___. Name that theorem.
    :::

    ::: steps
    1. **Centre: stack the average roll ten times.** $10 \times 3.5 = 35$
    2. **Name the emerging shape.** a **normal (bell)** curve
    3. **Name why — the lesson's one big idea.** the Central Limit Theorem: sums of many independent random variables tend toward normal, regardless of the shape of what's being summed
    :::

17. If 68% of values are within 1σ, what fraction of values are within 1σ *above* the mean but
    NOT within 1σ below it… trick question — untangle what that sentence even asks, then answer.

    ::: rephrase
    The sentence is deliberately tangled — untangle it *before* computing. "Within 1σ **above**
    the mean" already means the strip from $\mu$ up to $\mu+1\sigma$; everything in it is above
    the mean by construction. So "but NOT within 1σ below it" is describing something already
    true — it adds nothing. Strip the noise and it's just problem 8's move: how big is the upper
    half-band?
    :::

    ::: hint
    Sketch it. Shade "within 1σ above the mean," then try to shade "within 1σ below the mean."
    Do the two regions overlap at all?
    :::

    ::: hint
    They don't overlap, so "NOT below" removes nothing. You're left with just the band $\mu$ to
    $\mu+1\sigma$ — half of the $68\%$ band.
    :::

    ::: steps
    1. **Untangle: the "NOT below" clause is empty.** "above the mean" already excludes "below the mean," so it adds nothing
    2. **Reduce to the upper half-band.** the region is just $\mu$ to $\mu + 1\sigma$
    3. **Halve the 68% band by symmetry.** $68\% / 2 = 34\%$
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
