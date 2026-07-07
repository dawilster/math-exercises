# 3.3 — The Chain Rule: Sensitivities Multiply

*≤5 min read. Then straight to the worksheet.*

## Why this matters (the real reason)

A deep neural network is a **pipeline**: layer feeds layer feeds layer feeds loss (Module 1.4 —
machines feeding machines). Training needs to know how a weight buried at the *start* of the pipe
affects the loss at the *end*. The chain rule answers that, and the algorithm that applies it
layer-by-layer has a famous name: **backpropagation**. This lesson *is* backprop. Not "like"
backprop — the actual math.

## The one big idea

Think exchange rates. Suppose:

- 1 AUD buys 0.65 USD (sensitivity of USD to AUD: 0.65)
- 1 USD buys 150 JPY (sensitivity of JPY to USD: 150)

How sensitive is your yen to your Aussie dollar? **Multiply:** $0.65 \times 150 = 97.5$ JPY per AUD.
Sensitivities along a pipeline multiply. Same with gears: if gear B spins 3× faster than A,
and C spins 2× faster than B, then C spins 6× faster than A.

Now in function language. A pipeline $x \to g \to f$ is written $f(g(x))$, and:

$$\big(f(g(x))\big)' = \underbrace{f'(g(x))}_{\text{outer's sensitivity}} \times \underbrace{g'(x)}_{\text{inner's sensitivity}}$$

One subtlety, and it matters: the outer function's sensitivity is measured **at the value the
inner one hands it** — $f'(g(x))$, not $f'(x)$. The USD→JPY rate applies to your *dollars*,
not to your original Aussie amount.

## Watch one get played

Differentiate $h(x) = (3x + 1)^2$:

$$g(x) = 3x + 1, \quad f(u) = u^2 \qquad \leftarrow \text{move: name the pipeline (inner } g \text{, outer } f\text{)}$$
$$f'(u) = 2u, \qquad g'(x) = 3 \qquad \leftarrow \text{move: differentiate each stage alone (power rule; line slope)}$$
$$h'(x) = 2(3x+1) \cdot 3 = 6(3x+1) \qquad \leftarrow \text{move: multiply along the pipe, outer evaluated at } g(x)$$

**Sanity check by nudging** at $x = 1$: $h'(1) = 6 \times 4 = 24$. And numerically:
$\frac{(3(1.001)+1)^2 - 4^2}{0.001} = \frac{16.024\ldots - 16}{0.001} \approx 24.0$. The pipe agrees.

## The Python connection

Your nudge function from 3.1 checks any chain-rule answer — and so does sympy:

```python
def derivative(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h

def h_pipe(x):
    return (3*x + 1)**2          # the whole pipeline as one function

print(derivative(h_pipe, 1))     # ≈ 24  — matches 6(3·1+1)

import sympy as sp
x = sp.symbols("x")
print(sp.diff((3*x + 1)**2, x))  # 18*x + 6  — expand 6(3x+1): same thing
```

Longer pipes just mean more factors: $f(g(k(x)))$ has derivative $f' \cdot g' \cdot k'$,
each evaluated at what the previous stage handed it. Backprop walks a pipe *millions* of
functions wide and hundreds deep, multiplying as it goes.

## What breaks it (the classic traps)

- **Forgetting the inner derivative:** $(3x+1)^2 \to 2(3x+1)$ and stop. That drops the $\times 3$ —
  the single most common calculus error on Earth.
- **Evaluating the outer at $x$ instead of $g(x)$:** writing $2x \cdot 3$ instead of $2(3x+1) \cdot 3$.
- **Not seeing the pipeline:** $(x^2+1)^3$ is *not* handled by the power rule alone —
  first name the inner $x^2 + 1$, or the answer is wrong.

> **Deep-end question to hold in your head during the worksheet:**
> a pipe 10 stages long, each stage with sensitivity $0.5$. What's the end-to-end sensitivity?
> Now 100 stages. This tiny multiplication is why very deep networks once *couldn't* train —
> look up "vanishing gradients" after the worksheet and enjoy recognising the math.

**Now: worksheet `03-chain-rule` — pen and paper. Photograph it into `scans/inbox/` when done.**
