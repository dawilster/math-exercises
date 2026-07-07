# Boss Worksheet — Module 5: The Math of a Neural Net

**The rules (same as every boss, but this one is the last of the core curriculum):**

- **Cold.** No lessons, no notes, no notebooks open. Just you, a pen, and the math.
- **On paper.** Every step written and NAMED — the names are the marks.
- Photograph everything into `scans/inbox/` when done.
- Cheat card allowed (below) — values only, no methods.

# ≥ 85% = READY FOR FAST.AI

*That is not a module gate. That is the finish line of the core curriculum. Everything past this
point — fast.ai, computer vision, LLMs — is these same moves on bigger matrices.*

Cheat card: $\;\sigma(1) \approx 0.73,\; \sigma(1)(1-\sigma(1)) \approx 0.20,\; -\ln(0.73) \approx 0.315,\; \frac{1}{0.73} \approx 1.37$

---

## Section 1 — Forward pass (hand-trace, every move named)

The boss network — 2 inputs, 2 hidden ReLU neurons, 1 sigmoid output:

$$\mathbf{x} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad
W_1 = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}, \quad
\mathbf{b}_1 = \begin{pmatrix} -2 \\ 1 \end{pmatrix}, \quad
W_2 = \begin{pmatrix} 1 & 2 \end{pmatrix}, \quad
b_2 = -1$$

1. Compute $\mathbf{z}_1 = W_1\mathbf{x} + \mathbf{b}_1$, showing both dot products.

   ::: answer
   $\mathbf{z}_1 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$ — row 1: $2(1) + (-1)(1) = 1$, $+(-2) = -1$;
   row 2: $-1(1) + 1(1) = 0$, $+1 = 1$. Move: matrix–vector multiply, a dot product per row
   (Module 2.5), then add the bias shift (Module 1.3).
   :::

2. Compute $\mathbf{h} = \text{ReLU}(\mathbf{z}_1)$.

   ::: answer
   $\mathbf{h} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ — ReLU zeroes the negative entry and passes
   the positive one through unchanged. Move: $\max(0, z)$ applied entrywise (Module 1.5).
   :::

3. Compute $z_2 = W_2\mathbf{h} + b_2$ and $\hat{y} = \sigma(z_2)$ (cheat card).

   ::: answer
   $z_2 = 1(0) + 2(1) - 1 = 1$; $\hat{y} = \sigma(1) \approx 0.73$ (cheat card). Move: dot product
   plus bias shift, then squash through sigmoid (Module 1.5).
   :::

4. Write the shape of each of: $\mathbf{x}$, $W_1$, $\mathbf{z}_1$, $W_2$, $z_2$.

   ::: answer
   $\mathbf{x}$: $2{\times}1$; $W_1$: $2{\times}2$; $\mathbf{z}_1$: $2{\times}1$; $W_2$: $1{\times}2$;
   $z_2$: $1{\times}1$ (a scalar). Move: Module 2.5's shape rule $(m{\times}n)(n{\times}1) \to (m{\times}1)$,
   checked at each multiply.
   :::

---

## Section 2 — Loss

The true label is $y = 1$.

5. Write the correct branch of cross-entropy for $y = 1$, substitute your $\hat{y}$, and evaluate
   (cheat card).

   ::: answer
   $y=1 \Rightarrow L = -\ln\hat{y} = -\ln(0.73) \approx 0.315$ (cheat card). Move: pick the $y=1$
   branch of cross-entropy — negative log-likelihood of the probability given to the right answer
   (Module 4.5).
   :::

6. One sentence: why would MSE have been the wrong choice of loss here?

   ::: answer
   Because MSE's gradient goes flat exactly when the sigmoid output is confidently wrong — the
   moment training most needs a loud gradient — while cross-entropy's gradient stays loud
   ($\hat{y}-y$, always proportional to the error) no matter how confidently the network is wrong.
   :::

7. Softmax check: convert the two class scores $(0, 0)$ into probabilities. Show the formula, not
   just the answer.

   ::: answer
   $p_i = \dfrac{e^{s_i}}{\sum_j e^{s_j}}$. Here $p_1 = p_2 = \dfrac{e^0}{e^0+e^0} = \dfrac{1}{2} = 0.5$
   each. Move: softmax (Module 0.5's $e^x$ makes scores positive, Module 0.6's $\Sigma$ normalises them).
   :::

---

## Section 3 — Backprop (the summit: every chain-rule step NAMED)

Derive $\frac{\partial L}{\partial W_2}$ for the boss network. Required steps, each with its name
written beside it:

8. $\frac{\partial L}{\partial \hat{y}}$ — from $L = -\ln(\hat{y})$. Name the derivative rule and
   evaluate (cheat card).

   ::: answer
   $\dfrac{\partial L}{\partial \hat{y}} = -\dfrac{1}{\hat{y}} = -\dfrac{1}{0.73} \approx -1.37$
   (cheat card). Name: derivative of $-\ln u$ is $-\frac{1}{u}$ (Module 3.2).
   :::

