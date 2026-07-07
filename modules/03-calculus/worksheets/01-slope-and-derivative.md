# Worksheet 3.1 — Slope Everywhere

*Pen and paper. Write the **move you're making** next to each step ("substitute", "evaluate",
"divide by h"). A cheap calculator is fine for arithmetic — the moves are the point.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: lines first

Slope = rise over run. One computation each.

1. A line passes through $(1, 3)$ and $(4, 12)$. Slope?

   ::: answer
   Slope $= 3$ — move: $\frac{12 - 3}{4 - 1} = \frac{9}{3}$ (rise over run between the two points).
   :::

2. A line passes through $(0, 5)$ and $(10, 5)$. Slope? What does that number *say* about the line?

   ::: answer
   Slope $= 0$ — move: $\frac{5 - 5}{10 - 0} = \frac{0}{10}$. A slope of $0$ says the line is flat
   (horizontal): $y$ doesn't change at all as $x$ increases.
   :::

3. $f(x) = 4x - 7$. Compute $\frac{f(x+h) - f(x)}{h}$ for $h = 2$, then $h = 0.1$.
   Why do you get the same answer both times?

   ::: answer
   Both give $4$ — move: expand $f(x+h) - f(x) = 4h$, so $\frac{4h}{h} = 4$ regardless of $h$.
   Same answer both times because $f$ is a straight line: it has no curvature, so every secant
   (any two points) has the exact same slope as the line itself.
   :::

4. If the loss changes by $-0.06$ when a weight is nudged by $+0.01$, what is the sensitivity
   (rise over run)? Is loss going up or down as the weight increases?

   ::: answer
   Sensitivity $= \frac{-0.06}{0.01} = -6$ — move: rise over run, same as slope. Negative sign
   means loss is going **down** as the weight increases.
   :::

---

## Part B — Core: slope of a curve, by nudging

Use $\dfrac{f(x+h) - f(x)}{h}$ with $h = 0.1$. Name each move. Then write your *guess* for the
exact slope (the number your estimate is sneaking up on).

5. $f(x) = x^2$ at $x = 1$

   ::: answer
   Estimate $\frac{f(1.1) - f(1)}{0.1} = \frac{1.21 - 1}{0.1} = 2.1$ — move: substitute, evaluate,
   divide by $h$. Exact-slope guess: $2$.
   :::

6. $f(x) = x^2$ at $x = -2$   *(careful with signs — what does a negative answer mean about the curve there?)*

   ::: answer
   Estimate $\frac{f(-1.9) - f(-2)}{0.1} = \frac{3.61 - 4}{0.1} = -3.9$ — same moves, negative $x$.
   Exact-slope guess: $-4$. Negative means the curve is sloping **downward** there (still on the
   falling left branch of the parabola, heading toward the bottom at $x=0$).
   :::

7. $f(x) = x^3$ at $x = 2$

   ::: answer
   Estimate $\frac{f(2.1) - f(2)}{0.1} = \frac{9.261 - 8}{0.1} = 12.61$ — move: substitute, evaluate,
   divide by $h$. Exact-slope guess: $12$.
   :::

8. $f(x) = x^2$ at $x = 0$. Estimate, then answer: what does the curve *look like* at a point
   where the derivative is $0$?

   ::: answer
   Estimate $\frac{f(0.1) - f(0)}{0.1} = \frac{0.01 - 0}{0.1} = 0.1$ — exact-slope guess: $0$.
   At a point where the derivative is $0$ the curve is momentarily **flat** (horizontal tangent) —
   here, the bottom of the parabola.
   :::

---

## Part C — Spot the illegal move

Each "solution" contains exactly one broken move. Circle it and write what rule it broke.

