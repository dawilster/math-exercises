# Worksheet 5.5 — Convolutions

*Pen and paper. Draw the kernel's position on the image for at least your first two dot products —
seeing the overlap is half the skill. Name the move each time ("dot product of kernel and patch").
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up

1. One stop of the slide: kernel $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ sitting on patch
   $\begin{pmatrix} 5 & 2 \\ 3 & 1 \end{pmatrix}$. Multiply matching entries, sum. One number.

   ::: answer
   $4$ — move: elementwise multiply matching positions, then sum:
   $1(5) + 0(2) + 0(3) + (-1)(1) = 5 + 0 + 0 - 1 = 4$.
   :::

2. Output-size rule ($n - k + 1$ per side): what size feature map comes from
   (a) a $5{\times}5$ image with a $3{\times}3$ kernel, (b) $7{\times}7$ with $3{\times}3$,
   (c) $28{\times}28$ with $5{\times}5$ (the classic MNIST digit size)?

   ::: answer
   (a) $5-3+1=3$ → $3{\times}3$. (b) $7-3+1=5$ → $5{\times}5$. (c) $28-5+1=24$ → $24{\times}24$.
   Move: apply $n-k+1$ per side, every time.
   :::

3. How many *positions* does a $3{\times}3$ kernel visit on a $6{\times}6$ image in total?

   ::: answer
   $16$ positions — move: find the output size first ($6-3+1=4$ per side), *then* count
   positions as $4\times4=16$. (Not $6\times6$ — the kernel must fit entirely inside the image.)
   :::

4. The lesson's vertical-edge kernel computes "left column − right column". Write the $3{\times}3$
   kernel that computes "top row − bottom row". What kind of edge does it detect?

   ::: answer
   $\begin{pmatrix} 1 & 1 & 1 \\ 0 & 0 & 0 \\ -1 & -1 & -1 \end{pmatrix}$ — move: rotate the
   vertical kernel's idea 90°, swapping "columns" for "rows": top row $+1$s, bottom row $-1$s.
   Detects **horizontal edges** — boundaries that run left-right, like a horizon line.
   :::

---

## Part B — Core: full hand convolution

Image (a horizontal boundary: dark sky above, bright ground below) and your kernel from problem 4:

$$I = \begin{pmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
1 & 1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 & 1
\end{pmatrix}
\qquad
K = \begin{pmatrix}
1 & 1 & 1 \\
0 & 0 & 0 \\
-1 & -1 & -1
\end{pmatrix}$$

5. Compute the full $3{\times}3$ feature map $I * K$, showing the dot product for at least the
   first entry of each row.

   ::: answer
   $$I * K = \begin{pmatrix} -3 & -3 & -3 \\ -3 & -3 & -3 \\ 0 & 0 & 0 \end{pmatrix}$$
   Move: dot product of kernel and patch at each position. Row 0 (patch = image rows 0–2: sky,
   sky, ground): $(1{+}1{+}1)(0) + (0{+}0{+}0)(0) + (-1{-}1{-}1)(1) = 0 + 0 - 3 = -3$.
   Row 1 (patch = rows 1–3: sky, ground, ground): same pattern, top row hits sky ($0$), bottom
   row hits ground ($1$) → $-3$. Row 2 (patch = rows 2–4: ground, ground, ground): top row now
   hits ground too → $(1{+}1{+}1)(1) + 0 + (-1{-}1{-}1)(1) = 3 - 3 = 0$.
   :::

6. Every entry in your answer's middle rows should be $-3$. Explain the minus sign: what is this
   kernel's sign *telling* you about the edge? (Compare: the lesson's edge scored $+3$.)

   ::: answer
   The minus sign says brightness **increases** going top→bottom under the kernel (dark sky
   above, bright ground below) — the opposite polarity to the lesson's $+3$, where brightness
   *decreased* left→right (bright left, dark right). The sign tells you the *direction* of the
   transition, not just that one exists.
   :::

7. Where in the feature map did the detector go silent, and why does that match the picture?

   ::: answer
   The bottom row of the feature map (all $0$s) — move: that window (image rows 2–4) sits
   entirely inside the uniform "ground" region, so top row $-$ bottom row $= 1 - 1 = 0$ per
   column. No boundary under the kernel there, matching the flat part of the picture.
   :::

8. Convolve the same $I$ with the lesson's *vertical*-edge kernel (columns version). Predict before
   computing: what should a vertical-edge detector say about an image with only a horizontal edge?
   Then confirm with two or three sample dot products.

   ::: answer
   Predict: silence everywhere (all $0$s) — every row of $I$ is constant left-to-right, so a
   "left column − right column" detector has nothing to detect. Confirm: patch at $(0,0)$ (rows
   0–2, cols 0–2) $= \begin{pmatrix}0&0&0\\0&0&0\\1&1&1\end{pmatrix}$, dot with the vertical
   kernel gives $(1{-}1)(0)$ twice $+ (1{-}1)(1) = 0$; patch at $(2,0)$ (all-ground rows) gives
   $(1{-}1)(1)$ three times $= 0$. Move: elementwise multiply, sum — confirms the prediction.
   :::

---

## Part C — Spot the error

Circle the broken move; name the rule it broke.

