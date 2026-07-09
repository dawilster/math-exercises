# Worksheet 3.5 — Gradient Descent by Hand

*Pen and paper first — running the algorithm yourself, slowly, is what makes the Python version
feel obvious. Calculator fine. Name the move at each update ("slope here", "step downhill").
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: one step at a time

The update rule: $x_{\text{new}} = x - \eta \, f'(x)$.

1. $f(x) = x^2$, so $f'(x) = 2x$. From $x = 5$ with $\eta = 0.1$: compute ONE update step.

   ::: answer
   $x_{\text{new}} = 4$ — move: $x_{\text{new}} = x - \eta f'(x) = 5 - 0.1(10) = 4$.
   :::

2. Same setup, from $x = -5$. One step. Which *direction* did you move, and why does the
   minus sign in the rule get that right automatically?

   ::: answer
   $x_{\text{new}} = -4$ — moved right, toward $0$ (opposite direction from problem 1).
   Move: $x_{\text{new}} = x - \eta f'(x) = -5 - 0.1(-10) = -5 + 1 = -4$. The minus sign
   automatically flips: a negative slope makes $-\eta f'(x)$ positive (step right), a positive
   slope makes it negative (step left) — always downhill, no matter which side you start on.
   :::

3. $f(x) = x^2 - 6x$ (so $f'(x) = 2x - 6$). From $x = 5$, $\eta = 0.25$: one step.
   Toward what value is it heading? (Where is $f'(x) = 0$?)

   ::: answer
   $x_{\text{new}} = 5 - 0.25(4) = 4$ — move: $x_{\text{new}} = x - \eta f'(x)$. Heading toward
   $x = 3$, where $f'(x) = 2x - 6 = 0$.
   :::

4. If $f'(x) = 0$ exactly where you stand, what does the update rule do? Why is that the
   *right* behaviour?

   ::: answer
   $x_{\text{new}} = x - \eta \times 0 = x$ — no movement. That's correct: zero slope means the
   ground is locally flat (a candidate minimum), so there's no downhill direction left to step
   toward.
   :::

---

## Part B — Core: run the descent

5. $f(x) = x^2$, $\eta = 0.1$, start $x_0 = 4$. Compute $x_1, x_2, x_3, x_4$ (2-decimal
   accuracy). Beside each: the slope you felt and the step you took.

   ::: answer
   $x_1 = 3.20$ (slope $8.00$, step $-0.80$); $x_2 = 2.56$ (slope $6.40$, step $-0.64$);
   $x_3 = 2.05$ (slope $5.12$, step $-0.51$); $x_4 = 1.64$ (slope $4.10$, step $-0.41$).
   Move each time: $x_{\text{new}} = x - \eta f'(x)$ with $f'(x) = 2x$.
   :::

6. Same $f$, same start, but $\eta = 0.5$. Compute $x_1$ and $x_2$. Something dramatic
   happens — describe it in one sentence.

   ::: answer
   $x_1 = 4 - 0.5(8) = 0$; $x_2 = 0 - 0.5(0) = 0$ — it lands exactly on the minimum in a single
   step and then stays there forever. Move: $x_{\text{new}} = x - \eta f'(x) = (1-2\eta)x$;
   here $\eta = 0.5$ makes $(1-2\eta) = 0$.
   :::

7. Same $f$, same start, $\eta = 1.1$. Compute $x_1, x_2, x_3$. Name this failure mode.

   ::: answer
   $x_1 = 4 - 1.1(8) = -4.8$; $x_2 = -4.8 - 1.1(-9.6) = 5.76$; $x_3 = 5.76 - 1.1(11.52) = -6.912$.
   Failure mode: **divergence** — the update overshoots further each step because
   $|1-2\eta| = |1-2.2| = 1.2 > 1$, so the distance from the minimum grows instead of shrinking.
   :::

8. Same $f$, same start, $\eta = 0.01$. Compute $x_1$ and $x_2$. Roughly how many steps to
   get near the minimum at this rate? (Feel, don't prove — each step keeps $98\%$ of the
   distance.)

   ::: answer
   $x_1 = 4 - 0.01(8) = 3.92$; $x_2 = 3.92 - 0.01(7.84) = 3.84$. Move: $x_{\text{new}} =
   (1-2\eta)x$ with $1-2\eta = 0.98$. Feel: since each step only shaves off $2\%$ of the
   remaining distance, it takes on the order of **hundreds** of steps to get near the minimum —
   much slower than problem 5's $\eta = 0.1$.
   :::

---

## Part C — Spot the illegal move

Circle the broken line, name what broke.

9. Claimed descent on $f(x) = x^2$ from $x = 3$, $\eta = 0.1$:
   - line 1: $f'(3) = 6$
   - line 2: $x_1 = 3 + 0.1 \times 6 = 3.6$
   - line 3: $x_2 = 3.6 + 0.1 \times 7.2 = 4.32$ — "hmm, loss keeps rising, must need more steps"

   ::: answer
   Line 2 is broken (and line 3 repeats the mistake). The rule is $x_{\text{new}} = x -
   \eta f'(x)$; they **added** instead of subtracted, which is gradient **ascent**, not descent —
   climbing the hill on purpose. That's why the loss keeps rising; it isn't "needing more steps",
   it's moving the wrong way. Correct: $x_1 = 3 - 0.1(6) = 2.4$.
   :::

10. Claimed descent on $f(x) = x^2 - 8x$ from $x = 1$, $\eta = 0.1$:
    - line 1: $f'(x) = 2x - 8$
    - line 2: $x_1 = 1 - 0.1 \times f(1) = 1 - 0.1 \times (-7) = 1.7$
    - line 3: $x_2 = 1.7 - 0.1 \times f(1.7)\ldots$
    *(look closely at WHAT is being plugged into the update)*

    ::: answer
    Line 2 is broken: it plugs in $f(1) = 1 - 8 = -7$ (the function's **value**) instead of
    $f'(1) = 2(1) - 8 = -6$ (the **slope**). Gradient descent steps using the derivative, never
    the loss value itself. Correct: $x_1 = 1 - 0.1(-6) = 1.6$.
    :::

11. Claimed: "I'll speed things up by updating with $\eta = 0.1$ but skipping the derivative:
    $x_{\text{new}} = x - 0.1$, every step, until the loss stops improving."
    What behaviour does this lose that real gradient descent has? (Two things — think about
    steep vs flat ground, and overshooting.)

    ::: answer
    Two things: **(1) direction** — the real rule's $f'(x)$ carries a sign that says which way is
    downhill; a fixed $-0.1$ every step assumes downhill is always "left", so starting on the
    other side of the minimum it walks away forever instead of toward it. **(2) step sizing** —
    real steps shrink automatically as the slope flattens near the minimum ($f'(x) \to 0$),
    letting it settle there; a fixed $0.1$ step never shrinks, so it just oscillates around the
    minimum (or crawls slowly on steep ground) and never truly stops.
    :::

---

## Part D — Deep end

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

12. Two-parameter bowl: $f(w, b) = w^2 + b^2$, so $\nabla f = (2w, 2b)$.
    From $(w, b) = (4, 2)$ with $\eta = 0.25$, run TWO full updates of
    $(w, b) \leftarrow (w, b) - \eta \nabla f$. Plot the three points on a rough sketch
    with contour circles. What shape is the path making toward the origin?

    ::: rephrase
    Same downhill rule as Part B — but now you carry **two** numbers at once. The gradient
    $(2w, 2b)$ is just "the slope in the $w$-direction and the slope in the $b$-direction, side
    by side". So run problem 5's descent twice in parallel: step $w$ by its slope, step $b$ by
    its slope, each update. First move: apply $x_{\text{new}} = x - \eta f'(x)$ to $w$ and to $b$
    separately.
    :::

    ::: hint
    You have one copy of the update rule per coordinate. Update $w$ using slope $2w$, and
    *independently* update $b$ using slope $2b$ — they don't interact.
    :::

    ::: hint
    With $\eta = 0.25$ each coordinate becomes $(1 - 2\eta) = 0.5$ times itself. So the whole
    move is just "**halve both numbers**" each step.
    :::

    ::: steps
    1. **Update each coordinate by its own slope.** $(w,b) \leftarrow (w,b) - 0.25(2w,2b) = (1-2\eta)(w,b) = 0.5\,(w,b)$
    2. **First step from $(4,2)$** — halve both. $(4,2) \to (2,1)$
    3. **Second step from $(2,1)$** — halve again. $(2,1) \to (1,0.5)$
    4. **Read the path.** The three points $(4,2),(2,1),(1,0.5)$ lie on a straight line through the origin — the bowl is symmetric in $w$ and $b$, so the gradient always points directly at the centre.
    :::

13. From lesson 3.5's deep end: for $f(x)=x^2$ the update collapses to
    $x_{\text{new}} = (1 - 2\eta)\,x$. Using Module 0 algebra, find the range of $\eta$ for which
    $|1 - 2\eta| < 1$ (steps shrink). What happens exactly at $\eta = 0.5$? At $\eta = 1$?

    ::: rephrase
    Every step multiplies your position by the *fixed* number $(1-2\eta)$. For the position to
    shrink toward $0$, that multiplier has to be smaller than $1$ **in size** — which is exactly
    what $|1-2\eta| < 1$ says. So this isn't calculus at all: it's a pure Module 0 absolute-value
    inequality. Unwrap the $|\cdots|$ into a double inequality and solve for $\eta$, then plug the
    two special $\eta$ values into the multiplier to see what it does.
    :::

    ::: hint
    An absolute-value inequality $|A| < 1$ means $A$ is trapped between $-1$ and $1$. Write it as
    $-1 < 1 - 2\eta < 1$.
    :::

    ::: hint
    Solve the double inequality for $\eta$: subtract $1$ from all three parts, then divide by
    $-2$ — and remember dividing by a negative **flips both** inequality signs.
    :::

    ::: steps
    1. **Unwrap the absolute value.** $-1 < 1 - 2\eta < 1$
    2. **Subtract $1$ from all three parts.** $-2 < -2\eta < 0$
    3. **Divide by $-2$ (flips both signs).** $0 < \eta < 1$
    4. **Check $\eta = 0.5$.** $1 - 2(0.5) = 0$, so $x_{\text{new}} = 0 \cdot x = 0$ — lands exactly on the minimum in one step (problem 6).
    5. **Check $\eta = 1$.** $1 - 2(1) = -1$, so $x_{\text{new}} = -x$ — bounces forever between $x$ and $-x$: the boundary between shrinking and diverging.
    :::

14. Sketch a wavy curve with two valleys, one deeper than the other. Mark two starting points
    that end up in *different* valleys under gradient descent. One sentence: why can't the
    algorithm "see" the deeper valley from inside the shallow one?

    ::: rephrase
    Nothing to compute here — this is a "what can gradient descent actually *see*?" question. Sketch
    a curve with two dips (right one deeper), drop a ball at two spots, ask whether they always roll
    to the same bottom. Look back at the rule $x_{\text{new}} = x - \eta f'(x)$: the only thing it
    ever reads about the whole landscape is $f'(x)$ — the slope *right where it stands*.
    :::

    ::: hint
    The update never evaluates the curve anywhere except your current $x$ — it feels one local
    slope and steps. It has no memory of where it's been and no view of what's ahead.
    :::

    ::: hint
    So place your two starting dots on **opposite sides of the hump** separating the valleys — each
    one feels a slope pointing back down into its own dip.
    :::

    ::: steps
    1. **Mark two starts across the ridge.** A dot in the left (shallow) valley and a dot in the right (deep) valley; each feels a local slope pointing back down into the valley it started in.
    2. **Why it's blind.** Gradient descent only ever feels the **local slope** at its current $x$ — no memory, no view of the rest of the curve — so once inside a valley the slope always points back to that valley's own bottom, with no way to sense a deeper valley beyond the hump between them.
    :::

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
