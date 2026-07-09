# Worksheet 2.4 — Matrices: Tables and Machines

*Pen and paper. Say shapes out loud as (rows × columns) every single time.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: reading the grid

Use $\;M = \begin{pmatrix} 3 & 2 & 650 \\ 4 & 2 & 700 \\ 9 & 7 & 4000 \end{pmatrix}$ —
houses as rows, features (beds, baths, land m²) as columns.

1. What is the shape of $M$?

   ::: answer
   $(3 \times 3)$ — 3 rows, 3 columns. Move: count rows first, then columns (rows × columns, always).
   :::

2. Write down row 2 (math counting: the second row). As a data table, what does it represent?

   ::: answer
   Row 2 $= \begin{pmatrix} 4 & 2 & 700 \end{pmatrix}$ — house 2: 4 beds, 2 baths, 700 m² of land.
   :::

3. Write down column 3. What does *it* represent?

   ::: answer
   Column 3 $= \begin{pmatrix} 650 \\ 700 \\ 4000 \end{pmatrix}$ — the land size (m²) of every house.
   :::

4. What would Python's `M[0]` and `M[:, 1]` give? *(Careful — Python counts from 0.)*

   ::: answer
   `M[0]` is row 0 (Python-counting) = math row 1 = $\begin{pmatrix} 3 & 2 & 650 \end{pmatrix}$.
   `M[:, 1]` is column 1 (Python-counting) = math column 2 = $\begin{pmatrix} 2 \\ 2 \\ 7 \end{pmatrix}$ (the baths).
   Move: shift every human-counted index down by 1 to get the Python index.
   :::

---

## Part B — Core: feed the machine

5. Compute, naming each step "row $i$ · vector":

   a. $\begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$
   b. $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 3 \\ 2 \end{pmatrix}$
   c. $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix}$ — shape-check first: $(2\times3)(3\times1) = ?$

   ::: answer
   a. $\begin{pmatrix} 2(1) + 0(1) \\ 0(1) + 3(1) \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$.
   b. $\begin{pmatrix} 0(3) - 1(2) \\ 1(3) + 0(2) \end{pmatrix} = \begin{pmatrix} -2 \\ 3 \end{pmatrix}$.
   c. Shape check: $(2\times3)(3\times1) = (2\times1)$ — valid, output has 2 entries.
   $\begin{pmatrix} 1(2)+2(1)+0(1) \\ 0(2)+1(1)+3(1) \end{pmatrix} = \begin{pmatrix} 4 \\ 4 \end{pmatrix}$.
   Move throughout: each output entry is "row $i$ · vector" (multiply matching entries, then add).
   :::

6. For matrix (b) above: feed it $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$ and $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$,
   sketch inputs and outputs, and describe in one word what this machine does to the plane.

   ::: answer
   $\begin{pmatrix} 1 \\ 0 \end{pmatrix} \to \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ and
   $\begin{pmatrix} 0 \\ 1 \end{pmatrix} \to \begin{pmatrix} -1 \\ 0 \end{pmatrix}$ — every vector swings round
   the origin by $90°$ counterclockwise. One word: **rotates**.
   :::

7. Use the column decoder (columns = where the unit arrows land) to **write down** the matrix that:

   a. doubles every vector's length
   b. flips the plane left–right ($x \to -x$, $y$ unchanged)
   c. squashes everything flat onto the x-axis ($y \to 0$)

   ::: answer
   Column decoder: column 1 = where $\begin{pmatrix}1\\0\end{pmatrix}$ lands, column 2 = where $\begin{pmatrix}0\\1\end{pmatrix}$ lands.
   a. $\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$ — both unit arrows land twice as far out.
   b. $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ — the $x$-arrow flips to $-1$, the $y$-arrow is untouched.
   c. $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ — the $x$-arrow is untouched, the $y$-arrow lands on $0$.
   :::

---

## Part C — Spot the error / shape diagnosis

