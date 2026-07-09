# Worksheet 2.6 — Images ARE Matrices

*Pen and paper — yes, we're drawing images by hand first, that's the point: pixels are just
numbers you can reason about. Shade 0 = black, 1 = white, 0.5 = grey.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: numbers ↔ pictures

1. Draw (shade) the image
   $\begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$
   on a 4×4 grid. Remember: row 0 at the **top**.

   ::: answer
   A 4×4 grid, black all round, with a white $2\times 2$ square in the centre (rows 1–2,
   columns 1–2). Move: read each entry as the shade of that cell, row 0 at the top.
   :::

2. Write the matrix for a 4×4 image that is black everywhere except a white **top row**.

   ::: answer
   $\begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$
   — move: row 0 is the top row (all 1s / white), every other row stays 0 (black).
   :::

3. An image has shape $(1080, 1920)$. Is it portrait or landscape? How many pixels in total?

   ::: answer
   Landscape — shape is (height, width), and $1920 > 1080$ (wider than tall).
   Total pixels: $1080 \times 1920 = 2{,}073{,}600$. Move: read shape as (rows, cols), multiply for area.
   :::

---

## Part B — Core: editing with arithmetic

Work on $\;P = \begin{pmatrix} 0.0 & 0.2 & 0.4 \\ 0.2 & 0.8 & 0.2 \\ 0.4 & 0.2 & 0.0 \end{pmatrix}$.

4. Compute the "brightness doubled" image $2P$, then clip to $[0,1]$. Which pixels blew out
   (lost information)?

   ::: answer
   $2P = \begin{pmatrix} 0.0 & 0.4 & 0.8 \\ 0.4 & 1.6 & 0.4 \\ 0.8 & 0.4 & 0.0 \end{pmatrix}$,
   clipped to $\begin{pmatrix} 0.0 & 0.4 & 0.8 \\ 0.4 & 1.0 & 0.4 \\ 0.8 & 0.4 & 0.0 \end{pmatrix}$.
   Only the centre pixel (was $0.8$, the brightest) blew out — it hit $1.6$ before clipping,
   so the ceiling swallows exactly how far past 1 it really was. Move: scalar multiply, then `np.clip`.
   :::

5. Compute the negative $1 - P$. Which pixel was brightest before, and which is brightest now?

   ::: answer
   $1-P = \begin{pmatrix} 1.0 & 0.8 & 0.6 \\ 0.8 & 0.2 & 0.8 \\ 0.6 & 0.8 & 1.0 \end{pmatrix}$.
   Brightest before: the centre pixel ($0.8$). Brightest now: the two corners $(0,0)$ and $(2,2)$
   (value $1.0$) — they were the darkest before ($0.0$). Move: the negative flips the brightness
   ranking, since it's $1$ minus each value.
   :::

6. Write the matrix for $P$ flipped upside-down (reverse the row order).
   Then $P$ flipped left-to-right. Which pixels didn't move in each case?

   ::: answer
   Both flips give $\begin{pmatrix} 0.4 & 0.2 & 0.0 \\ 0.2 & 0.8 & 0.2 \\ 0.0 & 0.2 & 0.4 \end{pmatrix}$
   here (a coincidence of this particular $P$). Move: up-down flip reverses row order, so the
   **middle row** ($0.2, 0.8, 0.2$) is the axis and doesn't move. Left-right flip reverses column
   order, so the **middle column** ($0.2, 0.8, 0.2$ down the centre) doesn't move.
   :::

7. Crop: write the $2\times 2$ sub-matrix of $P$'s top-left corner. In Python slice notation,
   is that `P[0:2, 0:2]` or `P[1:3, 1:3]`?

   ::: answer
   $\begin{pmatrix} 0.0 & 0.2 \\ 0.2 & 0.8 \end{pmatrix}$ — `P[0:2, 0:2]`.
   Move: slices are end-exclusive, so `0:2` grabs indices $0,1$ (the top-left two rows/cols).
   `P[1:3, 1:3]` would grab the bottom-right region instead.
   :::

---

## Part C — Spot the error

8. "To brighten, I did $P + 0.5$ everywhere. My bright pixels turned into 1.3 — numpy showed them
   as pure white, same as 1.0. Two originally-different pixels now look identical." What was lost,
   and what step was skipped?

   ::: answer
   Lost: the distinction between any values that land above 1 — clipping isn't reversible, so
   e.g. $0.9+0.5=1.4$ and $0.95+0.5=1.45$ both display as $1.0$, indistinguishable. Skipped step:
   deliberately checking for/handling the overflow (`np.clip`) *before* trusting the result,
   instead of letting numpy silently saturate the display.
   :::

9. "I wanted the pixel 2 across and 1 down from the top-left, so I wrote `img[2, 1]`."
   Which pixel did they actually get? Give the correct indexing.

   ::: answer
   They got the pixel **1 across, 2 down** — numpy indexes images as `[row, col]` = `[down, across]`,
   so `img[2, 1]` means row 2 (2 down), column 1 (1 across). Correct indexing for "2 across, 1 down"
   is `img[1, 2]`. Move: don't read index order as (x, y); it's (down, across).
   :::

