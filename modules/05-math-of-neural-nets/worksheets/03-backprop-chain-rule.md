# Worksheet 5.3 — Backprop, by Hand

*Pen and paper — the summit worksheet. NAME EVERY STEP ("chain rule", "ReLU gate", "outer product
with the input"). The names are the marks. Photograph into `scans/inbox/` when done.*

*You'll need your worksheet 5.1 Part B forward pass. If it's not handy:
$\mathbf{x} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$, $W_2 = \begin{pmatrix} 3 & -1 \end{pmatrix}$,
$\mathbf{z}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $\mathbf{h} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$,
$z_2 = 1$, $\hat{y} \approx 0.73$ — round it to $0.75$ for clean hand arithmetic. True label: $y = 0$.*

---

## Part A — Warm-up: the local derivatives (Module 3.2 reps)

1. $L = -\ln(\hat{y})$. What is $\frac{dL}{d\hat{y}}$ at $\hat{y} = 0.5$? At $\hat{y} = 0.25$?

2. Sigmoid's derivative is $\sigma'(z) = \sigma(z)(1 - \sigma(z))$. Evaluate it at $z = 0$.
   Why can it never exceed $0.25$? *(What does Module 1.2 say about the graph of $p(1-p)$?)*

3. ReLU's derivative: $\text{ReLU}'(-2) = \;?$, $\;\text{ReLU}'(5) = \;?$, $\;\text{ReLU}'(-0.001) = \;?$

4. Pure chain rule (Module 3.3): $L = u^2$ where $u = 3w$. Find $\frac{dL}{dw}$ at $w = 1$,
   writing it as $\frac{dL}{du} \cdot \frac{du}{dw}$ first.

---

## Part B — Core: every gradient of the network

Use the forward values above ($\hat{y} = 0.75$, $y = 0$). Follow the lesson's seven steps; name each.

5. **Steps 1–3.** With $y = 0$ the loss is $L = -\ln(1 - \hat{y})$. Use the shortcut the lesson
   proved: $\delta_2 = \frac{\partial L}{\partial z_2} = \hat{y} - y$. Write its value, and one
   sentence on what its *sign* says the output should do.

6. **Step 4.** $\frac{\partial L}{\partial W_2} = \delta_2\, \mathbf{h}^\top$ and
   $\frac{\partial L}{\partial b_2} = \delta_2$. Compute both. Why is the gradient for $W_{2,2}$
   exactly zero? *(Look at what $h_2$ was.)*

7. **Step 5.** $\frac{\partial L}{\partial \mathbf{h}} = W_2^\top \delta_2$. Compute it (a 2-vector).

8. **Step 6.** Apply the ReLU gate: $\delta_1 = \frac{\partial L}{\partial \mathbf{h}} \odot \text{ReLU}'(\mathbf{z}_1)$,
   with $\mathbf{z}_1 = (1, 0)$ and the convention $\text{ReLU}'(0) = 0$. Compute $\delta_1$.

9. **Step 7.** $\frac{\partial L}{\partial W_1} = \delta_1 \mathbf{x}^\top$ (column times row — a
   $2{\times}2$ matrix) and $\frac{\partial L}{\partial \mathbf{b}_1} = \delta_1$. Compute both.

10. Circle every gradient entry that came out **zero**, and for each, say *which* forward-pass fact
    killed it. (There are two different killers in this network.)

---

## Part C — Spot the error

Each derivation contains exactly one broken move. Circle it; name the rule it broke.

11. Claimed output-layer gradient ($\hat{y} = 0.75$, $y = 0$):
    - line 1: $\delta_2 = y - \hat{y} = -0.75$
    - line 2: $\frac{\partial L}{\partial b_2} = -0.75$
    - line 3: "so gradient descent will *increase* $b_2$"

12. Claimed hidden-layer gradient, given $\frac{\partial L}{\partial \mathbf{h}} = \begin{pmatrix} 2.25 \\ -0.75 \end{pmatrix}$, $\mathbf{z}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$:
    - line 1: $\delta_1 = \begin{pmatrix} 2.25 \\ -0.75 \end{pmatrix}$ "(ReLU is basically the identity, skip the gate)"
    - line 2: $\frac{\partial L}{\partial \mathbf{b}_1} = \begin{pmatrix} 2.25 \\ -0.75 \end{pmatrix}$

13. Claimed sigmoid step: "$\sigma'(z_2) = \sigma(z_2)(1 - \sigma(z_2)) = 1(1 - 1) = 0$, because I
    plugged in $z_2 = 1$... so no gradient flows and the network can't learn." Two errors hide in
    one line — find at least one.

---

## Part D — Deep end

14. **Prove the beautiful shortcut** for the $y = 1$ case. Starting from
    $L = -\ln(\hat{y})$ and $\hat{y} = \sigma(z_2)$, chain
    $\frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z_2}$ symbolically
    and simplify to $\hat{y} - 1$. Every move is Module 0 algebra — name them.

15. **Gradient check** (Module 3.1, the nudge). Your answer to problem 9 says
    $\frac{\partial L}{\partial W_{1,11}} = 4.5$ (top-left entry). Predict: if $W_{1,11}$ went up by
    $0.01$ and everything was recomputed, roughly what would the new loss be? (Old loss:
    $-\ln(0.25) \approx 1.386$.)

16. Suppose an input landed where BOTH hidden neurons were off. Write down $\frac{\partial L}{\partial W_1}$
    without computing anything. What would happen if *every* training input did this? (This failure
    has a name — "dying ReLU" — and now you can explain it at a dinner party.)

---

## Part E — Python check (at the computer, after the pen work)

17. Verify Part B numerically — the finite-difference judge:

```python
import numpy as np

x  = np.array([2.0, 1.0]);  y = 0.0
W1 = np.array([[1.0, -2.0], [0.5, 1.0]]);  b1 = np.array([1.0, -2.0])
W2 = np.array([3.0, -1.0]);  b2 = -2.0

def loss(W1, b1, W2, b2):
    h = np.maximum(0, W1 @ x + b1)
    y_hat = 1 / (1 + np.exp(-(W2 @ h + b2)))
    return -(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))

base = loss(W1, b1, W2, b2)
W1_nudged = W1.copy();  W1_nudged[0, 0] += 0.001    # nudge one weight (Module 3.1)
print((loss(W1_nudged, b1, W2, b2) - base) / 0.001)  # ≈ your answer to problem 9, top-left
```

Nudge two more parameters of your choice and check them against Part B. Tick ✓ each match.
*(Tiny mismatches like 4.39 vs 4.5 are the $0.73 \to 0.75$ rounding — the notebook uses exact values.)*

> **Bonus thought:** this check needed TWO forward passes per weight. Our network has 9 parameters;
> GPT-class models have billions. Now say, in one sentence, why backprop's one-sweep-backwards
> design is the reason deep learning is computationally possible.
