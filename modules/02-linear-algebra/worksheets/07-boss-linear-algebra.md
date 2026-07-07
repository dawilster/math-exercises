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

2. Classify each pair by dot product sign — similar / perpendicular / opposite — showing the arithmetic:

   a. $\begin{pmatrix} 1 \\ 3 \end{pmatrix}, \begin{pmatrix} 6 \\ -2 \end{pmatrix}$
   b. $\begin{pmatrix} 2 \\ 2 \end{pmatrix}, \begin{pmatrix} 3 \\ 1 \end{pmatrix}$
   c. $\begin{pmatrix} 4 \\ -2 \end{pmatrix}, \begin{pmatrix} -2 \\ 1 \end{pmatrix}$

3. Attention warm-up, by hand: query $\vec{q} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$, keys
   $\vec{k_1} = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$, $\vec{k_2} = \begin{pmatrix} 4 \\ 1 \end{pmatrix}$,
   $\vec{k_3} = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$. Score all three, rank them, and state in one
   sentence what a transformer does with such scores.

4. Cosine similarity of $\begin{pmatrix} 3 \\ 4 \end{pmatrix}$ and $\begin{pmatrix} 6 \\ 8 \end{pmatrix}$.
   Explain in one sentence why the answer had to come out that way before you computed anything.

---

## Part B — Matrix multiplication with shape-checks

*Write the shape-check line first for every product, e.g. "$(2\times2)(2\times2) \to (2\times2)$ ✓".*

5. $\begin{pmatrix} 1 & 3 \\ 2 & 0 \end{pmatrix} \begin{pmatrix} 2 \\ 5 \end{pmatrix}$

6. $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}$

7. $\begin{pmatrix} 2 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 3 & 0 \\ 0 & 1 \end{pmatrix}$

8. Shapes only — legal or illegal? If legal, result shape; if illegal, say exactly which
   numbers collided:

   a. $(3\times2)(2\times5)$   b. $(4\times4)(3\times4)$   c. $(1\times3)(3\times1)$   d. $(2\times2)(2\times2)(2\times1)$

9. Weights $W$: $(10 \times 4)$. One data vector $\vec{x}$: 4 components. Batch $X$: $(32\times 4)$.
   Which of $W\vec{x}$, $WX$, $XW^{\mathsf T}$ are legal? Give each legal result's shape.
   ($W^{\mathsf T}$ = transpose = $W$ flipped over its diagonal, shape $(4\times10)$.)

---

## Part C — Transformation reasoning

10. Using the column decoder (columns = where $\begin{pmatrix}1\\0\end{pmatrix}$ and $\begin{pmatrix}0\\1\end{pmatrix}$ land), write the $2\times2$ matrix that:

    a. triples every vector
    b. rotates the plane 90° anticlockwise
    c. reflects across the x-axis ($y \to -y$)
    d. does nothing

11. $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ (rotate 90°),
    $F = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ (flip vertically).
    Compute $RF$ and $FR$. Test both on $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ and state which
    order each product applies the machines in.

12. Without computing entries: what is $R^4$ (rotate-90° four times)? Justify in one sentence.

13. A student's code multiplies a $(2\times2)$ shear onto every corner of a square and gets a
    parallelogram — expected. But their "flip left-right then shear" picture looks identical to
    their "shear then flip left-right" picture, and they conclude matrix order never matters.
    Explain the flaw in concluding from one example. Then give a concrete pair from this sheet
    where order visibly matters.

---

## Part D — Spot the error / shape diagnosis

14. "$\begin{pmatrix} 2 \\ 3 \end{pmatrix} \cdot \begin{pmatrix} 5 \\ 1 \end{pmatrix} = \begin{pmatrix} 10 \\ 3 \end{pmatrix}$"

15. "$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 3 & 4 \end{pmatrix}$"
    *(identify what was done instead of row·column)*

16. `img` is a grayscale photo, shape $(480, 640)$. Diagnose each line — what happens, is it
    what the comment claims?

    a. `crop = img[0:100]` — *"the left 100 columns"*
    b. `bright = img * 3` — *"3× brighter, done"*
    c. `flipped = img[::-1]` — *"mirrored left-to-right"*

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
