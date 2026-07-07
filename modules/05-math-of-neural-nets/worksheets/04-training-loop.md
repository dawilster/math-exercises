# Worksheet 5.4 — One Training Step, All the Way Through

*Pen and paper. This sheet chains worksheets 5.1 → 5.2 → 5.3 into one full loop iteration —
name each of the four moves (forward / loss / backward / step) as you enter it.
Photograph into `scans/inbox/` when done.*

Cheat card: $\;\sigma(-2.15) \approx 0.10,\; \sigma(0) = 0.5,\; -\ln(0.9) \approx 0.105,\; -\ln(0.25) \approx 1.386$

---

## Part A — Warm-up: the step move alone (Module 3.5 reps)

For each, apply $w \leftarrow w - \eta \, g$:

1. $w = 4$, gradient $g = 2$, $\eta = 0.1$. New $w$?

2. $w = 4$, gradient $g = -2$, $\eta = 0.1$. New $w$? (Negative gradient → weight moves which way?)

3. $w = 1$, $g = 0$, any $\eta$. New $w$? What does a zero gradient *mean*, in one sentence?

4. On $L = w^2$ (so $g = 2w$), start at $w = 2$ with $\eta = 0.1$ and take two steps, recomputing
   $g$ between them. Is $w$ heading where you'd expect?

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

6. **Forward move (5.1):** trace $\mathbf{x} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$ through the
   *updated* network. Show $\mathbf{z}_1$, $\mathbf{h}$, $z_2$, and $\hat{y}$ (cheat card).

7. **Loss move (5.2):** the truth is $y = 0$. Old loss was $-\ln(0.25) \approx 1.386$. Compute the
   new loss.

8. In one sentence each: (a) what happened to the loss, (b) what happened to the prediction,
   (c) who told the weights which way to move?

---

## Part C — Spot the error

Each training log contains exactly one broken move. Circle it; name what broke.

9. - line 1: `w = w + lr * grad` "step the weight"
   - line 2: (100 steps later) "loss went from 0.7 to 3.9 — smoothly uphill the whole way"
   - line 3: "conclusion: my network is too small"

10. - line 1: step 1 — forward, loss 0.9, backward → gradients, step. Fine.
    - line 2: step 2 — "to save compute, reuse step 1's gradients"; step again
    - line 3: step 3 — reuse them again; loss now *rising*

11. On $L = w^2$ starting at $w = 2$ with $\eta = 1.1$ (gradient $g = 2w$):
    - line 1: step → $w = 2 - 1.1(4) = -2.4$
    - line 2: step → $w = -2.4 - 1.1(-4.8) = 2.88$
    - line 3: "$|w|$ grows every step... gradient descent is broken"

---

## Part D — Deep end

12. **The averaging question.** With a batch of $n$ examples, the training loss is
    $\bar{L} = \frac{1}{n}\sum_{i=1}^{n} L_i$ (Module 0.6 + 4.2). One example in the batch is
    mislabelled junk with a huge loud gradient. Compare stepping on the average vs stepping on the
    junk example alone — which loop is steadier, and why? (Module 4.4's noise-in-sampling instincts apply.)

13. **After your Part B step, both hidden neurons are off** for this input, so the network's answer
    is $\sigma(b_2)$ — a constant. For a dataset where the answer is *always* "no" ($y = 0$ for
    everything), is this constant network actually bad? For what kind of dataset would it be a disaster?

14. **Learning-rate schedule.** Trainers often shrink $\eta$ over time, e.g. $\eta_t = 0.5 \times 0.9^t$
    (Module 0.5's exponential decay). Give one reason big-early is good and one reason small-late
    is good. (Think: rolling a marble into a narrow valley.)

15. When should the loop *stop*? Propose two different stopping rules and one risk for each.

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
