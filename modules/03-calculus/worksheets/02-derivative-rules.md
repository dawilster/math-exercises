# Worksheet 3.2 — Derivative Rules

*Pen and paper. Name the rule you're using at each step ("power rule", "sum rule",
"constant → 0", "coefficient rides along"). Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: one rule each

Differentiate. Name the rule.

1. $f(x) = x^5$

2. $f(x) = 12$

3. $f(x) = 7x^3$

4. $f(x) = e^x$

5. $f(x) = \ln x$

---

## Part B — Core: combining rules

Differentiate, naming every rule as it fires.

6. $f(x) = x^3 + x^2$

7. $f(x) = 4x^2 - 9x + 2$

8. $f(x) = \frac{1}{2}x^6 - 10x$

9. $f(x) = 5e^x + 2\ln x$

10. $f(x) = x^{100} - x$. Then evaluate $f'(1)$.

11. Rewrite first, then differentiate: $f(x) = \dfrac{1}{x}$
    *(hint from Module 0 exponents: $\frac{1}{x} = x^{-1}$; the power rule doesn't mind negatives)*

12. Rewrite first, then differentiate: $f(x) = \sqrt{x}$
    *(hint: $\sqrt{x} = x^{1/2}$)*

---

## Part C — Spot the illegal move

Each "solution" contains exactly one broken move. Circle it, name the broken rule.

13. Claimed: $\frac{d}{dx}\left(x^4 + 6\right)$
    - line 1: $= 4x^3 + 6$   *(the constant survived)*

14. Claimed: $\frac{d}{dx}\left(e^x\right)$
    - line 1: $= x e^{x-1}$   *(power rule applied)*

15. Claimed: $\frac{d}{dx}\left(3x^5\right)$
    - line 1: $= 3 \cdot 5 x^4$
    - line 2: $= 15x^4$
    - line 3: so $f'(2) = 15 \cdot 2^4 = 15 \cdot 16 = 240$… "but wait, I'll simplify $15x^4$
      to $60x$ first by multiplying 15 by 4" → $f'(2) = 120$

16. Claimed: $\frac{d}{dx}\left(\ln x + 1\right) = \frac{1}{x+1}$

---

## Part D — Deep end

*Attempt with named moves; struggle is the workout.*

17. Find *all* $x$ where $f(x) = x^3 - 12x$ has derivative zero. (Differentiate, set $f'(x) = 0$,
    solve with balance-game moves.) These are the flat spots — the hilltops and valley floors.

18. $L(w) = (w - 3)^2$ is a tiny loss function with one weight. Expand it (Module 0.3), then
    differentiate. For what $w$ is $L'(w) = 0$? Check: is that the $w$ that makes the loss
    smallest? You just trained a one-weight model by algebra.

19. The derivative of $e^x$ is $e^x$. Using only the rules on this sheet, show that
    $g(x) = 5e^x$ is *also* its own derivative, but $h(x) = e^x + 1$ is not.

20. Guess time: using the pattern of the power rule, what do you *think* $\frac{d}{dx}(x \cdot x^2)$
    is? Now simplify $x \cdot x^2$ first and differentiate. Do "differentiate each factor and
    multiply" and the true answer agree? (This failed experiment is why a *product rule* exists —
    Claude will show you when a derivation needs it.)

---

## Part E — Python check (at the computer, after the pen work)

21. Make sympy the referee for Parts B and D:

```python
import sympy as sp
x = sp.symbols("x")

print(sp.diff(x**3 + x**2, x))        # problem 6 — compare with your answer
print(sp.diff(5*sp.exp(x) + 2*sp.log(x), x))   # problem 9
print(sp.solve(sp.Eq(sp.diff(x**3 - 12*x, x), 0), x))  # problem 17's flat spots
```

Write ✓ next to each problem sympy confirmed. For any ✗: find *which move* broke before
looking anything up.

> **Bonus thought:** also check problem 5 numerically with the nudge machine from 3.1 at $x=2$:
> does $(f(2+h)-f(2))/h \approx \frac{1}{2}$? Two referees, one answer — that's how you know
> the rules aren't magic.
