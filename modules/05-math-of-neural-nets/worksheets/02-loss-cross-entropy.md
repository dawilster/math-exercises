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

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

12. Softmax the scores $(1, 1)$ by hand. Then $(0, 0)$. Then $(5, 5)$. What's the pattern, and why
    does it make sense that all three agree?

    ::: rephrase
    You're just running the softmax formula from the lesson three times by hand. For a pair of
    scores $(a,b)$, softmax is $\left(\frac{e^a}{e^a+e^b},\,\frac{e^b}{e^a+e^b}\right)$ — same
    machine that turned $(2,0)$ into $(0.88,0.12)$. "What's the pattern" just means: do all three,
    then look at what the answers have in common. First move: write the formula and plug $(1,1)$ in.
    :::

    ::: hint
    In each of the three pairs the two scores are **equal**. When $a=b$, the two numerators
    $e^a$ and $e^b$ are the same. What does that force each probability to be?
    :::

    ::: hint
    Softmax reacts only to the **difference** between the scores, not their size. Equal scores
    have a difference of $0$ — so $(1,1)$, $(0,0)$ and $(5,5)$ can't tell themselves apart.
    :::

    ::: steps
    1. **Plug $(1,1)$ into the formula.** $\left(\frac{e^1}{e^1+e^1},\frac{e^1}{e^1+e^1}\right)=\left(\frac{e}{2e},\frac{e}{2e}\right)=(0.5,0.5)$
    2. **Repeat for $(0,0)$ and $(5,5)$.** each is $\frac{e^k}{e^k+e^k}=\frac{e^k}{2e^k}=0.5$, so both also give $(0.5,0.5)$
    3. **Read off the pattern.** all three agree at $(0.5,0.5)$ — equal scores → a fair coin, because softmax sees only the difference $a-b$, here $0$ every time.
    :::

13. Softmax $(3, 1)$ using $e^3 \approx 20.1$, $e^1 \approx 2.7$. Compare with the lesson's answer
    for $(2, 0)$. What did you just discover about *shifting all scores by the same amount*?
    (This fact is used inside every real softmax implementation to stop $e^{big}$ overflowing.)

    ::: rephrase
    Same softmax machine as problem 12, but now the two scores differ. Run $(3,1)$ through
    $\left(\frac{e^a}{e^a+e^b},\frac{e^b}{e^a+e^b}\right)$ using the $e$-values you're handed,
    then set your answer next to the lesson's $(2,0)\to(0.88,0.12)$ and ask what $(3,1)$ and
    $(2,0)$ have in common. First move: plug $(3,1)$ in.
    :::

    ::: hint
    Substitute $e^3\approx20.1$ and $e^1\approx2.7$ into the formula and get the two probabilities.
    :::

    ::: hint
    Compare the **gap** between the scores: $(3,1)$ has gap $2$, and so does $(2,0)$. Notice
    $(3,1)$ is just $(2,0)$ with $1$ added to both scores — what did adding that constant change?
    :::

    ::: steps
    1. **Plug $(3,1)$ into softmax.** $p_1=\frac{20.1}{20.1+2.7}=\frac{20.1}{22.8}\approx0.88,\quad p_2\approx0.12$
    2. **Set it beside $(2,0)$.** $(2,0)$ gave $(0.88,0.12)$ too — identical, even though every score is bigger by $1$.
    3. **Name the discovery.** adding the same constant to every score leaves softmax unchanged (only the gap between scores matters) — so real code subtracts the max score first, shrinking the exponents for free before $e^{(\cdot)}$ can overflow.
    :::

14. From the lesson's deep-end question: a network that always says $\hat{y} = 0.5$ scores 0.693
    forever. Describe a dataset where *no* network can average better than 0.693 — what would the
    relationship between inputs and labels have to be? (Module 4.1's coin knows.)

    ::: rephrase
    Flip the usual question around. Normally the network is the weak part; here you're asked to
    invent a **dataset** so nasty that the always-$0.5$ guesser is genuinely the best anyone can do.
    Ask: when is looking at $x$ completely useless for predicting $y$? That's Module 4.1's coin —
    the label is a fair flip that ignores the input entirely.
    :::

    ::: hint
    A better-than-$0.5$ prediction has to come from somewhere: $x$ would have to tell you something
    about $y$. So build a dataset where $x$ tells you **nothing** — what's the relationship between
    input and label then?
    :::

    ::: steps
    1. **Make the label independent of the input.** let $y$ be a fair coin flip with no connection to $x$ at all — the input carries zero information about the label.
    2. **See why $0.5$ is unbeatable.** with nothing in $x$ to lean on, any honest prediction is $\hat{y}=0.5$, giving the coin-flip loss $-\ln(0.5)=\ln2\approx0.693$ on every example — so the best achievable average loss is exactly $0.693$.
    :::

15. Sketch (rough, Module 1.2 shape-zoo style) $L = -\ln(\hat{y})$ for $\hat{y}$ between 0 and 1.
    Mark where the loss is 0 and what happens as $\hat{y} \to 0$. One sentence: why is this exact
    shape the behaviour you *want* from a penalty?

    ::: rephrase
    You don't need a plotting tool — just find the shape by testing a few points, like the
    Module 1.2 shape-zoo. This is the $y=1$ branch of cross-entropy you've been computing all
    worksheet ($-\ln(0.9)$, $-\ln(0.5)$, $-\ln(0.1)$ from Part A); those three numbers already
    *are* three heights on this curve. First move: plot those points and connect them.
    :::

    ::: hint
    Use Part A's values as anchor points: $\hat{y}=0.9\to0.105$ (low), $\hat{y}=0.5\to0.693$,
    $\hat{y}=0.1\to2.303$ (high). What's the height at $\hat{y}=1$, where the prediction is perfect?
    :::

    ::: hint
    Now push $\hat{y}$ toward $0$ — a confident but totally wrong prediction. $-\ln$ of a tinier and
    tinier number does what? (Recall the $\ln(0)$ trap from the lesson.)
    :::

    ::: steps
    1. **Anchor with Part A's points.** $(0.9,0.105),\,(0.5,0.693),\,(0.1,2.303)$ — the curve rides through these, steep on the left, gentle on the right.
    2. **Mark the zero.** at $\hat{y}=1$, $L=-\ln(1)=0$ — the loss touches $0$ exactly when the prediction is certain-and-right.
    3. **Mark the blow-up.** as $\hat{y}\to0$, $-\ln(\hat{y})\to+\infty$ — the loss climbs without any ceiling.
    4. **Say why it's the shape you want.** confident-and-right costs almost nothing, but confident-and-wrong costs more and more without limit — a penalty that never goes quiet, exactly the loud teaching signal MSE lacks.
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
