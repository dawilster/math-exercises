# 5.3 — Backprop: the Chain Rule, Walking Backwards

*≤5 min read — but the slowest 5 minutes in the course. This is the summit.*

## Why this matters (the real reason)

To improve a weight, gradient descent (Module 3.5) needs $\frac{\partial L}{\partial w}$ —
"if I nudge this weight, how does the loss move?" (Module 3.1). But every weight sits inside a
pipeline: weight → layer → activation → layer → loss. Sensitivities through a pipeline **multiply** —
that's the chain rule, Module 3.3, and it's the *entire* trick. **Backpropagation is not new math.
It's the chain rule, organised so you never compute anything twice.** People pay course fees to
demystify this word. You already own every piece.

## The one big idea

The forward pass (5.1) was a pipeline:

$$\mathbf{x} \;\to\; \mathbf{z}_1 \;\to\; \mathbf{h} \;\to\; z_2 \;\to\; \hat{y} \;\to\; L$$

The chain rule says: the sensitivity of $L$ to anything upstream is **the product of the local
sensitivities along the path**. So compute sensitivities starting at $L$ and walk *backwards*,
reusing each result for the next step — one cheap sweep gives you every gradient. Backwards isn't
mysterious; it's just **not repeating yourself**.

## Hand-derive every gradient of our network

From 5.1–5.2 (keep these forward values handy — backprop feeds on them):
$\mathbf{x} = \begin{pmatrix}1\\2\end{pmatrix}$, $\mathbf{z}_1 = \begin{pmatrix}-1\\1\end{pmatrix}$, $\mathbf{h} = \begin{pmatrix}0\\1\end{pmatrix}$, $z_2 = 0$, $\hat{y} = 0.5$, $y = 1$, $L = 0.693$.

**Step 1 — loss → output (name: derivative of $-\ln$, Module 3.2).**
$L = -\ln\hat{y}$, so
$$\frac{\partial L}{\partial \hat{y}} = -\frac{1}{\hat{y}} = -\frac{1}{0.5} = -2$$

**Step 2 — output → pre-sigmoid (name: sigmoid's derivative).**
A beautiful fact worth memorising: $\;\sigma'(z) = \sigma(z)\,(1-\sigma(z))$.
$$\frac{\partial \hat{y}}{\partial z_2} = 0.5 \times 0.5 = 0.25$$

**Step 3 — chain them (name: chain rule, Module 3.3).**
$$\frac{\partial L}{\partial z_2} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z_2} = -2 \times 0.25 = -0.5$$

Pause. $-0.5$ is exactly $\hat{y} - y = 0.5 - 1$. **Not a coincidence:** cross-entropy and sigmoid
are designed partners — chained together they always collapse to
$$\frac{\partial L}{\partial z_2} = \hat{y} - y$$
*prediction minus truth.* The gradient IS the error. This is why 5.2 said cross-entropy "stays loud":
wronger prediction → bigger gradient, always. Call this $\delta_2 = -0.5$.

**Step 4 — into $W_2$ and $b_2$ (name: derivative of a linear function, Module 3.2).**
$z_2 = W_2\mathbf{h} + b_2$ — nudge a weight, and $z_2$ moves by *the input that weight multiplies*:
$$\frac{\partial L}{\partial W_2} = \delta_2 \,\mathbf{h}^\top = -0.5 \times \begin{pmatrix} 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -0.5 \end{pmatrix}, \qquad \frac{\partial L}{\partial b_2} = \delta_2 = -0.5$$

**Step 5 — back through $W_2$ into $\mathbf{h}$ (name: chain rule again, one hop deeper).**
$\mathbf{h}$'s influence on $z_2$ runs through the weights, so the error flows back *through* them:
$$\frac{\partial L}{\partial \mathbf{h}} = W_2^\top \delta_2 = \begin{pmatrix} -1 \\ 2 \end{pmatrix} \times (-0.5) = \begin{pmatrix} 0.5 \\ -1 \end{pmatrix}$$

**Step 6 — back through ReLU (name: ReLU's derivative is a gate).**
$\text{ReLU}'(z) = 1$ if $z > 0$, else $0$. Recall $\mathbf{z}_1 = (-1, 1)$: neuron 1 was off, neuron 2 on.
$$\delta_1 = \frac{\partial L}{\partial \mathbf{h}} \odot \text{ReLU}'(\mathbf{z}_1) = \begin{pmatrix} 0.5 \times 0 \\ -1 \times 1 \end{pmatrix} = \begin{pmatrix} 0 \\ -1 \end{pmatrix}$$
($\odot$ = multiply entry-by-entry.) The gradient through the switched-off neuron is **zero** —
a "dead" path learns nothing from this example. That 0 you noted in 5.1 just came home.

**Step 7 — into $W_1$ and $\mathbf{b}_1$ (name: same move as Step 4, one layer down).**
$$\frac{\partial L}{\partial W_1} = \delta_1 \mathbf{x}^\top = \begin{pmatrix} 0 \\ -1 \end{pmatrix}\begin{pmatrix} 1 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ -1 & -2 \end{pmatrix}, \qquad \frac{\partial L}{\partial \mathbf{b}_1} = \delta_1 = \begin{pmatrix} 0 \\ -1 \end{pmatrix}$$

Done. Every gradient of a working neural network, by hand, and every step was a named move you
already knew. Sanity-read the signs: $\partial L/\partial W_2 = (0, -0.5)$ means *increasing* $W_{2,2}$
*decreases* the loss — makes sense, since $h_2 = 1$ pushes the output up toward the truth $y=1$.

## The Python connection

The derivation above, verbatim:

```python
d_z2 = y_hat - y                 # Step 1–3 collapsed: prediction minus truth
d_W2 = d_z2 * h.T                # Step 4
d_b2 = d_z2
d_h  = W2.T * d_z2               # Step 5: error flows back through the weights
d_z1 = d_h * (z1 > 0)            # Step 6: (z1 > 0) is the ReLU gate — True/False acts as 1/0
d_W1 = d_z1 @ x.T                # Step 7: @ with a column times a row = outer product
d_b1 = d_z1
```

## The classic traps

- **Sign errors.** $\delta_2 = \hat{y} - y$, never $y - \hat{y}$. Flip it and gradient descent
  becomes gradient *ascent* — your loss climbs. (It's the most common bug in from-scratch nets.)
- **Forgetting the ReLU gate.** Skipping Step 6's $\odot$ sends gradient through dead neurons — silently wrong.
- **Using the wrong forward values.** The gate needs $\mathbf{z}_1$, Step 4 needs $\mathbf{h}$, Step 3 needs $\hat{y}$.
  This is why real frameworks *cache* the forward pass — and why you keep yours written down.

> **Deep-end question to hold in your head during the worksheet:**
> gradient checking: you can *verify* any of these numbers with Module 3.1 alone — nudge one weight
> by 0.001, rerun the forward pass, and watch the loss. What should $\frac{L_{\text{new}} - L_{\text{old}}}{0.001}$
> come out to for $W_{2,2}$? (The notebook does this. It's deeply satisfying.)

**Now: worksheet `03-backprop-chain-rule` — pen and paper. Photograph it into `scans/inbox/` when done.**
