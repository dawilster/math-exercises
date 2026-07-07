# Worksheet 3.3 — The Chain Rule

*Pen and paper. For every pipeline problem, write the three moves explicitly:
**name the pipeline** (inner $g$, outer $f$), **differentiate each stage**, **multiply along
the pipe**. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: exchange rates and gear trains

No calculus yet — just multiply sensitivities.

1. 1 AUD → 0.65 USD, and 1 USD → 0.90 EUR. How many EUR does 1 AUD move?

2. Gear B turns 4× as fast as gear A; gear C turns $\frac{1}{2}$× as fast as B.
   How fast does C turn relative to A?

3. A pipeline of 3 stages has sensitivities $2$, $-3$, and $0.5$. End-to-end sensitivity?
   What does the sign of your answer mean?

4. Nudging weight $w$ moves a neuron's output at rate 5; nudging that output moves the loss at
   rate $0.2$. If $w$ is nudged by $+0.01$, roughly how much does the loss change?

---

## Part B — Core: pipelines of functions

Differentiate using the three named moves.

5. $h(x) = (2x + 5)^3$

6. $h(x) = (x^2 + 1)^4$

7. $h(x) = e^{3x}$

8. $h(x) = \ln(5x)$   *(after differentiating, simplify — the answer is surprisingly clean)*

9. $h(x) = e^{-x^2}$   *(the bell-curve engine — you'll meet it again in Module 4)*

10. $h(x) = (1 + e^x)^2$. Then evaluate $h'(0)$.

---

## Part C — Spot the illegal move

Each "solution" contains exactly one broken move. Circle it, name what broke.

11. Claimed: $\frac{d}{dx}(4x + 1)^2$
    - line 1: outer $u^2 \to 2u$
    - line 2: $= 2(4x + 1)$   *(done!)*

12. Claimed: $\frac{d}{dx}(x^2 + 3)^5$
    - line 1: inner $g = x^2 + 3$, outer $f(u) = u^5$
    - line 2: $f'(u) = 5u^4$, $g'(x) = 2x$
    - line 3: $= 5x^4 \cdot 2x = 10x^5$   *(multiplied along the pipe)*

13. Claimed: $\frac{d}{dx}\, e^{2x}$
    - line 1: "$e$ to anything is its own derivative"
    - line 2: $= e^{2x}$

---

## Part D — Deep end

14. Three stages: $h(x) = \left(e^{2x} + 1\right)^3$. Name the whole pipeline
    ($x \to 2x \to e^{2x} \to e^{2x}+1 \to (\cdot)^3$) and multiply all the sensitivities.

15. The sigmoid $\sigma(x) = \dfrac{1}{1 + e^{-x}}$ (Module 1.5's friend) can be written as a
    pipeline: $x \to -x \to e^{-x} \to 1 + e^{-x} \to (\cdot)^{-1}$.
    Differentiate it. (Messy is fine — every neural-net library computes exactly this.)

16. A 10-stage pipeline where every stage has sensitivity $0.5$: end-to-end sensitivity?
    Same question with every stage at $2$. Write one sentence on why *deep* pipelines make
    gradients either starve or explode.

17. Solve for the symbol (Module 0 flashback): if $h(x) = f(g(x))$ and you know
    $h'(2) = 12$ and $g'(2) = 3$, what is $f'(g(2))$?

---

## Part E — Python check (at the computer, after the pen work)

18. Check Part B numerically AND symbolically — two referees:

```python
def derivative(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h

import math                       # math.exp(x) is e^x, math.log(x) is ln x

def h5(x):
    return (2*x + 5)**3
print(derivative(h5, 1))          # compare with YOUR h'(1) from problem 5

import sympy as sp
x = sp.symbols("x")
print(sp.diff((2*x + 5)**3, x))   # the symbolic referee
print(sp.diff(sp.exp(-x**2), x))  # problem 9
```

Write ✓ next to each confirmed problem. Any mismatch: hunt the broken move — it's nearly
always a forgotten inner derivative.

> **Bonus thought:** get sympy to differentiate the sigmoid (problem 15):
> `sp.diff(1/(1 + sp.exp(-x)), x)`. Then try to show its answer equals $\sigma(x)(1 - \sigma(x))$
> — the tidiest derivative in deep learning, and the reason sigmoid layers are cheap to backprop.
