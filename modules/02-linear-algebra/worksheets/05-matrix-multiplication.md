# Worksheet 2.5 — Matrix Multiplication

*Pen and paper. Shape-check in writing BEFORE every multiplication — the habit is half the marks
here and most of the value in real ML debugging. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: shapes only, no arithmetic

For each product: legal or illegal? If legal, give the result's shape. $(m\times n)(n\times p)=(m\times p)$.

1. $(2\times 3)(3\times 2)$

   ::: answer
   Legal — result shape $(2\times 2)$. Move: check inner dimensions match ($3=3$).
   :::

2. $(3\times 3)(3\times 1)$

   ::: answer
   Legal — result shape $(3\times 1)$. Move: inner dimensions match ($3=3$).
   :::

3. $(2\times 3)(2\times 3)$

   ::: answer
   Illegal — inner dimensions don't match ($3 \ne 2$). Move: shape-check $(m\times n)(n\times p)$ fails when the middle numbers differ.
   :::

4. $(1\times 4)(4\times 1)$ — and what everyday operation from 2.3 is this product secretly?

   ::: answer
   Legal — result shape $(1\times 1)$, a single number. Move: this is the **dot product** from 2.3, dressed up as a $1\times1$ matrix.
   :::

---

## Part B — Core: row · column, entry by entry

5. Compute, shape-check first, one dot product per entry:

   a. $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$

   b. $\begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 4 \\ 2 & 0 \end{pmatrix}$

   ::: answer
   a. $\begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$ — move: row of the first matrix dot column of the second, one entry at a time.

   b. $\begin{pmatrix} 2 & 8 \\ 7 & 4 \end{pmatrix}$ — same move, e.g. entry $(2,1)$: $(1,3)\cdot(1,2) = 1+6 = 7$.
   :::

6. Using your matrices from 5b: compute the product in the **other order**,
   $\begin{pmatrix} 1 & 4 \\ 2 & 0 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}$.
   Same answer? Write the moral in one sentence.

   ::: answer
   $\begin{pmatrix} 6 & 12 \\ 4 & 0 \end{pmatrix}$ — different from 5b's $\begin{pmatrix} 2 & 8 \\ 7 & 4 \end{pmatrix}$.
   Moral: matrix multiplication is not commutative — order (which machine acts first) matters, so $AB \ne BA$ in general.
   :::

7. Compute $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.
   Explain the result using the "machine that does nothing" from worksheet 2.4.

   ::: answer
   $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ — unchanged. Move: multiplying by the identity is the "do nothing" machine, same as $f(x) = x$.
   :::

8. A non-square one: $\begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 0 & 3 \end{pmatrix}$.
   Shape-check first, then compute.

   ::: answer
   Legal, shapes $(2\times 3)(3\times 2) \to (2\times 2)$. Result: $\begin{pmatrix} 1 & 7 \\ 2 & 3 \end{pmatrix}$ — move: row · column, e.g. entry $(1,2)$: $(1,0,2)\cdot(1,0,3) = 1+0+6 = 7$.
   :::

---

## Part C — Spot the error / shape diagnosis

9. "$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 5 & 12 \\ 21 & 32 \end{pmatrix}$."
   Which Python operator did this person effectively use, and which should they have used?

   ::: answer
   They used elementwise multiplication (numpy's `*`, i.e. `A * B`) — multiplying matching entries directly ($1\times5=5$, $2\times6=12$, ...). They should have used `A @ B` (or `np.matmul`), which gives $\begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$.
   :::

10. A network layer holds weights $W$ of shape $(64, 128)$. A batch of data arrives as $X$,
    shape $(32, 128)$ — 32 samples, 128 features. The code `W @ X` crashes.
    Diagnose with the shape rule. Then: `X @ ?` of what shape *would* run, and what output shape results?
    *(Hint: a matrix can be flipped over its diagonal — the transpose — turning $(64,128)$ into $(128,64)$.)*

    ::: answer
    Shape rule: $W(64,128) @ X(32,128)$ needs $128 = 32$ — fails, hence the crash.
    Move: transpose $W$ so its trailing dimension matches $X$'s features: `X @ W.T` runs, since $(32,128)@(128,64)$ is legal, giving output shape $(32, 64)$.
    :::

11. "Matrix multiplication is just a grid of dot products, and dot products don't care about order —
    so $AB = BA$." The first two claims are true. Where does the conclusion break?

    ::: answer
    Individual numbers commute ($a \cdot b = b \cdot a$), but $AB$ and $BA$ pair up *different* dot products: entry $(i,j)$ of $AB$ is row $i$ of $A$ with column $j$ of $B$, while entry $(i,j)$ of $BA$ is row $i$ of $B$ with column $j$ of $A$ — different vectors entirely (and for non-square matrices, often not even the same shape). Move: commuting the *numbers inside* a dot product doesn't commute the *matrices*.
    :::

---

## Part D — Deep end: composition (the why)

12. Rotate-90° $= R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, stretch-x
    $= S = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$.
    Compute both $SR$ and $RS$. Then test each on $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$
    and explain the difference in plain words: which one *rotates first*?

    ::: answer
    $SR = \begin{pmatrix} 0 & -2 \\ 1 & 0 \end{pmatrix}$, $RS = \begin{pmatrix} 0 & -1 \\ 2 & 0 \end{pmatrix}$.
    $SR\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}0\\1\end{pmatrix}$; $RS\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}0\\2\end{pmatrix}$.
    Move: in $SR$, $R$ (rightmost) acts on the vector first — it rotates $(1,0)$ onto the $y$-axis before the stretch can touch its $x$-part, so the stretch does nothing. In $RS$, $S$ acts first, doubling the $x$-part to $(2,0)$ *while it's still on the $x$-axis*, and only then $R$ rotates the doubled vector. $SR$ rotates first; $RS$ stretches first.
    :::

13. Compute $RR$ (rotate-90° twice). Feed the result $\begin{pmatrix} x \\ y \end{pmatrix}$ —
    what single machine is $R^2$?

    ::: answer
    $RR = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I$. Fed $\begin{pmatrix}x\\y\end{pmatrix}$ it returns $\begin{pmatrix}-x\\-y\end{pmatrix}$ — move: two 90° rotations compose into a single 180° rotation (point reflection through the origin).
    :::

14. From lesson 2.5's deep-end question: a 3-layer net computes $C(B(A\vec{v}))$.
    Using shapes $A: (100\times 2)$, $B: (50\times 100)$, $C: (1\times 50)$ — check the whole
    pipeline is legal and give the shape of the final output. What shape is the pre-combined
    machine $M = CBA$? Why might combining save a phone battery?

    ::: answer
    Legal throughout: $A\vec v: (100\times2)(2\times1)\to(100\times1)$; $B(\cdot): (50\times100)(100\times1)\to(50\times1)$; $C(\cdot): (1\times50)(50\times1)\to(1\times1)$ — a single number.
    $M = CBA$: $(1\times50)(50\times100)\to(1\times100)$, then $(1\times100)(100\times2)\to(1\times2)$.
    Move: precompute $M$ once (shape $1\times2$), then each new $\vec v$ costs one small $(1\times2)(2\times1)$ multiply instead of three multiplies through 100- and 50-wide intermediates — far fewer operations per inference, which is exactly what saves battery on a phone.
    :::

---

## Part E — Python check (after the pen work)

15. In notebook `05-matrix-multiplication.ipynb`, verify Part B with `@`, and question 9 by
    printing `A * B` and `A @ B` side by side. Mark ✓ here per verified answer.
