# Worksheet 2.6 — Images ARE Matrices

*Pen and paper — yes, we're drawing images by hand first, that's the point: pixels are just
numbers you can reason about. Shade 0 = black, 1 = white, 0.5 = grey.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: numbers ↔ pictures

1. Draw (shade) the image
   $\begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$
   on a 4×4 grid. Remember: row 0 at the **top**.

2. Write the matrix for a 4×4 image that is black everywhere except a white **top row**.

3. An image has shape $(1080, 1920)$. Is it portrait or landscape? How many pixels in total?

---

## Part B — Core: editing with arithmetic

Work on $\;P = \begin{pmatrix} 0.0 & 0.2 & 0.4 \\ 0.2 & 0.8 & 0.2 \\ 0.4 & 0.2 & 0.0 \end{pmatrix}$.

4. Compute the "brightness doubled" image $2P$, then clip to $[0,1]$. Which pixels blew out
   (lost information)?

5. Compute the negative $1 - P$. Which pixel was brightest before, and which is brightest now?

6. Write the matrix for $P$ flipped upside-down (reverse the row order).
   Then $P$ flipped left-to-right. Which pixels didn't move in each case?

7. Crop: write the $2\times 2$ sub-matrix of $P$'s top-left corner. In Python slice notation,
   is that `P[0:2, 0:2]` or `P[1:3, 1:3]`?

---

## Part C — Spot the error

8. "To brighten, I did $P + 0.5$ everywhere. My bright pixels turned into 1.3 — numpy showed them
   as pure white, same as 1.0. Two originally-different pixels now look identical." What was lost,
   and what step was skipped?

9. "I wanted the pixel 2 across and 1 down from the top-left, so I wrote `img[2, 1]`."
   Which pixel did they actually get? Give the correct indexing.

10. "An RGB photo with height 600 and width 800 is an array of shape $(3, 600, 800)$… or was it
    $(600, 800, 3)$? Whatever, same thing." Why does the difference matter to code like
    `img[100, 200]`? *(Convention in this course: channels last — $(600, 800, 3)$.)*

---

## Part D — Deep end

11. Using only operations from this module, describe (in words or formulas) how to make a 50/50
    **blend** of two same-shape images $A$ and $B$. Which lesson-2.2 operation is doing the work?
    *(This is literally the crossfade in every video editor.)*

12. Design on paper an $8 \times 8$ checkerboard matrix (alternating 0s and 1s). Now the challenge:
    the notebook builds one with `board[::2, ::2] = 1` and `board[1::2, 1::2] = 1`.
    Decode what `::2` and `1::2` select, and confirm it paints your board.

13. A grayscale gradient that fades 0 → 1 left-to-right, in one line of numpy. Sketch the idea:
    what should each *column* contain? Would every row be identical? What numpy trick from
    the notebooks so far makes an evenly-spaced run of numbers?

---

## Part E — Python check (after the pen work)

14. In notebook `06-images-are-matrices.ipynb`, build $P$ with `np.array`, run your Part B edits
    (`2*P` with clip, `1-P`, `P[::-1]`, the crop) and `imshow` each. Mark ✓ per matching answer —
    and keep that notebook open, the boss project uses it.
