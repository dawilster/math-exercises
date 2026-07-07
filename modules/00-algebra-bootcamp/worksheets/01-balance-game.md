# Worksheet 0.1 — The Balance Game

*Pen and paper. For every problem, write the **move you're making** next to each step, like
"−2 both sides". The moves are the point, not the answers. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: one move each

Solve for $x$. One legal move is enough. Name the move.

1. $x + 7 = 15$

2. $x - 3 = 11$

3. $5x = 35$

4. $\frac{x}{6} = 4$

---

## Part B — Two-move games

Solve for $x$, naming each move. Strategy: peel the outermost layer first.

5. $2x + 5 = 17$

6. $4x - 9 = 19$

7. $\frac{x}{3} + 2 = 7$

8. $10 - x = 4$   *(trickier than it looks — what move deals with the minus in front of $x$?)*

---

## Part C — Spot the illegal move

Each "solution" below contains exactly one broken move. Circle the broken line and write
*what rule it broke*.

9. Claimed solution of $3x + 6 = 18$:
   - line 1: $3x + 6 = 18$
   - line 2: $x + 6 = 6$   *(divided by 3)*
   - line 3: $x = 0$

10. Claimed solution of $5x - 4 = 21$:
    - line 1: $5x - 4 = 21$
    - line 2: $5x = 17$   *(subtracted 4 from the left, added 4... somewhere)*
    - line 3: $x = \frac{17}{5}$

---

## Part D — Deep end

*These use ideas we haven't formally covered. Attempt them anyway — struggling here is the workout.
Wrong attempts with named moves are worth more than blank space.*

11. $2(x + 3) = 16$   *(two different move-orders both work — can you find both?)*

12. $\frac{20}{x} = 5$   *(the $x$ is in the basement. What move gets it out?)*

13. $3x + 4 = x + 10$   *(mystery weights on BOTH pans. The moves still work.)*

14. Solve for $a$: $\;v = a t$   *(no numbers at all — just symbols. Same game, same moves.
    This is 90% of what reading ML papers requires.)*

---

## Part E — Python check (at the computer, after the pen work)

15. For each answer in Part B, verify it in Python the way the lesson showed:

```python
x = ???          # your answer to problem 5
print(2 * x + 5 == 17)   # should print True
```

Write next to each Part B problem: ✓ if Python said `True`.

> **Bonus thought:** problem 14 can't be checked with one `==` line because there are no numbers.
> How *would* you check it? (Hint: pick random numbers for $v$ and $t$…)
