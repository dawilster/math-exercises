# Worksheet 5.5 — Convolutions

*Pen and paper. Draw the kernel's position on the image for at least your first two dot products —
seeing the overlap is half the skill. Name the move each time ("dot product of kernel and patch").
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up

1. One stop of the slide: kernel $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ sitting on patch
   $\begin{pmatrix} 5 & 2 \\ 3 & 1 \end{pmatrix}$. Multiply matching entries, sum. One number.

2. Output-size rule ($n - k + 1$ per side): what size feature map comes from
   (a) a $5{\times}5$ image with a $3{\times}3$ kernel, (b) $7{\times}7$ with $3{\times}3$,
   (c) $28{\times}28$ with $5{\times}5$ (the classic MNIST digit size)?

3. How many *positions* does a $3{\times}3$ kernel visit on a $6{\times}6$ image in total?

4. The lesson's vertical-edge kernel computes "left column − right column". Write the $3{\times}3$
   kernel that computes "top row − bottom row". What kind of edge does it detect?

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

6. Every entry in your answer's middle rows should be $-3$. Explain the minus sign: what is this
   kernel's sign *telling* you about the edge? (Compare: the lesson's edge scored $+3$.)

7. Where in the feature map did the detector go silent, and why does that match the picture?

8. Convolve the same $I$ with the lesson's *vertical*-edge kernel (columns version). Predict before
   computing: what should a vertical-edge detector say about an image with only a horizontal edge?
   Then confirm with two or three sample dot products.

---

## Part C — Spot the error

Circle the broken move; name the rule it broke.

9. Claimed: "a $3{\times}3$ kernel on a $5{\times}5$ image gives a $5{\times}5$ output — one number
   per pixel." What rule does this break, and what extra trick (mentioned in the lesson) would make
   it true?

10. Claimed first entry of a convolution, kernel $\begin{pmatrix} 1 & 0 & -1 \\ 1 & 0 & -1 \\ 1 & 0 & -1 \end{pmatrix}$ on an all-ones patch:
    - line 1: "sum the kernel entries that touch the patch: $1+0-1+1+0-1+1+0-1$"
    - line 2: "$= 0$... wait, actually since the patch is all ones I'll just count the kernel's
      positive entries: answer $3$."

11. A friend convolves a $4{\times}4$ image with a $3{\times}3$ kernel and reports the output entry
    at position $(2, 3)$ — row 2, column 3 of the feature map. Without seeing any numbers, how do
    you know something's wrong?

---

## Part D — Deep end

12. **The blur.** Apply the all-$\frac{1}{9}$ kernel to the centre position of
    $\begin{pmatrix} 0 & 0 & 0 \\ 0 & 9 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ (a single bright pixel).
    What happened to the spike? Which Module 4.2 statistic did this kernel compute, and why does
    averaging = blurring?

13. **Design your own detector.** Invent a $3{\times}3$ kernel that responds strongly to a lone
    bright pixel surrounded by darkness, and weakly (ideally 0) to any flat region. *(Hint: for
    silence on flat regions, what must the kernel's entries sum to?)*

14. In a CNN, the kernel entries are **weights, learned by backprop** (5.3). A convolution output
    is a sum of (weight × pixel) terms — structurally the same as the $W\mathbf{x}$ in 5.1. So:
    a $3{\times}3$ kernel scanning a whole $28{\times}28$ image uses how many distinct weights?
    A fully-connected layer mapping all 784 pixels to ONE output uses how many? Write one sentence
    on what convolution buys you.

15. What might TWO convolutions in a row see — e.g. an edge detector applied to the *output* of an
    edge detector? No computation needed; speculate in a sentence. (This "features of features"
    idea is literally why deep vision networks are deep.)

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
