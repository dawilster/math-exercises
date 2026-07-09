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

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

9. $2(x + 3) = 16$   *(two different move-orders both work — can you find both?)*

    ::: rephrase
    The mystery weight is wrapped twice: first a $+3$ inside the bracket, then the whole group
    doubled. "Solve" = unwrap the layers until $x$ sits alone. This is problem 5 ($2x+5=17$),
    except the $+3$ is trapped *inside* a bracket. The bracket just means "whatever move you
    make hits the whole group." Two clean ways in.
    :::

    ::: hint
    Two layers are wrapped around $x$: a $\times 2$ on the outside and a $+3$ inside the bracket.
    Which is the *outermost* layer you can peel with one legal move?
    :::

    ::: hint
    Peel the outer $\times 2$ with $\div 2$ on both sides — that clears the whole bracket in one
    move and leaves a one-mover behind.
    :::

    ::: steps
    1. **Order A — divide both sides by 2.** peels the outer layer, clearing the bracket: $x + 3 = 8$
    2. **Subtract 3 from both sides.** $x = 5$
    3. **Order B — expand the bracket instead** ($2\times x$ and $2\times 3$). $2x + 6 = 16$
    4. **Subtract 6, then divide by 2.** $2x = 10 \Rightarrow x = 5$ — same answer either way.
    :::

10. $\frac{20}{x} = 5$   *(the $x$ is in the basement. What move gets it out?)*

    ::: rephrase
    $x$ is stuck in the *basement* of the fraction (the denominator). No add, subtract, or divide
    on the outside can free a variable that's doing the dividing. Ask: what's the opposite of
    "divide by $x$"? Same idea as problem 7, where $\times 3$ undid a $\div 3$ — here you multiply
    by the very thing $x$ is dividing.
    :::

    ::: hint
    Adding or subtracting won't touch an $x$ that's dividing. To undo a "divide by $x$", you need
    its opposite move.
    :::

    ::: hint
    Multiply both sides by $x$ — that lifts it out of the basement and onto the other pan.
    :::

    ::: steps
    1. **Multiply both sides by $x$.** lifts it out of the denominator: $20 = 5x$
    2. **Divide both sides by 5.** $x = 4$
    :::

11. $3x + 4 = x + 10$   *(mystery weights on BOTH pans. The moves still work.)*

    ::: rephrase
    First time a mystery weight sits on *both* pans. Same balance rules — but your opening job is
    new: gather all the $x$'s onto one pan and the plain numbers onto the other. Subtracting from
    both sides still works even when the thing you subtract is an $x$. Do that once and it collapses
    into an ordinary two-mover like problem 5.
    :::

    ::: hint
    You can subtract an $x$ from both pans, exactly like subtracting a number. Take it off the side
    that has fewer $x$'s, so you're not left chasing a negative $x$.
    :::

    ::: hint
    Subtract $x$ from both sides to gather the mystery weights on the left — then finish it as a
    normal two-move game.
    :::

    ::: steps
    1. **Subtract $x$ from both sides.** gathers the $x$'s on one pan: $2x + 4 = 10$
    2. **Subtract 4 from both sides.** $2x = 6$
    3. **Divide both sides by 2.** $x = 3$
    :::

12. Solve for $a$: $\;v = a t$   *(no numbers at all — just symbols. Same game, same moves.
    This is 90% of what reading ML papers requires.)*

    ::: rephrase
    No numbers, just letters — don't let that freeze you. $a$ is the mystery weight; $v$ and $t$
    are known weights whose values simply aren't printed. "Solve for $a$" = get $a$ alone, the exact
    same move you'd use if $t$ were a number. This is problem 3 ($5x = 35$) wearing letters instead
    of digits — and reading it fluently is 90% of what ML papers ask of you.
    :::

    ::: hint
    $a$ is multiplied by $t$. To undo a multiplication you have one move — and it works even though
    $t$ is a letter, not a number.
    :::

    ::: steps
    1. **Divide both sides by $t$.** undoes the $\times t$; treat $t$ like any number: $a = \dfrac{v}{t}$
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
