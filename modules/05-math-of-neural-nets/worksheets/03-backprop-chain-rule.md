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

   ::: answer
   $\frac{dL}{d\hat{y}} = -\frac{1}{\hat{y}}$. At $\hat{y}=0.5$: $-2$. At $\hat{y}=0.25$: $-4$.
   :::

2. Sigmoid's derivative is $\sigma'(z) = \sigma(z)(1 - \sigma(z))$. Evaluate it at $z = 0$.
   Why can it never exceed $0.25$? *(What does Module 1.2 say about the graph of $p(1-p)$?)*

   ::: answer
   $\sigma'(0) = 0.5(1-0.5) = 0.25$. Move: $p(1-p)$ is a downward parabola (Module 1.2) with vertex
   at $p = 0.5$, peak value $0.25$ — so $\sigma'(z)$ can never exceed it.
   :::

3. ReLU's derivative: $\text{ReLU}'(-2) = \;?$, $\;\text{ReLU}'(5) = \;?$, $\;\text{ReLU}'(-0.001) = \;?$

   ::: answer
   $\text{ReLU}'(-2) = 0$, $\text{ReLU}'(5) = 1$, $\text{ReLU}'(-0.001) = 0$ — the gate only cares about the
   sign of the input, not its size.
   :::

4. Pure chain rule (Module 3.3): $L = u^2$ where $u = 3w$. Find $\frac{dL}{dw}$ at $w = 1$,
   writing it as $\frac{dL}{du} \cdot \frac{du}{dw}$ first.

   ::: answer
   $\frac{dL}{dw} = \frac{dL}{du}\cdot\frac{du}{dw} = 2u \cdot 3 = 6u = 18w$. At $w=1$: $u=3$, so $\frac{dL}{dw}=18$.
   :::

---

## Part B — Core: every gradient of the network

Use the forward values above ($\hat{y} = 0.75$, $y = 0$). Follow the lesson's seven steps; name each.

5. **Steps 1–3.** With $y = 0$ the loss is $L = -\ln(1 - \hat{y})$. Use the shortcut the lesson
   proved: $\delta_2 = \frac{\partial L}{\partial z_2} = \hat{y} - y$. Write its value, and one
   sentence on what its *sign* says the output should do.

   ::: answer
   $\delta_2 = \hat{y} - y = 0.75 - 0 = 0.75$. Sign: positive means $\hat{y}$ is too *high* relative to
   $y$ — gradient descent will push $z_2$ (and so $\hat{y}$) *down*.
   :::

6. **Step 4.** $\frac{\partial L}{\partial W_2} = \delta_2\, \mathbf{h}^\top$ and
   $\frac{\partial L}{\partial b_2} = \delta_2$. Compute both. Why is the gradient for $W_{2,2}$
   exactly zero? *(Look at what $h_2$ was.)*

   ::: answer
   $\frac{\partial L}{\partial W_2} = \delta_2\,\mathbf{h}^\top = 0.75\,(1,\ 0) = (0.75,\ 0)$, and
   $\frac{\partial L}{\partial b_2} = \delta_2 = 0.75$. $W_{2,2}$'s gradient is $\delta_2 \cdot h_2 = 0.75 \cdot 0 = 0$ —
   killed because the second hidden unit's activation $h_2$ is zero, not because of any local derivative.
   :::

7. **Step 5.** $\frac{\partial L}{\partial \mathbf{h}} = W_2^\top \delta_2$. Compute it (a 2-vector).

   ::: answer
   $\frac{\partial L}{\partial \mathbf{h}} = W_2^\top \delta_2 = \begin{pmatrix} 3 \\ -1 \end{pmatrix} \times 0.75 = \begin{pmatrix} 2.25 \\ -0.75 \end{pmatrix}$.
   :::

8. **Step 6.** Apply the ReLU gate: $\delta_1 = \frac{\partial L}{\partial \mathbf{h}} \odot \text{ReLU}'(\mathbf{z}_1)$,
   with $\mathbf{z}_1 = (1, 0)$ and the convention $\text{ReLU}'(0) = 0$. Compute $\delta_1$.

   ::: answer
   $\text{ReLU}'(\mathbf{z}_1) = (1, 0)$ (gate open for unit 1, shut for unit 2). Move: elementwise multiply —
   $\delta_1 = \begin{pmatrix} 2.25 \\ -0.75 \end{pmatrix} \odot \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2.25 \\ 0 \end{pmatrix}$.
   :::

9. **Step 7.** $\frac{\partial L}{\partial W_1} = \delta_1 \mathbf{x}^\top$ (column times row — a
   $2{\times}2$ matrix) and $\frac{\partial L}{\partial \mathbf{b}_1} = \delta_1$. Compute both.

   ::: answer
   $\frac{\partial L}{\partial W_1} = \delta_1 \mathbf{x}^\top = \begin{pmatrix} 2.25 \\ 0 \end{pmatrix}(2,\ 1) = \begin{pmatrix} 4.5 & 2.25 \\ 0 & 0 \end{pmatrix}$,
   and $\frac{\partial L}{\partial \mathbf{b}_1} = \delta_1 = \begin{pmatrix} 2.25 \\ 0 \end{pmatrix}$.
   :::

