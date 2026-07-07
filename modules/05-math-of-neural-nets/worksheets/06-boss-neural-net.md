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

2. Compute $\mathbf{h} = \text{ReLU}(\mathbf{z}_1)$.

3. Compute $z_2 = W_2\mathbf{h} + b_2$ and $\hat{y} = \sigma(z_2)$ (cheat card).

4. Write the shape of each of: $\mathbf{x}$, $W_1$, $\mathbf{z}_1$, $W_2$, $z_2$.

---

## Section 2 — Loss

The true label is $y = 1$.

5. Write the correct branch of cross-entropy for $y = 1$, substitute your $\hat{y}$, and evaluate
   (cheat card).

6. One sentence: why would MSE have been the wrong choice of loss here?

7. Softmax check: convert the two class scores $(0, 0)$ into probabilities. Show the formula, not
   just the answer.

---

## Section 3 — Backprop (the summit: every chain-rule step NAMED)

Derive $\frac{\partial L}{\partial W_2}$ for the boss network. Required steps, each with its name
written beside it:

8. $\frac{\partial L}{\partial \hat{y}}$ — from $L = -\ln(\hat{y})$. Name the derivative rule and
   evaluate (cheat card).

9. $\frac{\partial \hat{y}}{\partial z_2}$ — sigmoid's derivative. Write the formula and evaluate
   (cheat card).

10. Chain them: $\frac{\partial L}{\partial z_2} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z_2}$.
    Name the rule that lets you multiply. Then verify your number against the shortcut
    $\hat{y} - y$ — if they disagree, one of your steps has a sign or arithmetic slip: find it.

11. $\frac{\partial L}{\partial W_2} = \frac{\partial L}{\partial z_2}\,\mathbf{h}^\top$ — evaluate
    (a $1{\times}2$ result), and state in one sentence *why* the input $\mathbf{h}$ shows up here.

12. One entry of your answer is exactly zero. Which forward-pass event caused it, and what does it
    mean for that weight this step?

13. **(Stretch — attempt for full marks.)** Continue one layer down: compute
    $\frac{\partial L}{\partial \mathbf{h}} = W_2^\top \frac{\partial L}{\partial z_2}$, apply the
    ReLU gate to get $\delta_1$, and give $\frac{\partial L}{\partial \mathbf{b}_1}$.

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

15. Your nonzero entries are negative. What is the sign telling you about this image's edge,
    compared to the positive response in the lesson?

16. Why is the output $3{\times}3$ and not $5{\times}5$? State the rule.

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

18. Final question of the core curriculum. In two or three sentences, to an imaginary friend who
    thinks AI is magic: what is a neural network, and how does it learn? You are now qualified to
    answer.

---

*Scan it in. If the marking comes back ≥85%: Module 5 is beaten, the core curriculum is complete,
and the next session starts with a Wonder Interlude of your choosing — then fast.ai.
Your math built a thing that learns. It was never magic. It was moves.*
