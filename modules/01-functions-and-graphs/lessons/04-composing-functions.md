# 1.4 — Composing Functions: Machines Feeding Machines

*≤5 min read. Then straight to the worksheet.*

## Why this matters (the real reason)

You've heard "deep learning" a thousand times. Here's the secret: **"deep" just means "deeply
composed"**. A 50-layer network is 50 machines bolted output-to-input:
$f_{50}(f_{49}(\dots f_2(f_1(x))\dots))$. A "layer" IS one machine in the chain. When you finish
this unit, the architecture diagrams in every ML paper stop being boxes-and-arrows mysticism and
become something you learned today: composition.

## The one big idea

Bolt two machines together: the output chute of $g$ empties into the input slot of $f$.

$$f(g(x)) \qquad \text{— read inside-out: } x \text{ enters } g \text{ FIRST, then } f$$

With $g(x) = x + 3$ and $f(x) = x^2$:

$$f(g(2)) = f(5) = 25 \qquad \text{but} \qquad g(f(2)) = g(4) = 7$$

**Order matters.** $f(g(x))$ and $g(f(x))$ are different machines. "Add 3 then square" ≠
"square then add 3" — exactly like Module 0's order of operations, but at machine scale.

## Building the combined blueprint

You can compute a composition's blueprint once and for all: feed the *entire* blueprint of $g$
into the slot of $f$ (whole, in brackets — the 1.1 rule):

$$f(g(x)) = f(x + 3) = (x+3)^2$$

And you can run it backwards — **decomposing** is the ML-reading superpower. See $h(x) = (2x-1)^3$
in a paper? Recognise it as a pipeline: *inner machine* $2x - 1$, *outer machine* $(\;)^3$.
Every gnarly formula is small machines in a trench coat.

## The Python connection

Composition is just calling a function on a function's result — you've probably already done it:

```python
def g(x): return x + 3
def f(x): return x ** 2

print(f(g(2)))    # 25 — g runs first, then f
print(g(f(2)))    # 7  — different machine!

# a "deep network" is literally this, repeated:
def network(x):
    return f3(f2(f1(x)))    # layer 1, then 2, then 3 — reading right to left
```

One notation gotcha: math writes $f(g(x))$ with $g$ *first in execution* but *second on the page*.
Pipelines run right-to-left in this notation. (Data people often draw it left-to-right as
$x \to g \to f$; same machine, friendlier arrow.)

## A whisper of what's coming

Module 3's headline act, the **chain rule**, answers: *if I wiggle the input of a pipeline, how
much does the final output wiggle?* Spoiler: each machine multiplies the wiggle, and the effects
**multiply down the chain**. That rule, applied to a deep network, is called **backpropagation** —
the algorithm that trains every model you've ever heard of. You now know the structure it runs on.

## Classic traps

- **Assuming $f(g(x)) = g(f(x))$.** Almost never true. Always check which machine eats first.
- **Feeding the blueprint in piecemeal.** $f(x+3)$ where $f(x)=x^2$ is $(x+3)^2$, not $x^2 + 3$.
  The entire input goes in the slot, bracketed.
- **Ignoring the middle domain.** $g$'s *output* must be a legal *input* for $f$. If
  $f(x) = \sqrt{x}$ and $g(x) = x - 5$, then $f(g(1)) = \sqrt{-4}$ — crash. A pipeline's domain
  is squeezed by every machine in it.

> **Deep-end question to hold in your head during the worksheet:**
> what if a machine eats its own output — $f(f(f(\dots f(x))))$? Try $f(x) = \frac{x}{2} + 1$
> starting from $x = 0$, by hand, five times. Where is it heading? Some self-feeding machines
> settle down like this one… and some do something so wild it has its own branch of mathematics.
> The notebook will show you.

**Now: worksheet `04-composing-functions` — pen and paper. Photograph into `scans/inbox/` when done.**
