# Worksheet 3.2 — Derivative Rules

*Pen and paper. Name the rule you're using at each step ("power rule", "sum rule",
"constant → 0", "coefficient rides along"). Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: one rule each

Differentiate. Name the rule.

1. $f(x) = x^5$

   ::: answer
   $f'(x) = 5x^4$ — move: power rule.
   :::

2. $f(x) = 12$

   ::: answer
   $f'(x) = 0$ — move: constant rule (a constant's derivative is always 0).
   :::

3. $f(x) = 7x^3$

   ::: answer
   $f'(x) = 21x^2$ — move: power rule, coefficient rides along ($7 \cdot 3 = 21$).
   :::

4. $f(x) = e^x$

   ::: answer
   $f'(x) = e^x$ — move: exponential rule ($e^x$ is its own derivative).
   :::

5. $f(x) = \ln x$

   ::: answer
   $f'(x) = \dfrac{1}{x}$ — move: log rule.
   :::

---

## Part B — Core: combining rules

Differentiate, naming every rule as it fires.

6. $f(x) = x^3 + x^2$

   ::: answer
   $f'(x) = 3x^2 + 2x$ — move: power rule on each term, then sum rule.
   :::

7. $f(x) = 4x^2 - 9x + 2$

   ::: answer
   $f'(x) = 8x - 9$ — move: power rule (coefficient rides along) on each term, constant → 0, sum/difference rule.
   :::

8. $f(x) = \frac{1}{2}x^6 - 10x$

   ::: answer
   $f'(x) = 3x^5 - 10$ — move: power rule ($\frac{1}{2} \cdot 6 = 3$), coefficient rides along.
   :::

9. $f(x) = 5e^x + 2\ln x$

   ::: answer
   $f'(x) = 5e^x + \dfrac{2}{x}$ — move: exponential rule + log rule, coefficient rides along, sum rule.
   :::

10. $f(x) = x^{100} - x$. Then evaluate $f'(1)$.

    ::: answer
    $f'(x) = 100x^{99} - 1$ — move: power rule. $f'(1) = 100(1)^{99} - 1 = 99$.
    :::

11. Rewrite first, then differentiate: $f(x) = \dfrac{1}{x}$
    *(hint from Module 0 exponents: $\frac{1}{x} = x^{-1}$; the power rule doesn't mind negatives)*

    ::: answer
    $f(x) = x^{-1} \Rightarrow f'(x) = -x^{-2} = -\dfrac{1}{x^2}$ — move: rewrite as a negative exponent, then power rule.
    :::

12. Rewrite first, then differentiate: $f(x) = \sqrt{x}$
    *(hint: $\sqrt{x} = x^{1/2}$)*

    ::: answer
    $f(x) = x^{1/2} \Rightarrow f'(x) = \dfrac{1}{2}x^{-1/2} = \dfrac{1}{2\sqrt{x}}$ — move: rewrite as a fractional exponent, then power rule.
    :::

---

## Part C — Spot the illegal move

Each "solution" contains exactly one broken move. Circle it, name the broken rule.

13. Claimed: $\frac{d}{dx}\left(x^4 + 6\right)$
    - line 1: $= 4x^3 + 6$   *(the constant survived)*

    ::: answer
    Line 1 is broken: the constant → 0 rule was never applied to the $+6$. Correct: $f'(x) = 4x^3$.
    :::

14. Claimed: $\frac{d}{dx}\left(e^x\right)$
    - line 1: $= x e^{x-1}$   *(power rule applied)*

    ::: answer
    Line 1 is broken: the power rule is for $x^n$ (variable base, constant exponent) — here the
    variable is in the exponent, so the exponential rule applies instead. Correct: $f'(x) = e^x$.
    :::

15. Claimed: $\frac{d}{dx}\left(3x^5\right)$
    - line 1: $= 3 \cdot 5 x^4$
    - line 2: $= 15x^4$
    - line 3: so $f'(2) = 15 \cdot 2^4 = 15 \cdot 16 = 240$… "but wait, I'll simplify $15x^4$
      to $60x$ first by multiplying 15 by 4" → $f'(2) = 120$

    ::: answer
    Line 3's "simplification" is broken: there's no legal move that turns $15x^4$ into $60x$ —
    multiplying the coefficient by the exponent changes the function, it doesn't simplify it.
    The earlier working was correct: $f'(x) = 15x^4$, so $f'(2) = 15 \cdot 16 = 240$.
    :::

16. Claimed: $\frac{d}{dx}\left(\ln x + 1\right) = \frac{1}{x+1}$

    ::: answer
    Broken: $\ln x + 1$ was treated like $\ln(x+1)$. The sum rule says differentiate term by
    term: $\ln x \to \frac{1}{x}$ and the constant $+1 \to 0$. Correct: $f'(x) = \dfrac{1}{x}$.
    :::

---

## Part D — Deep end

*Attempt with named moves; struggle is the workout.*

17. Find *all* $x$ where $f(x) = x^3 - 12x$ has derivative zero. (Differentiate, set $f'(x) = 0$,
    solve with balance-game moves.) These are the flat spots — the hilltops and valley floors.

    ::: answer
    $f'(x) = 3x^2 - 12$ — move: power rule. Setting $3x^2 - 12 = 0$: $+12$, $\div 3$ →
    $x^2 = 4$, then $\sqrt{\phantom{x}}$ both sides → $x = \pm 2$.
    :::

18. $L(w) = (w - 3)^2$ is a tiny loss function with one weight. Expand it (Module 0.3), then
    differentiate. For what $w$ is $L'(w) = 0$? Check: is that the $w$ that makes the loss
    smallest? You just trained a one-weight model by algebra.

    ::: answer
    $L(w) = w^2 - 6w + 9 \Rightarrow L'(w) = 2w - 6$ — move: expand, then power rule termwise.
    $2w - 6 = 0 \Rightarrow w = 3$. Yes — $L(3) = 0$, the smallest a squared term can ever be.
    :::

19. The derivative of $e^x$ is $e^x$. Using only the rules on this sheet, show that
    $g(x) = 5e^x$ is *also* its own derivative, but $h(x) = e^x + 1$ is not.

    ::: answer
    $g'(x) = 5e^x$ — move: exponential rule, coefficient rides along — so $g'(x) = g(x)$.
    $h'(x) = e^x$ — move: exponential rule + constant → 0 — but $h(x) = e^x + 1 \ne e^x = h'(x)$.
    :::

20. Guess time: using the pattern of the power rule, what do you *think* $\frac{d}{dx}(x \cdot x^2)$
    is? Now simplify $x \cdot x^2$ first and differentiate. Do "differentiate each factor and
    multiply" and the true answer agree? (This failed experiment is why a *product rule* exists —
    Claude will show you when a derivation needs it.)

    ::: answer
    Guess ("differentiate each factor and multiply"): $1 \cdot 2x = 2x$. True answer:
    $x \cdot x^2 = x^3 \Rightarrow$ power rule gives $3x^2$. They disagree ($2x \ne 3x^2$) —
    "differentiate factors and multiply" isn't a legal move, which is why a product rule exists.
    :::

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
