# Worksheet 2.4 — Matrices: Tables and Machines

*Pen and paper. Say shapes out loud as (rows × columns) every single time.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: reading the grid

Use $\;M = \begin{pmatrix} 3 & 2 & 650 \\ 4 & 2 & 700 \\ 9 & 7 & 4000 \end{pmatrix}$ —
houses as rows, features (beds, baths, land m²) as columns.

1. What is the shape of $M$?

2. Write down row 2 (math counting: the second row). As a data table, what does it represent?

3. Write down column 3. What does *it* represent?

4. What would Python's `M[0]` and `M[:, 1]` give? *(Careful — Python counts from 0.)*

---

## Part B — Core: feed the machine

5. Compute, naming each step "row $i$ · vector":

   a. $\begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$
   b. $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 3 \\ 2 \end{pmatrix}$
   c. $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix}$ — shape-check first: $(2\times3)(3\times1) = ?$

6. For matrix (b) above: feed it $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$ and $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$,
   sketch inputs and outputs, and describe in one word what this machine does to the plane.

7. Use the column decoder (columns = where the unit arrows land) to **write down** the matrix that:

   a. doubles every vector's length
   b. flips the plane left–right ($x \to -x$, $y$ unchanged)
   c. squashes everything flat onto the x-axis ($y \to 0$)

---

## Part C — Spot the error / shape diagnosis

8. "$M$ has shape $(2, 3)$: 2 columns, 3 rows."

9. "$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 \\ 6 \end{pmatrix} = \begin{pmatrix} 5 & 12 \\ 18 & 24 \end{pmatrix}$."
   What did this person do instead of the matrix product?

10. A student tries $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \end{pmatrix} \begin{pmatrix} 4 \\ 5 \end{pmatrix}$
    and numpy raises an error. Diagnose using shapes: what sizes collided, and what input *would* fit?

---

## Part D — Deep end

11. Which matrix does nothing — sends every vector to itself? Use the column decoder,
    write it down, verify on $\begin{pmatrix} 3 \\ 7 \end{pmatrix}$.
    *(Its name: the identity matrix, $I$ — the matrix world's number 1.)*

12. Every output of a matrix machine is dot products with the matrix's rows. Question 5's machines
    were fed one vector at a time. If you wanted to feed **all three houses of $M$** through a machine
    at once… you'd need to multiply a matrix by a matrix. What shape would the machine need to be
    to accept $M$'s rows? *(Sets up 2.5 — reason, don't compute.)*

13. The machine $\begin{pmatrix} 0.5 & 0 \\ 0 & 0.5 \end{pmatrix}$ is applied to a photo's pixel
    *coordinates*. What happens to the photo? What about $\begin{pmatrix} 1 & 0.5 \\ 0 & 1 \end{pmatrix}$
    (try the unit arrows)? *(You'll see this one lean in the notebook — it's called a shear.)*

---

## Part E — Python check (after the pen work)

14. In notebook `04-matrices.ipynb`, verify Part B with `@`, then watch your Part D-13 shear
    transform an actual shape. Mark ✓ here for each match.