9. Claimed: slope of $f(x) = x^2$ at $x = 3$.
   - line 1: $\frac{f(3.1) - f(3)}{h}$
   - line 2: $= \frac{9.61 - 9}{3}$   *(divided by the x-value)*
   - line 3: $= 0.203\overline{3}$

   ::: answer
   Line 2 is broken — it divided by $3$ (the $x$-value) instead of by $h = 0.1$. Correct:
   $\frac{9.61 - 9}{0.1} = 6.1$, which is sneaking up on the exact derivative $2(3) = 6$.
   :::

10. Claimed: slope of $f(x) = x^2$ at $x = 2$, "exactly, using $h = 0$":
    - line 1: $\frac{f(2+0) - f(2)}{0}$
    - line 2: $= \frac{4 - 4}{0} = \frac{0}{0}$
    - line 3: $= 1$, since anything divided by itself is 1

    ::: answer
    Line 3 is broken. "Anything divided by itself is 1" only holds for nonzero numbers —
    $\frac{0}{0}$ isn't $1$, it's undefined. That's exactly *why* we nudge with a tiny but
    nonzero $h$ and watch where the estimates head, instead of plugging in $h=0$ directly.
    The exact slope (found via that limit) is $2(2) = 4$.
    :::

11. Claimed: "$f(5) = 25$, so the derivative of $f(x)=x^2$ at $x = 5$ is $25$."
    What two different questions got mixed up?

    ::: answer
    $f(5) = 25$ is the **value** of the function at $x=5$ (how high the curve is).
    The derivative asks a different question — how **steep** the curve is there. Move:
    $f'(x) = 2x$, so $f'(5) = 10$, not $25$. Height and steepness are not the same thing.
    :::

---

## Part D — Deep end

*Not fully covered yet. Attempt anyway — wrong attempts with named moves beat blank space.*

12. Do the nudge algebraically: simplify $\dfrac{(x+h)^2 - x^2}{h}$ using Module 0 moves
    (expand, cancel, divide). You'll get an expression with an $h$ still in it.
    Now imagine $h$ tiny — what's left? You've just *derived* the derivative of $x^2$.

    ::: answer
    Move: expand $(x+h)^2 - x^2 = 2xh + h^2$, factor out $h$, then $\div h$:
    $\dfrac{h(2x+h)}{h} = 2x + h$. Shrink $h$ toward $0$ and you're left with $2x$ —
    the derivative of $x^2$.
    :::

13. Repeat problem 12 for $f(x) = x^2 + 5$. Compare with problem 12's answer.
    Why did the $+5$ vanish? (Think: what does adding 5 do to the *shape* of the graph?)

    ::: answer
    Same result: $2x + h \to 2x$. The $+5$ vanishes at the very first move — in
    $(x+h)^2 + 5 - (x^2+5)$ the two $5$s cancel immediately. A constant shifts the whole
    graph up or down without changing its steepness anywhere, so it never affects the slope.
    :::

14. Sketch (roughly) $f(x) = x^2 - 4x$. Using your Part D answers, find the $x$ where the
    derivative equals $0$. What is special about that spot on your sketch — and why might a
    "loss valley" be exactly the place where a derivative is zero?

    ::: answer
    Same nudge moves give derivative $2x - 4$. Setting it to $0$: $x = 2$ — move: $+4$ both
    sides then $\div 2$. That's the bottom (vertex) of the upward-opening parabola, where the
    tangent is horizontal. A "loss valley" floor is exactly this: the point gradient descent is
    hunting for, where the derivative is zero and you've stopped rolling downhill.
    :::

---

## Part E — Python check (at the computer, after the pen work)

15. Build the nudge machine and check every Part B answer:

```python
def derivative(f, x, h=0.1):
    return (f(x + h) - f(x)) / h

def f(x):
    return x**2

print(derivative(f, 1))          # compare with your problem 5
```

Then rerun with `h=1e-6` and watch each estimate sharpen toward your exact-slope guesses.
Write next to each Part B problem: ✓ if Python agreed.

> **Bonus thought:** keep shrinking — `h=1e-12`, `h=1e-15`. At some point the answers go *weird*.
> Tiny-but-not-too-tiny, it turns out. Ask Claude why when you next session.