9. $\frac{\partial \hat{y}}{\partial z_2}$ — sigmoid's derivative. Write the formula and evaluate
   (cheat card).

   ::: answer
   $\sigma'(z) = \sigma(z)\big(1-\sigma(z)\big)$, so
   $\dfrac{\partial \hat{y}}{\partial z_2} = \sigma(1)\big(1-\sigma(1)\big) \approx 0.20$ (cheat card).
   Name: sigmoid's derivative.
   :::

10. Chain them: $\frac{\partial L}{\partial z_2} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z_2}$.
    Name the rule that lets you multiply. Then verify your number against the shortcut
    $\hat{y} - y$ — if they disagree, one of your steps has a sign or arithmetic slip: find it.

    ::: answer
    $\dfrac{\partial L}{\partial z_2} = (-1.37)(0.20) \approx -0.27$. Name: chain rule (Module 3.3).
    Shortcut: $\hat{y}-y = 0.73-1 = -0.27$ — matches (any tiny residue is just cheat-card rounding,
    not a slip). Call this $\delta_2 = -0.27$.
    :::

11. $\frac{\partial L}{\partial W_2} = \frac{\partial L}{\partial z_2}\,\mathbf{h}^\top$ — evaluate
    (a $1{\times}2$ result), and state in one sentence *why* the input $\mathbf{h}$ shows up here.

    ::: answer
    $\dfrac{\partial L}{\partial W_2} = \delta_2\,\mathbf{h}^\top = -0.27 \times \begin{pmatrix}0 & 1\end{pmatrix} = \begin{pmatrix}0 & -0.27\end{pmatrix}$.
    $\mathbf{h}$ shows up because $z_2 = W_2\mathbf{h}+b_2$ is linear in $W_2$ — nudging a weight
    moves $z_2$ by exactly the input that weight multiplies (Module 3.2, derivative of a linear function).
    :::

12. One entry of your answer is exactly zero. Which forward-pass event caused it, and what does it
    mean for that weight this step?

    ::: answer
    The first entry, $0$. It's zero because $h_1 = 0$ — ReLU switched off hidden neuron 1 (its
    pre-activation $z_{1,1}=-1$ was negative). No gradient can flow to $W_{2,1}$ through a dead
    neuron, so that weight doesn't move this step — it learns nothing from this example.
    :::

13. **(Stretch — attempt for full marks.)** Continue one layer down: compute
    $\frac{\partial L}{\partial \mathbf{h}} = W_2^\top \frac{\partial L}{\partial z_2}$, apply the
    ReLU gate to get $\delta_1$, and give $\frac{\partial L}{\partial \mathbf{b}_1}$.

    ::: answer
    $\dfrac{\partial L}{\partial \mathbf{h}} = W_2^\top \delta_2 = \begin{pmatrix}1\\2\end{pmatrix}(-0.27) = \begin{pmatrix}-0.27\\-0.54\end{pmatrix}$.
    ReLU gate: $\text{ReLU}'(\mathbf{z}_1) = \begin{pmatrix}0\\1\end{pmatrix}$ (since $\mathbf{z}_1=(-1,1)$),
    so $\delta_1 = \begin{pmatrix}-0.27\\-0.54\end{pmatrix} \odot \begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}0\\-0.54\end{pmatrix}$.
    $\dfrac{\partial L}{\partial \mathbf{b}_1} = \delta_1 = \begin{pmatrix}0\\-0.54\end{pmatrix}$
    (bias gradient equals the upstream delta directly). Names: chain rule back through $W_2$, then
    ReLU's derivative acting as a gate.
    :::

---

## Section 4 — Convolution

14. Compute the full $3{\times}3$ feature map of $I * K$, showing the dot product working for at
    least three entries:

    $$I = \begin{pmatrix}
    0 & 0 & 0 & 1 & 1 \\
    0 & 0 & 0 & 1 & 1 \\
    0 & 0 & 0 & 1 & 1 \\
    0 & 0 & 0 & 1 & 1 \\
    0 & 0 & 0 & 1 & 1
    \end{pmatrix}
    \qquad
    K = \begin{pmatrix}
    1 & 0 & -1 \\
    1 & 0 & -1 \\
    1 & 0 & -1
    \end{pmatrix}$$

    ::: answer
    $$I * K = \begin{pmatrix} 0 & -3 & -3 \\ 0 & -3 & -3 \\ 0 & -3 & -3 \end{pmatrix}$$
    Every row is identical, so one dot product per column position covers all three rows.
    Left patch (columns 1–3, all $0$s): $3(0{\cdot}1 + 0{\cdot}0 + 0{\cdot}(-1)) = 0$.
    Middle patch (columns 2–4, each row $0,0,1$): $3(0{\cdot}1 + 0{\cdot}0 + 1{\cdot}(-1)) = -3$.
    Right patch (columns 3–5, each row $0,1,1$): $3(0{\cdot}1 + 1{\cdot}0 + 1{\cdot}(-1)) = -3$.
    Move: dot product of kernel and patch (Module 2.3), repeated at every slide position.
    :::