8. "$M$ has shape $(2, 3)$: 2 columns, 3 rows."

   ::: answer
   Backwards. Shape is always (rows × columns), so $(2, 3)$ means **2 rows, 3 columns** — they swapped the convention.
   :::

9. "$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 \\ 6 \end{pmatrix} = \begin{pmatrix} 5 & 12 \\ 18 & 24 \end{pmatrix}$."
   What did this person do instead of the matrix product?

   ::: answer
   Shape check catches it immediately: $(2\times2)(2\times1)$ must give a $(2\times1)$ **vector**, not a $2\times2$ matrix.
   The real product is $\begin{pmatrix} 1(5)+2(6) \\ 3(5)+4(6) \end{pmatrix} = \begin{pmatrix} 17 \\ 39 \end{pmatrix}$ — row · vector each time.
   They multiplied entries in place instead (matrix entry × matching vector entry, kept separate) rather than
   summing each row's products into one number — never collapsing the row into a single dot product.
   :::

10. A student tries $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \end{pmatrix} \begin{pmatrix} 4 \\ 5 \end{pmatrix}$
    and numpy raises an error. Diagnose using shapes: what sizes collided, and what input *would* fit?

    ::: answer
    Matrix is $(2\times3)$, vector is $(2\times1)$. For a valid product the matrix's **columns** must match the
    vector's **rows**: $3 \ne 2$ — collision. A vector with 3 entries, e.g. $\begin{pmatrix} 4\\5\\6 \end{pmatrix}$
    (shape $3\times1$), would fit and give a $(2\times1)$ output.
    :::

---

## Part D — Deep end

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

