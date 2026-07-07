# Worksheet 2.2 — Vector Arithmetic

*Pen and paper. For the drawing questions, sketch roughly — the tip-to-tail picture is the point.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: components in, components out

1. $\begin{pmatrix} 2 \\ 5 \end{pmatrix} + \begin{pmatrix} 3 \\ -1 \end{pmatrix}$

   ::: answer
   $\begin{pmatrix} 5 \\ 4 \end{pmatrix}$ — move: add component-wise.
   :::

2. $\begin{pmatrix} 4 \\ 1 \\ 0 \end{pmatrix} - \begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix}$

   ::: answer
   $\begin{pmatrix} 3 \\ 0 \\ -2 \end{pmatrix}$ — move: subtract component-wise.
   :::

3. $4 \begin{pmatrix} 2 \\ -3 \end{pmatrix}$

   ::: answer
   $\begin{pmatrix} 8 \\ -12 \end{pmatrix}$ — move: scale each component by $k=4$.
   :::

4. $-1 \begin{pmatrix} 5 \\ 2 \end{pmatrix}$ — then say in words what multiplying by $-1$ did to the arrow.

   ::: answer
   $\begin{pmatrix} -5 \\ -2 \end{pmatrix}$ — move: scale each component by $k=-1$. In words: the arrow
   flips to point exactly the opposite way, same length.
   :::

---

## Part B — Core: both views must agree

5. For $\vec{a} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}$ and $\vec{b} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$:
   compute $\vec{a} + \vec{b}$ with components, **then** draw it tip-to-tail and confirm the arrow
   lands on your answer.

   ::: answer
   $\vec{a} + \vec{b} = \begin{pmatrix} 4 \\ 3 \end{pmatrix}$ — move: add component-wise. Tip-to-tail:
   draw $\vec{a}$, then start $\vec{b}$ at $\vec{a}$'s tip; the final arrow (tail at origin, tip at
   the end of $\vec{b}$) lands at $(4,3)$, matching the components.
   :::

6. Same $\vec{a}, \vec{b}$: draw $\vec{b} + \vec{a}$ (other order). Where does it land? What does
   this say about vector addition and order?

   ::: answer
   It lands at the same point, $(4,3)$ — the two tip-to-tail paths trace opposite sides of a
   parallelogram and finish together. Move: order doesn't matter; vector addition is commutative,
   $\vec{a}+\vec{b} = \vec{b}+\vec{a}$, same as it is for plain numbers.
   :::

7. Compute $\vec{a} - \vec{b}$, and $2\vec{a} + 3\vec{b}$. *(Combinations like $2\vec{a} + 3\vec{b}$
   are called linear combinations — the bread and butter of every neural layer.)*

   ::: answer
   $\vec{a} - \vec{b} = \begin{pmatrix} 2 \\ -1 \end{pmatrix}$ — move: subtract component-wise.
   $2\vec{a} + 3\vec{b} = \begin{pmatrix} 6 \\ 2 \end{pmatrix} + \begin{pmatrix} 3 \\ 6 \end{pmatrix} = \begin{pmatrix} 9 \\ 8 \end{pmatrix}$
   — move: scale each vector first, then add component-wise.
   :::

8. Solve for $\vec{x}$ using balance-game moves (Module 0 — moves work on vectors too):
   $$\vec{x} + \begin{pmatrix} 2 \\ 7 \end{pmatrix} = \begin{pmatrix} 5 \\ 3 \end{pmatrix}$$

   ::: answer
   $\vec{x} = \begin{pmatrix} 3 \\ -4 \end{pmatrix}$ — move: subtract $\begin{pmatrix} 2 \\ 7 \end{pmatrix}$
   from both sides (component-wise), same balance-scale move as Module 0, just done to every row at once.
   :::

---

## Part C — Spot the error

9. "$\begin{pmatrix} 3 \\ 4 \end{pmatrix} + \begin{pmatrix} 1 \\ 2 \\ 5 \end{pmatrix} = \begin{pmatrix} 4 \\ 6 \\ 5 \end{pmatrix}$
   — just add what matches and copy the rest down."

   ::: answer
   Broken — undefined, not just wrong. Vector addition is only defined between vectors of the
   **same dimension**; you can't add a 2D vector to a 3D one and "copy down" the leftover component.
   The move that broke: mixing dimensions instead of checking they match first.
   :::

