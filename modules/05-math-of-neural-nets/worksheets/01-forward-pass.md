# Worksheet 5.1 — The Forward Pass

*Pen and paper. Name every move as you go ("dot product row 1", "add bias", "ReLU").
Write shapes next to every vector and matrix — shape-checking is a professional habit, not a chore.
Photograph into `scans/inbox/` when done.*

Cheat card (fine to use): $\;\sigma(-2) \approx 0.12,\; \sigma(-1) \approx 0.27,\; \sigma(0) = 0.5,\; \sigma(1) \approx 0.73,\; \sigma(2) \approx 0.88$

---

## Part A — Warm-up: the three moves, separately

1. Dot product (Module 2.3): $\begin{pmatrix} 2 & -1 \end{pmatrix} \cdot \begin{pmatrix} 3 \\ 4 \end{pmatrix} = \;?$

2. Matrix × vector (Module 2.5): $\begin{pmatrix} 1 & 2 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 3 \\ 1 \end{pmatrix} = \;?$ — and what shape comes out?

3. ReLU each entry: $\text{ReLU}\begin{pmatrix} -3 \\ 0.5 \\ 0 \end{pmatrix} = \;?$

4. From the cheat card: $\sigma(2) = \;?$ and $\sigma(-2) = \;?$ What do the two values add up to? (Not a coincidence — sigmoid is symmetric.)

---

## Part B — Core: hand-trace a full network

This network appears again in worksheets 5.3 and 5.4 — your answers here get reused, so keep them.

$$\mathbf{x} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \quad
W_1 = \begin{pmatrix} 1 & -2 \\ 0.5 & 1 \end{pmatrix}, \quad
\mathbf{b}_1 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}, \quad
W_2 = \begin{pmatrix} 3 & -1 \end{pmatrix}, \quad
b_2 = -2$$

Hidden activation ReLU, output activation sigmoid.

5. Compute $\mathbf{z}_1 = W_1\mathbf{x} + \mathbf{b}_1$. Show the two dot products separately, then the bias move.

6. Compute $\mathbf{h} = \text{ReLU}(\mathbf{z}_1)$. Which hidden neuron is off?

7. Compute $z_2 = W_2\mathbf{h} + b_2$, then $\hat{y} = \sigma(z_2)$ from the cheat card.

8. Same network, new input $\mathbf{x} = \begin{pmatrix} 0 \\ 2 \end{pmatrix}$ — trace it again.
   Both hidden neurons switch off. What is $\hat{y}$ now, and which single parameter is deciding
   the network's whole answer?

---

## Part C — Spot the error

Each trace contains exactly one broken move. Circle the broken line and name what went wrong.

9. Claimed trace of $W_1 = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, $\mathbf{x} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$, $\mathbf{b}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, ReLU:
   - line 1: $W_1\mathbf{x} = \begin{pmatrix} 1(1) + 3(2) \\ 2(1) + 4(2) \end{pmatrix} = \begin{pmatrix} 7 \\ 10 \end{pmatrix}$
   - line 2: $\mathbf{z}_1 = \begin{pmatrix} 8 \\ 11 \end{pmatrix}$
   - line 3: $\mathbf{h} = \begin{pmatrix} 8 \\ 11 \end{pmatrix}$

10. Claimed trace of $W = \begin{pmatrix} 2 & -3 \end{pmatrix}$, $\mathbf{h} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $b = 4$, sigmoid output:
    - line 1: $W\mathbf{h} = 2 - 3 = -1$
    - line 2: $\hat{y} = \sigma(-1) \approx 0.27$
    - line 3: $\text{final output} = 0.27 + 4 = 4.27$

11. A friend claims: "$W$ is $3{\times}2$ and $\mathbf{x}$ is $3{\times}1$, so $W\mathbf{x}$ works and gives a $2{\times}1$ result." Two things are wrong — name both, using Module 2.5's inner/outer rule.

---

## Part D — Deep end

*Ideas we haven't formally covered. Attempt anyway — named wrong moves beat blank space.*

12. **The collapse.** Take Part B's network but DELETE both activations (no ReLU, no sigmoid).
    Compute the single matrix $M = W_2 W_1$ and the single bias $c = W_2\mathbf{b}_1 + b_2$, then verify
    $M\mathbf{x} + c$ gives the same answer as tracing the two layers on $\mathbf{x} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
    You've just proven: *without activations, "deep" is a lie — any stack of linear layers is one layer.*

13. **Wake the dead neuron.** In the lesson's network, hidden neuron 1 computes
    $\text{ReLU}(0.5 x_1 - x_2 + 0.5)$. Find any input $(x_1, x_2)$ that switches it ON.
    Then describe the *set* of all such inputs — what shape does the boundary
    $0.5x_1 - x_2 + 0.5 = 0$ make in the plane? (Module 1.2 knows.)

14. A network goes $3 \to 4 \to 2$. Write the shape of every object in the forward pass:
    $\mathbf{x}$, $W_1$, $\mathbf{b}_1$, $\mathbf{h}$, $W_2$, $\mathbf{b}_2$, output. How many numbers
    (weights + biases) does this network own in total?

---

## Part E — Python check (at the computer, after the pen work)

15. Verify your Part B trace in numpy:

```python
import numpy as np
x  = np.array([2.0, 1.0])
W1 = np.array([[1.0, -2.0], [0.5, 1.0]])
b1 = np.array([1.0, -2.0])
W2 = np.array([3.0, -1.0])
b2 = -2.0

z1 = W1 @ x + b1
h  = np.maximum(0, z1)
z2 = W2 @ h + b2
y_hat = 1 / (1 + np.exp(-z2))
print(z1, h, z2, y_hat)     # match your hand trace?
```

Tick ✓ next to each Part B line numpy agrees with.

> **Bonus thought:** change one entry of `W1` and rerun. Which downstream numbers change, and
> which survive untouched? (Backprop, coming in 5.3, is exactly this question asked in reverse.)
