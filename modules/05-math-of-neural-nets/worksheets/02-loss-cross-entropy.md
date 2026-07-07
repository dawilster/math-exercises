# Worksheet 5.2 — Loss & Cross-Entropy

*Pen and paper. Name the move at each step ("pick the $y=1$ branch", "apply $-\ln$").
Photograph into `scans/inbox/` when done.*

Cheat card: $\;\ln 2 \approx 0.693,\; \ln 4 \approx 1.386,\; \ln 10 \approx 2.303,\;
-\ln(0.9) \approx 0.105,\; -\ln(0.73) \approx 0.315,\; -\ln(0.27) \approx 1.309,\; -\ln(0.12) \approx 2.120$

---

## Part A — Warm-up: reading the penalty scale

1. Cross-entropy, $y = 1$: write the loss for $\hat{y} = 0.9$, $\hat{y} = 0.5$, $\hat{y} = 0.1$
   (as $-\ln$ expressions, then numbers — note $-\ln(0.1) = \ln 10$, a log law from Module 0.5).

   ::: answer
   $-\ln(0.9) \approx 0.105$, $-\ln(0.5) = \ln 2 \approx 0.693$, $-\ln(0.1) = \ln 10 \approx 2.303$ —
   move: $y=1$ branch, $L = -\ln\hat{y}$, then evaluate each.
   :::

2. Rank those three predictions from cheapest to most expensive. Does the ranking match your gut?

   ::: answer
   Cheapest → most expensive: $\hat{y}=0.9$ ($0.105$), then $\hat{y}=0.5$ ($0.693$), then
   $\hat{y}=0.1$ ($2.303$) most expensive. Matches gut — closer to the truth costs less.
   :::

3. MSE for the same three predictions against $y = 1$: $(\hat{y} - 1)^2$ each. Which loss punishes
   the confident wrong answer ($\hat{y} = 0.1$) harder — MSE or cross-entropy?

   ::: answer
   MSE: $(0.9-1)^2=0.01$, $(0.5-1)^2=0.25$, $(0.1-1)^2=0.81$. Cross-entropy punishes the confident
   wrong answer harder — $2.303$ vs MSE's $0.81$ — and unlike MSE (capped at $1$), $-\ln\hat{y}\to\infty$
   as $\hat{y}\to0$.
   :::

4. Why is the loss for $\hat{y} = 0.5$ the same whether $y = 1$ or $y = 0$? One sentence.

   ::: answer
   Because $1-\hat{y}=1-0.5=0.5$ too — the $y=0$ branch $-\ln(1-\hat{y})$ becomes $-\ln(0.5)$,
   identical to the $y=1$ branch. Move: sub $\hat{y}=0.5$ into either branch, they collapse to the same number.
   :::

---

## Part B — Core: score real networks

5. Worksheet 5.1 Part B gave $\hat{y} \approx 0.73$. The true label is $y = 0$.
   Write the correct branch of cross-entropy, substitute, and evaluate with the cheat card.

   ::: answer
   $y=0$ branch: $L = -\ln(1-\hat{y}) = -\ln(1-0.73) = -\ln(0.27) \approx 1.309$ — move: compute
   $1-\hat{y}$ first, then read the cheat card.
   :::

6. Same prediction, but suppose the truth had been $y = 1$. Evaluate again. Which world is the
   network living in — lucky or unlucky?

   ::: answer
   If $y=1$: $L = -\ln(0.73) \approx 0.315$. The real loss (problem 5) was $1.309$, much bigger —
   the network is in the **unlucky** world: it leaned toward class $1$ ($\hat{y}=0.73$) but the truth was $0$.
   :::

7. A network scores three examples: $(\hat{y}, y) = (0.9, 1),\; (0.73, 1),\; (0.12, 0)$.
   Compute each loss, then the **mean loss** $\frac{1}{3}\sum L_i$ (Module 0.6's $\Sigma$, Module 4.2's mean).
   This one number is what a training curve plots.

   ::: answer
   $L_1=-\ln(0.9)\approx0.105$ ($y=1$ branch). $L_2=-\ln(0.73)\approx0.315$ ($y=1$ branch).
   $L_3=-\ln(1-0.12)=-\ln(0.88)\approx0.128$ ($y=0$ branch — the cheat card's $-\ln(0.12)\approx2.120$
   is the *wrong* branch here, watch for that trap). Mean $=\frac{0.105+0.315+0.128}{3}\approx0.183$.
   :::

