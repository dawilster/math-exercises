# Worksheet 2.1 — Vectors: Arrows and Lists

*Pen and paper. Sketch axes freehand — accuracy of thinking beats accuracy of drawing.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: two views of the same thing

1. Draw the arrows $\vec{a} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}$,
   $\vec{b} = \begin{pmatrix} -2 \\ 2 \end{pmatrix}$ and
   $\vec{c} = \begin{pmatrix} 0 \\ -3 \end{pmatrix}$ from the origin on one set of axes.

2. Write the vector drawn as an arrow from the origin to the point $(-4, 2)$ as a column of numbers.

3. For $\vec{v} = \begin{pmatrix} 5 \\ -2 \\ 7 \end{pmatrix}$: what is $v_1$ (math counting)?
   What would Python's `v[1]` give? *(They're different — say why.)*

---

## Part B — Core: magnitude and meaning

4. Compute the magnitude of each, naming the three steps (square, add, root):

   a. $\begin{pmatrix} 6 \\ 8 \end{pmatrix}$
   b. $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$
   c. $\begin{pmatrix} 2 \\ 3 \\ 6 \end{pmatrix}$ *(same steps, one more component)*

5. A streaming service describes each user as
   $\begin{pmatrix} \text{hours of sci-fi} \\ \text{hours of comedy} \\ \text{hours of documentaries} \end{pmatrix}$ per month.
   Write plausible user-vectors for: (a) a documentary addict, (b) someone who watches nothing,
   (c) yourself, honestly.

6. Two users: $\begin{pmatrix} 20 \\ 2 \\ 1 \end{pmatrix}$ and $\begin{pmatrix} 40 \\ 4 \\ 2 \end{pmatrix}$.
   One watches double the hours — but as *arrows*, what do these two have in common?
   What might that mean about their taste?

---

## Part C — Spot the error

Each claim contains one mistake. Find it and say what went wrong.

7. "$\vec{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$, so $|\vec{v}| = 3^2 + 4^2 = 25$."

8. "`v = np.array([10, 20, 30])`, so `v[3]` gives `30`."

9. "$\begin{pmatrix} 2 \\ 5 \end{pmatrix}$ and $\begin{pmatrix} 5 \\ 2 \end{pmatrix}$ are the same
   vector — same numbers, after all."

---

## Part D — Deep end

*Not fully taught yet. Attempt anyway — reasoned guesses beat blank space.*

10. A **unit vector** has magnitude exactly 1. Find a unit vector pointing the same direction as
    $\begin{pmatrix} 6 \\ 8 \end{pmatrix}$. *(Hint: you found its length in Part B. What scalar fixes it?)*

11. How far apart are the *tips* of $\begin{pmatrix} 1 \\ 2 \end{pmatrix}$ and
    $\begin{pmatrix} 4 \\ 6 \end{pmatrix}$? *(Hint: sketch both. The gap between the tips is itself
    an arrow — which one? Then measure it.)*

12. A word embedding has 768 components. Write the magnitude formula for a 768-component vector
    using $\dots$ notation — or better, as a $\Sigma$ (Module 0.6 pays off).

---

## Part E — Python check (after the pen work)

13. Open notebook `01-vectors.ipynb`. Verify your Part B magnitudes with `np.linalg.norm`,
    and your Part D unit vector (its norm should print `1.0`). Mark each ✓ on this sheet.