10. Circle every gradient entry that came out **zero**, and for each, say *which* forward-pass fact
    killed it. (There are two different killers in this network.)

    ::: answer
    Zeros: $W_{2,2}$'s gradient, plus the whole bottom row of $\frac{\partial L}{\partial W_1}$ and the
    second entry of $\frac{\partial L}{\partial \mathbf{b}_1}$. Killer 1 (forward-value kill): $h_2 = 0$
    zeroes $W_{2,2}$'s gradient by direct multiplication in the outer product $\delta_2 \mathbf{h}^\top$ —
    no gate involved. Killer 2 (gate kill): the second entry of $\mathbf{z}_1$ is $0$, so
    $\text{ReLU}'=0$ there by convention — the gate blocks backward flow entirely for that unit,
    zeroing the second entry of $\delta_1$ and everything downstream of it.
    :::

---

## Part C — Spot the error

Each derivation contains exactly one broken move. Circle it; name the rule it broke.

11. Claimed output-layer gradient ($\hat{y} = 0.75$, $y = 0$):
    - line 1: $\delta_2 = y - \hat{y} = -0.75$
    - line 2: $\frac{\partial L}{\partial b_2} = -0.75$
    - line 3: "so gradient descent will *increase* $b_2$"

    ::: answer
    Line 1 is broken: the shortcut is $\delta_2 = \hat{y} - y$, not $y - \hat{y}$ — they flipped the sign.
    Correct: $\delta_2 = 0.75 - 0 = 0.75$, so $\frac{\partial L}{\partial b_2} = 0.75$ (positive), and
    gradient descent moves $b_2 \leftarrow b_2 - \text{lr}\cdot 0.75$, i.e. $b_2$ *decreases*, not increases.
    :::

12. Claimed hidden-layer gradient, given $\frac{\partial L}{\partial \mathbf{h}} = \begin{pmatrix} 2.25 \\ -0.75 \end{pmatrix}$, $\mathbf{z}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$:
    - line 1: $\delta_1 = \begin{pmatrix} 2.25 \\ -0.75 \end{pmatrix}$ "(ReLU is basically the identity, skip the gate)"
    - line 2: $\frac{\partial L}{\partial \mathbf{b}_1} = \begin{pmatrix} 2.25 \\ -0.75 \end{pmatrix}$

    ::: answer
    Line 1 is broken: ReLU is not the identity — it's a gate. Since $\mathbf{z}_1 = (1, 0)$,
    $\text{ReLU}'(\mathbf{z}_1) = (1, 0)$, so
    $\delta_1 = \begin{pmatrix} 2.25 \\ -0.75 \end{pmatrix} \odot \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2.25 \\ 0 \end{pmatrix}$,
    and $\frac{\partial L}{\partial \mathbf{b}_1} = \begin{pmatrix} 2.25 \\ 0 \end{pmatrix}$ too — the second
    entry must be $0$, not $-0.75$.
    :::

13. Claimed sigmoid step: "$\sigma'(z_2) = \sigma(z_2)(1 - \sigma(z_2)) = 1(1 - 1) = 0$, because I
    plugged in $z_2 = 1$... so no gradient flows and the network can't learn." Two errors hide in
    one line — find at least one.

    ::: answer
    Error 1 (arithmetic): $\sigma(1) \neq 1$ — $\sigma(1) \approx 0.731$, so
    $\sigma'(1) \approx 0.731(0.269) \approx 0.197$, nowhere near zero. (Sigmoid only *approaches* $1$ as
    $z\to\infty$; it never reaches it at $z=1$.) Error 2 (conceptual): this network never needs
    $\sigma'(z_2)$ on its own — the lesson's shortcut $\delta_2 = \hat{y}-y$ already folds the sigmoid
    derivative into the loss derivative, sidestepping this exact multiplication.
    :::

---

## Part D — Deep end

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

