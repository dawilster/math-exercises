# Worksheet 3.4 — Partials & the Gradient

*Pen and paper. When taking a partial, first write down **who's frozen** — it prevents the
classic slip. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: freeze and differentiate

For each, find $\dfrac{\partial f}{\partial x}$ AND $\dfrac{\partial f}{\partial y}$.
Write "freeze $y$" / "freeze $x$" before each one.

1. $f(x, y) = x^2 + y^2$

2. $f(x, y) = 5xy$

3. $f(x, y) = x^3 + 2y$

4. $f(x, y) = 7$   *(what does it mean that both partials are what they are?)*

---

## Part B — Core: gradients at a point

For each: find $\nabla f$ as a vector of partials, then evaluate it at the given point.
State which input the output is *more sensitive to* there.

5. $f(x, y) = x^2 + y^2$ at $(3, 1)$

6. $f(x, y) = x^2 y$ at $(2, 5)$

7. $f(x, y) = x^2 - 4x + y^2 - 2y$ at $(1, 1)$. Then find the point where $\nabla f = (0, 0)$
   — the flat spot. (Set both partials to zero; two small balance games.)

8. $L(w, b) = (2w + b - 7)^2$ — a real one-data-point loss: prediction $2w + b$, target $7$.
   Use the chain rule from 3.3 for each partial (inner: $2w + b - 7$). Find $\nabla L$ at
   $(w, b) = (1, 1)$.

---

## Part C — Spot the illegal move

Circle the broken line, name what broke.

9. Claimed: $\dfrac{\partial}{\partial x}\left(3xy + y^2\right)$
   - line 1: $= 3y \cdot 1 + 2y$   *(differentiated everything in sight)*

10. Claimed: $f(x,y) = x^2 + y^2$ at $(1, 2)$, so $\nabla f(1,2) = (2, 4)$.
    "To decrease $f$ fastest, step in the direction $(2, 4)$."

11. Claimed: $\dfrac{\partial}{\partial y}\left(x^2 y^3\right)$
    - line 1: freeze $x$
    - line 2: $= x^2 \cdot 3y^2$
    - line 3: $= 3x^2 y^2$, "so at any point on the $x$-axis (where $y = 0$) the function is
      completely insensitive to $x$ as well, since the whole gradient must be zero there."

---

## Part D — Deep end: read the loss surface

12. Sketch rough contour circles for $f(x, y) = x^2 + y^2$ (they're circles centred at the
    origin — label contours $f = 1, 4, 9$). Draw the gradient arrow at $(2, 0)$, at $(0, 3)$,
    and at $(1, 1)$ (direction only). What do all three arrows do relative to the contour
    they sit on?

13. On your sketch: standing at $(2, 2)$, a friend proposes walking in direction $(-1, 1)$.
    Roughly what happens to the height? (Hint: is that direction along a contour, uphill,
    or downhill?)

14. A loss surface has $\nabla L = (0.001, \; 40)$ at the current weights.
    In plain words: which weight is the training signal *screaming* about, and which one
    barely matters right now?

15. True or false, with one sentence: "if $\nabla f = (0,0)$ at a point, that point must be
    the lowest point of the surface." (Think about hilltops. And saddles, if you dare.)

---

## Part E — Python check (at the computer, after the pen work)

16. Check Part B by nudging one input at a time:

```python
def f(x, y):
    return x**2 + y**2

h = 1e-6
point = (3, 1)                    # problem 5
df_dx = (f(point[0] + h, point[1]) - f(*point)) / h   # f(*point) unpacks the pair
df_dy = (f(point[0], point[1] + h) - f(*point)) / h
print(df_dx, df_dy)               # compare with your ∇f(3, 1)
```

Repeat for problems 6–8 (edit `f` and `point`). Write ✓ next to each confirmed gradient.

> **Bonus thought:** sympy speaks partials too: `sp.diff(x**2 * y, x)` where
> `x, y = sp.symbols("x y")`. Get it to confirm problem 8 — chain rule and all.
