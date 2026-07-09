# Worksheet 5.4 — One Training Step, All the Way Through

*Pen and paper. This sheet chains worksheets 5.1 → 5.2 → 5.3 into one full loop iteration —
name each of the four moves (forward / loss / backward / step) as you enter it.
Photograph into `scans/inbox/` when done.*

Cheat card: $\;\sigma(-2.15) \approx 0.10,\; \sigma(0) = 0.5,\; -\ln(0.9) \approx 0.105,\; -\ln(0.25) \approx 1.386$

---

## Part A — Warm-up: the step move alone (Module 3.5 reps)

For each, apply $w \leftarrow w - \eta \, g$:

1. $w = 4$, gradient $g = 2$, $\eta = 0.1$. New $w$?

   ::: answer
   $w = 3.8$ — move: $w \leftarrow w - \eta g = 4 - 0.1(2) = 3.8$.
   :::

2. $w = 4$, gradient $g = -2$, $\eta = 0.1$. New $w$? (Negative gradient → weight moves which way?)

   ::: answer
   $w = 4.2$ — move: $4 - 0.1(-2) = 4 + 0.2$. A negative gradient means loss falls as $w$
   *increases*, so the step pushes $w$ **up**.
   :::

3. $w = 1$, $g = 0$, any $\eta$. New $w$? What does a zero gradient *mean*, in one sentence?

   ::: answer
   $w = 1$ — unchanged, since $\eta \times 0 = 0$ no matter what $\eta$ is. A zero gradient means
   the loss is (locally) flat here — you're sitting at a minimum, maximum, or saddle point.
   :::

4. On $L = w^2$ (so $g = 2w$), start at $w = 2$ with $\eta = 0.1$ and take two steps, recomputing
   $g$ between them. Is $w$ heading where you'd expect?

   ::: answer
   Step 1: $g = 2(2) = 4$, $w = 2 - 0.1(4) = 1.6$. Step 2: $g = 2(1.6) = 3.2$, $w = 1.6 - 0.1(3.2) = 1.28$.
   Yes — $w$ is heading toward $0$, the minimum of $L = w^2$, exactly as expected.
   :::

---

## Part B — Core: a full step of the real network

Gather your worksheet 5.3 results (with the $0.75$ rounding):
$\frac{\partial L}{\partial W_2} = \begin{pmatrix} 0.75 & 0 \end{pmatrix}$,
$\frac{\partial L}{\partial b_2} = 0.75$,
$\frac{\partial L}{\partial W_1} = \begin{pmatrix} 4.5 & 2.25 \\ 0 & 0 \end{pmatrix}$,
$\frac{\partial L}{\partial \mathbf{b}_1} = \begin{pmatrix} 2.25 \\ 0 \end{pmatrix}$.
Old parameters: $W_1 = \begin{pmatrix} 1 & -2 \\ 0.5 & 1 \end{pmatrix}$, $\mathbf{b}_1 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$, $W_2 = \begin{pmatrix} 3 & -1 \end{pmatrix}$, $b_2 = -2$. Learning rate $\eta = 0.2$.

5. **Step move:** update all four parameter blocks. (Most entries barely move or don't move at all —
   which ones, and why? Your problem-10 answer from worksheet 5.3 already knows.)

   ::: answer
   $\theta \leftarrow \theta - \eta \nabla\theta$ applied to each block:
   $W_1 = \begin{pmatrix} 0.1 & -2.45 \\ 0.5 & 1 \end{pmatrix}$,
   $\mathbf{b}_1 = \begin{pmatrix} 0.55 \\ -2 \end{pmatrix}$,
   $W_2 = \begin{pmatrix} 2.85 & -1 \end{pmatrix}$, $b_2 = -2.15$.
   The bottom row of $W_1$, the second entry of $\mathbf{b}_1$, and the second entry of $W_2$
   don't move at all — their gradients were $0$, because the second hidden neuron was dead
   (ReLU output $0$) for this input, so no error signal flowed back through it.
   :::

6. **Forward move (5.1):** trace $\mathbf{x} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$ through the
   *updated* network. Show $\mathbf{z}_1$, $\mathbf{h}$, $z_2$, and $\hat{y}$ (cheat card).

   ::: answer
   $\mathbf{z}_1 = W_1\mathbf{x} + \mathbf{b}_1 = \begin{pmatrix} 0.1(2) - 2.45(1) \\ 0.5(2) + 1(1) \end{pmatrix} + \begin{pmatrix} 0.55 \\ -2 \end{pmatrix} = \begin{pmatrix} -1.7 \\ 0 \end{pmatrix}$.
   $\mathbf{h} = \mathrm{ReLU}(\mathbf{z}_1) = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$ — both neurons off.
   $z_2 = W_2\mathbf{h} + b_2 = 0 + 0 - 2.15 = -2.15$.
   $\hat{y} = \sigma(-2.15) \approx 0.10$ (cheat card).
   :::

