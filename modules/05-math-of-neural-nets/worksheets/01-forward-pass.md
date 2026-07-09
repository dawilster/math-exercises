# Worksheet 5.1 — The Forward Pass

*Pen and paper. Name every move as you go ("dot product row 1", "add bias", "ReLU").
Write shapes next to every vector and matrix — shape-checking is a professional habit, not a chore.
Photograph into `scans/inbox/` when done.*

Cheat card (fine to use): $\;\sigma(-2) \approx 0.12,\; \sigma(-1) \approx 0.27,\; \sigma(0) = 0.5,\; \sigma(1) \approx 0.73,\; \sigma(2) \approx 0.88$

---

## Part A — Warm-up: the three moves, separately

1. Dot product (Module 2.3): $\begin{pmatrix} 2 & -1 \end{pmatrix} \cdot \begin{pmatrix} 3 \\ 4 \end{pmatrix} = \;?$

   ::: answer
   $2(3) + (-1)(4) = 6 - 4 = 2$ — move: dot product (pairwise multiply, then sum).
   :::

2. Matrix × vector (Module 2.5): $\begin{pmatrix} 1 & 2 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 3 \\ 1 \end{pmatrix} = \;?$ — and what shape comes out?

   ::: answer
   $\begin{pmatrix} 1(3) + 2(1) \\ 0(3) + (-1)(1) \end{pmatrix} = \begin{pmatrix} 5 \\ -1 \end{pmatrix}$ — move: one dot product per row.
   Shape: $2 \times 1$ (a 2-vector) — rows of the matrix, columns of the vector.
   :::

3. ReLU each entry: $\text{ReLU}\begin{pmatrix} -3 \\ 0.5 \\ 0 \end{pmatrix} = \;?$

   ::: answer
   $\begin{pmatrix} 0 \\ 0.5 \\ 0 \end{pmatrix}$ — move: ReLU clamps negatives to 0, leaves non-negatives untouched.
   :::

4. From the cheat card: $\sigma(2) = \;?$ and $\sigma(-2) = \;?$ What do the two values add up to? (Not a coincidence — sigmoid is symmetric.)

   ::: answer
   $\sigma(2) \approx 0.88$, $\sigma(-2) \approx 0.12$. They add to $1.00$ — move: sigmoid symmetry,
   $\sigma(x) + \sigma(-x) = 1$.
   :::

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

   ::: answer
   Row 1: $1(2) + (-2)(1) = 2 - 2 = 0$, $+1 = 1$. Row 2: $0.5(2) + 1(1) = 1 + 1 = 2$, $+(-2) = 0$.
   $\mathbf{z}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ — move: dot product per row, then add the bias vector.
   :::

6. Compute $\mathbf{h} = \text{ReLU}(\mathbf{z}_1)$. Which hidden neuron is off?

   ::: answer
   $\mathbf{h} = \text{ReLU}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ — move: clamp negatives/zero.
   Neuron 2 is off ($z=0 \Rightarrow$ output $0$); neuron 1 fires at $1$.
   :::

7. Compute $z_2 = W_2\mathbf{h} + b_2$, then $\hat{y} = \sigma(z_2)$ from the cheat card.

   ::: answer
   $z_2 = 3(1) + (-1)(0) + (-2) = 3 - 0 - 2 = 1$. $\hat{y} = \sigma(1) \approx 0.73$ — move: weighted sum
   then activation (output layer).
   :::

8. Same network, new input $\mathbf{x} = \begin{pmatrix} 0 \\ 2 \end{pmatrix}$ — trace it again.
   Both hidden neurons switch off. What is $\hat{y}$ now, and which single parameter is deciding
   the network's whole answer?

   ::: answer
   $\mathbf{z}_1 = \begin{pmatrix} 1(0) + (-2)(2) + 1 \\ 0.5(0) + 1(2) - 2 \end{pmatrix} = \begin{pmatrix} -3 \\ 0 \end{pmatrix}$,
   so $\mathbf{h} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$ — both neurons off. Then $z_2 = 3(0) + (-1)(0) - 2 = -2$,
   $\hat{y} = \sigma(-2) \approx 0.12$. Move: with $\mathbf{h} = \mathbf{0}$, the whole output collapses to
   $\sigma(b_2)$ — the output bias $b_2$ alone is deciding the answer.
   :::

---

## Part C — Spot the error

Each trace contains exactly one broken move. Circle the broken line and name what went wrong.

