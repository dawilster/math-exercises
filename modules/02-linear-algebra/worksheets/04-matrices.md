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

11. Which matrix does nothing — sends every vector to itself? Use the column decoder,
    write it down, verify on $\begin{pmatrix} 3 \\ 7 \end{pmatrix}$.
    *(Its name: the identity matrix, $I$ — the matrix world's number 1.)*

    ::: answer
    $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ — each unit arrow lands on itself.
    Check: $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 3 \\ 7 \end{pmatrix} = \begin{pmatrix} 1(3)+0(7) \\ 0(3)+1(7) \end{pmatrix} = \begin{pmatrix} 3 \\ 7 \end{pmatrix}$ — unchanged.
    :::

12. Every output of a matrix machine is dot products with the matrix's rows. Question 5's machines
    were fed one vector at a time. If you wanted to feed **all three houses of $M$** through a machine
    at once… you'd need to multiply a matrix by a matrix. What shape would the machine need to be
    to accept $M$'s rows? *(Sets up 2.5 — reason, don't compute.)*

    ::: answer
    $M$ is $(3\times3)$ with 3 feature-columns per house-row. To multiply $M \cdot A$, $A$'s **rows** must match
    $M$'s **columns** (3), so the machine $A$ needs to be $(3\times3)$ — same shape-matching move as the
    vector case, just with the vector's single column replaced by $A$'s many columns.
    :::

13. The machine $\begin{pmatrix} 0.5 & 0 \\ 0 & 0.5 \end{pmatrix}$ is applied to a photo's pixel
    *coordinates*. What happens to the photo? What about $\begin{pmatrix} 1 & 0.5 \\ 0 & 1 \end{pmatrix}$
    (try the unit arrows)? *(You'll see this one lean in the notebook — it's called a shear.)*

    ::: answer
    $\begin{pmatrix} 0.5 & 0 \\ 0 & 0.5 \end{pmatrix} = 0.5I$ scales both coordinates by a half — the photo
    **shrinks to half size**, evenly.
    For $\begin{pmatrix} 1 & 0.5 \\ 0 & 1 \end{pmatrix}$: $\begin{pmatrix}1\\0\end{pmatrix} \to \begin{pmatrix}1\\0\end{pmatrix}$
    (unchanged) but $\begin{pmatrix}0\\1\end{pmatrix} \to \begin{pmatrix}0.5\\1\end{pmatrix}$ (pushed sideways).
    The bottom row of pixels stays put while higher rows slide right — the photo **shears/leans over**, like italic text.
    :::

---

## Part E — Python check (after the pen work)

14. In notebook `04-matrices.ipynb`, verify Part B with `@`, then watch your Part D-13 shear
    transform an actual shape. Mark ✓ here for each match.