8. A weather model says "90% chance of rain" and it rains. A second model said "50%". Using
   cross-entropy, how many times cheaper was the better model's bill? *(Divide the losses.)*

   ::: answer
   Both $y=1$ (it rained): $-\ln(0.9)\approx0.105$ vs $-\ln(0.5)\approx0.693$. Ratio
   $0.693/0.105\approx6.6$ — the $90\%$ model's bill was about $6.6\times$ cheaper.
   :::

---

## Part C — Spot the error

Each solution contains exactly one broken move. Circle it, name the rule it broke.

9. Claimed loss for $\hat{y} = 0.5$, $y = 1$:
   - line 1: $L = \ln(0.5)$
   - line 2: $L = -0.693$
   - line 3: "negative loss — the network is doing *better* than perfect!"

   ::: answer
   Line 1 is broken — it dropped the leading minus sign; cross-entropy is $L=-\ln\hat{y}$, not $\ln\hat{y}$.
   Correct: $L=-\ln(0.5)\approx0.693$ (positive — loss can never be negative, since $\hat{y}\in(0,1)$
   makes $\ln\hat{y}$ always negative).
   :::

10. Claimed loss for $\hat{y} = 0.9$, $y = 0$:
    - line 1: $y = 0$, so use $L = -\ln(\hat{y})$
    - line 2: $L = -\ln(0.9) \approx 0.105$
    - line 3: "tiny loss — great prediction!"

    ::: answer
    Line 1 is broken — wrong branch. $y=0$ means $L=-\ln(1-\hat{y})$, not $-\ln(\hat{y})$. Correct:
    $L=-\ln(1-0.9)=-\ln(0.1)=\ln10\approx2.303$ — a big loss, not tiny: predicting $90\%$ for class $1$
    when the truth is $0$ is a confident, costly miss.
    :::

11. Claimed softmax of scores $(2, 0)$:
    - line 1: $p_1 = \frac{2}{2 + 0}$... "division by total makes probabilities"
    - line 2: $p = (1, 0)$
    - line 3: "100% confident in class 1"

    ::: answer
    Line 1 is broken — softmax normalises **exponentials** of the scores, not the raw scores
    themselves. Correct: $p_1=\frac{e^2}{e^2+e^0}\approx\frac{7.39}{8.39}\approx0.88$, $p_2\approx0.12$
    — about $88\%$ confident, not $100\%$.
    :::

---

## Part D — Deep end

*Not fully covered yet. Attempt anyway.*

12. Softmax the scores $(1, 1)$ by hand. Then $(0, 0)$. Then $(5, 5)$. What's the pattern, and why
    does it make sense that all three agree?

    ::: answer
    All three give $(0.5, 0.5)$ — when both scores are equal, softmax is a fair coin no matter how
    big the shared number is. Move: softmax depends only on the **difference** between scores, and
    equal scores have a difference of $0$.
    :::

13. Softmax $(3, 1)$ using $e^3 \approx 20.1$, $e^1 \approx 2.7$. Compare with the lesson's answer
    for $(2, 0)$. What did you just discover about *shifting all scores by the same amount*?
    (This fact is used inside every real softmax implementation to stop $e^{big}$ overflowing.)

    ::: answer
    $p_1=\frac{20.1}{20.1+2.7}=\frac{20.1}{22.8}\approx0.88$, $p_2\approx0.12$ — same as $(2,0)$.
    Discovery: softmax is unchanged by adding a constant to every score (only the gap between scores,
    here $2$ both times, matters) — this is exactly why real implementations subtract off the max
    score first, for free, before exponentiating.
    :::

14. From the lesson's deep-end question: a network that always says $\hat{y} = 0.5$ scores 0.693
    forever. Describe a dataset where *no* network can average better than 0.693 — what would the
    relationship between inputs and labels have to be? (Module 4.1's coin knows.)

    ::: answer
    A dataset where $y$ is a coin flip with no relationship to $x$ at all — the label carries zero
    information about the input. Then no model can beat guessing $\hat{y}=0.5$ always, and the best
    achievable average loss is the coin-flip value $\ln2\approx0.693$.
    :::

15. Sketch (rough, Module 1.2 shape-zoo style) $L = -\ln(\hat{y})$ for $\hat{y}$ between 0 and 1.
    Mark where the loss is 0 and what happens as $\hat{y} \to 0$. One sentence: why is this exact
    shape the behaviour you *want* from a penalty?

    ::: answer
    The curve falls from $+\infty$ at $\hat{y}=0$ down to exactly $0$ at $\hat{y}=1$ — steep on the
    left, flattening on the right, always positive. As $\hat{y}\to0$ the loss blows up without bound.
    That's the wanted shape: confident-and-right costs almost nothing, but confident-and-wrong costs
    more and more without limit — a penalty that never goes quiet.
    :::

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