9. Claimed trace of $W_1 = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, $\mathbf{x} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$, $\mathbf{b}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, ReLU:
   - line 1: $W_1\mathbf{x} = \begin{pmatrix} 1(1) + 3(2) \\ 2(1) + 4(2) \end{pmatrix} = \begin{pmatrix} 7 \\ 10 \end{pmatrix}$
   - line 2: $\mathbf{z}_1 = \begin{pmatrix} 8 \\ 11 \end{pmatrix}$
   - line 3: $\mathbf{h} = \begin{pmatrix} 8 \\ 11 \end{pmatrix}$

   ::: answer
   Line 1 is broken: it mixed up rows and columns, computing $W_1^{\mathsf T}\mathbf{x}$ instead of $W_1\mathbf{x}$
   (row 1 should be $1(1) + 2(2) = 5$, row 2 should be $3(1) + 4(2) = 11$, giving $\begin{pmatrix}5\\11\end{pmatrix}$,
   not $\begin{pmatrix}7\\10\end{pmatrix}$). Correct trace: $\mathbf{z}_1 = \begin{pmatrix}6\\12\end{pmatrix}$,
   $\mathbf{h} = \begin{pmatrix}6\\12\end{pmatrix}$ (ReLU leaves both unchanged since both are positive).
   :::

10. Claimed trace of $W = \begin{pmatrix} 2 & -3 \end{pmatrix}$, $\mathbf{h} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $b = 4$, sigmoid output:
    - line 1: $W\mathbf{h} = 2 - 3 = -1$
    - line 2: $\hat{y} = \sigma(-1) \approx 0.27$
    - line 3: $\text{final output} = 0.27 + 4 = 4.27$

    ::: answer
    Line 3 is broken: the bias must go in **before** the activation, not added on afterwards.
    Correct move: $z = W\mathbf{h} + b = -1 + 4 = 3$, then $\hat{y} = \sigma(3) \approx 0.95$ — a single
    sigmoid call, not sigmoid-then-add.
    :::

11. A friend claims: "$W$ is $3{\times}2$ and $\mathbf{x}$ is $3{\times}1$, so $W\mathbf{x}$ works and gives a $2{\times}1$ result." Two things are wrong — name both, using Module 2.5's inner/outer rule.

    ::: answer
    (1) The inner dimensions don't actually match: $W$'s inner number is its column count, $2$; $\mathbf{x}$'s
    inner number is its row count, $3$. $2 \neq 3$, so $W\mathbf{x}$ is undefined as stated.
    (2) Even if it worked, the result shape is the two *outer* numbers — $W$'s rows ($3$) by $\mathbf{x}$'s
    columns ($1$) — so it would be $3{\times}1$, not $2{\times}1$.
    :::

---

## Part D — Deep end

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

12. **The collapse.** Take Part B's network but DELETE both activations (no ReLU, no sigmoid).
    Compute the single matrix $M = W_2 W_1$ and the single bias $c = W_2\mathbf{b}_1 + b_2$, then verify
    $M\mathbf{x} + c$ gives the same answer as tracing the two layers on $\mathbf{x} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
    You've just proven: *without activations, "deep" is a lie — any stack of linear layers is one layer.*

    ::: rephrase
    "Delete both activations" = run the pipeline as pure linear moves: layer 1 is just
    $W_1\mathbf{x} + \mathbf{b}_1$, layer 2 is just $W_2(\cdots) + b_2$, no ReLU or sigmoid in
    between. The claim to check: those two linear layers equal **one** linear layer — a single
    matrix $M$ and single bias $c$. You find $M$ and $c$ by substituting layer 1 *into* layer 2
    and collecting terms, then plug in $\mathbf{x}=\begin{pmatrix}2\\1\end{pmatrix}$ to confirm
    both routes give the same number. This is the lesson's "forgetting the activation" trap, made
    concrete.
    :::

    ::: hint
    Write layer 2 fed by layer 1 with nothing in between:
    $z_2 = W_2\big(W_1\mathbf{x} + \mathbf{b}_1\big) + b_2$. Now you need to reshape this into the
    form $M\mathbf{x} + c$.
    :::

    ::: hint
    Distribute $W_2$ across the bracket: $W_2 W_1\mathbf{x} + W_2\mathbf{b}_1 + b_2$. The part
    riding on $\mathbf{x}$ is your $M = W_2 W_1$; everything with no $\mathbf{x}$ is your
    $c = W_2\mathbf{b}_1 + b_2$.
    :::

    ::: steps
    1. **Write both layers, activations removed.** $z_2 = W_2\big(W_1\mathbf{x} + \mathbf{b}_1\big) + b_2$
    2. **Distribute $W_2$, group the $\mathbf{x}$-term.** $z_2 = (W_2 W_1)\mathbf{x} + (W_2\mathbf{b}_1 + b_2)$
    3. **Compute $M = W_2 W_1$** (each row of $W_2$ dot the columns of $W_1$). $M = \begin{pmatrix} 3(1) + (-1)(0.5) & 3(-2) + (-1)(1) \end{pmatrix} = \begin{pmatrix} 2.5 & -7 \end{pmatrix}$
    4. **Compute $c = W_2\mathbf{b}_1 + b_2$.** $c = \big(3(1) + (-1)(-2)\big) + (-2) = 5 - 2 = 3$
    5. **Check on $\mathbf{x}=\begin{pmatrix}2\\1\end{pmatrix}$.** $M\mathbf{x} + c = 2.5(2) + (-7)(1) + 3 = 5 - 7 + 3 = 1$ — matches the two-layer trace ($\mathbf{z}_1 = \begin{pmatrix}1\\0\end{pmatrix}$ no ReLU, then $z_2 = 3(1) - 1(0) - 2 = 1$). Move: collapsing two linear layers into one matrix and one bias.
    :::

