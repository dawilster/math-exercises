# Worksheet 0.3 — Expand & Factor

*Pen and paper. For every problem, write the **move you're making** next to each step, like
"distribute the 3" or "factor: pull out common 4". The moves are the point, not the answers.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: single distributions

Expand (problems 1–2) or factor (problems 3–4). Name the move each time.

1. $3(x + 5)$

   ::: answer
   $3x + 15$ — move: distribute the 3 over both terms in the bracket.
   :::

2. $-2(x - 4)$   *(watch every sign)*

   ::: answer
   $-2x + 8$ — move: distribute the $-2$; $-2 \times -4 = +8$, sign flips.
   :::

3. $6x + 9$   *(what's the biggest thing both terms share?)*

   ::: answer
   $3(2x + 3)$ — move: factor out the common factor 3 (the biggest thing both terms share).
   :::

4. $x^2 + 7x$

   ::: answer
   $x(x + 7)$ — move: factor out the common factor $x$.
   :::

---

## Part B — Core: double handshakes and reshaping to solve

5. Expand: $(x + 3)(x + 4)$   *(all four handshakes — show each product)*

   ::: answer
   $x^2 + 7x + 12$ — move: distribute every term over every term (FOIL):
   $x^2 + 4x + 3x + 12$, then combine like terms.
   :::

6. Expand: $(x + 5)(x - 5)$   *(notice what vanishes; this pattern has a name)*

   ::: answer
   $x^2 - 25$ — the middle terms $+5x$ and $-5x$ cancel. Move: difference of squares,
   $(a+b)(a-b) = a^2 - b^2$.
   :::

7. Expand: $(x + 4)^2$   *(write it as $(x+4)(x+4)$ first — no freshman's dream)*

   ::: answer
   $x^2 + 8x + 16$ — move: distribute $(x+4)(x+4)$ term by term:
   $x^2 + 4x + 4x + 16$, combine like terms. (Not $x^2 + 16$ — that's the freshman's dream trap.)
   :::

8. Factor: $x^2 + 8x + 15$   *(two numbers that add to 8, multiply to 15)*

   ::: answer
   $(x + 3)(x + 5)$ — move: find two numbers that add to 8 and multiply to 15 (3 and 5),
   then reverse-FOIL.
   :::

9. Factor: $x^2 - 9$   *(problem 6, played backwards)*

   ::: answer
   $(x + 3)(x - 3)$ — move: difference of squares in reverse, $a^2 - b^2 = (a+b)(a-b)$
   with $a=x$, $b=3$.
   :::

10. Solve by reshaping first: $x^2 + 6x + 8 = 0$
    *(moves: factor, zero product, then 0.1 moves. Name all three stages.)*

    ::: answer
    $x = -2$ or $x = -4$. Stage 1 — move: factor ($2$ and $4$ add to 6, multiply to 8):
    $(x+2)(x+4) = 0$. Stage 2 — move: zero product (if $ab=0$ then $a=0$ or $b=0$):
    $x+2=0$ or $x+4=0$. Stage 3 — move: 0.1 balance move ($-2$ / $-4$ each side).
    :::

---

## Part C — Spot the illegal move

Each line of working contains exactly one broken move. Circle it and name the rule it broke.

11. Claimed expansion:
    - line 1: $(x + 3)^2$
    - line 2: $x^2 + 9$   *(squared each thing)*

    ::: answer
    Line 2 is broken — the freshman's dream: $(a+b)^2 \neq a^2 + b^2$. You can't square
    each term separately; you must distribute $(x+3)(x+3)$ fully.
    Correct: $x^2 + 6x + 9$.
    :::

12. Claimed solution of $x^2 - 5x = 0$:
    - line 1: $x^2 - 5x = 0$
    - line 2: $x - 5 = 0$   *(divided both sides by x)*
    - line 3: $x = 5$
    *(Hint: line 2's move is legal only under a condition — and breaking it lost one of the
    two solutions. Which solution went missing?)*

    ::: answer
    Line 2 is broken. Dividing both sides by $x$ is only legal if $x \neq 0$ — and here $x=0$
    is one of the actual solutions, so that move silently threw it away.
    Correct move: factor instead, $x(x-5) = 0$, then zero product: $x = 0$ or $x = 5$.
    The missing solution was $x = 0$.
    :::

13. Claimed simplification:
    - line 1: $\frac{3x + 6}{3}$
    - line 2: $x + 6$   *(cancelled the 3s)*

    ::: answer
    Line 2 is broken. Dividing by 3 must apply to **every** term in the numerator:
    $\frac{3x}{3} + \frac{6}{3} = x + 2$, not $x + 6$. They divided the $3x$ term but left the
    $6$ untouched. Correct: $x + 2$.
    :::

---

## Part D — Deep end

*Beyond what was taught — this is where the workout lives. Attempt everything; name your
moves even when unsure. A wrong path with named moves teaches more than a blank page.*

14. Solve $(x + 2)(x - 3) = 6$.
    *(Trap from the lesson's deep-end question: you can NOT split this while the right side
    is 6. What single 0.1 move makes the zero-product move legal?)*

    ::: answer
    $x = 4$ or $x = -3$. The needed 0.1 move: $-6$ both sides first, so the right side is 0
    (zero product only works against zero). That gives $(x+2)(x-3) - 6 = 0$.
    Expand: $x^2 - x - 6 - 6 = 0 \Rightarrow x^2 - x - 12 = 0$.
    Factor ($-4$ and $3$ multiply to $-12$, add to $-1$): $(x-4)(x+3) = 0$.
    Zero product: $x = 4$ or $x = -3$.
    :::

15. Expand $(a + b)^2$ with pure symbols, then use your result to compute $31^2$ **in your
    head** by writing it as $(30 + 1)^2$. Show the three pieces.

    ::: answer
    $(a+b)^2 = a^2 + 2ab + b^2$. With $a=30$, $b=1$: $30^2 + 2(30)(1) + 1^2 = 900 + 60 + 1 = 961$.
    Move: same double-handshake expansion as problem 7, just with symbols first.
    :::

16. Factor $2x^2 + 10x + 12$.   *(Two stages: pull out a common number first, then factor
    what's left.)*

    ::: answer
    $2(x + 2)(x + 3)$. Stage 1 — move: factor out the common 2: $2(x^2 + 5x + 6)$.
    Stage 2 — move: factor the trinomial (2 and 3 add to 5, multiply to 6): $2(x+2)(x+3)$.
    :::

17. Expand $(x + y)(x - y)$, then use the pattern to compute $102 \times 98$ in your head.

    ::: answer
    $(x+y)(x-y) = x^2 - y^2$ — move: difference of squares.
    Write $102 \times 98 = (100+2)(100-2) = 100^2 - 2^2 = 10000 - 4 = 9996$.
    :::

---

## Part E — Python check (at the computer, after the pen work)

18. Let sympy referee every Part B answer:

```python
import sympy as sp
x = sp.symbols("x")

print(sp.expand((x + 3) * (x + 4)))    # compare with your problem 5
print(sp.factor(x**2 + 8*x + 15))      # compare with your problem 8
print(sp.solve(x**2 + 6*x + 8, x))     # compare with your problem 10
```

Write ✓ next to each problem sympy confirms.

> **Bonus thought:** `sp.expand` and `sp.factor` never change what a expression *equals* —
> only its shape. Test the claim: pick $x = 17$ and evaluate $x^2+8x+15$ and your factored
> form. Same number?
