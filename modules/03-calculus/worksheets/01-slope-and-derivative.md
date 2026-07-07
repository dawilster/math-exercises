# Worksheet 3.1 — Slope Everywhere

*Pen and paper. Write the **move you're making** next to each step ("substitute", "evaluate",
"divide by h"). A cheap calculator is fine for arithmetic — the moves are the point.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: lines first

Slope = rise over run. One computation each.

1. A line passes through $(1, 3)$ and $(4, 12)$. Slope?

2. A line passes through $(0, 5)$ and $(10, 5)$. Slope? What does that number *say* about the line?

3. $f(x) = 4x - 7$. Compute $\frac{f(x+h) - f(x)}{h}$ for $h = 2$, then $h = 0.1$.
   Why do you get the same answer both times?

4. If the loss changes by $-0.06$ when a weight is nudged by $+0.01$, what is the sensitivity
   (rise over run)? Is loss going up or down as the weight increases?

---

## Part B — Core: slope of a curve, by nudging

Use $\dfrac{f(x+h) - f(x)}{h}$ with $h = 0.1$. Name each move. Then write your *guess* for the
exact slope (the number your estimate is sneaking up on).

5. $f(x) = x^2$ at $x = 1$

6. $f(x) = x^2$ at $x = -2$   *(careful with signs — what does a negative answer mean about the curve there?)*

7. $f(x) = x^3$ at $x = 2$

8. $f(x) = x^2$ at $x = 0$. Estimate, then answer: what does the curve *look like* at a point
   where the derivative is $0$?

---

## Part C — Spot the illegal move

Each "solution" contains exactly one broken move. Circle it and write what rule it broke.

9. Claimed: slope of $f(x) = x^2$ at $x = 3$.
   - line 1: $\frac{f(3.1) - f(3)}{h}$
   - line 2: $= \frac{9.61 - 9}{3}$   *(divided by the x-value)*
   - line 3: $= 0.203\overline{3}$

10. Claimed: slope of $f(x) = x^2$ at $x = 2$, "exactly, using $h = 0$":
    - line 1: $\frac{f(2+0) - f(2)}{0}$
    - line 2: $= \frac{4 - 4}{0} = \frac{0}{0}$
    - line 3: $= 1$, since anything divided by itself is 1

11. Claimed: "$f(5) = 25$, so the derivative of $f(x)=x^2$ at $x = 5$ is $25$."
    What two different questions got mixed up?

---

## Part D — Deep end

*Not fully covered yet. Attempt anyway — wrong attempts with named moves beat blank space.*

12. Do the nudge algebraically: simplify $\dfrac{(x+h)^2 - x^2}{h}$ using Module 0 moves
    (expand, cancel, divide). You'll get an expression with an $h$ still in it.
    Now imagine $h$ tiny — what's left? You've just *derived* the derivative of $x^2$.

13. Repeat problem 12 for $f(x) = x^2 + 5$. Compare with problem 12's answer.
    Why did the $+5$ vanish? (Think: what does adding 5 do to the *shape* of the graph?)

14. Sketch (roughly) $f(x) = x^2 - 4x$. Using your Part D answers, find the $x$ where the
    derivative equals $0$. What is special about that spot on your sketch — and why might a
    "loss valley" be exactly the place where a derivative is zero?

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
