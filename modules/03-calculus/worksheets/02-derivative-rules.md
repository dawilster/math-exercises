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

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

17. Find *all* $x$ where $f(x) = x^3 - 12x$ has derivative zero. (Differentiate, set $f'(x) = 0$,
    solve with balance-game moves.) These are the flat spots — the hilltops and valley floors.

    ::: rephrase
    "Derivative zero" = *flat spot* = the slope is $0$ there. So this is a two-part job:
    first **find the slope function** $f'(x)$ (that's just Part B power-rule work), then
    **ask where that slope equals $0$** — which turns into a balance-game equation
    $f'(x) = 0$ to solve for $x$, exactly like the solving you did in Module 0.
    :::

    ::: hint
    Step one is pure Part B: differentiate $x^3 - 12x$ term by term with the power rule.
    Don't touch "set to zero" yet — just get $f'(x)$.
    :::

    ::: hint
    Now set your $f'(x) = 0$ and solve for $x$ with balance moves. It ends at $x^2 = 4$ —
    and remember a square root gives **two** answers, $+$ and $-$.
    :::

    ::: steps
    1. **Power rule, term by term.** $f'(x) = 3x^2 - 12$
    2. **Set the slope to zero.** $3x^2 - 12 = 0$
    3. **$+12$ both sides, then $\div 3$.** $x^2 = 4$
    4. **Square-root both sides — keep both signs.** $x = \pm 2$ (the hilltop and the valley floor)
    :::

18. $L(w) = (w - 3)^2$ is a tiny loss function with one weight. Expand it (Module 0.3), then
    differentiate. For what $w$ is $L'(w) = 0$? Check: is that the $w$ that makes the loss
    smallest? You just trained a one-weight model by algebra.

    ::: rephrase
    Same flat-spot hunt as problem 17, but there's a warm-up move first: the power rule
    wants a *sum of powers* like $w^2 - 6w + 9$, not a bracket $(w-3)^2$. So **expand first**
    (that's the FOIL/expand move from Module 0.3), *then* it's differentiate-and-set-to-zero.
    The "loss function" story: $L'(w)=0$ marks the bottom of the bowl — the best weight.
    :::

    ::: hint
    You can't power-rule a bracket directly. Multiply $(w-3)(w-3)$ out into three terms first.
    :::

    ::: hint
    Once expanded, differentiate term by term, set $L'(w)=0$, and solve the (now linear)
    equation for $w$.
    :::

    ::: steps
    1. **Expand the square** ($(w-3)(w-3)$). $L(w) = w^2 - 6w + 9$
    2. **Power rule term by term** ($9$ is constant → $0$). $L'(w) = 2w - 6$
    3. **Set the slope to zero and solve.** $2w - 6 = 0 \Rightarrow w = 3$
    4. **Check it's really the minimum.** $L(3) = 0$ — the smallest a squared term can ever be, so $w=3$ is the valley floor.
    :::

19. The derivative of $e^x$ is $e^x$. Using only the rules on this sheet, show that
    $g(x) = 5e^x$ is *also* its own derivative, but $h(x) = e^x + 1$ is not.

    ::: rephrase
    "Is its own derivative" just means: differentiate it, and check whether the answer is the
    *exact same expression* you started with. So do two ordinary derivatives — $g'(x)$ and
    $h'(x)$ — then compare each to its original. No new rules; it's Part A's $e^x$ rule plus
    "coefficient rides along" and "constant → 0", read carefully.
    :::

    ::: hint
    Differentiate $g(x) = 5e^x$ (exponential rule, the $5$ rides along) and place $g'(x)$ next
    to $g(x)$ — same or not?
    :::

    ::: hint
    Now $h(x) = e^x + 1$: differentiate term by term. Watch what the $+1$ becomes — that's the
    whole point of the comparison.
    :::

    ::: steps
    1. **Differentiate $g$** (exponential rule, coefficient $5$ rides along). $g'(x) = 5e^x$
    2. **Compare to $g$.** $g'(x) = 5e^x = g(x)$ ✓ — still its own derivative.
    3. **Differentiate $h$** (exponential rule on $e^x$, constant $+1 \to 0$). $h'(x) = e^x$
    4. **Compare to $h$.** $h(x) = e^x + 1 \ne e^x = h'(x)$ ✗ — the $+1$ vanished, so it's *not* its own derivative.
    :::

20. Guess time: using the pattern of the power rule, what do you *think* $\frac{d}{dx}(x \cdot x^2)$
    is? Now simplify $x \cdot x^2$ first and differentiate. Do "differentiate each factor and
    multiply" and the true answer agree? (This failed experiment is why a *product rule* exists —
    Claude will show you when a derivation needs it.)

    ::: rephrase
    This one asks you to *deliberately try a wrong move and catch it*. Route 1: guess that
    you can differentiate each factor separately and multiply the results. Route 2: the safe
    move you already own — collapse $x \cdot x^2$ into a single power first (add exponents,
    Module 0), then power-rule it. Then hold the two answers side by side: if they disagree,
    the guessed move is illegal. That's a mini-experiment, not a memorised fact.
    :::

    ::: hint
    Route 2 is trustworthy: use the exponent rule $x \cdot x^2 = x^{1+2}$ to get one power,
    then differentiate that with the power rule.
    :::

    ::: hint
    Now build the tempting-but-wrong Route 1: differentiate $x$ (gives $1$) and $x^2$ (gives
    $2x$) separately and multiply them. Compare the two numbers.
    :::

    ::: steps
    1. **Guessed move: differentiate each factor, multiply.** $\dfrac{d}{dx}(x)\cdot\dfrac{d}{dx}(x^2) = 1 \cdot 2x = 2x$
    2. **Safe move: collapse to one power first** (add exponents). $x \cdot x^2 = x^3$
    3. **Power rule on the true form.** $\dfrac{d}{dx}(x^3) = 3x^2$
    4. **Compare — they disagree.** $2x \ne 3x^2$, so "differentiate factors and multiply" is *not* a legal move — which is exactly why a separate **product rule** has to exist.
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
