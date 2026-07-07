# Worksheet 3.5 — Gradient Descent by Hand

*Pen and paper first — running the algorithm yourself, slowly, is what makes the Python version
feel obvious. Calculator fine. Name the move at each update ("slope here", "step downhill").
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: one step at a time

The update rule: $x_{\text{new}} = x - \eta \, f'(x)$.

1. $f(x) = x^2$, so $f'(x) = 2x$. From $x = 5$ with $\eta = 0.1$: compute ONE update step.

2. Same setup, from $x = -5$. One step. Which *direction* did you move, and why does the
   minus sign in the rule get that right automatically?

3. $f(x) = x^2 - 6x$ (so $f'(x) = 2x - 6$). From $x = 5$, $\eta = 0.25$: one step.
   Toward what value is it heading? (Where is $f'(x) = 0$?)

4. If $f'(x) = 0$ exactly where you stand, what does the update rule do? Why is that the
   *right* behaviour?

---

## Part B — Core: run the descent

5. $f(x) = x^2$, $\eta = 0.1$, start $x_0 = 4$. Compute $x_1, x_2, x_3, x_4$ (2-decimal
   accuracy). Beside each: the slope you felt and the step you took.

6. Same $f$, same start, but $\eta = 0.5$. Compute $x_1$ and $x_2$. Something dramatic
   happens — describe it in one sentence.

7. Same $f$, same start, $\eta = 1.1$. Compute $x_1, x_2, x_3$. Name this failure mode.

8. Same $f$, same start, $\eta = 0.01$. Compute $x_1$ and $x_2$. Roughly how many steps to
   get near the minimum at this rate? (Feel, don't prove — each step keeps $98\%$ of the
   distance.)

---

## Part C — Spot the illegal move

Circle the broken line, name what broke.

9. Claimed descent on $f(x) = x^2$ from $x = 3$, $\eta = 0.1$:
   - line 1: $f'(3) = 6$
   - line 2: $x_1 = 3 + 0.1 \times 6 = 3.6$
   - line 3: $x_2 = 3.6 + 0.1 \times 7.2 = 4.32$ — "hmm, loss keeps rising, must need more steps"

10. Claimed descent on $f(x) = x^2 - 8x$ from $x = 1$, $\eta = 0.1$:
    - line 1: $f'(x) = 2x - 8$
    - line 2: $x_1 = 1 - 0.1 \times f(1) = 1 - 0.1 \times (-7) = 1.7$
    - line 3: $x_2 = 1.7 - 0.1 \times f(1.7)\ldots$
    *(look closely at WHAT is being plugged into the update)*

11. Claimed: "I'll speed things up by updating with $\eta = 0.1$ but skipping the derivative:
    $x_{\text{new}} = x - 0.1$, every step, until the loss stops improving."
    What behaviour does this lose that real gradient descent has? (Two things — think about
    steep vs flat ground, and overshooting.)

---

## Part D — Deep end

12. Two-parameter bowl: $f(w, b) = w^2 + b^2$, so $\nabla f = (2w, 2b)$.
    From $(w, b) = (4, 2)$ with $\eta = 0.25$, run TWO full updates of
    $(w, b) \leftarrow (w, b) - \eta \nabla f$. Plot the three points on a rough sketch
    with contour circles. What shape is the path making toward the origin?

13. From lesson 3.5's deep end: for $f(x)=x^2$ the update collapses to
    $x_{\text{new}} = (1 - 2\eta)\,x$. Using Module 0 algebra, find the range of $\eta$ for which
    $|1 - 2\eta| < 1$ (steps shrink). What happens exactly at $\eta = 0.5$? At $\eta = 1$?

14. Sketch a wavy curve with two valleys, one deeper than the other. Mark two starting points
    that end up in *different* valleys under gradient descent. One sentence: why can't the
    algorithm "see" the deeper valley from inside the shallow one?

---

## Part E — Python check (at the computer, after the pen work)

15. Automate Part B and check your hand-run numbers:

```python
x = 4.0
lr = 0.1
for step in range(4):
    slope = 2 * x            # f'(x) for x²
    x = x - lr * slope
    print(f"step {step+1}: x = {x:.2f}")   # f-string: puts values inside text, .2f = 2 decimals
```

Compare with problem 5. Then set `lr = 1.1` and rerun — watch problem 7's explosion happen
live. Write ✓ next to each Part B run Python confirmed.

> **Bonus thought:** change the slope line to `slope = 2*x - 6` (problem 3's function) and
> start from `x = 0.0`. Where does it settle? You never told it the answer — it *found*
> the bottom of a function it has never "seen". Sit with how strange and wonderful that is.
> The notebook turns this into pictures.
