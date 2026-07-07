# Worksheet 2.3 — Dot Product = Similarity

*Pen and paper. Show the multiply-then-add working every time — the rhythm is the skill.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: multiply matching, then add

1. $\begin{pmatrix} 3 \\ 2 \end{pmatrix} \cdot \begin{pmatrix} 4 \\ 5 \end{pmatrix}$

   ::: answer
   $22$ — move: dot product = sum of pairwise products, $3(4) + 2(5) = 12 + 10 = 22$.
   :::

2. $\begin{pmatrix} 1 \\ 0 \end{pmatrix} \cdot \begin{pmatrix} 7 \\ 9 \end{pmatrix}$
   *(interesting — what did dotting with $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$ do?)*

   ::: answer
   $7$ — move: $1(7) + 0(9) = 7 + 0 = 7$. Dotting with $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$
   just picks out the first component — it acts like a "reader" that extracts one coordinate.
   :::

3. $\begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} \cdot \begin{pmatrix} 1 \\ 4 \\ 0 \end{pmatrix}$

   ::: answer
   $-2$ — move: $2(1) + (-1)(4) + 3(0) = 2 - 4 + 0 = -2$.
   :::

4. $\begin{pmatrix} 3 \\ 4 \end{pmatrix} \cdot \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ — a vector
dotted with *itself*. Compare with $|\vec{v}|$ from 2.1. What do you notice?

   ::: answer
   $25$ — move: $3(3) + 4(4) = 9 + 16 = 25$. And $|\vec{v}| = \sqrt{3^2+4^2} = 5$, so
   $\vec{v}\cdot\vec{v} = |\vec{v}|^2$ — dotting a vector with itself always gives its
   magnitude squared.
   :::

---

## Part B — Core: sign tells the story

5. For each pair, compute the dot product and classify: *similar direction / perpendicular / opposite*.

   a. $\begin{pmatrix} 2 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} 4 \\ 3 \end{pmatrix}$
   b. $\begin{pmatrix} 2 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} -1 \\ 2 \end{pmatrix}$
   c. $\begin{pmatrix} 2 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} -4 \\ -2 \end{pmatrix}$

   ::: answer
   a. $2(4)+1(3) = 11$ — positive → similar direction.
   b. $2(-1)+1(2) = 0$ — zero → perpendicular.
   c. $2(-4)+1(-2) = -10$ — negative → opposite direction.
   Move: the *sign* of the dot product tells the story — positive/zero/negative ↔
   similar/perpendicular/opposite.
   :::

6. Sketch the three pairs from question 5. Do the pictures match the verdicts?

   ::: answer
   Yes: a) the two arrows point in a similar general direction (a narrow angle between them),
   b) they meet at a right angle (90°), c) they point in roughly opposite directions (a wide
   angle, near 180°). Move: angle between arrows ↔ sign of dot product.
   :::

7. Find **two different** vectors perpendicular to $\begin{pmatrix} 3 \\ 5 \end{pmatrix}$.
   *(Strategy: make the multiply-then-add total zero. There's a swap-and-negate trick — find it.)*

   ::: answer
   e.g. $\begin{pmatrix} 5 \\ -3 \end{pmatrix}$ and $\begin{pmatrix} -5 \\ 3 \end{pmatrix}$ —
   move: swap the two components and negate one of them, so
   $3(5) + 5(-3) = 15 - 15 = 0$. (Any scalar multiple of these also works — there's a whole
   line of vectors perpendicular to $\begin{pmatrix} 3 \\ 5 \end{pmatrix}$.)
   :::

8. Movie-taste vectors (sci-fi, comedy, romance hours):
   you $= \begin{pmatrix} 8 \\ 2 \\ 0 \end{pmatrix}$,
   Alice $= \begin{pmatrix} 6 \\ 1 \\ 1 \end{pmatrix}$,
   Bob $= \begin{pmatrix} 0 \\ 1 \\ 9 \end{pmatrix}$.
   Dot yourself with each. Whose recommendations should the algorithm show you? That decision
   rule — dot, then rank — **is** how recommender systems and attention both start.

   ::: answer
   you $\cdot$ Alice $= 8(6)+2(1)+0(1) = 48+2+0 = 50$.
   you $\cdot$ Bob $= 8(0)+2(1)+0(9) = 0+2+0 = 2$.
   Move: dot product = similarity score, then rank by it. Alice (50) beats Bob (2) by a wide
   margin, so the algorithm should recommend Alice's picks.
   :::

---

## Part C — Spot the error

9. "$\begin{pmatrix} 2 \\ 3 \end{pmatrix} \cdot \begin{pmatrix} 4 \\ 5 \end{pmatrix} = \begin{pmatrix} 8 \\ 15 \end{pmatrix}$."
   What operation did this person actually do, and what's missing?

   ::: answer
   They computed the **element-wise product**, $\begin{pmatrix} 2(4) \\ 3(5) \end{pmatrix} =
   \begin{pmatrix} 8 \\ 15 \end{pmatrix}$, but never added the entries. Move missing: sum the
   products. Correct dot product: $2(4)+3(5) = 8+15 = 23$ — a single number, not a vector.
   :::

10. "Doc A scored dot product 90 with my query, Doc B scored 12, so A is more relevant."
    A's embedding is enormously long; B's is tiny. Why is the conclusion unsafe,
    and which formula fixes it?

    ::: answer
    Unsafe because a raw dot product is inflated by vector *length*, not just direction — A's
    huge embedding can out-score B on size alone, even if B actually points closer to the
    query. Fix: **cosine similarity**,
    $\cos\theta = \dfrac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|}$, which divides out both
    magnitudes so only direction (true relevance) is compared.
    :::

