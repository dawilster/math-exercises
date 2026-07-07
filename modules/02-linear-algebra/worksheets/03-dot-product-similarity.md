# Worksheet 2.3 — Dot Product = Similarity

*Pen and paper. Show the multiply-then-add working every time — the rhythm is the skill.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: multiply matching, then add

1. $\begin{pmatrix} 3 \\ 2 \end{pmatrix} \cdot \begin{pmatrix} 4 \\ 5 \end{pmatrix}$

2. $\begin{pmatrix} 1 \\ 0 \end{pmatrix} \cdot \begin{pmatrix} 7 \\ 9 \end{pmatrix}$
   *(interesting — what did dotting with $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$ do?)*

3. $\begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} \cdot \begin{pmatrix} 1 \\ 4 \\ 0 \end{pmatrix}$

4. $\begin{pmatrix} 3 \\ 4 \end{pmatrix} \cdot \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ — a vector
   dotted with *itself*. Compare with $|\vec{v}|$ from 2.1. What do you notice?

---

## Part B — Core: sign tells the story

5. For each pair, compute the dot product and classify: *similar direction / perpendicular / opposite*.

   a. $\begin{pmatrix} 2 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} 4 \\ 3 \end{pmatrix}$
   b. $\begin{pmatrix} 2 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} -1 \\ 2 \end{pmatrix}$
   c. $\begin{pmatrix} 2 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} -4 \\ -2 \end{pmatrix}$

6. Sketch the three pairs from question 5. Do the pictures match the verdicts?

7. Find **two different** vectors perpendicular to $\begin{pmatrix} 3 \\ 5 \end{pmatrix}$.
   *(Strategy: make the multiply-then-add total zero. There's a swap-and-negate trick — find it.)*

8. Movie-taste vectors (sci-fi, comedy, romance hours):
   you $= \begin{pmatrix} 8 \\ 2 \\ 0 \end{pmatrix}$,
   Alice $= \begin{pmatrix} 6 \\ 1 \\ 1 \end{pmatrix}$,
   Bob $= \begin{pmatrix} 0 \\ 1 \\ 9 \end{pmatrix}$.
   Dot yourself with each. Whose recommendations should the algorithm show you? That decision
   rule — dot, then rank — **is** how recommender systems and attention both start.

---

## Part C — Spot the error

9. "$\begin{pmatrix} 2 \\ 3 \end{pmatrix} \cdot \begin{pmatrix} 4 \\ 5 \end{pmatrix} = \begin{pmatrix} 8 \\ 15 \end{pmatrix}$."
   What operation did this person actually do, and what's missing?

10. "Doc A scored dot product 90 with my query, Doc B scored 12, so A is more relevant."
    A's embedding is enormously long; B's is tiny. Why is the conclusion unsafe,
    and which formula fixes it?

11. "Our vectors gave dot product 0, so at least one of them must be the zero vector."

---

## Part D — Deep end

12. Compute the cosine similarity of $\begin{pmatrix} 6 \\ 8 \end{pmatrix}$ and
    $\begin{pmatrix} 3 \\ 4 \end{pmatrix}$ (dot, then divide by both magnitudes).
    Before computing: predict the answer from the arrow picture.

13. Query and keys, exactly like attention: query $\vec{q} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$,
    keys $\vec{k_1} = \begin{pmatrix} 2 \\ 4 \end{pmatrix}$,
    $\vec{k_2} = \begin{pmatrix} 3 \\ 0 \end{pmatrix}$,
    $\vec{k_3} = \begin{pmatrix} -1 \\ -2 \end{pmatrix}$.
    Compute all three scores $\vec{q} \cdot \vec{k_i}$ and rank them. You have just done the
    first half of a transformer attention head by hand.

14. Using the $\Sigma$ notation from Module 0.6, write the dot product of two $n$-component
    vectors as one summation. Then write it as a Python `for` loop.

---

## Part E — Python check (after the pen work)

15. In notebook `03-dot-product-similarity.ipynb`, verify Part A with `a @ b`, and question 9
    by printing `a * b` vs `a @ b` — see both results side by side. Mark ✓ here.