10. "An RGB photo with height 600 and width 800 is an array of shape $(3, 600, 800)$… or was it
    $(600, 800, 3)$? Whatever, same thing." Why does the difference matter to code like
    `img[100, 200]`? *(Convention in this course: channels last — $(600, 800, 3)$.)*

    ::: answer
    With channels-last $(600, 800, 3)$, `img[100, 200]` indexes (row, col) and returns the full
    length-3 $(R,G,B)$ triple for that pixel — exactly what you want. With channels-first
    $(3, 600, 800)$, `img[100, 200]` would try to index the **channel** axis with 100, which only
    has 3 valid indices — error (or nonsense if it happened to work). Move: axis order defines what
    each index number means; mixing it up doesn't just look wrong, it breaks indexing.
    :::

---

## Part D — Deep end

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

11. Using only operations from this module, describe (in words or formulas) how to make a 50/50
    **blend** of two same-shape images $A$ and $B$. Which lesson-2.2 operation is doing the work?
    *(This is literally the crossfade in every video editor.)*

    ::: rephrase
    You have two images $A$ and $B$, same shape, and you want a third image that's "half of
    each". Ask it pixel by pixel: for one pixel, if $A$ says $0.8$ and $B$ says $0.2$, what's
    the halfway brightness? ($0.5$.) Whatever single formula does that for *one* pixel does it
    for *all* of them at once — that's the whole point of Part B: an operation on the matrix is
    the operation on every pixel simultaneously.
    :::

    ::: hint
    "Half of each" = take half of $A$, take half of $B$. What single operation from lesson 2.2
    turns $A$ into "half of $A$"?
    :::

    ::: hint
    Now you have two dimmed images, $0.5A$ and $0.5B$. Combine them into one — which operation
    lays two same-shape matrices on top of each other, pixel-for-pixel?
    :::

    ::: steps
    1. **Halve each image (scalar multiply, lesson 2.2).** $0.5A$ and $0.5B$
    2. **Add the two elementwise.** $\text{blend} = 0.5A + 0.5B$ (equivalently $\dfrac{A+B}{2}$) — the crossfade is nothing but a weighted elementwise sum.
    :::

12. Design on paper an $8 \times 8$ checkerboard matrix (alternating 0s and 1s). Now the challenge:
    the notebook builds one with `board[::2, ::2] = 1` and `board[1::2, 1::2] = 1`.
    Decode what `::2` and `1::2` select, and confirm it paints your board.

    ::: rephrase
    You already know `1:3` means "indices 1 and 2" (problem 7). This is the same slice notation
    with the third number switched on: `start:stop:step`. Leave `start`/`stop` blank and they
    mean "from the beginning" / "to the end", so `::2` reads "every index, stepping by 2". Your
    job is just to *list out* which indices `::2` and `1::2` actually land on for a row of length 8,
    then check those two paint-strokes reproduce the board you drew.
    :::

    ::: hint
    Write out the indices $0..7$. Starting at $0$ and stepping by $2$, circle the ones `::2` hits.
    Then starting at $1$ and stepping by $2$, circle the ones `1::2` hits.
    :::

    ::: hint
    `board[::2, ::2]` applies that row-pattern to *both* axes at once — it sets 1 at every
    (row from the first list, col from the second list) crossing. Ask: which cells $(r,c)$ get a 1
    from the two commands combined, and how do $r$ and $c$ relate there?
    :::

    ::: steps
    1. **Decode the slices.** `::2` selects every **even** index $(0,2,4,6)$; `1::2` selects every **odd** index $(1,3,5,7)$.
    2. **Read each paint command.** `board[::2, ::2]` sets 1 at every (even row, even col); `board[1::2, 1::2]` sets 1 at every (odd row, odd col).
    3. **Combine.** Cell $(r,c)$ is 1 exactly when $r$ and $c$ have the **same parity** — which alternates row-to-row and col-to-col, i.e. a checkerboard.
    :::

13. A grayscale gradient that fades 0 → 1 left-to-right, in one line of numpy. Sketch the idea:
    what should each *column* contain? Would every row be identical? What numpy trick from
    the notebooks so far makes an evenly-spaced run of numbers?

    ::: rephrase
    "Fades 0 → 1 left-to-right" means: leftmost column black ($0$), rightmost column white ($1$),
    and a smooth climb across the columns in between. Picture the fade image from the lesson —
    within any single column the brightness never changes (it's one shade top to bottom), and the
    *column position* is what sets that shade. So the real question is two smaller ones: what does
    one row look like, and how do you stack that same row down the whole image?
    :::

    ::: hint
    Focus on a single row first. It has to be an evenly-spaced run climbing from $0$ up to $1$
    across `width` numbers. Which numpy function builds an evenly-spaced run between two endpoints?
    :::

    ::: hint
    Every row is that *same* run (the fade doesn't change as you go down). So you need to repeat one
    row down all the rows — numpy's broadcasting/tiling copies it for free rather than looping.
    :::

    ::: steps
    1. **One row = an evenly-spaced run $0\to1$.** `np.linspace(0, 1, width)` builds it.
    2. **Every row is identical**, so stack (broadcast/tile) that run down every row to fill the image — a gradient that fades left-to-right.
    :::

---

## Part E — Python check (after the pen work)

14. In notebook `06-images-are-matrices.ipynb`, build $P$ with `np.array`, run your Part B edits
    (`2*P` with clip, `1-P`, `P[::-1]`, the crop) and `imshow` each. Mark ✓ per matching answer —
    and keep that notebook open, the boss project uses it.
