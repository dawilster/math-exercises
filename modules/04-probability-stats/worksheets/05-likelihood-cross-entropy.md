# Worksheet 4.5 — Likelihood & Cross-Entropy

*Pen and paper. You'll need these logs (natural log, 3 d.p.) — no calculator required:*
$\ln 0.9 \approx -0.105$, $\ln 0.8 \approx -0.223$, $\ln 0.7 \approx -0.357$, $\ln 0.5 \approx -0.693$,
$\ln 0.25 \approx -1.386$, $\ln 0.2 \approx -1.609$, $\ln 0.1 \approx -2.303$, $\ln 0.05 \approx -2.996$,
$\ln 0.01 \approx -4.605$. *Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: surprise = $-\ln p$

1. Compute the surprise $-\ln p$ for $p = 0.9$, $p = 0.5$, $p = 0.1$, $p = 0.01$.

2. Rank these events from least to most surprising, no computation needed:
   a coin lands heads ($p=0.5$); your team wins as $p=0.9$ favourites; a $p=0.01$ outsider wins.

3. What is the surprise when $p = 1$? What happens to $-\ln p$ as $p \to 0$, and why is that
   exactly the right behaviour for a measure of surprise?

4. A model gives the correct class probability 0.8. Cross-entropy for that example?
   (PICK → LOG → NEGATE.)

---

## Part B — Core

5. A model claims a coin has $P(\text{H}) = 0.8$. You observe **H, H, T**.
   a) Likelihood $L$ of this data (multiply it out).
   b) Log-likelihood $\ln L$ (use the table — no multiplying).
   c) Negative log-likelihood.

6. A rival model claims $P(\text{H}) = 0.5$. Same data H, H, T: compute its likelihood and
   negative log-likelihood. Which model does the data prefer, and by which comparison —
   higher $L$ or lower $-\ln L$? (Trick question: check they agree.)

7. Classifier outputs for a photo: $[\text{cat: } 0.7,\ \text{dog: } 0.2,\ \text{bird: } 0.1]$.
   Cross-entropy if the truth is **cat**? If the truth is **bird**?

8. A batch of three photos; the model gave the *true* class these probabilities: $0.9, 0.7, 0.05$.
   Average cross-entropy for the batch. Which single photo dominates the loss, and what fraction
   of the total does it contribute (roughly)?

9. Why do we work with $\ln L$ instead of $L$ itself? Give both reasons from the lesson
   (one is about computers, one is about calculus/Σ).

---

## Part C — Diagnose the claim

10. "My classifier's cross-entropy on one example is $-\ln 0.7 + -\ln 0.2 + -\ln 0.1$, summing
    the surprise of all three classes." What's the misunderstanding? Which probability is the
    only one that gets PICKed?

11. "To combine the likelihood of three independent flips I added: $0.8 + 0.8 + 0.2 = 1.8$."
    Two errors here — one about combining, one visible in the result itself.

12. "Model X is 92% accurate; Model Y is 90% accurate. So X necessarily has lower cross-entropy."
    Construct a tiny counter-scenario (two or three examples suffice) or explain which behaviour
    of X could break the claim.

---

## Part D — Deep end

13. A 4-class model shrugs: $p = 0.25$ for every class. Cross-entropy on any example?
    A 10-class shrugger scores $\ln 10 \approx 2.303$. What's the pattern, and why is
    "loss ≈ $\ln(\text{classes})$ at step 0" a sanity check ML engineers actually use?

14. Your 10-class model reads loss 4.0 — *above* the 2.303 shrug-line. What must it be doing to
    score worse than knowing nothing? (Think: what kind of wrong?)

15. An LLM is trained by cross-entropy on the true next token. Sentence: "The cat sat on the ___".
    Model gives "mat" 0.4, "floor" 0.3, "roof" 0.05, others tiny. Compute the loss if the actual
    next word was "mat"; then if it was "roof". Which document teaches the model more, in the
    sense of a larger corrective signal — the expected one or the surprising one?

16. You observe H, H, T. Compute the likelihood under $p = 0.5$, $p = \frac{2}{3}$, and $p = 0.8$
    ($0.8^2 \times 0.2 = 0.128$; $(\frac{2}{3})^2 \times \frac{1}{3} \approx 0.148$;
    $0.5^3 = 0.125$). Which wins? Notice *which* value of $p$ matches the observed frequency of
    heads. Coincidence? (You'll test this properly in the notebook.)

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
