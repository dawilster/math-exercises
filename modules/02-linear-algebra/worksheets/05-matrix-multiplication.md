# Worksheet 2.5 — Matrix Multiplication

*Pen and paper. Shape-check in writing BEFORE every multiplication — the habit is half the marks
here and most of the value in real ML debugging. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: shapes only, no arithmetic

For each product: legal or illegal? If legal, give the result's shape. $(m\times n)(n\times p)=(m\times p)$.

1. $(2\times 3)(3\times 2)$

2. $(3\times 3)(3\times 1)$

3. $(2\times 3)(2\times 3)$

4. $(1\times 4)(4\times 1)$ — and what everyday operation from 2.3 is this product secretly?

---

## Part B — Core: row · column, entry by entry

5. Compute, shape-check first, one dot product per entry:

   a. $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$

   b. $\begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 4 \\ 2 & 0 \end{pmatrix}$

6. Using your matrices from 5b: compute the product in the **other order**,
   $\begin{pmatrix} 1 & 4 \\ 2 & 0 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}$.
   Same answer? Write the moral in one sentence.

7. Compute $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.
   Explain the result using the "machine that does nothing" from worksheet 2.4.

8. A non-square one: $\begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 0 & 3 \end{pmatrix}$.
   Shape-check first, then compute.

---

## Part C — Spot the error / shape diagnosis

9. "$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 5 & 12 \\ 21 & 32 \end{pmatrix}$."
   Which Python operator did this person effectively use, and which should they have used?

10. A network layer holds weights $W$ of shape $(64, 128)$. A batch of data arrives as $X$,
    shape $(32, 128)$ — 32 samples, 128 features. The code `W @ X` crashes.
    Diagnose with the shape rule. Then: `X @ ?` of what shape *would* run, and what output shape results?
    *(Hint: a matrix can be flipped over its diagonal — the transpose — turning $(64,128)$ into $(128,64)$.)*

11. "Matrix multiplication is just a grid of dot products, and dot products don't care about order —
    so $AB = BA$." The first two claims are true. Where does the conclusion break?

---

## Part D — Deep end: composition (the why)

12. Rotate-90° $= R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, stretch-x
    $= S = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$.
    Compute both $SR$ and $RS$. Then test each on $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$
    and explain the difference in plain words: which one *rotates first*?

13. Compute $RR$ (rotate-90° twice). Feed the result $\begin{pmatrix} x \\ y \end{pmatrix}$ —
    what single machine is $R^2$?

14. From lesson 2.5's deep-end question: a 3-layer net computes $C(B(A\vec{v}))$.
    Using shapes $A: (100\times 2)$, $B: (50\times 100)$, $C: (1\times 50)$ — check the whole
    pipeline is legal and give the shape of the final output. What shape is the pre-combined
    machine $M = CBA$? Why might combining save a phone battery?

---

## Part E — Python check (after the pen work)

15. In notebook `05-matrix-multiplication.ipynb`, verify Part B with `@`, and question 9 by
    printing `A * B` and `A @ B` side by side. Mark ✓ here per verified answer.
