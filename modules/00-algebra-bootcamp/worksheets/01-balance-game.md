# Worksheet 0.1 — The Balance Game

*Pen and paper. For every problem, write the **move you're making** next to each step, like
"−2 both sides". The moves are the point, not the answers. Photograph into `scans/inbox/` when done.*

*Answers are hidden — hover (or tap) a blurred box to check one after you've attempted it.
Use the **🔓 / 🔒 toggle** (bottom-right) to lock them so you can't peek by accident.*

---

## Part A — Warm-up: one move each

Solve for $x$. One legal move is enough. Name the move.

1. $x + 7 = 15$

   ::: answer
   $x = 8$ — move: $-7$ both sides.
   :::

2. $x - 3 = 11$

   ::: answer
   $x = 14$ — move: $+3$ both sides.
   :::

3. $5x = 35$

   ::: answer
   $x = 7$ — move: $\div 5$ both sides.
   :::

4. $\frac{x}{6} = 4$

   ::: answer
   $x = 24$ — move: $\times 6$ both sides.
   :::

---

## Part B — Two-move games

Solve for $x$, naming each move. Strategy: peel the outermost layer first.

5. $2x + 5 = 17$

   ::: answer
   $x = 6$ — peel the $+5$ first ($-5$: $2x = 12$), then $\div 2$.
   :::

6. $4x - 9 = 19$

   ::: answer
   $x = 7$ — $+9$: $4x = 28$, then $\div 4$.
   :::

7. $\frac{x}{3} + 2 = 7$

   ::: answer
   $x = 15$ — $-2$: $\frac{x}{3} = 5$, then $\times 3$.
   :::

8. $10 - x = 4$   *(trickier than it looks — what move deals with the minus in front of $x$?)*

   ::: answer
   $x = 6$. The move: $+x$ both sides to get $x$ off the minus → $10 = 4 + x$, then $-4$.
   (Or $-10$ both sides → $-x = -6$, then $\times(-1)$.)
   :::

---

## Part D — Deep end

*These use ideas we haven't formally covered. Attempt them anyway — struggling here is the workout.
Wrong attempts with named moves are worth more than blank space.*

9. $2(x + 3) = 16$   *(two different move-orders both work — can you find both?)*

    ::: answer
    $x = 5$. Order A: $\div 2$ first → $x + 3 = 8$, then $-3$. Order B: expand → $2x + 6 = 16$,
    $-6$: $2x = 10$, $\div 2$. Same answer either way.
    :::

10. $\frac{20}{x} = 5$   *(the $x$ is in the basement. What move gets it out?)*

    ::: answer
    $x = 4$. Move: $\times x$ both sides to lift it out of the basement → $20 = 5x$, then $\div 5$.
    :::

11. $3x + 4 = x + 10$   *(mystery weights on BOTH pans. The moves still work.)*

    ::: answer
    $x = 3$. Move: $-x$ both sides to gather $x$ on one pan → $2x + 4 = 10$, $-4$: $2x = 6$, $\div 2$.
    :::

12. Solve for $a$: $\;v = a t$   *(no numbers at all — just symbols. Same game, same moves.
    This is 90% of what reading ML papers requires.)*

    ::: answer
    $a = \dfrac{v}{t}$ — move: $\div t$ both sides. No numbers needed; the move is identical.
    :::

---

## Part E — Python check (at the computer, after the pen work)

13. For each answer in Part B, verify it in Python the way the lesson showed:

```python
x = ???          # your answer to problem 5
print(2 * x + 5 == 17)   # should print True
```

Write next to each Part B problem: ✓ if Python said `True`.

> **Bonus thought:** problem 12 can't be checked with one `==` line because there are no numbers.
> How *would* you check it? (Hint: pick random numbers for $v$ and $t$…)