9. Claimed: "a $3{\times}3$ kernel on a $5{\times}5$ image gives a $5{\times}5$ output — one number
   per pixel." What rule does this break, and what extra trick (mentioned in the lesson) would make
   it true?

   ::: answer
   Breaks the output-size rule $n-k+1$ (real size is $5-3+1=3$, i.e. $3{\times}3$, not
   $5{\times}5$) — the kernel can't be centred on border pixels without running off the image.
   The lesson's fix: **zero-pad** the border so the kernel can visit every pixel and the output
   stays $5{\times}5$.
   :::

10. Claimed first entry of a convolution, kernel $\begin{pmatrix} 1 & 0 & -1 \\ 1 & 0 & -1 \\ 1 & 0 & -1 \end{pmatrix}$ on an all-ones patch:
    - line 1: "sum the kernel entries that touch the patch: $1+0-1+1+0-1+1+0-1$"
    - line 2: "$= 0$... wait, actually since the patch is all ones I'll just count the kernel's
      positive entries: answer $3$."

    ::: answer
    Line 2 is broken. Line 1's move is actually correct — multiplying by $1$ changes nothing, so
    the dot product equals the sum of the kernel entries: $1+0-1+1+0-1+1+0-1=0$. Line 2 abandons
    that sum halfway and invents a new rule, "count only the positive entries", which throws away
    the negative terms instead of summing everything. Correct answer: $0$.
    :::

11. A friend convolves a $4{\times}4$ image with a $3{\times}3$ kernel and reports the output entry
    at position $(2, 3)$ — row 2, column 3 of the feature map. Without seeing any numbers, how do
    you know something's wrong?

    ::: answer
    Output size is $4-3+1=2$, so the feature map is only $2{\times}2$ — valid positions run
    $(0,0)$ to $(1,1)$ (or $(1,1)$ to $(2,2)$ if 1-indexed). Either way, index $3$ doesn't exist —
    the kernel would have to run off the edge of the image.
    :::

---

## Part D — Deep end

12. **The blur.** Apply the all-$\frac{1}{9}$ kernel to the centre position of
    $\begin{pmatrix} 0 & 0 & 0 \\ 0 & 9 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ (a single bright pixel).
    What happened to the spike? Which Module 4.2 statistic did this kernel compute, and why does
    averaging = blurring?

    ::: answer
    Only one valid position (the centre): $\frac19(0{+}0{+}0{+}0{+}9{+}0{+}0{+}0{+}0) = 1$. The
    spike of $9$ got spread into $1$ — diluted by its eight dark ($0$) neighbours. This is the
    **mean** (Module 4.2): averaging = blurring because it replaces every pixel with the average
    of its neighbourhood, smoothing away sharp spikes.
    :::

13. **Design your own detector.** Invent a $3{\times}3$ kernel that responds strongly to a lone
    bright pixel surrounded by darkness, and weakly (ideally 0) to any flat region. *(Hint: for
    silence on flat regions, what must the kernel's entries sum to?)*

    ::: answer
    e.g. $\begin{pmatrix} -1 & -1 & -1 \\ -1 & 8 & -1 \\ -1 & -1 & -1 \end{pmatrix}$ — move: make
    the entries sum to $0$ so a flat patch of value $v$ gives $8v - 8v = 0$ (silence), while a
    lone bright centre pixel gives a large $8\times(\text{spike})$ response with no cancelling
    neighbours to drag it down.
    :::

14. In a CNN, the kernel entries are **weights, learned by backprop** (5.3). A convolution output
    is a sum of (weight × pixel) terms — structurally the same as the $W\mathbf{x}$ in 5.1. So:
    a $3{\times}3$ kernel scanning a whole $28{\times}28$ image uses how many distinct weights?
    A fully-connected layer mapping all 784 pixels to ONE output uses how many? Write one sentence
    on what convolution buys you.

    ::: answer
    Convolution: $9$ distinct weights (the kernel entries), reused at every position. Fully
    connected: $784$ weights, one per pixel, none shared. Convolution buys you the same tiny
    detector applied everywhere instead of a unique weight per pixel — far fewer parameters for
    the same-sized input.
    :::

15. What might TWO convolutions in a row see — e.g. an edge detector applied to the *output* of an
    edge detector? No computation needed; speculate in a sentence. (This "features of features"
    idea is literally why deep vision networks are deep.)

    ::: answer
    Not raw edges anymore but "edges of edges" — combinations like corners, curves, or short
    line segments; stacking convolutions builds increasingly complex features layer by layer,
    which is exactly why deep vision networks are deep.
    :::

---

## Part E — Python check (at the computer, after the pen work)

16. Verify Part B with the honest-loops convolution:

```python
import numpy as np
I = np.array([[0,0,0,0,0], [0,0,0,0,0], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]], dtype=float)
K = np.array([[1,1,1], [0,0,0], [-1,-1,-1]], dtype=float)

out = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        patch = I[i:i+3, j:j+3]          # the window at (i, j) — slicing from Module 2.6
        out[i, j] = np.sum(patch * K)    # elementwise multiply, then Σ
print(out)                                # match your problem 5?
```

Tick ✓ if it matches, then run notebook `05-convolutions` for the real payoff: your kernels
finding edges in actual images.

> **Bonus thought:** swap in your problem-13 kernel and convolve an image you invent. Did it
> behave? If not, whose bug is it — the kernel's or your prediction's? (Both happen. Both teach.)
