# Boss Worksheet — Module 2: Linear Algebra

*The mastery gate. Rules:*

- *Parts A–D are done **cold** — pen and paper, no notes, no lessons open, no Python.*
- *Photograph everything into `scans/inbox/` for marking.*
- *≥85% with sound reasoning unlocks Module 3 (Calculus) — and the Mandelbrot interlude first.*
- *Part E is the take-home mini-project — Python allowed (that's the point), done after the hand parts are scanned.*
- *Show working: named steps and written shape-checks earn the marks.*

---

## Part A — Vectors and dot products (hand-computed)

1. $\vec{u} = \begin{pmatrix} 3 \\ -1 \\ 2 \end{pmatrix}$, $\vec{w} = \begin{pmatrix} 2 \\ 4 \\ 1 \end{pmatrix}$. Compute:

   a. $\vec{u} + 2\vec{w}$
   b. $|\vec{u}|$ *(name the three steps)*
   c. $\vec{u} \cdot \vec{w}$

   ::: answer
   a. $\vec{u} + 2\vec{w} = \begin{pmatrix} 3+4 \\ -1+8 \\ 2+2 \end{pmatrix} = \begin{pmatrix} 7 \\ 7 \\ 4 \end{pmatrix}$ — move: scale $\vec{w}$ by 2 first, then add component-wise.
   b. $|\vec{u}| = \sqrt{3^2+(-1)^2+2^2} = \sqrt{9+1+4} = \sqrt{14}$ — steps: square each component, sum them, square-root the sum.
   c. $\vec{u} \cdot \vec{w} = 3(2)+(-1)(4)+2(1) = 6-4+2 = 4$ — move: multiply matching components, sum the products.
   :::

2. Classify each pair by dot product sign — similar / perpendicular / opposite — showing the arithmetic:

   a. $\begin{pmatrix} 1 \\ 3 \end{pmatrix}, \begin{pmatrix} 6 \\ -2 \end{pmatrix}$
   b. $\begin{pmatrix} 2 \\ 2 \end{pmatrix}, \begin{pmatrix} 3 \\ 1 \end{pmatrix}$
   c. $\begin{pmatrix} 4 \\ -2 \end{pmatrix}, \begin{pmatrix} -2 \\ 1 \end{pmatrix}$

   ::: answer
   a. $1(6)+3(-2) = 6-6 = 0$ → **perpendicular**.
   b. $2(3)+2(1) = 6+2 = 8 > 0$ → **similar**.
   c. $4(-2)+(-2)(1) = -8-2 = -10 < 0$ → **opposite**.
   :::

3. Attention warm-up, by hand: query $\vec{q} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$, keys
   $\vec{k_1} = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$, $\vec{k_2} = \begin{pmatrix} 4 \\ 1 \end{pmatrix}$,
   $\vec{k_3} = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$. Score all three, rank them, and state in one
   sentence what a transformer does with such scores.

   ::: answer
   $\vec{q}\cdot\vec{k_1} = 2(1)+1(3) = 5$, $\vec{q}\cdot\vec{k_2} = 2(4)+1(1) = 9$, $\vec{q}\cdot\vec{k_3} = 2(-1)+1(1) = -1$.
   Rank: $k_2 > k_1 > k_3$. A transformer turns these scores into weights (via softmax) that decide how much of each key's value vector gets blended into the output.
   :::

4. Cosine similarity of $\begin{pmatrix} 3 \\ 4 \end{pmatrix}$ and $\begin{pmatrix} 6 \\ 8 \end{pmatrix}$.
   Explain in one sentence why the answer had to come out that way before you computed anything.

   ::: answer
   Cosine similarity $= 1$. Move: $\begin{pmatrix} 6 \\ 8 \end{pmatrix} = 2\begin{pmatrix} 3 \\ 4 \end{pmatrix}$ is just the first vector scaled by a positive number, so it points in exactly the same direction — cosine similarity depends only on direction, not length, so it had to come out as $1$ before any arithmetic.
   :::

---

## Part B — Matrix multiplication with shape-checks

*Write the shape-check line first for every product, e.g. "$(2\times2)(2\times2) \to (2\times2)$ ✓".*

5. $\begin{pmatrix} 1 & 3 \\ 2 & 0 \end{pmatrix} \begin{pmatrix} 2 \\ 5 \end{pmatrix}$

   ::: answer
   $(2\times2)(2\times1) \to (2\times1)$ ✓. $\begin{pmatrix} 1(2)+3(5) \\ 2(2)+0(5) \end{pmatrix} = \begin{pmatrix} 17 \\ 4 \end{pmatrix}$ — move: each output entry is a row·column dot product.
   :::

6. $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}$

   ::: answer
   $(2\times2)(2\times2) \to (2\times2)$ ✓. $\begin{pmatrix} 1(3)+2(1) & 1(0)+2(2) \\ 0(3)+1(1) & 0(0)+1(2) \end{pmatrix} = \begin{pmatrix} 5 & 4 \\ 1 & 2 \end{pmatrix}$ — row·column dot products.
   :::

