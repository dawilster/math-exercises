# Worksheet 4.3 — The Normal Distribution

*Pen and paper. Sketch the bell for every problem in Parts B–D — the sketch IS the method:
z-score, sketch, split into half-bands, add. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up

1. For $\mathcal{N}(\mu = 100, \sigma = 15)$ (IQ scores), mark on a sketched bell:
   $\mu$, $\mu \pm 1\sigma$, $\mu \pm 2\sigma$, $\mu \pm 3\sigma$ (actual numbers).

2. What percentage of values fall within $1\sigma$ of the mean? Within $2\sigma$? Within $3\sigma$?

3. z-score of an IQ of 130? Of 85?

4. Two curves: $\mathcal{N}(0, 1)$ and $\mathcal{N}(5, 1)$. Same paper, rough sketch of both.
   Which dial changed — shift or stretch?

---

## Part B — Core

*(Use $\mathcal{N}(100, 15)$ throughout. Symmetry + 68/95/99.7 is all you need.)*

5. What fraction of people have IQ **above 100**?

6. What fraction fall **between 85 and 115**?

7. What fraction fall **above 130**? *(Sketch: what's outside ±2σ, and what does symmetry
   say about just the right tail?)*

8. What fraction fall **between 85 and 130**? Show the half-bands you added.

9. Out of 1,000 people, roughly how many have IQ above 145?

10. Adult male heights are $\mathcal{N}(178, 7)$ cm. A doorway is 192 cm. What fraction of men
    must duck? *(z-score first.)*

---

## Part C — Diagnose the claim

11. "The bell curve for heights peaks at 178 cm with height 0.057 on the y-axis, so 5.7% of men
    are exactly 178 cm tall." What's the misread? Where does probability actually live on
    this graph?

12. "Household wealth has $\mu = \$400k$, so wealth is $\mathcal{N}(400k, \sigma)$ for some σ."
    Two sentences: why is wealth a bad candidate for a bell curve? (What does the curve assume
    that wealth violates? Think about what a billionaire does to symmetry.)

13. "I generated noise with `rng.normal(0, 1, 100)` and got a value of 3.2. The generator must
    be broken — 99.7% of values are within 3σ." Is a 3.2 among 100 draws actually alarming?
    Roughly how often should a value beyond ±3σ show up?

---

## Part D — Deep end

14. $\mathcal{N}(0, 1)$ is the standard normal. Using Module 1.3 language, describe exactly what
    the transformation $x = 7z + 178$ does to it, and name the distribution you land on.

15. Diffusion models add noise as $x_{\text{noisy}} = x + \varepsilon$, $\varepsilon \sim \mathcal{N}(0, \sigma)$,
    with σ growing each step. A pixel has true value 0.5. With $\sigma = 0.1$, between what two
    values will the noisy pixel land ~95% of the time? What about $\sigma = 0.5$? One sentence:
    why does big σ eventually destroy the image?

16. Sum of two dice: the possible totals 2–12 are not equally likely (4.1). Sketch the shape of
    the distribution of the sum of **ten** dice, mark its rough centre, and say what famous shape
    it's heading toward and *why* (which idea from the lesson?).

17. If 68% of values are within 1σ, what fraction of values are within 1σ *above* the mean but
    NOT within 1σ below it… trick question — untangle what that sentence even asks, then answer.

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
