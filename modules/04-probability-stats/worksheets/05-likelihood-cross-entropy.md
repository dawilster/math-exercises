# Worksheet 4.5 — Likelihood & Cross-Entropy

*Pen and paper. You'll need these logs (natural log, 3 d.p.) — no calculator required:*
$\ln 0.9 \approx -0.105$, $\ln 0.8 \approx -0.223$, $\ln 0.7 \approx -0.357$, $\ln 0.5 \approx -0.693$,
$\ln 0.25 \approx -1.386$, $\ln 0.2 \approx -1.609$, $\ln 0.1 \approx -2.303$, $\ln 0.05 \approx -2.996$,
$\ln 0.01 \approx -4.605$. *Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: surprise = $-\ln p$

1. Compute the surprise $-\ln p$ for $p = 0.9$, $p = 0.5$, $p = 0.1$, $p = 0.01$.

   ::: answer
   $-\ln 0.9 \approx 0.105$, $-\ln 0.5 \approx 0.693$, $-\ln 0.1 \approx 2.303$, $-\ln 0.01 \approx 4.605$ —
   move: surprise $= -\ln p$ (log, then negate).
   :::

2. Rank these events from least to most surprising, no computation needed:
   a coin lands heads ($p=0.5$); your team wins as $p=0.9$ favourites; a $p=0.01$ outsider wins.

   ::: answer
   Least → most surprising: team wins ($p=0.9$), coin heads ($p=0.5$), outsider wins ($p=0.01$) —
   move: higher $p$ means lower surprise, so just order by probability, descending.
   :::

3. What is the surprise when $p = 1$? What happens to $-\ln p$ as $p \to 0$, and why is that
   exactly the right behaviour for a measure of surprise?

   ::: answer
   Surprise at $p=1$ is $-\ln 1 = 0$ (a certain event carries no information). As $p \to 0$,
   $-\ln p \to \infty$ — exactly right, because an event you thought near-impossible actually
   happening should be maximally surprising.
   :::

4. A model gives the correct class probability 0.8. Cross-entropy for that example?
   (PICK → LOG → NEGATE.)

   ::: answer
   Cross-entropy $= -\ln 0.8 \approx 0.223$ — move: PICK the true-class probability (0.8),
   LOG it, NEGATE.
   :::

---

## Part B — Core

5. A model claims a coin has $P(\text{H}) = 0.8$. You observe **H, H, T**.
   a) Likelihood $L$ of this data (multiply it out).
   b) Log-likelihood $\ln L$ (use the table — no multiplying).
   c) Negative log-likelihood.

   ::: answer
   a) $L = 0.8 \times 0.8 \times 0.2 = 0.128$.
   b) $\ln L = \ln 0.8 + \ln 0.8 + \ln 0.2 \approx -0.223 - 0.223 - 1.609 = -2.055$.
   c) $-\ln L \approx 2.055$.
   Move: independent events multiply; $\ln$ turns that product into a sum of table values.
   :::

6. A rival model claims $P(\text{H}) = 0.5$. Same data H, H, T: compute its likelihood and
   negative log-likelihood. Which model does the data prefer, and by which comparison —
   higher $L$ or lower $-\ln L$? (Trick question: check they agree.)

   ::: answer
   $L = 0.5 \times 0.5 \times 0.5 = 0.125$; $\ln L = 3(-0.693) = -2.079$, so $-\ln L \approx 2.079$.
   $p=0.8$ wins: higher $L$ ($0.128 > 0.125$) *and* lower $-\ln L$ ($2.055 < 2.079$) — they agree
   because $-\ln(\cdot)$ is decreasing, so it never flips an ordering.
   :::

7. Classifier outputs for a photo: $[\text{cat: } 0.7,\ \text{dog: } 0.2,\ \text{bird: } 0.1]$.
   Cross-entropy if the truth is **cat**? If the truth is **bird**?

   ::: answer
   Truth = cat: $-\ln 0.7 \approx 0.357$. Truth = bird: $-\ln 0.1 \approx 2.303$. Move: PICK →
   LOG → NEGATE the true class's probability only.
   :::

8. A batch of three photos; the model gave the *true* class these probabilities: $0.9, 0.7, 0.05$.
   Average cross-entropy for the batch. Which single photo dominates the loss, and what fraction
   of the total does it contribute (roughly)?

   ::: answer
   Per-photo cross-entropy: $-\ln 0.9 \approx 0.105$, $-\ln 0.7 \approx 0.357$, $-\ln 0.05 \approx 2.996$.
   Average $= (0.105+0.357+2.996)/3 \approx 1.153$. The $p=0.05$ photo dominates: it contributes
   $2.996 / 3.458 \approx 87\%$ of the total. Move: average the per-example $-\ln p_{\text{true}}$
   values; the lowest-probability example dominates the sum.
   :::

9. Why do we work with $\ln L$ instead of $L$ itself? Give both reasons from the lesson
   (one is about computers, one is about calculus/Σ).

   ::: answer
   (1) Computers: multiplying many probabilities underflows toward $0$; summing their logs doesn't.
   (2) Calculus/Σ: $\ln$ turns a product into a sum, so the derivative of the total is just the sum
   of per-term derivatives — no repeated product rule across every factor. Move: $\ln(\prod) = \sum \ln$.
   :::

