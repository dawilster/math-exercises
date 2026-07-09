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

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

Use this toy meaning-space: component 1 = royalty, component 2 = gender (0 male → 1 female), component 3 = plural (0 one → 1 many).

$$\vec{king} = \begin{pmatrix} 9 \\ 0 \\ 0 \end{pmatrix} \quad
\vec{man} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \quad
\vec{woman} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} \quad
\vec{kings} = \begin{pmatrix} 9 \\ 0 \\ 1 \end{pmatrix}$$

12. Compute $\vec{king} - \vec{man} + \vec{woman}$ and name the word it should equal.

    ::: rephrase
    This is the lesson's famous example (king − man + woman → queen), just with a third slot
    (plural) riding along. "Compute" = do the arithmetic one operation at a time, left to right,
    component by component. "Name the word" = read what the three final numbers *mean*: royalty,
    gender ($0$ male, $1$ female), plural. First move: subtract man from king.
    :::

    ::: hint
    It's a **linear combination** — take it one operation at a time, component by component. Don't
    do all three vectors at once; start with $\vec{king} - \vec{man}$.
    :::

    ::: hint
    Subtract man from king first, row by row: $9-1,\; 0-0,\; 0-0$. Then add $\vec{woman}$ to that result.
    :::

    ::: steps
    1. **Subtract man from king** (component-wise). $\begin{pmatrix} 9 \\ 0 \\ 0 \end{pmatrix} - \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 8 \\ 0 \\ 0 \end{pmatrix}$ — strips the "man-ness" off king.
    2. **Add woman** (component-wise). $\begin{pmatrix} 8 \\ 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 9 \\ 1 \\ 0 \end{pmatrix}$ — paints "woman-ness" back on.
    3. **Read the result as a word.** royalty 9, gender female, not plural → **queen**.
    :::

13. Compute $\vec{kings} - \vec{king}$. What *concept* is that vector? Add it to $\vec{woman}$ —
    what word do you get?

    ::: rephrase
    $\vec{kings}$ and $\vec{king}$ are identical except for one slot. When you subtract two words
    that differ in only one axis, the shared components cancel to $0$ and you're left with the one
    thing that differs — that leftover *is* a concept, the same trick as king − man isolating
    "man-ness" in the lesson. Do $\vec{kings} - \vec{king}$, see which slot survives, then add that
    concept vector onto $\vec{woman}$ and read the word.
    :::

    ::: hint
    Subtracting two near-identical words **cancels** their shared components, isolating the one
    concept that differs. Compute $\vec{kings} - \vec{king}$ component-wise and watch which slot survives.
    :::

    ::: hint
    $\vec{kings} - \vec{king}$, row by row: $9-9,\; 0-0,\; 1-0$ — only the plural slot survives.
    That leftover is the pure "plural" vector; now add it to $\vec{woman}$.
    :::

    ::: steps
    1. **Subtract king from kings** (component-wise). $\begin{pmatrix} 9 \\ 0 \\ 1 \end{pmatrix} - \begin{pmatrix} 9 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$ — shared slots cancel.
    2. **Name the isolated concept.** only the plural slot is nonzero → the pure **"plural"** vector.
    3. **Add it to woman** (component-wise). $\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$ — royalty 1, female, plural → **women**.
    :::

14. Invent your own third axis (e.g. "age", "size") and a four-word analogy in your space,
    written as vector arithmetic. Show it works with components.

    ::: rephrase
    There's no single right answer — you're building your own, so this rung just shows you the
    *shape* to copy. Pick a new meaning axis (say "age", $0$ young, $1$ old), write a few words as
    vectors on your axes, then form an analogy like $\vec{A} - \vec{B} + \vec{C}$ and check it lands
    on a fourth word. The verification is identical to Q12–13: subtract to isolate one concept, add
    it elsewhere.
    :::

    ::: hint
    Choose your third axis and pin down what its $0$ and $1$ mean *first* (e.g. age: $0$ young,
    $1$ old). Then write a few words as 3-slot vectors using royalty / gender / your-axis.
    :::

    ::: hint
    Build the analogy as "$\vec{A} - \vec{B} + \vec{C}$" where going $\vec{B}\to\vec{A}$ adds exactly
    one concept; predict the fourth word, then verify component-wise just like Q12.
    :::

    ::: steps
    1. **Set up an axis and word vectors.** age ($0$ young, $1$ old): $\vec{boy}=\begin{pmatrix}1\\0\\0\end{pmatrix},\ \vec{man}=\begin{pmatrix}1\\0\\1\end{pmatrix},\ \vec{princess}=\begin{pmatrix}9\\1\\0\end{pmatrix}$
    2. **Isolate the concept** (man − boy = "aging"). $\begin{pmatrix}1\\0\\1\end{pmatrix}-\begin{pmatrix}1\\0\\0\end{pmatrix}=\begin{pmatrix}0\\0\\1\end{pmatrix}$
    3. **Apply it elsewhere and read the word.** $\begin{pmatrix}0\\0\\1\end{pmatrix}+\begin{pmatrix}9\\1\\0\end{pmatrix}=\begin{pmatrix}9\\1\\1\end{pmatrix}=\vec{queen}$ (an old princess). Your own answer will differ — the moves won't.
    :::

15. The midpoint trick: what is $\frac{1}{2}(\vec{man} + \vec{woman})$, and what might that
    vector *mean*? Only today's two operations were used — notice that.

    ::: rephrase
    Only today's two operations are needed, in order: **add**, then **scale**. First add $\vec{man}$
    and $\vec{woman}$ component-wise, then multiply the result by $\frac12$ — that's just scaling an
    arrow by a scalar, exactly like Part A's $4\vec{v}$, only with $k=\frac12$. "What might it mean" =
    read the halved gender slot. A midpoint sits exactly halfway between two arrow tips.
    :::

    ::: hint
    Two moves: add-then-scale. Add $\vec{man} + \vec{woman}$ first (component-wise), then apply the
    scalar $\frac12$ to every component (scaling an arrow, Part A).
    :::

    ::: hint
    $\vec{man} + \vec{woman} = \begin{pmatrix}2\\1\\0\end{pmatrix}$; now scale by $\frac12$ — halve every component.
    :::

    ::: steps
    1. **Add man and woman** (component-wise). $\begin{pmatrix}1\\0\\0\end{pmatrix}+\begin{pmatrix}1\\1\\0\end{pmatrix}=\begin{pmatrix}2\\1\\0\end{pmatrix}$
    2. **Scale by $\frac12$** (halve every component). $\frac12\begin{pmatrix}2\\1\\0\end{pmatrix}=\begin{pmatrix}1\\0.5\\0\end{pmatrix}$
    3. **Read the result.** same royalty, gender exactly halfway male↔female, not plural → a gender-neutral **"person"**.
    :::

---

## Part E — Python check (after the pen work)

16. In notebook `02-vector-arithmetic.ipynb`, verify Parts A and D with numpy
    (`king - man + woman` etc.). Mark ✓ next to each verified answer here.
