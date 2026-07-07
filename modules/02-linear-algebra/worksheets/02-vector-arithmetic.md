# Worksheet 2.2 — Vector Arithmetic

*Pen and paper. For the drawing questions, sketch roughly — the tip-to-tail picture is the point.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: components in, components out

1. $\begin{pmatrix} 2 \\ 5 \end{pmatrix} + \begin{pmatrix} 3 \\ -1 \end{pmatrix}$

2. $\begin{pmatrix} 4 \\ 1 \\ 0 \end{pmatrix} - \begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix}$

3. $4 \begin{pmatrix} 2 \\ -3 \end{pmatrix}$

4. $-1 \begin{pmatrix} 5 \\ 2 \end{pmatrix}$ — then say in words what multiplying by $-1$ did to the arrow.

---

## Part B — Core: both views must agree

5. For $\vec{a} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}$ and $\vec{b} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$:
   compute $\vec{a} + \vec{b}$ with components, **then** draw it tip-to-tail and confirm the arrow
   lands on your answer.

6. Same $\vec{a}, \vec{b}$: draw $\vec{b} + \vec{a}$ (other order). Where does it land? What does
   this say about vector addition and order?

7. Compute $\vec{a} - \vec{b}$, and $2\vec{a} + 3\vec{b}$. *(Combinations like $2\vec{a} + 3\vec{b}$
   are called linear combinations — the bread and butter of every neural layer.)*

8. Solve for $\vec{x}$ using balance-game moves (Module 0 — moves work on vectors too):
   $$\vec{x} + \begin{pmatrix} 2 \\ 7 \end{pmatrix} = \begin{pmatrix} 5 \\ 3 \end{pmatrix}$$

---

## Part C — Spot the error

9. "$\begin{pmatrix} 3 \\ 4 \end{pmatrix} + \begin{pmatrix} 1 \\ 2 \\ 5 \end{pmatrix} = \begin{pmatrix} 4 \\ 6 \\ 5 \end{pmatrix}$
   — just add what matches and copy the rest down."

10. "$2 \begin{pmatrix} 3 \\ 5 \end{pmatrix} = \begin{pmatrix} 6 \\ 5 \end{pmatrix}$ — the 2 multiplies
    the first component."

11. A Python one: `[1, 2] + [3, 4]` prints `[1, 2, 3, 4]`. The student says "Python got vector
    addition wrong." What actually happened?

---

## Part D — Deep end: the algebra of meaning

Use this toy meaning-space: component 1 = royalty, component 2 = gender (0 male → 1 female), component 3 = plural (0 one → 1 many).

$$\vec{king} = \begin{pmatrix} 9 \\ 0 \\ 0 \end{pmatrix} \quad
\vec{man} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \quad
\vec{woman} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} \quad
\vec{kings} = \begin{pmatrix} 9 \\ 0 \\ 1 \end{pmatrix}$$

12. Compute $\vec{king} - \vec{man} + \vec{woman}$ and name the word it should equal.

13. Compute $\vec{kings} - \vec{king}$. What *concept* is that vector? Add it to $\vec{woman}$ —
    what word do you get?

14. Invent your own third axis (e.g. "age", "size") and a four-word analogy in your space,
    written as vector arithmetic. Show it works with components.

15. The midpoint trick: what is $\frac{1}{2}(\vec{man} + \vec{woman})$, and what might that
    vector *mean*? Only today's two operations were used — notice that.

---

## Part E — Python check (after the pen work)

16. In notebook `02-vector-arithmetic.ipynb`, verify Parts A and D with numpy
    (`king - man + woman` etc.). Mark ✓ next to each verified answer here.
