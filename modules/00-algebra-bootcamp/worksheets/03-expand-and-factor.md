# Worksheet 0.3 — Expand & Factor

*Pen and paper. For every problem, write the **move you're making** next to each step, like
"distribute the 3" or "factor: pull out common 4". The moves are the point, not the answers.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: single distributions

Expand (problems 1–2) or factor (problems 3–4). Name the move each time.

1. $3(x + 5)$

2. $-2(x - 4)$   *(watch every sign)*

3. $6x + 9$   *(what's the biggest thing both terms share?)*

4. $x^2 + 7x$

---

## Part B — Core: double handshakes and reshaping to solve

5. Expand: $(x + 3)(x + 4)$   *(all four handshakes — show each product)*

6. Expand: $(x + 5)(x - 5)$   *(notice what vanishes; this pattern has a name)*

7. Expand: $(x + 4)^2$   *(write it as $(x+4)(x+4)$ first — no freshman's dream)*

8. Factor: $x^2 + 8x + 15$   *(two numbers that add to 8, multiply to 15)*

9. Factor: $x^2 - 9$   *(problem 6, played backwards)*

10. Solve by reshaping first: $x^2 + 6x + 8 = 0$
    *(moves: factor, zero product, then 0.1 moves. Name all three stages.)*

---

## Part C — Spot the illegal move

Each line of working contains exactly one broken move. Circle it and name the rule it broke.

11. Claimed expansion:
    - line 1: $(x + 3)^2$
    - line 2: $x^2 + 9$   *(squared each thing)*

12. Claimed solution of $x^2 - 5x = 0$:
    - line 1: $x^2 - 5x = 0$
    - line 2: $x - 5 = 0$   *(divided both sides by x)*
    - line 3: $x = 5$
    *(Hint: line 2's move is legal only under a condition — and breaking it lost one of the
    two solutions. Which solution went missing?)*

13. Claimed simplification:
    - line 1: $\frac{3x + 6}{3}$
    - line 2: $x + 6$   *(cancelled the 3s)*

---

## Part D — Deep end

*Beyond what was taught — this is where the workout lives. Attempt everything; name your
moves even when unsure. A wrong path with named moves teaches more than a blank page.*

14. Solve $(x + 2)(x - 3) = 6$.
    *(Trap from the lesson's deep-end question: you can NOT split this while the right side
    is 6. What single 0.1 move makes the zero-product move legal?)*

15. Expand $(a + b)^2$ with pure symbols, then use your result to compute $31^2$ **in your
    head** by writing it as $(30 + 1)^2$. Show the three pieces.

16. Factor $2x^2 + 10x + 12$.   *(Two stages: pull out a common number first, then factor
    what's left.)*

17. Expand $(x + y)(x - y)$, then use the pattern to compute $102 \times 98$ in your head.

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