---

## Part C — Diagnose the claim

10. "My classifier's cross-entropy on one example is $-\ln 0.7 + -\ln 0.2 + -\ln 0.1$, summing
    the surprise of all three classes." What's the misunderstanding? Which probability is the
    only one that gets PICKed?

    ::: answer
    Only the true class's probability gets PICKed — cross-entropy for one example is
    $-\ln p_{\text{true}}$, a single term, not a sum over every class's own surprise. If the
    true class is cat, cross-entropy $= -\ln 0.7$ only; dog and bird don't enter.
    :::

11. "To combine the likelihood of three independent flips I added: $0.8 + 0.8 + 0.2 = 1.8$."
    Two errors here — one about combining, one visible in the result itself.

    ::: answer
    Error 1: independent events combine by *multiplying*, not adding
    ($0.8 \times 0.8 \times 0.2 = 0.128$, not $1.8$). Error 2: visible without even checking the
    rule — a probability can never exceed $1$, and $1.8 > 1$ is an immediate red flag.
    :::

12. "Model X is 92% accurate; Model Y is 90% accurate. So X necessarily has lower cross-entropy."
    Construct a tiny counter-scenario (two or three examples suffice) or explain which behaviour
    of X could break the claim.

    ::: answer
    Accuracy only checks whether the top prediction is correct (argmax); cross-entropy also cares
    how confident the correct predictions were. Example: X correct on 2/2 examples but only just
    ($p_{\text{true}}=0.34$ each) → average CE $= -\ln 0.34 \approx 1.079$. Y correct on only 1/2
    (lower accuracy) but confidently ($p=0.99$, CE $\approx 0.01$) and only mildly wrong on the
    other ($p_{\text{true}}=0.33$, CE $\approx 1.109$) → average CE $\approx 0.56$. X has higher
    accuracy but worse (higher) cross-entropy — move: accuracy ignores confidence, cross-entropy
    doesn't.
    :::

---

## Part D — Deep end

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

13. A 4-class model shrugs: $p = 0.25$ for every class. Cross-entropy on any example?
    A 10-class shrugger scores $\ln 10 \approx 2.303$. What's the pattern, and why is
    "loss ≈ $\ln(\text{classes})$ at step 0" a sanity check ML engineers actually use?

    ::: rephrase
    "Shrugs" = gives every class the same probability. With 4 classes that's $\frac14 = 0.25$
    each. Cross-entropy is still just PICK → LOG → NEGATE the *true* class's probability
    (problems 4 and 7) — and whatever the true class is, this model handed it $0.25$. So compute
    $-\ln 0.25$, then spot what that number has to do with the **4** and generalise.
    :::

    ::: hint
    You already know the one-example move: cross-entropy $= -\ln(p_{\text{true}})$. Here
    $p_{\text{true}} = 0.25$ no matter which class is right. Compute $-\ln 0.25$ from the table.
    :::

    ::: hint
    To see the pattern, don't leave it as a decimal: $0.25 = \frac14$, and $4$ is the number of
    classes. Turn $-\ln\frac1n$ into $+\ln n$ using the reciprocal/log rule.
    :::

    ::: steps
    1. **PICK → LOG → NEGATE the true class.** Every class got $0.25$, so $\text{CE} = -\ln 0.25 \approx 1.386$
    2. **Rewrite the shrug as $1/n$.** $0.25 = \tfrac14$, so $\text{CE} = -\ln\tfrac14 = \ln 4$ (and the 10-class shrug $= \ln 10 \approx 2.303$)
    3. **Name the pattern + why it's a sanity check.** A uniform model over $n$ classes scores $-\ln(1/n) = \ln n$; a freshly-initialised network outputs roughly uniform probabilities, so its step-0 loss should land near $\ln(\text{classes})$ — if it doesn't, the model/loss wiring is broken.
    :::

14. Your 10-class model reads loss 4.0 — *above* the 2.303 shrug-line. What must it be doing to
    score worse than knowing nothing? (Think: what kind of wrong?)

    ::: rephrase
    Problem 13 set the shrug-line: a model that knows nothing (uniform) scores exactly
    $\ln 10 \approx 2.303$ on 10 classes. This one scored $4.0$ — *worse than knowing nothing*.
    Since $\text{CE} = -\ln(p_{\text{true}})$, work backwards: what would $p_{\text{true}}$ have
    to be to make $-\ln(p_{\text{true}}) = 4$, and how does that compare to the $0.1$ a shrugger
    gives the true class?
    :::

    ::: hint
    Cross-entropy on one example is $-\ln(p_{\text{true}})$. "Loss above the shrug-line" means
    $-\ln(p_{\text{true}})$ is *bigger* than $-\ln 0.1$. What does more surprise say about the
    size of $p_{\text{true}}$?
    :::

    ::: hint
    More surprise ⇒ smaller $p_{\text{true}}$. So the model gives the true class *less* than the
    $0.1$ a shrugger would — probability it must be spending on the *wrong* classes instead. Name
    that behaviour.
    :::

    ::: steps
    1. **Recall the one-example loss and the shrug-line.** $\text{CE} = -\ln(p_{\text{true}})$; the shrug-line is $-\ln\tfrac{1}{10} = \ln 10 \approx 2.303$
    2. **Read what loss $> $ shrug-line forces.** $-\ln(p_{\text{true}}) > 2.303 \Rightarrow p_{\text{true}} < 0.1$ — the true class got *less* than a uniform guess
    3. **Name the behaviour.** The model is confidently wrong: actively misdirecting probability mass onto wrong classes, not merely uncertain. Uniform-but-honest is capped at $\ln 10$; only misdirection scores higher.
    :::