11. "Our vectors gave dot product 0, so at least one of them must be the zero vector."

    ::: answer
    False. Counterexample: $\begin{pmatrix} 1 \\ 0 \end{pmatrix} \cdot \begin{pmatrix} 0 \\ 1 \end{pmatrix} = 0$
    and neither is the zero vector — they're simply perpendicular. Move: dot product $=0$ means
    *perpendicular OR one vector is zero*, not that one of them must be zero.
    :::

---

## Part D — Deep end

12. Compute the cosine similarity of $\begin{pmatrix} 6 \\ 8 \end{pmatrix}$ and
    $\begin{pmatrix} 3 \\ 4 \end{pmatrix}$ (dot, then divide by both magnitudes).
    Before computing: predict the answer from the arrow picture.

    ::: answer
    $\cos\theta = \dfrac{6(3)+8(4)}{|\begin{pmatrix}6\\8\end{pmatrix}||\begin{pmatrix}3\\4\end{pmatrix}|}
    = \dfrac{50}{10 \times 5} = 1$ — move: dot, then divide by both magnitudes. Makes sense
    from the picture: $\begin{pmatrix} 6 \\ 8 \end{pmatrix} = 2\begin{pmatrix} 3 \\ 4 \end{pmatrix}$,
    so the two arrows point in *exactly* the same direction (angle $=0°$, and $\cos 0° = 1$).
    :::

13. Query and keys, exactly like attention: query $\vec{q} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$,
    keys $\vec{k_1} = \begin{pmatrix} 2 \\ 4 \end{pmatrix}$,
    $\vec{k_2} = \begin{pmatrix} 3 \\ 0 \end{pmatrix}$,
    $\vec{k_3} = \begin{pmatrix} -1 \\ -2 \end{pmatrix}$.
    Compute all three scores $\vec{q} \cdot \vec{k_i}$ and rank them. You have just done the
    first half of a transformer attention head by hand.

    ::: answer
    $\vec{q}\cdot\vec{k_1} = 1(2)+2(4) = 10$, $\vec{q}\cdot\vec{k_2} = 1(3)+2(0) = 3$,
    $\vec{q}\cdot\vec{k_3} = 1(-1)+2(-2) = -5$. Ranking: $\vec{k_1}\ (10) > \vec{k_2}\ (3) >
    \vec{k_3}\ (-5)$ — move: dot product = attention score; the highest-scoring key gets the
    most "attention".
    :::

14. Using the $\Sigma$ notation from Module 0.6, write the dot product of two $n$-component
    vectors as one summation. Then write it as a Python `for` loop.

    ::: answer
    $\vec{a}\cdot\vec{b} = \sum_{i=1}^{n} a_i b_i$ — move: sigma notation is just
    "multiply matching, then add", written compactly. As a `for` loop:
    ```python
    total = 0
    for i in range(n):
        total += a[i] * b[i]
    ```
    :::

---

## Part E — Python check (after the pen work)

15. In notebook `03-dot-product-similarity.ipynb`, verify Part A with `a @ b`, and question 9
    by printing `a * b` vs `a @ b` — see both results side by side. Mark ✓ here.
