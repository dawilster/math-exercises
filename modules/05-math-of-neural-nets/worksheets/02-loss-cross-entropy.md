# Worksheet 5.2 — Loss & Cross-Entropy

*Pen and paper. Name the move at each step ("pick the $y=1$ branch", "apply $-\ln$").
Photograph into `scans/inbox/` when done.*

Cheat card: $\;\ln 2 \approx 0.693,\; \ln 4 \approx 1.386,\; \ln 10 \approx 2.303,\;
-\ln(0.9) \approx 0.105,\; -\ln(0.73) \approx 0.315,\; -\ln(0.27) \approx 1.309,\; -\ln(0.12) \approx 2.120$

---

## Part A — Warm-up: reading the penalty scale

1. Cross-entropy, $y = 1$: write the loss for $\hat{y} = 0.9$, $\hat{y} = 0.5$, $\hat{y} = 0.1$
   (as $-\ln$ expressions, then numbers — note $-\ln(0.1) = \ln 10$, a log law from Module 0.5).

2. Rank those three predictions from cheapest to most expensive. Does the ranking match your gut?

3. MSE for the same three predictions against $y = 1$: $(\hat{y} - 1)^2$ each. Which loss punishes
   the confident wrong answer ($\hat{y} = 0.1$) harder — MSE or cross-entropy?

4. Why is the loss for $\hat{y} = 0.5$ the same whether $y = 1$ or $y = 0$? One sentence.

---

## Part B — Core: score real networks

5. Worksheet 5.1 Part B gave $\hat{y} \approx 0.73$. The true label is $y = 0$.
   Write the correct branch of cross-entropy, substitute, and evaluate with the cheat card.

6. Same prediction, but suppose the truth had been $y = 1$. Evaluate again. Which world is the
   network living in — lucky or unlucky?

7. A network scores three examples: $(\hat{y}, y) = (0.9, 1),\; (0.73, 1),\; (0.12, 0)$.
   Compute each loss, then the **mean loss** $\frac{1}{3}\sum L_i$ (Module 0.6's $\Sigma$, Module 4.2's mean).
   This one number is what a training curve plots.

8. A weather model says "90% chance of rain" and it rains. A second model said "50%". Using
   cross-entropy, how many times cheaper was the better model's bill? *(Divide the losses.)*

---

## Part C — Spot the error

Each solution contains exactly one broken move. Circle it, name the rule it broke.

9. Claimed loss for $\hat{y} = 0.5$, $y = 1$:
   - line 1: $L = \ln(0.5)$
   - line 2: $L = -0.693$
   - line 3: "negative loss — the network is doing *better* than perfect!"

10. Claimed loss for $\hat{y} = 0.9$, $y = 0$:
    - line 1: $y = 0$, so use $L = -\ln(\hat{y})$
    - line 2: $L = -\ln(0.9) \approx 0.105$
    - line 3: "tiny loss — great prediction!"

11. Claimed softmax of scores $(2, 0)$:
    - line 1: $p_1 = \frac{2}{2 + 0}$... "division by total makes probabilities"
    - line 2: $p = (1, 0)$
    - line 3: "100% confident in class 1"

---

## Part D — Deep end

*Not fully covered yet. Attempt anyway.*

12. Softmax the scores $(1, 1)$ by hand. Then $(0, 0)$. Then $(5, 5)$. What's the pattern, and why
    does it make sense that all three agree?

13. Softmax $(3, 1)$ using $e^3 \approx 20.1$, $e^1 \approx 2.7$. Compare with the lesson's answer
    for $(2, 0)$. What did you just discover about *shifting all scores by the same amount*?
    (This fact is used inside every real softmax implementation to stop $e^{big}$ overflowing.)

14. From the lesson's deep-end question: a network that always says $\hat{y} = 0.5$ scores 0.693
    forever. Describe a dataset where *no* network can average better than 0.693 — what would the
    relationship between inputs and labels have to be? (Module 4.1's coin knows.)

15. Sketch (rough, Module 1.2 shape-zoo style) $L = -\ln(\hat{y})$ for $\hat{y}$ between 0 and 1.
    Mark where the loss is 0 and what happens as $\hat{y} \to 0$. One sentence: why is this exact
    shape the behaviour you *want* from a penalty?

---

## Part E — Python check (at the computer, after the pen work)

16. Verify Part B with numpy:

```python
import numpy as np

def cross_entropy(y_hat, y):
    return -(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))

print(cross_entropy(0.73, 0))    # problem 5
print(cross_entropy(0.73, 1))    # problem 6
losses = [cross_entropy(0.9, 1), cross_entropy(0.73, 1), cross_entropy(0.12, 0)]
print(np.mean(losses))           # problem 7
```

Tick ✓ each answer numpy confirms.

> **Bonus thought:** try `cross_entropy(1.0, 0)` and look at the result. Now you've *met* the
> $\ln(0)$ trap from the lesson. What tiny change to `y_hat` would a library make to prevent this?
