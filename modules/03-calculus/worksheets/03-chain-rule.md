# Worksheet 3.3 — The Chain Rule

*Pen and paper. For every pipeline problem, write the three moves explicitly:
**name the pipeline** (inner $g$, outer $f$), **differentiate each stage**, **multiply along
the pipe**. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: exchange rates and gear trains

No calculus yet — just multiply sensitivities.

1. 1 AUD → 0.65 USD, and 1 USD → 0.90 EUR. How many EUR does 1 AUD move?

   ::: answer
   $0.65 \times 0.90 = 0.585$ EUR — move: multiply the sensitivities along the pipeline
   (this *is* the chain rule, no calculus needed yet).
   :::

2. Gear B turns 4× as fast as gear A; gear C turns $\frac{1}{2}$× as fast as B.
   How fast does C turn relative to A?

   ::: answer
   $4 \times \frac{1}{2} = 2$ — C turns twice as fast as A. Sensitivities multiply straight
   through the chain.
   :::

3. A pipeline of 3 stages has sensitivities $2$, $-3$, and $0.5$. End-to-end sensitivity?
   What does the sign of your answer mean?

   ::: answer
   $2 \times (-3) \times 0.5 = -3$. The negative sign means nudging the input up moves the
   final output *down* — one stage in the pipeline flips the direction.
   :::

4. Nudging weight $w$ moves a neuron's output at rate 5; nudging that output moves the loss at
   rate $0.2$. If $w$ is nudged by $+0.01$, roughly how much does the loss change?

   ::: answer
   $5 \times 0.2 \times 0.01 = 0.01$ — move: multiply the sensitivities (chain rule in
   miniature), then scale by the actual nudge size.
   :::

---

## Part B — Core: pipelines of functions

Differentiate using the three named moves.

5. $h(x) = (2x + 5)^3$

   ::: answer
   $h'(x) = 6(2x+5)^2$ — outer $f(u)=u^3 \to f'(u)=3u^2$, inner $u=2x+5 \to u'=2$;
   chain: $3(2x+5)^2 \cdot 2$.
   :::

6. $h(x) = (x^2 + 1)^4$

   ::: answer
   $h'(x) = 8x(x^2+1)^3$ — outer $f(u)=u^4 \to 4u^3$, inner $u=x^2+1 \to u'=2x$;
   chain: $4(x^2+1)^3 \cdot 2x$.
   :::

7. $h(x) = e^{3x}$

   ::: answer
   $h'(x) = 3e^{3x}$ — outer $f(u)=e^u \to e^u$, inner $u=3x \to u'=3$; chain: $e^{3x}\cdot 3$.
   :::

8. $h(x) = \ln(5x)$   *(after differentiating, simplify — the answer is surprisingly clean)*

   ::: answer
   $h'(x) = \dfrac{1}{x}$ — outer $f(u)=\ln u \to \frac{1}{u}$, inner $u=5x \to u'=5$;
   chain: $\frac{1}{5x}\cdot 5 = \frac{1}{x}$ (the 5s cancel — $\ln(kx)$ and $\ln x$ always
   have the same derivative).
   :::

