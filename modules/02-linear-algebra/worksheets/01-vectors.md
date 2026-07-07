# Worksheet 2.1 — Vectors: Arrows and Lists

*Pen and paper. Sketch axes freehand — accuracy of thinking beats accuracy of drawing.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: two views of the same thing

1. Draw the arrows $\vec{a} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}$,
   $\vec{b} = \begin{pmatrix} -2 \\ 2 \end{pmatrix}$ and
   $\vec{c} = \begin{pmatrix} 0 \\ -3 \end{pmatrix}$ from the origin on one set of axes.

   ::: answer
   Arrowheads land at $(3,1)$, $(-2,2)$ and $(0,-3)$. Move: a vector's components
   *are* the coordinates of its tip when the tail sits at the origin.
   :::

2. Write the vector drawn as an arrow from the origin to the point $(-4, 2)$ as a column of numbers.

   ::: answer
   $\begin{pmatrix} -4 \\ 2 \end{pmatrix}$ — move: the tip's coordinates become the vector's components directly.
   :::

3. For $\vec{v} = \begin{pmatrix} 5 \\ -2 \\ 7 \end{pmatrix}$: what is $v_1$ (math counting)?
   What would Python's `v[1]` give? *(They're different — say why.)*

   ::: answer
   $v_1 = 5$ (math counts components from 1). Python's `v[1]` gives $-2$, the *second*
   component — move: Python indexes from 0, so `v[0]` is the first entry and `v[1]` is the second.
   :::

---

## Part B — Core: magnitude and meaning

4. Compute the magnitude of each, naming the three steps (square, add, root):

   a. $\begin{pmatrix} 6 \\ 8 \end{pmatrix}$
   b. $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$
   c. $\begin{pmatrix} 2 \\ 3 \\ 6 \end{pmatrix}$ *(same steps, one more component)*

   ::: answer
   a. square: $36, 64$ → add: $100$ → root: $|\vec{v}| = 10$.
   b. square: $1, 1$ → add: $2$ → root: $|\vec{v}| = \sqrt{2} \approx 1.414$.
   c. square: $4, 9, 36$ → add: $49$ → root: $|\vec{v}| = 7$.
   Move: square each component, add them, take the square root (Pythagoras generalised).
   :::

5. A streaming service describes each user as
   $\begin{pmatrix} \text{hours of sci-fi} \\ \text{hours of comedy} \\ \text{hours of documentaries} \end{pmatrix}$ per month.
   Write plausible user-vectors for: (a) a documentary addict, (b) someone who watches nothing,
   (c) yourself, honestly.

   ::: answer
   No single correct numbers — but a sane shape: (a) large third component, small others,
   e.g. $\begin{pmatrix} 0 \\ 1 \\ 20 \end{pmatrix}$. (b) $\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$ —
   the zero vector, no arrow at all. (c) yours will vary — move: each axis is a fixed category,
   the number on it is "how much", consistent units across users.
   :::

6. Two users: $\begin{pmatrix} 20 \\ 2 \\ 1 \end{pmatrix}$ and $\begin{pmatrix} 40 \\ 4 \\ 2 \end{pmatrix}$.
   One watches double the hours — but as *arrows*, what do these two have in common?
   What might that mean about their taste?

   ::: answer
   The second is exactly $2\times$ the first component-wise, so the two arrows point in the
   **same direction** — only the length differs. Move: spot a scalar multiple. Same direction ⇒
   identical taste *ratio* (sci-fi : comedy : documentaries), just different total viewing time.
   :::

---

## Part C — Spot the error

Each claim contains one mistake. Find it and say what went wrong.

7. "$\vec{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$, so $|\vec{v}| = 3^2 + 4^2 = 25$."

   ::: answer
   Stopped one move too early. $3^2 + 4^2 = 25$ is the sum of squares, not the magnitude —
   the missing move is the square root: $|\vec{v}| = \sqrt{25} = 5$.
   :::

8. "`v = np.array([10, 20, 30])`, so `v[3]` gives `30`."

   ::: answer
   Off-by-one from forgetting zero-indexing. Indices are $0, 1, 2$ for a length-3 array, so
   `v[3]` is out of range (`IndexError`). `v[2]` is the one that gives `30`.
   :::

9. "$\begin{pmatrix} 2 \\ 5 \end{pmatrix}$ and $\begin{pmatrix} 5 \\ 2 \end{pmatrix}$ are the same
   vector — same numbers, after all."

   ::: answer
   False — **position matters**, not just the numbers present. Component 1 is the first axis,
   component 2 is the second; swapping them gives a different point (different arrow) unless
   the components happen to be equal.
   :::

---

## Part D — Deep end

*Not fully taught yet. Attempt anyway — reasoned guesses beat blank space.*

10. A **unit vector** has magnitude exactly 1. Find a unit vector pointing the same direction as
    $\begin{pmatrix} 6 \\ 8 \end{pmatrix}$. *(Hint: you found its length in Part B. What scalar fixes it?)*

    ::: answer
    $\begin{pmatrix} 0.6 \\ 0.8 \end{pmatrix}$ — move: divide every component by the magnitude
    (from 4a, $|\vec{v}| = 10$), i.e. $\frac{1}{10}\begin{pmatrix} 6 \\ 8 \end{pmatrix}$. Check:
    $\sqrt{0.6^2 + 0.8^2} = \sqrt{0.36 + 0.64} = 1$.
    :::

11. How far apart are the *tips* of $\begin{pmatrix} 1 \\ 2 \end{pmatrix}$ and
    $\begin{pmatrix} 4 \\ 6 \end{pmatrix}$? *(Hint: sketch both. The gap between the tips is itself
    an arrow — which one? Then measure it.)*

    ::: answer
    $5$. Move: the gap is the difference vector $\begin{pmatrix} 4-1 \\ 6-2 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$;
    its magnitude is $\sqrt{3^2+4^2} = \sqrt{25} = 5$.
    :::

12. A word embedding has 768 components. Write the magnitude formula for a 768-component vector
    using $\dots$ notation — or better, as a $\Sigma$ (Module 0.6 pays off).

    ::: answer
    $|\vec{v}| = \sqrt{v_1^2 + v_2^2 + \dots + v_{768}^2} = \sqrt{\displaystyle\sum_{i=1}^{768} v_i^2}$
    — move: same square–add–root recipe, just written compactly for many components.
    :::

---

## Part E — Python check (after the pen work)

13. Open notebook `01-vectors.ipynb`. Verify your Part B magnitudes with `np.linalg.norm`,
    and your Part D unit vector (its norm should print `1.0`). Mark each ✓ on this sheet.
