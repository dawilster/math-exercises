# Worksheet 3.4 — Partials & the Gradient

*Pen and paper. When taking a partial, first write down **who's frozen** — it prevents the
classic slip. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: freeze and differentiate

For each, find $\dfrac{\partial f}{\partial x}$ AND $\dfrac{\partial f}{\partial y}$.
Write "freeze $y$" / "freeze $x$" before each one.

1. $f(x, y) = x^2 + y^2$

   ::: answer
   $\dfrac{\partial f}{\partial x} = 2x$ (freeze $y$), $\dfrac{\partial f}{\partial y} = 2y$ (freeze $x$).
   :::

2. $f(x, y) = 5xy$

   ::: answer
   $\dfrac{\partial f}{\partial x} = 5y$ — move: freeze $y$, it's now just a constant multiplier on $x$.
   $\dfrac{\partial f}{\partial y} = 5x$ — move: freeze $x$ instead.
   :::

3. $f(x, y) = x^3 + 2y$

   ::: answer
   $\dfrac{\partial f}{\partial x} = 3x^2$ — move: freeze $y$, so $2y$ is a constant and differentiates to $0$.
   $\dfrac{\partial f}{\partial y} = 2$ — move: freeze $x$, so $x^3$ is a constant and differentiates to $0$.
   :::

4. $f(x, y) = 7$   *(what does it mean that both partials are what they are?)*

   ::: answer
   $\dfrac{\partial f}{\partial x} = 0$, $\dfrac{\partial f}{\partial y} = 0$ — move: freeze either variable,
   a constant's derivative is always $0$. Meaning: a flat, constant surface is equally
   (zero) sensitive to every input, everywhere.
   :::

---

## Part B — Core: gradients at a point

For each: find $\nabla f$ as a vector of partials, then evaluate it at the given point.
State which input the output is *more sensitive to* there.

5. $f(x, y) = x^2 + y^2$ at $(3, 1)$

   ::: answer
   $\nabla f = (2x, 2y)$, so $\nabla f(3,1) = (6, 2)$ — move: gradient is the vector of
   partials, then plug in the point. More sensitive to $x$ (component $6 > 2$).
   :::

6. $f(x, y) = x^2 y$ at $(2, 5)$

   ::: answer
   $\dfrac{\partial f}{\partial x} = 2xy$ (freeze $y$), $\dfrac{\partial f}{\partial y} = x^2$
   (freeze $x$). At $(2,5)$: $\nabla f = (20, 4)$ — move: substitute the point into each
   partial separately. More sensitive to $x$.
   :::

7. $f(x, y) = x^2 - 4x + y^2 - 2y$ at $(1, 1)$. Then find the point where $\nabla f = (0, 0)$
   — the flat spot. (Set both partials to zero; two small balance games.)

   ::: answer
   $\dfrac{\partial f}{\partial x} = 2x - 4$, $\dfrac{\partial f}{\partial y} = 2y - 2$.
   At $(1,1)$: $\nabla f = (-2, 0)$. Flat spot: solve $2x - 4 = 0$ and $2y - 2 = 0$
   separately (two small balance games) — move: set each partial to zero on its own,
   giving $(x, y) = (2, 1)$.
   :::

8. $L(w, b) = (2w + b - 7)^2$ — a real one-data-point loss: prediction $2w + b$, target $7$.
   Use the chain rule from 3.3 for each partial (inner: $2w + b - 7$). Find $\nabla L$ at
   $(w, b) = (1, 1)$.

   ::: answer
   Let $u = 2w + b - 7$; at $(1,1)$, $u = 2(1) + 1 - 7 = -4$. Move: chain rule outside-in,
   then freeze the other variable for the inner partial. $\dfrac{\partial L}{\partial w} =
   2u \cdot 2 = 4u = -16$ (inner derivative w.r.t. $w$ is $2$). $\dfrac{\partial L}{\partial b}
   = 2u \cdot 1 = 2u = -8$ (inner derivative w.r.t. $b$ is $1$). $\nabla L(1,1) = (-16, -8)$.
   :::

---

## Part C — Spot the illegal move

Circle the broken line, name what broke.

9. Claimed: $\dfrac{\partial}{\partial x}\left(3xy + y^2\right)$
   - line 1: $= 3y \cdot 1 + 2y$   *(differentiated everything in sight)*

   ::: answer
   Line 1 is broken. This is $\partial/\partial x$, so $y$ must be frozen:
   $\dfrac{\partial}{\partial x}(3xy) = 3y$, but $\dfrac{\partial}{\partial x}(y^2) = 0$
   (a frozen $y^2$ is just a constant) — not $2y$, which is the derivative w.r.t. $y$,
   the wrong variable. Correct: $3y$.
   :::

10. Claimed: $f(x,y) = x^2 + y^2$ at $(1, 2)$, so $\nabla f(1,2) = (2, 4)$.
    "To decrease $f$ fastest, step in the direction $(2, 4)$."

    ::: answer
    The gradient itself, $\nabla f(1,2) = (2,4)$, is correct. The broken move is the
    conclusion: $\nabla f$ points in the direction of **steepest increase**, not decrease.
    To decrease $f$ fastest, step in $-\nabla f = (-2, -4)$.
    :::

11. Claimed: $\dfrac{\partial}{\partial y}\left(x^2 y^3\right)$
    - line 1: freeze $x$
    - line 2: $= x^2 \cdot 3y^2$
    - line 3: $= 3x^2 y^2$, "so at any point on the $x$-axis (where $y = 0$) the function is
      completely insensitive to $x$ as well, since the whole gradient must be zero there."

    ::: answer
    Lines 1–3 are correct ($\partial f/\partial y = 3x^2y^2$). The broken move is the
    closing claim: knowing $\partial f/\partial y$ tells you nothing about $\partial
    f/\partial x$ — they're independent computations, each freezing a different variable.
    (It happens that $\partial f/\partial x = 2xy^3$ is also $0$ when $y = 0$, but that's a
    coincidence of this particular function, not something the argument actually earned.)
    :::