10. "$2 \begin{pmatrix} 3 \\ 5 \end{pmatrix} = \begin{pmatrix} 6 \\ 5 \end{pmatrix}$ — the 2 multiplies
    the first component."

    ::: answer
    Broken. Correct: $2 \begin{pmatrix} 3 \\ 5 \end{pmatrix} = \begin{pmatrix} 6 \\ 10 \end{pmatrix}$.
    The move that broke: a scalar multiplies **every** component, not just the first.
    :::

11. A Python one: `[1, 2] + [3, 4]` prints `[1, 2, 3, 4]`. The student says "Python got vector
    addition wrong." What actually happened?

    ::: answer
    Python didn't get it "wrong" — `+` on two `list`s means **concatenation**, a different operation
    that happens to share the `+` symbol. No component-wise math ever ran. To get real vector
    addition you need `numpy` arrays: `np.array([1,2]) + np.array([3,4])` gives `[4, 6]`.
    :::

---

## Part D — Deep end: the algebra of meaning

Use this toy meaning-space: component 1 = royalty, component 2 = gender (0 male → 1 female), component 3 = plural (0 one → 1 many).

$$\vec{king} = \begin{pmatrix} 9 \\ 0 \\ 0 \end{pmatrix} \quad
\vec{man} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \quad
\vec{woman} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} \quad
\vec{kings} = \begin{pmatrix} 9 \\ 0 \\ 1 \end{pmatrix}$$

12. Compute $\vec{king} - \vec{man} + \vec{woman}$ and name the word it should equal.

    ::: answer
    $\begin{pmatrix} 9 \\ 0 \\ 0 \end{pmatrix} - \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 9 \\ 1 \\ 0 \end{pmatrix}$
    — royalty 9, gender female, not plural: **queen**. Move: subtract to strip "man-ness" off
    "king", then add "woman-ness" — a linear combination, component-wise throughout.
    :::

13. Compute $\vec{kings} - \vec{king}$. What *concept* is that vector? Add it to $\vec{woman}$ —
    what word do you get?

    ::: answer
    $\vec{kings} - \vec{king} = \begin{pmatrix} 9 \\ 0 \\ 1 \end{pmatrix} - \begin{pmatrix} 9 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$
    — the pure **"plural"** concept, isolated from royalty or gender (move: subtract to cancel
    the shared components, leaving only what differs). Add it to $\vec{woman} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$:
    $\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$ — royalty 1, female, plural: **women**.
    :::

14. Invent your own third axis (e.g. "age", "size") and a four-word analogy in your space,
    written as vector arithmetic. Show it works with components.

    ::: answer
    No single correct answer — it's your invention, but the check is the same as Q12–13. Example
    with axis "age" (0 = young, 1 = old): $\vec{boy}=\begin{pmatrix}1\\0\\0\end{pmatrix}$,
    $\vec{man}=\begin{pmatrix}1\\0\\1\end{pmatrix}$, $\vec{princess}=\begin{pmatrix}9\\1\\0\end{pmatrix}$.
    Then $\vec{man} - \vec{boy} + \vec{princess} = \begin{pmatrix}0\\0\\1\end{pmatrix} + \begin{pmatrix}9\\1\\0\end{pmatrix} = \begin{pmatrix}9\\1\\1\end{pmatrix} = \vec{queen}$.
    Move: subtract to isolate a concept vector (here, "aging"), then add it elsewhere to transfer
    that concept to a new word.
    :::

15. The midpoint trick: what is $\frac{1}{2}(\vec{man} + \vec{woman})$, and what might that
    vector *mean*? Only today's two operations were used — notice that.

    ::: answer
    $\frac{1}{2}\left(\begin{pmatrix}1\\0\\0\end{pmatrix} + \begin{pmatrix}1\\1\\0\end{pmatrix}\right) = \frac{1}{2}\begin{pmatrix}2\\1\\0\end{pmatrix} = \begin{pmatrix}1\\0.5\\0\end{pmatrix}$
    — same royalty, gender exactly halfway between male and female, not plural: a gender-neutral
    **"person"** concept. Move: add, then scale by $\frac12$ — addition and scaling, the only two
    operations of a linear combination, are all it takes to build an "average" word.
    :::

---

## Part E — Python check (after the pen work)

16. In notebook `02-vector-arithmetic.ipynb`, verify Parts A and D with numpy
    (`king - man + woman` etc.). Mark ✓ next to each verified answer here.