7. **Loss move (5.2):** the truth is $y = 0$. Old loss was $-\ln(0.25) \approx 1.386$. Compute the
   new loss.

   ::: answer
   For $y = 0$, loss $= -\ln(1 - \hat{y})$. New: $-\ln(1 - 0.10) = -\ln(0.9) \approx 0.105$
   (cheat card). Move: plug the new $\hat{y}$ from problem 6 into the same loss formula —
   loss fell from $1.386$ to $\approx 0.105$.
   :::

8. In one sentence each: (a) what happened to the loss, (b) what happened to the prediction,
   (c) who told the weights which way to move?

   ::: answer
   (a) It dropped sharply, from $\approx 1.386$ to $\approx 0.105$.
   (b) The prediction moved from $\hat{y} = 0.75$ (confidently, wrongly "yes") to $\hat{y} \approx 0.10$
   (confidently, correctly "no"). (c) The backward pass (chain rule) — it turned the loss's error
   into a gradient for every weight, and the step move used that gradient to decide which way to nudge each one.
   :::

---

## Part C — Spot the error

Each training log contains exactly one broken move. Circle it; name what broke.

9. - line 1: `w = w + lr * grad` "step the weight"
   - line 2: (100 steps later) "loss went from 0.7 to 3.9 — smoothly uphill the whole way"
   - line 3: "conclusion: my network is too small"

   ::: answer
   Line 1 is broken: it should be `w = w - lr * grad`. Adding the gradient climbs *uphill*
   (gradient ascent), which is exactly why the loss rose smoothly instead of falling. The
   network size was never the problem — the step's sign was.
   :::

10. - line 1: step 1 — forward, loss 0.9, backward → gradients, step. Fine.
    - line 2: step 2 — "to save compute, reuse step 1's gradients"; step again
    - line 3: step 3 — reuse them again; loss now *rising*

    ::: answer
    Line 2 is broken. A gradient is only valid at the parameters it was computed from — once you
    step, $w$ has moved, so the old gradient no longer points the right way. Skipping the
    forward/backward recompute means later steps aren't descending the *current* loss surface,
    which is why the loss eventually rises.
    :::

11. On $L = w^2$ starting at $w = 2$ with $\eta = 1.1$ (gradient $g = 2w$):
    - line 1: step → $w = 2 - 1.1(4) = -2.4$
    - line 2: step → $w = -2.4 - 1.1(-4.8) = 2.88$
    - line 3: "$|w|$ grows every step... gradient descent is broken"

    ::: answer
    Lines 1–2 are correct arithmetic — nothing computational is broken. Line 3's *conclusion* is
    the broken move: it isn't gradient descent that's broken, it's $\eta = 1.1$ that's too big for
    this curve's steepness. Each step multiplies $w$ by $(1 - 2\eta) = -1.2$, and $|-1.2| > 1$, so
    the steps overshoot further each time and diverge. Fix: shrink $\eta$ (need $\eta < 1$ here),
    not "abandon gradient descent."
    :::

---

## Part D — Deep end

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

12. **The averaging question.** With a batch of $n$ examples, the training loss is
    $\bar{L} = \frac{1}{n}\sum_{i=1}^{n} L_i$ (Module 0.6 + 4.2). One example in the batch is
    mislabelled junk with a huge loud gradient. Compare stepping on the average vs stepping on the
    junk example alone — which loop is steadier, and why? (Module 4.4's noise-in-sampling instincts apply.)

    ::: rephrase
    "Steadier" means smaller, less erratic steps. Picture the batch as $n$ sensible examples plus
    one junk one screaming a huge gradient. Two recipes: **(A)** average all $n$ gradients, then
    take one step; **(B)** step on the junk example's gradient alone. The real question is: how
    much can that one loud example yank the weights in each recipe? Tie it to problem 11 — a step
    that's too big overshoots.
    :::

    ::: hint
    Write down what "step on the average" does to the junk gradient specifically: the $\frac{1}{n}$
    out front of $\bar{L} = \frac{1}{n}\sum_i L_i$ lands on *every* example's gradient, junk included.
    :::

    ::: hint
    A gradient's size sets the step's size (the step move is $\eta \times g$). So compare the junk
    example's influence when it's one voice out of $n$ versus when it's the *only* voice.
    :::

    ::: steps
    1. **Write the batch step.** the junk term enters averaged: $\frac{1}{n}\, g_{\text{junk}}$
    2. **Compare the lone step.** stepping on junk alone uses the full $g_{\text{junk}}$ — that's $n\times$ the influence
    3. **Name the consequence.** the lone step's oversized gradient → a large, erratic jump (problem 11's overshoot), while the average dilutes junk by $n$ → **stepping on the average is steadier**
    :::