7. $\begin{pmatrix} 2 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 3 & 0 \\ 0 & 1 \end{pmatrix}$

   ::: answer
   $(2\times3)(3\times2) \to (2\times2)$ ✓. $\begin{pmatrix} 2(1)+1(3)+0(0) & 2(2)+1(0)+0(1) \\ 0(1)+1(3)+1(0) & 0(2)+1(0)+1(1) \end{pmatrix} = \begin{pmatrix} 5 & 4 \\ 3 & 1 \end{pmatrix}$.
   :::

8. Shapes only — legal or illegal? If legal, result shape; if illegal, say exactly which
   numbers collided:

   a. $(3\times2)(2\times5)$   b. $(4\times4)(3\times4)$   c. $(1\times3)(3\times1)$   d. $(2\times2)(2\times2)(2\times1)$

   ::: answer
   a. Legal → $(3\times5)$.
   b. Illegal — inner numbers $4$ and $3$ collide (cols of first $=4 \neq$ rows of second $=3$).
   c. Legal → $(1\times1)$.
   d. Legal — $(2\times2)(2\times2)\to(2\times2)$, then $(2\times2)(2\times1)\to(2\times1)$; final shape $(2\times1)$.
   :::

9. Weights $W$: $(10 \times 4)$. One data vector $\vec{x}$: 4 components. Batch $X$: $(32\times 4)$.
   Which of $W\vec{x}$, $WX$, $XW^{\mathsf T}$ are legal? Give each legal result's shape.
   ($W^{\mathsf T}$ = transpose = $W$ flipped over its diagonal, shape $(4\times10)$.)

   ::: answer
   $W\vec{x}$: $(10\times4)(4\times1) \to$ legal, $(10\times1)$.
   $WX$: $(10\times4)(32\times4) \to$ illegal — inner numbers $4$ and $32$ collide.
   $XW^{\mathsf T}$: $(32\times4)(4\times10) \to$ legal, $(32\times10)$.
   :::

---

## Part C — Transformation reasoning

10. Using the column decoder (columns = where $\begin{pmatrix}1\\0\end{pmatrix}$ and $\begin{pmatrix}0\\1\end{pmatrix}$ land), write the $2\times2$ matrix that:

    a. triples every vector
    b. rotates the plane 90° anticlockwise
    c. reflects across the x-axis ($y \to -y$)
    d. does nothing

    ::: answer
    a. $\begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix}$
    b. $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$
    c. $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$
    d. $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ — the identity.
    :::

11. $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ (rotate 90°),
    $F = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ (flip vertically).
    Compute $RF$ and $FR$. Test both on $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ and state which
    order each product applies the machines in.

    ::: answer
    $RF = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $FR = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$.
    On $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$: $RF\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $FR\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} -1 \\ -1 \end{pmatrix}$ — different results, so order matters.
    In $RF$ the **rightmost** matrix acts first: $F$ (flip) is applied, then $R$ (rotate); $FR$ applies $R$ first, then $F$.
    :::

12. Without computing entries: what is $R^4$ (rotate-90° four times)? Justify in one sentence.

    ::: answer
    $R^4 = I$ (the identity) — four quarter-turns is a full $360°$ rotation, which returns every vector to where it started.
    :::