---

## Part D — Deep end: read the loss surface

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

12. Sketch rough contour circles for $f(x, y) = x^2 + y^2$ (they're circles centred at the
    origin — label contours $f = 1, 4, 9$). Draw the gradient arrow at $(2, 0)$, at $(0, 3)$,
    and at $(1, 1)$ (direction only). What do all three arrows do relative to the contour
    they sit on?

    ::: rephrase
    This one asks you to *draw*, not crunch. The "circles" $f = 1, 4, 9$ are just rings of
    equal height — the topographic map from the lesson. At each of the three spots you draw
    the little uphill arrow (the gradient). The real question is only: does that arrow lie
    *along* the ring or *across* it? Look back at the lesson figure where every red arrow
    crossed its contour at a right angle — that's the pattern you're checking here.
    :::

    ::: hint
    You have a formula for the gradient of $x^2 + y^2$: $\nabla f = (2x, 2y)$. Compute it at
    each of the three points — that vector *is* the arrow's direction.
    :::

    ::: hint
    Notice $(2x, 2y) = 2(x, y)$: every arrow is just a scaled copy of the line from the origin
    out to that point. Where does a spoke from a circle's centre sit relative to the circle?
    :::

    ::: steps
    1. **Write the gradient.** $\nabla f = (2x, 2y)$
    2. **Evaluate at each point (direction only).** $\nabla f(2,0) = (4,0)$, $\nabla f(0,3) = (0,6)$, $\nabla f(1,1) = (2,2)$
    3. **Read the pattern.** each equals $2(x, y)$ — points radially outward from the origin.
    4. **Name what that means.** the arrow is perpendicular (normal) to the contour circle it sits on, pointing toward increasing $f$.
    :::

13. On your sketch: standing at $(2, 2)$, a friend proposes walking in direction $(-1, 1)$.
    Roughly what happens to the height? (Hint: is that direction along a contour, uphill,
    or downhill?)

    ::: rephrase
    "What happens to the height" as you take a step = how steep that step is. One number
    measures it: the **dot product** of the gradient with the step direction (Module 2's dot
    product finally earning its keep). Positive means uphill, negative downhill, zero means
    flat — along the contour. So: find the gradient here, then dot it with $(-1, 1)$.
    :::

    ::: hint
    You need two vectors: the gradient at $(2,2)$, and the step $(-1,1)$. Find the gradient first.
    :::

    ::: hint
    Dot the two together. The *sign* of that single number tells you uphill $(+)$, downhill
    $(-)$, or along-the-contour $(0)$.
    :::

    ::: steps
    1. **Gradient at the point.** $\nabla f(2,2) = (2\cdot 2,\; 2\cdot 2) = (4,4)$
    2. **Dot it with the step direction.** $(4,4)\cdot(-1,1) = -4 + 4 = 0$
    3. **Read the sign.** zero → the step is tangent to the contour (perpendicular to the gradient).
    4. **Conclusion.** neither uphill nor downhill — the height barely changes, to first order.
    :::

14. A loss surface has $\nabla L = (0.001, \; 40)$ at the current weights.
    In plain words: which weight is the training signal *screaming* about, and which one
    barely matters right now?

    ::: rephrase
    The gradient is the list of each weight's *sensitivity* (from the lesson: $\nabla L$ =
    "how much the loss reacts to nudging each weight"). A big component means the loss is very
    sensitive to that weight — the signal is loud. So you're just comparing two numbers:
    $0.001$ versus $40$.
    :::

    ::: hint
    A gradient component's *size* (magnitude) is how loud the training signal is for that
    weight. Which of $0.001$ and $40$ is bigger?
    :::

    ::: steps
    1. **Compare the component magnitudes.** $0.001 \ll 40$
    2. **Read sensitivity from size.** partial $= 40$ → loss is very sensitive to the second weight; partial $= 0.001$ → the first weight barely matters.
    3. **Name it.** a gradient-descent step moves most along the largest component — the second weight is the one the training signal is screaming about.
    :::

15. True or false, with one sentence: "if $\nabla f = (0,0)$ at a point, that point must be
    the lowest point of the surface." (Think about hilltops. And saddles, if you dare.)

    ::: rephrase
    You're judging a claim, not computing. $\nabla f = (0,0)$ means every direction is flat
    right here — no uphill lean anywhere nearby. The question is whether "flat" is the same as
    "lowest". Picture the saddle from the lesson (the Pringle) and the top of a hill. One
    counterexample is enough to make a "must" statement false.
    :::

    ::: hint
    Think of the top of a hill: is the ground flat there? Is it the lowest point? That single
    picture settles true vs false.
    :::

    ::: hint
    Name the three kinds of flat spot the lesson mentioned — minimum, maximum, and the
    Pringle-shaped one — to pin down what zero gradient actually guarantees (and what it doesn't).
    :::

    ::: steps
    1. **Verdict.** False.
    2. **What zero gradient does mean.** $\nabla f = (0,0)$ → the point is *flat*, a critical point.
    3. **The counterexamples.** it could be a minimum, a maximum (hilltop), or a saddle (the lesson's Pringle).
    4. **What's actually needed to tell them apart.** how the surface curves — second derivatives; zero gradient alone can't distinguish them.
    :::

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