13. **After your Part B step, both hidden neurons are off** for this input, so the network's answer
    is $\sigma(b_2)$ — a constant. For a dataset where the answer is *always* "no" ($y = 0$ for
    everything), is this constant network actually bad? For what kind of dataset would it be a disaster?

    ::: rephrase
    Two questions bundled. First: the network now ignores its input entirely and always outputs
    $\sigma(-2.15) \approx 0.10$ (problem 6). Is $0.10$ a good answer? — but good *for what*? If the
    truth is always $y = 0$, then always guessing $\approx 0$ might be fine — check the loss.
    Second: invent a dataset where "always $0.10$" is terrible. Reuse the loss formula from
    problem 7 / lesson 5.2.
    :::

    ::: hint
    For the always-"no" dataset, score the constant $\hat{y} \approx 0.10$ against $y = 0$ — you
    already computed this exact number in problem 7.
    :::

    ::: hint
    For the disaster case, ask what a fixed output does when a true label is $y = 1$. Plug
    $\hat{y} = 0.10$ into the $y = 1$ loss, $-\ln(\hat{y})$, and see what it costs.
    :::

    ::: steps
    1. **Score the constant on the all-"no" data.** every $y = 0$, so loss $= -\ln(1 - 0.10) = -\ln(0.9) \approx 0.105$ per example — low, so **not bad**
    2. **Break it: let some labels be $y = 1$.** a constant network can't tell inputs apart, so it still emits $\hat{y} \approx 0.10$ on a true "yes"
    3. **Price the mistake.** for $y = 1$, loss $= -\ln(0.10) \approx 2.3$ on every positive case — a disaster on rare-positive data (e.g. rare-disease screening)
    :::

14. **Learning-rate schedule.** Trainers often shrink $\eta$ over time, e.g. $\eta_t = 0.5 \times 0.9^t$
    (Module 0.5's exponential decay). Give one reason big-early is good and one reason small-late
    is good. (Think: rolling a marble into a narrow valley.)

    ::: rephrase
    You're arguing for a design, not solving. Take the marble analogy literally: rolling toward the
    bottom of a valley. *Early* = the marble is far up the outer slope; *late* = it's near the
    bottom of a narrow groove. Ask what step size you'd want in each spot. Problem 11 already showed
    what a too-big step does near the bottom.
    :::

    ::: hint
    Early on, the weights are far from the minimum. What's the downside of a *tiny* step $\eta$ when
    you still have a long way to travel?
    :::

    ::: hint
    Late on, you're close to the bottom of a narrow valley. Recall problem 11: what does a step
    that's too big do right near the minimum?
    :::

    ::: steps
    1. **Big-early reason.** far from the minimum → a big $\eta$ covers ground fast, rolling the marble quickly down the outer slope instead of crawling
    2. **Small-late reason.** near the minimum → a big $\eta$ overshoots and bounces or diverges (problem 11's failure mode); shrinking $\eta$ lets the marble settle into the valley floor instead of leaping over it
    :::

15. When should the loop *stop*? Propose two different stopping rules and one risk for each.

    ::: rephrase
    Open-ended design — no single right answer, you're proposing. A "stopping rule" is a concrete
    condition that ends the `for step in range(...)` loop from the lesson. Think: what could you
    *watch* to know the loop is done? Give two different watchable signals, and for each, one way it
    can mislead you. The lesson's own rule was "loop until the loss stops falling."
    :::

    ::: hint
    The simplest rule needs no measurement at all — just count. What's the obvious downside of
    fixing that count in advance, before you've seen how training goes?
    :::

    ::: hint
    A smarter rule watches a number and stops when it plateaus. Which loss should you watch —
    training or a held-out set — and what makes that number unreliable?
    :::

    ::: steps
    1. **Rule 1 — fixed number of epochs.** stop after a preset count; simple, but the count is arbitrary → risks underfitting (stopped while still improving) or wasted compute / overfitting (learning long done)
    2. **Rule 2 — early stopping on validation loss.** stop once held-out loss hasn't improved for a patience window; tracks the thing you care about, but validation loss is noisy → risks stopping too soon (a random bad batch) or too late (patience set too generously)
    :::

---

## Part E — Python check (at the computer, after the pen work)

16. Verify your Part B step in numpy, then open notebook `04-training-loop` — it runs this exact
    loop hundreds of times on real 2D data and *shows* you the decision boundary learning:

```python
import numpy as np
W1 = np.array([[1.0, -2.0], [0.5, 1.0]]); b1 = np.array([1.0, -2.0])
W2 = np.array([3.0, -1.0]);               b2 = -2.0
dW1 = np.array([[4.5, 2.25], [0.0, 0.0]]); db1 = np.array([2.25, 0.0])
dW2 = np.array([0.75, 0.0]);               db2 = 0.75
lr = 0.2

W1 -= lr * dW1;  b1 -= lr * db1     # -= : update in place (Module 3.5's move)
W2 -= lr * dW2;  b2 -= lr * db2
print(W1, b1, W2, b2)               # match your problem 5?
```

Tick ✓ each block that matches.

> **Bonus thought:** our loop uses one example. The notebook averages gradients over 200 points
> every step. Find the ONE line in the notebook's `backward` that does the averaging, and write
> down which two modules it comes from.