11. Which matrix does nothing — sends every vector to itself? Use the column decoder,
    write it down, verify on $\begin{pmatrix} 3 \\ 7 \end{pmatrix}$.
    *(Its name: the identity matrix, $I$ — the matrix world's number 1.)*

    ::: rephrase
    You're being asked to build a machine, not compute one. The column decoder says: column 1
    is *where $\begin{pmatrix}1\\0\end{pmatrix}$ lands*, column 2 is *where $\begin{pmatrix}0\\1\end{pmatrix}$ lands*.
    "Does nothing" means every vector — including the two unit arrows — must come out exactly where
    it went in. So the whole question is: **where should the unit arrows land if nothing moves?**
    Write those two landing spots as the columns and you've built the machine. This is problem 7
    (build-a-machine from the decoder) with the simplest possible instruction.
    :::

    ::: hint
    Column 1 = where $\begin{pmatrix}1\\0\end{pmatrix}$ lands; column 2 = where $\begin{pmatrix}0\\1\end{pmatrix}$ lands.
    If the machine changes nothing, where does each unit arrow have to end up?
    :::

    ::: hint
    Each arrow must land on *itself*: $\begin{pmatrix}1\\0\end{pmatrix} \to \begin{pmatrix}1\\0\end{pmatrix}$
    and $\begin{pmatrix}0\\1\end{pmatrix} \to \begin{pmatrix}0\\1\end{pmatrix}$. Write those two vectors as the columns.
    :::

    ::: steps
    1. **Decode "does nothing" into the unit arrows.** $\begin{pmatrix}1\\0\end{pmatrix} \to \begin{pmatrix}1\\0\end{pmatrix}$, $\begin{pmatrix}0\\1\end{pmatrix} \to \begin{pmatrix}0\\1\end{pmatrix}$
    2. **Write the landing spots as columns.** $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$
    3. **Verify on $\begin{pmatrix}3\\7\end{pmatrix}$** (row $\cdot$ vector each time). $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 3 \\ 7 \end{pmatrix} = \begin{pmatrix} 1(3)+0(7) \\ 0(3)+1(7) \end{pmatrix} = \begin{pmatrix} 3 \\ 7 \end{pmatrix}$ — unchanged.
    :::

12. Every output of a matrix machine is dot products with the matrix's rows. Question 5's machines
    were fed one vector at a time. If you wanted to feed **all three houses of $M$** through a machine
    at once… you'd need to multiply a matrix by a matrix. What shape would the machine need to be
    to accept $M$'s rows? *(Sets up 2.5 — reason, don't compute.)*

    ::: rephrase
    No arithmetic here — it's pure shape-detective work. Remember the rule that made problems 5c
    and 10 work: a product is only legal when the **left thing's columns match the right thing's rows**
    (that's why the $(2\times3)$ matrix needed a 3-entry vector, not a 2-entry one). Now the "vector"
    being fed in is a whole matrix $A$. The question is just: for $M \cdot A$ to fit, what shape must $A$ be?
    :::

    ::: hint
    Reuse the shape-matching rule from problems 5c and 10: for $M \cdot A$, $A$'s **rows** must equal
    $M$'s **columns**. So first — how many columns does $M$ have?
    :::

    ::: hint
    $M$ is $(3\times3)$, so it has 3 columns. That forces $A$ to have 3 rows. A square machine that
    keeps each house as 3 features in, 3 out is $(3\times 3)$.
    :::

    ::: steps
    1. **Recall the shape rule.** left's columns $=$ right's rows.
    2. **Count $M$'s columns.** $M$ is $(3\times3)$ → 3 feature-columns per house-row.
    3. **Match $A$'s rows to that.** $A$ needs 3 rows, so the machine is $(3\times3)$ — the same shape-matching move as the vector case, just with the vector's single column replaced by $A$'s many columns.
    :::

13. The machine $\begin{pmatrix} 0.5 & 0 \\ 0 & 0.5 \end{pmatrix}$ is applied to a photo's pixel
    *coordinates*. What happens to the photo? What about $\begin{pmatrix} 1 & 0.5 \\ 0 & 1 \end{pmatrix}$
    (try the unit arrows)? *(You'll see this one lean in the notebook — it's called a shear.)*

    ::: rephrase
    Don't be thrown by "photo" — a photo is just a big cloud of coordinate-vectors (one per pixel),
    and a matrix moves *every* vector the same way (View 2, the machine). So you only have to figure
    out what each machine does to a typical arrow. For the first, read the numbers off the diagonal;
    for the second, feed it the two unit arrows and see where they land — exactly the move you did in
    problem 6, watching what a machine does to the plane.
    :::

    ::: hint
    First machine: it multiplies both coordinates by $0.5$. What does halving every point's coordinates
    do to its distance from the origin? Second machine: feed it $\begin{pmatrix}1\\0\end{pmatrix}$ and
    $\begin{pmatrix}0\\1\end{pmatrix}$ (as in problem 6) and compare where they land.
    :::

    ::: hint
    First: both coordinates halve, so the whole picture scales down by a factor of $\tfrac12$.
    Second: $\begin{pmatrix}1\\0\end{pmatrix}$ stays put, but $\begin{pmatrix}0\\1\end{pmatrix}$ picks up
    a sideways $0.5$ — the higher a point sits, the further it slides.
    :::

    ::: steps
    1. **Read the first machine as a scale** ($0.5$ down the diagonal $= 0.5I$). Every coordinate $\times 0.5$, so the photo **shrinks to half size**, evenly.
    2. **Feed the shear its unit arrows** (column decoder / problem 6). $\begin{pmatrix}1\\0\end{pmatrix} \to \begin{pmatrix}1\\0\end{pmatrix}$ (unchanged), $\begin{pmatrix}0\\1\end{pmatrix} \to \begin{pmatrix}0.5\\1\end{pmatrix}$ (pushed sideways).
    3. **Interpret the landings.** The bottom row of pixels stays put while higher rows slide right — the photo **shears/leans over**, like italic text.
    :::

---

## Part E — Python check (after the pen work)

14. In notebook `04-matrices.ipynb`, verify Part B with `@`, then watch your Part D-13 shear
    transform an actual shape. Mark ✓ here for each match.