13. A student's code multiplies a $(2\times2)$ shear onto every corner of a square and gets a
    parallelogram — expected. But their "flip left-right then shear" picture looks identical to
    their "shear then flip left-right" picture, and they conclude matrix order never matters.
    Explain the flaw in concluding from one example. Then give a concrete pair from this sheet
    where order visibly matters.

    ::: answer
    The flaw: one matching example doesn't prove a general rule — matrix multiplication is not commutative in general, and this pair may just happen to agree on this particular square (a coincidence of symmetry), not a proof for all matrices/shapes. A concrete counterexample from this sheet: $R$ and $F$ from Q11 — $RF \neq FR$, since $RF\begin{pmatrix}1\\1\end{pmatrix} = \begin{pmatrix}1\\1\end{pmatrix}$ but $FR\begin{pmatrix}1\\1\end{pmatrix} = \begin{pmatrix}-1\\-1\end{pmatrix}$.
    :::

---

## Part D — Spot the error / shape diagnosis

14. "$\begin{pmatrix} 2 \\ 3 \end{pmatrix} \cdot \begin{pmatrix} 5 \\ 1 \end{pmatrix} = \begin{pmatrix} 10 \\ 3 \end{pmatrix}$"

    ::: answer
    Wrong. A dot product must collapse to a single **scalar**, not stay a vector. They multiplied matching components $(2\cdot5, 3\cdot1)=(10,3)$ and stopped (that's the Hadamard/entrywise product) instead of summing them. Correct: $2(5)+3(1) = 10+3 = 13$.
    :::

15. "$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 3 & 4 \end{pmatrix}$"
    *(identify what was done instead of row·column)*

    ::: answer
    They multiplied entrywise (each entry $\times$ the entry in the same position: $1\cdot2, 2\cdot0, 3\cdot1, 4\cdot1$) instead of taking row·column dot products. Correct matrix product: $\begin{pmatrix} 1(2)+2(1) & 1(0)+2(1) \\ 3(2)+4(1) & 3(0)+4(1) \end{pmatrix} = \begin{pmatrix} 4 & 2 \\ 10 & 4 \end{pmatrix}$.
    :::

16. `img` is a grayscale photo, shape $(480, 640)$. Diagnose each line — what happens, is it
    what the comment claims?

    a. `crop = img[0:100]` — *"the left 100 columns"*
    b. `bright = img * 3` — *"3× brighter, done"*
    c. `flipped = img[::-1]` — *"mirrored left-to-right"*

    ::: answer
    a. Wrong claim. `img[0:100]` slices the **first** axis, which is rows — this gives the **top 100 rows** (full width), not the left 100 columns. Columns would need `img[:, 0:100]`.
    b. Half-right. It does triple every value, but with no clipping/cast, `uint8` pixels above 255 **overflow and wrap around** — the comment's "done" is wrong unless you clip (e.g. `np.clip(img*3, 0, 255)`) first.
    c. Wrong claim. `img[::-1]` reverses the first axis (rows), which flips the image **top-to-bottom** (upside down), not left-to-right. Left-right mirroring needs `img[:, ::-1]`.
    :::

---

## Part E — Take-home mini-project: the numpy darkroom

*At the computer, open-book, unhurried. Create `notebooks/boss-darkroom.ipynb` in this module.
Everything from numpy only — no image files, no downloads.*

Build and `imshow` each of the following, in one notebook, with a one-line markdown comment
above each stating which lesson-skill it uses:

1. **Canvas** — a 100×100 grayscale image of your own design built from array indexing and
   slicing: at minimum a border, a filled rectangle, and a diagonal (the diagonal needs a loop
   or a clever index — your choice).
2. **Gradient sky** — a 100×100 image fading 0 → 1 top-to-bottom. *(Hint: what should each row contain?)*
3. **Checkerboard** — 8×8, then zoom it to 80×80 **without loops** using `np.repeat` (look its
   docs up — reading numpy docs is part of the exercise).
4. **Edits gallery** — take your canvas and show, side by side: brightened (clipped), negative,
   upside-down, left-right mirrored, and a crop of its most interesting quarter.
5. **Colour finale** — stack three different grayscale matrices into an RGB image of shape
   $(100, 100, 3)$ using `np.stack(..., axis=-1)` and make something you find genuinely
   pleasing. This one's art: spend ten extra minutes on it.
6. **Boss twist** — blend your canvas 50/50 with the gradient sky (worksheet 2.6 Part D taught
   the math). Then try 20/80 and 80/20. One sentence in markdown: which vector-arithmetic
   operation *is* blending?

Run it top-to-bottom clean, then tell Claude it's ready for review.

---

*Scan Parts A–D into `scans/inbox/` before opening Python. Good luck — then the Mandelbrot set awaits.*