15. Your nonzero entries are negative. What is the sign telling you about this image's edge,
    compared to the positive response in the lesson?

    ::: answer
    Negative instead of positive because this image is the mirror of the lesson's: dark ($0$) on
    the left, bright ($1$) on the right — brightness *rises* left to right instead of dropping.
    The kernel computes (left column) $-$ (right column), so a rise gives a negative number of the
    same size ($3$) as the lesson's positive drop. Same edge, opposite direction.
    :::

16. Why is the output $3{\times}3$ and not $5{\times}5$? State the rule.

    ::: answer
    Output size $= n - k + 1 = 5 - 3 + 1 = 3$ each way — a $3{\times}3$ kernel only has 3 valid
    positions to sit on a 5-wide image without hanging off the edge.
    :::

---

## Section 5 — Explain every line

Below is a complete numpy training loop — the same species as your notebook's. `X` is a
$200{\times}2$ matrix of data points, `y` is a $200{\times}1$ column of 0/1 labels.

**For each numbered line, write: (a) the math it performs, in your own words, and (b) which module
taught it.** One short phrase each is enough. Full marks needs all 14.

```python
for step in range(500):
    Z1 = X @ W1.T + b1                                            # (1)
    H  = np.maximum(0, Z1)                                        # (2)
    z2 = H @ W2.T + b2                                            # (3)
    y_hat = 1 / (1 + np.exp(-z2))                                 # (4)
    loss = -np.mean(y * np.log(y_hat) + (1-y) * np.log(1-y_hat))  # (5)
    d_z2 = (y_hat - y) / len(X)                                   # (6)
    d_W2 = d_z2.T @ H                                             # (7)
    d_b2 = d_z2.sum(axis=0)                                       # (8)
    d_H  = d_z2 @ W2                                              # (9)
    d_Z1 = d_H * (Z1 > 0)                                         # (10)
    d_W1 = d_Z1.T @ X                                             # (11)
    d_b1 = d_Z1.sum(axis=0)                                       # (12)
    W1 -= lr * d_W1;  b1 -= lr * d_b1                             # (13)
    W2 -= lr * d_W2;  b2 -= lr * d_b2                             # (14)
```

17. Annotate lines (1)–(14).

    ::: answer
    (1) Matrix multiply + bias shift, first layer — $Z_1 = XW_1^\top + \mathbf{b}_1$ (5.1, Module 2.5 + 1.3).
    (2) ReLU activation, entrywise $\max(0,\cdot)$ (5.1, Module 1.5).
    (3) Matrix multiply + bias shift, second layer (5.1, Module 2.5 + 1.3).
    (4) Sigmoid activation, squashes to a probability (5.1, Module 1.5).
    (5) Cross-entropy loss, averaged over the batch (5.2, Module 4.5; the mean is Module 0.6's $\Sigma$ then Module 4.2's divide-by-$n$).
    (6) The collapsed loss+sigmoid gradient $\hat{y}-y$, divided by $n$ for the batch mean (5.3's chain-rule collapse, Module 4.2).
    (7) Gradient into $W_2$ — outer product of the upstream error and the input $H$ (5.3, Module 3.2).
    (8) Gradient into $b_2$ — upstream error summed over the batch (5.3, Module 0.6's $\Sigma$).
    (9) Error backed up through $W_2$ into the hidden layer (5.3, chain rule/Module 3.3).
    (10) ReLU gate applied — zeroes gradient wherever the forward pass was off (5.3).
    (11) Gradient into $W_1$ — outer product of the gated error and the input $X$ (5.3, Module 3.2).
    (12) Gradient into $b_1$ — gated error summed over the batch (5.3, Module 0.6's $\Sigma$).
    (13) Gradient descent step, hidden layer: $w \leftarrow w - \eta\,\partial L/\partial w$ (Module 3.5).
    (14) Gradient descent step, output layer — same move as (13) (Module 3.5).
    :::

18. Final question of the core curriculum. In two or three sentences, to an imaginary friend who
    thinks AI is magic: what is a neural network, and how does it learn? You are now qualified to
    answer.

    ::: answer
    A neural network is just composed functions — matrix multiply, add a bias, squash through a
    nonlinearity, repeat (Module 1.4's $g(f(x))$ with bigger matrices). It learns by measuring how
    wrong its guess was with a loss, using the chain rule to work out how each individual weight
    contributed to that wrongness, then nudging every weight a small step in the direction that
    makes the loss smaller (gradient descent). No magic — just dot products, derivatives, and
    repetition, done thousands of times.
    :::

---

*Scan it in. If the marking comes back ≥85%: Module 5 is beaten, the core curriculum is complete,
and the next session starts with a Wonder Interlude of your choosing — then fast.ai.
Your math built a thing that learns. It was never magic. It was moves.*
