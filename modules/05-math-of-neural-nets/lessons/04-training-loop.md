# 5.4 — The Training Loop: Watch Your Math Learn

*≤5 min read. Then the notebook — today has THE moment.*

## Why this matters (the real reason)

You can run a network (5.1), score it (5.2), and get every gradient (5.3). One piece remains, and
you built it in Module 3.5: **gradient descent** — step each weight a little way downhill. Wire the
four pieces into a loop and something extraordinary happens: the numbers *learn*. Today you train a
network built from nothing but your own Modules 0–4 math, and watch it carve a decision boundary
through data. This is the actual algorithm behind GPT and stable diffusion — smaller, not different.

## The one big idea

**Training = four moves, repeated:**

$$\text{forward} \;\to\; \text{loss} \;\to\; \text{backward} \;\to\; \text{step}$$

| Move | What happens | Built in |
|---|---|---|
| forward | run $\mathbf{x}$ through the layers → $\hat{y}$ | 5.1 (Modules 1.4, 2.5) |
| loss | score $\hat{y}$ against truth $y$ | 5.2 (Module 4.5) |
| backward | chain rule → every $\frac{\partial L}{\partial w}$ | 5.3 (Module 3.3) |
| step | $w \leftarrow w - \eta \frac{\partial L}{\partial w}$ | Module 3.5 |

$\eta$ (eta) is the **learning rate** — step size. Each trip through the loop is one **step**;
a full pass over the dataset is an **epoch**. Loop until the loss stops falling.

## One full training step, by hand

Take 5.3's gradients and step with $\eta = 0.1$. **The move (Module 3.5): new = old − η × gradient.**

**Step the output layer:**
$$W_2 \leftarrow \begin{pmatrix} -1 & 2 \end{pmatrix} - 0.1\begin{pmatrix} 0 & -0.5 \end{pmatrix} = \begin{pmatrix} -1 & 2.05 \end{pmatrix}, \qquad b_2 \leftarrow -2 - 0.1(-0.5) = -1.95$$

**Step the hidden layer:**
$$W_1 \leftarrow \begin{pmatrix} 0.5 & -1 \\ 1 & 0.5 \end{pmatrix} - 0.1\begin{pmatrix} 0 & 0 \\ -1 & -2 \end{pmatrix} = \begin{pmatrix} 0.5 & -1 \\ 1.1 & 0.7 \end{pmatrix}, \qquad \mathbf{b}_1 \leftarrow \begin{pmatrix} 0.5 \\ -0.9 \end{pmatrix}$$

Note the minus signs doing their job: gradient $-0.5$ on $W_{2,2}$ → weight goes **up** by 0.05.
Downhill means *against* the gradient.

**Now rerun the forward pass (5.1's moves) with the new weights:**
$$\mathbf{z}_1 = \begin{pmatrix} -1 \\ 1.6 \end{pmatrix} \to \mathbf{h} = \begin{pmatrix} 0 \\ 1.6 \end{pmatrix} \to z_2 = 2.05(1.6) - 1.95 = 1.33 \to \hat{y} = \sigma(1.33) \approx 0.79$$

**Re-score (5.2's move):** $L = -\ln(0.79) \approx 0.235$.

**The loss fell from 0.693 to 0.235 in one step.** The prediction moved from a 0.5 shrug to 0.79 —
toward the truth $y = 1$. Nobody told it how. The gradients *are* the how. That's learning,
and you just did every arithmetic operation of it by hand.

## The Python connection

The whole loop — every line is a lesson you've done:

```python
for step in range(1000):
    h, y_hat = forward(X)                    # 5.1
    loss = cross_entropy(y_hat, y)           # 5.2
    grads = backward(X, y, h, y_hat)         # 5.3
    for w, g in zip(params, grads):          # zip pairs each weight with its gradient
        w -= lr * g                          # Module 3.5  (-= means: subtract in place)
```

In the notebook this trains on a 2D dataset no straight line can split — and you'll *watch* the
decision boundary bend itself around the data, epoch by epoch.

## The classic traps

- **Learning rate too big** → steps overshoot the valley; the loss bounces or explodes (you saw
  this exact failure on parabolas in Module 3.5). **Too small** → training crawls. It's the
  most-tuned number in deep learning.
- **Adding the gradient instead of subtracting** → loss rises smoothly. If training makes things
  *steadily worse*, check that sign first.
- **Stale gradients.** Gradients must be recomputed from a *fresh* forward pass every step —
  yesterday's slopes describe a hill you're no longer standing on.

> **Deep-end question to hold in your head during the worksheet:**
> our hand-trace stepped using ONE training example. Real training averages gradients over a
> **batch** of examples (Module 0.6's $\Sigma$, then divide by $n$ — Module 4.2's mean). What does
> averaging buy you? What might one loud, weird example do to a step taken alone?

**Now: worksheet `04-training-loop`, then notebook `04-training-loop` — the payoff. Photograph the worksheet into `scans/inbox/`.**