14. **Prove the beautiful shortcut** for the $y = 1$ case. Starting from
    $L = -\ln(\hat{y})$ and $\hat{y} = \sigma(z_2)$, chain
    $\frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z_2}$ symbolically
    and simplify to $\hat{y} - 1$. Every move is Module 0 algebra — name them.

    ::: rephrase
    "Prove" here just means: show that $\delta_2 = \hat{y}-y$ *falls out* of the chain rule — you're
    not inventing anything. You already own both pieces: $\frac{\partial L}{\partial \hat{y}}$ is
    problem 1's rule, and $\frac{\partial \hat{y}}{\partial z_2}$ is sigmoid's derivative from problem 2.
    This is problem 4 (pure chain rule) wearing symbols: multiply the two local derivatives, then the
    only work left is Module 0 algebra — cancel, then distribute a minus sign.
    :::

    ::: hint
    Write both local derivatives side by side first: $\frac{\partial L}{\partial \hat{y}} = -\frac{1}{\hat{y}}$
    (problem 1) and $\frac{\partial \hat{y}}{\partial z_2} = \hat{y}(1-\hat{y})$ (sigmoid's derivative).
    :::

    ::: hint
    Chain rule = multiply them. Once you write $-\frac{1}{\hat{y}} \cdot \hat{y}(1-\hat{y})$, look for a
    $\frac{\hat{y}}{\hat{y}}$ you can cancel.
    :::

    ::: steps
    1. **Write the two local derivatives.** $\frac{\partial L}{\partial \hat{y}} = -\frac{1}{\hat{y}}, \quad \frac{\partial \hat{y}}{\partial z_2} = \hat{y}(1-\hat{y})$
    2. **Chain rule — multiply them.** $\frac{\partial L}{\partial z_2} = -\frac{1}{\hat{y}} \cdot \hat{y}(1-\hat{y})$
    3. **Cancel the $\hat{y}$'s** (a $\frac{\hat{y}}{\hat{y}}=1$ move). $= -(1-\hat{y})$
    4. **Distribute the minus sign.** $= \hat{y} - 1 = \hat{y} - y$ (since $y=1$) — the same shortcut as the $y=0$ case.
    :::

15. **Gradient check** (Module 3.1, the nudge). Your answer to problem 9 says
    $\frac{\partial L}{\partial W_{1,11}} = 4.5$ (top-left entry). Predict: if $W_{1,11}$ went up by
    $0.01$ and everything was recomputed, roughly what would the new loss be? (Old loss:
    $-\ln(0.25) \approx 1.386$.)

    ::: rephrase
    The gradient $4.5$ is a *promise*: "the loss changes about $4.5$ units for every $1$ unit I move
    $W_{1,11}$" — exactly the nudge idea from Module 3.1. So a tiny step $\Delta w = 0.01$ changes the loss
    by roughly $\text{gradient} \times \Delta w$. It's the slope-reads-rise move: $\text{rise} = \text{slope} \times \text{run}$.
    You don't rerun the whole network — you trust the gradient for one small step.
    :::

    ::: hint
    Local-linear approximation: $\Delta L \approx \text{gradient} \times \Delta w$. Compute that, then
    add it onto the old loss.
    :::

    ::: steps
    1. **Local-linear step: $\Delta L \approx \text{gradient} \times \Delta w$.** $\Delta L \approx 4.5 \times 0.01 = 0.045$
    2. **Add to the old loss.** $L_{\text{new}} \approx 1.386 + 0.045 = 1.431$
    :::

16. Suppose an input landed where BOTH hidden neurons were off. Write down $\frac{\partial L}{\partial W_1}$
    without computing anything. What would happen if *every* training input did this? (This failure
    has a name — "dying ReLU" — and now you can explain it at a dinner party.)

    ::: rephrase
    "Both neurons off" means both pre-activations in $\mathbf{z}_1$ are $\le 0$, so **both ReLU gates are
    shut** (Step 6 — the gate). You don't need any numbers: just trace what a shut gate does to the
    backward flow. In problems 8 and 10, one shut gate zeroed *one* entry of $\delta_1$ and everything
    downstream of it. Now both are shut — so ask what that forces $\frac{\partial L}{\partial W_1} = \delta_1 \mathbf{x}^\top$ to be.
    :::

    ::: hint
    The gate multiplies each entry of $\frac{\partial L}{\partial \mathbf{h}}$ by $\text{ReLU}'(\mathbf{z}_1)$.
    Both gates shut $\Rightarrow \text{ReLU}'(\mathbf{z}_1) = (0, 0)$. What is $\delta_1$ then, no matter what
    $\frac{\partial L}{\partial \mathbf{h}}$ was?
    :::

    ::: hint
    With $\delta_1 = \mathbf{0}$, the outer product $\delta_1 \mathbf{x}^\top$ can only be one thing. Then ask:
    if *every* input shuts the gates, when does $W_1$ ever get a nonzero update?
    :::

    ::: steps
    1. **Both gates shut $\Rightarrow \text{ReLU}'(\mathbf{z}_1) = (0,0)$.** $\delta_1 = \frac{\partial L}{\partial \mathbf{h}} \odot \begin{pmatrix} 0 \\ 0 \end{pmatrix} = \mathbf{0}$ (regardless of $\frac{\partial L}{\partial \mathbf{h}}$)
    2. **Outer product with a zero $\delta_1$.** $\frac{\partial L}{\partial W_1} = \delta_1 \mathbf{x}^\top = \mathbf{0}$ (the full $2{\times}2$ zero matrix); likewise $\frac{\partial L}{\partial \mathbf{b}_1} = \delta_1 = \mathbf{0}$
    3. **Every input $\Rightarrow$ no signal, ever.** With gradient $\mathbf{0}$ on every example, $W_1$ and $\mathbf{b}_1$ never update again — the unit is permanently dead ("dying ReLU"), since gradient descent has zero signal to move it back to positive $z$.
    :::

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