13. **Wake the dead neuron.** In the lesson's network, hidden neuron 1 computes
    $\text{ReLU}(0.5 x_1 - x_2 + 0.5)$. Find any input $(x_1, x_2)$ that switches it ON.
    Then describe the *set* of all such inputs — what shape does the boundary
    $0.5x_1 - x_2 + 0.5 = 0$ make in the plane? (Module 1.2 knows.)

    ::: rephrase
    ReLU passes a positive number straight through and clamps anything $\le 0$ to zero. So this
    neuron is "ON" (nonzero output) exactly when the *inside*, $0.5x_1 - x_2 + 0.5$, is
    **positive**. "Switch it on" therefore just means: find any $(x_1, x_2)$ making that
    expression $> 0$ — try the easiest point you can think of. Then "the set of all such inputs"
    is a whole region of the plane, and its edge is where the inside equals $0$ — a Module 1.2
    line equation.
    :::

    ::: hint
    You don't need ReLU's output value, only its sign switch: it fires when its input is strictly
    positive. So solve the single condition $0.5x_1 - x_2 + 0.5 > 0$. Test the origin $(0,0)$.
    :::

    ::: hint
    For the boundary shape, set the inside to zero: $0.5x_1 - x_2 + 0.5 = 0$. Rearrange it into
    $x_2 = m x_1 + b$ form — that $y = mx + b$ pattern from Module 1.2 is a straight line.
    :::

    ::: steps
    1. **ReLU on $\Rightarrow$ input positive.** require $0.5x_1 - x_2 + 0.5 > 0$
    2. **Test the origin.** $0.5(0) - 0 + 0.5 = 0.5 > 0$ — ON, outputs $0.5$
    3. **Find the boundary** (set the inside to $0$). $0.5x_1 - x_2 + 0.5 = 0$
    4. **Rearrange to slope-intercept.** $x_2 = 0.5x_1 + 0.5$ — a **straight line** (slope $0.5$, intercept $0.5$); "ON" is the half-plane below it. The neuron is a half-plane detector.
    :::

14. A network goes $3 \to 4 \to 2$. Write the shape of every object in the forward pass:
    $\mathbf{x}$, $W_1$, $\mathbf{b}_1$, $\mathbf{h}$, $W_2$, $\mathbf{b}_2$, output. How many numbers
    (weights + biases) does this network own in total?

    ::: rephrase
    "$3 \to 4 \to 2$" is the neuron count at each stage: $3$ inputs, a hidden layer of $4$
    neurons, $2$ outputs. Each arrow is one layer — "multiply, shift, squash." You just need the
    shape (rows $\times$ cols) of every object as data flows through, plus a final headcount of
    individual numbers. The one rule that decides every weight matrix is Part C problem 11 /
    Module 2.5: a layer turning an (in)-vector into an (out)-vector has weight shape
    $(\text{out}) \times (\text{in})$.
    :::

    ::: hint
    Start with the first layer: it maps a $3$-vector to a $4$-vector, so its weight is
    $(\text{out}) \times (\text{in}) = 4 \times 3$, and it has one bias per output neuron
    (a $4$-vector). Apply the same reasoning to the $4 \to 2$ layer.
    :::

    ::: hint
    To count numbers: a matrix holds $\text{rows} \times \text{cols}$ of them, a bias holds one
    per output neuron. Add up $W_1, \mathbf{b}_1, W_2, \mathbf{b}_2$ (inputs and activations own no
    numbers).
    :::

    ::: steps
    1. **Input shape.** $\mathbf{x}: 3{\times}1$
    2. **First layer maps $3 \to 4$** (weight is $(\text{out}){\times}(\text{in})$). $W_1: 4{\times}3, \quad \mathbf{b}_1: 4{\times}1, \quad \mathbf{h}: 4{\times}1$
    3. **Second layer maps $4 \to 2$.** $W_2: 2{\times}4, \quad \mathbf{b}_2: 2{\times}1, \quad \text{output}: 2{\times}1$
    4. **Count every number** (rows$\times$cols per matrix, one per bias). $W_1(12) + \mathbf{b}_1(4) + W_2(8) + \mathbf{b}_2(2) = 26$
    :::

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