15. An LLM is trained by cross-entropy on the true next token. Sentence: "The cat sat on the ___".
    Model gives "mat" 0.4, "floor" 0.3, "roof" 0.05, others tiny. Compute the loss if the actual
    next word was "mat"; then if it was "roof". Which document teaches the model more, in the
    sense of a larger corrective signal — the expected one or the surprising one?

    ::: rephrase
    Each word's number is the probability the model gave *that word*. "Loss on the true next
    token" is just PICK → LOG → NEGATE (problem 7) applied to whichever word actually came next.
    Do it twice: once picking "mat" ($0.4$), once picking "roof" ($0.05$). Then compare the two
    surprises — the bigger surprise is the bigger correction.
    :::

    ::: hint
    This is problem 7 in words: cross-entropy $= -\ln(\text{probability of the true word})$. PICK
    the true word's number, LOG it, NEGATE — once for "mat", once for "roof".
    :::

    ::: hint
    For "which teaches more," compare the two losses: bigger loss = bigger surprise = bigger
    gradient = bigger push. Which of $0.4$ and $0.05$ gives the bigger $-\ln$?
    :::

    ::: steps
    1. **PICK → LOG → NEGATE for "mat".** $\text{loss} = -\ln 0.4 \approx 0.916$
    2. **Same move for "roof".** $\text{loss} = -\ln 0.05 \approx 2.996$
    3. **Compare the surprises.** "roof"'s loss (and gradient) is far larger, so the surprising word teaches more — a bigger corrective push.
    :::

16. You observe H, H, T. Compute the likelihood under $p = 0.5$, $p = \frac{2}{3}$, and $p = 0.8$
    ($0.8^2 \times 0.2 = 0.128$; $(\frac{2}{3})^2 \times \frac{1}{3} \approx 0.148$;
    $0.5^3 = 0.125$). Which wins? Notice *which* value of $p$ matches the observed frequency of
    heads. Coincidence? (You'll test this properly in the notebook.)

    ::: rephrase
    This is problem 5 done three times. Likelihood $=$ the probability the model assigns to the
    exact data H, H, T; independent flips *multiply*, so $L = p \cdot p \cdot (1-p) = p^2(1-p)$.
    Drop each of the three $p$-values into that (the problem even hands you the arithmetic), read
    off the largest $L$, then check the winning $p$ against the fraction of flips that were heads.
    :::

    ::: hint
    Likelihood of H, H, T under bias $p$ multiplies the flips: $p$ (H) $\times\, p$ (H)
    $\times\, (1-p)$ (T) $= p^2(1-p)$. The three values are given — just find the largest.
    :::

    ::: hint
    Once $p=\frac23$ wins, count the data: 2 heads out of 3 flips $= \frac23$. The best $p$ equals
    that fraction — name the pattern (it isn't luck).
    :::

    ::: steps
    1. **Write the likelihood as $p^2(1-p)$.** $L(0.5)=0.125,\; L(\tfrac23)\approx 0.148,\; L(0.8)=0.128$
    2. **Pick the largest.** $p=\tfrac23$ wins with $L \approx 0.148$
    3. **Match it to the data + name the pattern.** $\frac23$ is exactly the observed fraction of heads — not a coincidence: the maximum-likelihood estimate of $p$ *is* the observed proportion of successes.
    :::

---

## Part E — Python check (at the computer, after the pen work)

17. Check problems 7 and 8:

```python
import numpy as np
probs = np.array([0.7, 0.2, 0.1])
print(-np.log(probs[0]), -np.log(probs[2]))          # problem 7, both truths
print((-np.log(np.array([0.9, 0.7, 0.05]))).mean())  # problem 8
```

18. Check problem 16: `for p in [0.5, 2/3, 0.8]: print(p, p*p*(1-p))`. Then try a few more values
    of `p` — can you beat $\frac{2}{3}$? ✓ each answer Python confirmed.

    ::: answer
    No — $p=\frac{2}{3}$ is the maximum-likelihood estimate, the actual peak of
    $L(p) = p^2(1-p)$ on $[0,1]$ (found by setting $\frac{dL}{dp}=0$), so no other value of $p$
    scores higher on this data. Move: MLE for observed successes/trials = the sample proportion.
    :::
