# 0.1 — Equations as a Balance Game

*≤5 min read. Then straight to the worksheet.*

## Why this matters (the real reason)

Every scary equation in machine learning — loss functions, gradient updates, attention formulas —
gets understood the same way: someone takes an equation and **legally rearranges it** until it says
something useful. School taught you *recipes* for specific equation types. That's why unfamiliar
shapes froze you: no recipe, no move. We're replacing recipes with **moves**.

## The one big idea

An equation is a **balance scale**. The `=` sign says: *left pan and right pan weigh the same.*

$$3x + 2 = 14$$

That's a claim: "some mystery weight, tripled, plus a 2-gram weight, balances 14 grams."

**A legal move is anything you do to BOTH pans that keeps the balance true.**

| Move | Example | Why it's legal |
|---|---|---|
| Add the same to both sides | $x - 5 = 9 \;\to\; x = 14$ | Both pans gain equal weight → still balanced |
| Subtract the same from both | $3x + 2 = 14 \;\to\; 3x = 12$ | Both pans lose equal weight |
| Multiply both by the same | $\frac{x}{4} = 3 \;\to\; x = 12$ | Both pans scale equally |
| Divide both by the same (never 0) | $3x = 12 \;\to\; x = 4$ | Same, in reverse |

That's it. **Solving an equation is just choosing moves that leave the mystery weight alone on one pan.**

## Watch one game get played

Solve $3x + 2 = 14$:

$$3x + 2 = 14$$
$$3x = 12 \qquad \leftarrow \text{move: subtract } 2 \text{ from both pans}$$
$$x = 4 \qquad \leftarrow \text{move: divide both pans by } 3$$

Notice the *strategy*: peel away whatever is furthest from $x$, one legal move at a time.
Like unwrapping a present — outermost layer first.

## The Python connection

Each move is a tiny function applied to *both* sides:

```python
# the equation 3x + 2 = 14, as two sides
left = "3x + 2"      # conceptually
right = 14

# move 1: subtract 2 from BOTH sides
# move 2: divide BOTH sides by 3
# Python can check our answer by substituting it back in:
x = 4
print(3 * x + 2 == 14)   # True → the balance holds → x = 4 is right
```

That last line is your **superpower**: you can always *verify* your algebra by substituting
your answer back and asking Python if both sides match.

## What breaks the balance (the classic traps)

- Doing a move to **one pan only** — e.g. subtracting 2 from the left but not the right.
- Dividing by zero, or dividing by something that *might* be zero.
- Doing a move to *part* of a pan — e.g. in $3x + 2 = 14$, dividing only the $3x$ by 3.
  **A move applies to the ENTIRE side, always.**

> **Deep-end question to hold in your head during the worksheet:**
> if legal moves keep a true equation true… what happens if you apply legal moves to an equation
> that was *false* to begin with? Can moves ever turn a false claim into a true one?

**Now: worksheet `01-balance-game` — pen and paper. Photograph it into `scans/inbox/` when done.**