9. $h(x) = e^{-x^2}$   *(the bell-curve engine — you'll meet it again in Module 4)*

   ::: answer
   $h'(x) = -2x\,e^{-x^2}$ — outer $f(u)=e^u \to e^u$, inner $u=-x^2 \to u'=-2x$;
   chain: $e^{-x^2}\cdot(-2x)$.
   :::

10. $h(x) = (1 + e^x)^2$. Then evaluate $h'(0)$.

    ::: answer
    $h'(x) = 2e^x(1+e^x)$ — outer $f(u)=u^2 \to 2u$, inner $u=1+e^x \to u'=e^x$;
    chain: $2(1+e^x)\cdot e^x$. At $x=0$: $h'(0) = 2e^0(1+e^0) = 2\cdot1\cdot2 = 4$.
    :::

---

## Part C — Spot the illegal move

Each "solution" contains exactly one broken move. Circle it, name what broke.

11. Claimed: $\frac{d}{dx}(4x + 1)^2$
    - line 1: outer $u^2 \to 2u$
    - line 2: $= 2(4x + 1)$   *(done!)*

    ::: answer
    Line 2 is broken — they never multiplied by the inner derivative $g'(x)=4$
    (forgot to "multiply along the pipe"). Correct: $2(4x+1)\cdot 4 = 8(4x+1) = 32x+8$.
    :::

12. Claimed: $\frac{d}{dx}(x^2 + 3)^5$
    - line 1: inner $g = x^2 + 3$, outer $f(u) = u^5$
    - line 2: $f'(u) = 5u^4$, $g'(x) = 2x$
    - line 3: $= 5x^4 \cdot 2x = 10x^5$   *(multiplied along the pipe)*

    ::: answer
    Line 3 is broken — they plugged $x$ straight into $f'(u)=5u^4$ instead of $u=x^2+3$
    (wrote $5x^4$ instead of $5(x^2+3)^4$). Correct: $5(x^2+3)^4 \cdot 2x = 10x(x^2+3)^4$.
    :::

13. Claimed: $\frac{d}{dx}\, e^{2x}$
    - line 1: "$e$ to anything is its own derivative"
    - line 2: $= e^{2x}$

    ::: answer
    Line 1 is broken — $e^u$ is its own derivative *with respect to $u$*; they forgot to
    multiply by the inner derivative $u'=2$. Correct: $2e^{2x}$.
    :::

---

## Part D — Deep end

14. Three stages: $h(x) = \left(e^{2x} + 1\right)^3$. Name the whole pipeline
    ($x \to 2x \to e^{2x} \to e^{2x}+1 \to (\cdot)^3$) and multiply all the sensitivities.

    ::: answer
    Stage sensitivities: $2$ (for $x\to 2x$), $e^{2x}$ (for $2x \to e^{2x}$), $1$
    (for $+1$), $3(e^{2x}+1)^2$ (for the cube). Multiply along the pipe:
    $h'(x) = 3(e^{2x}+1)^2 \cdot 1 \cdot e^{2x} \cdot 2 = 6e^{2x}(e^{2x}+1)^2$.
    :::

15. The sigmoid $\sigma(x) = \dfrac{1}{1 + e^{-x}}$ (Module 1.5's friend) can be written as a
    pipeline: $x \to -x \to e^{-x} \to 1 + e^{-x} \to (\cdot)^{-1}$.
    Differentiate it. (Messy is fine — every neural-net library computes exactly this.)

    ::: answer
    Stage sensitivities: $-1$ (for $x\to -x$), $e^{-x}$ (for $\to e^{-x}$), $1$ (for $+1$),
    $-(1+e^{-x})^{-2}$ (for $(\cdot)^{-1}$). Multiply along the pipe:
    $\sigma'(x) = (-1)\cdot e^{-x}\cdot 1 \cdot\bigl(-(1+e^{-x})^{-2}\bigr)
    = \dfrac{e^{-x}}{(1+e^{-x})^2}$, which equals $\sigma(x)\bigl(1-\sigma(x)\bigr)$.
    :::

16. A 10-stage pipeline where every stage has sensitivity $0.5$: end-to-end sensitivity?
    Same question with every stage at $2$. Write one sentence on why *deep* pipelines make
    gradients either starve or explode.

    ::: answer
    $0.5^{10} = \frac{1}{1024} \approx 0.001$ — the gradient shrinks toward zero (vanishes).
    $2^{10} = 1024$ — the gradient blows up (explodes). Because sensitivities multiply along
    the pipe, many stages below 1 crush the gradient to nothing and many stages above 1 send
    it to infinity — deep networks need careful initialisation/normalisation to keep every
    stage's sensitivity near 1.
    :::

17. Solve for the symbol (Module 0 flashback): if $h(x) = f(g(x))$ and you know
    $h'(2) = 12$ and $g'(2) = 3$, what is $f'(g(2))$?

    ::: answer
    $f'(g(2)) = 4$ — move: $h'(x) = f'(g(x))\cdot g'(x)$, so $12 = f'(g(2))\cdot 3$;
    $\div 3$ both sides.
    :::

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
