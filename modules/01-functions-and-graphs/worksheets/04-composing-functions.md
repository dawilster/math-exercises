# Worksheet 1.4 — Composing Functions

*Pen and paper. When evaluating compositions, write the intermediate value — show the output of the
inner machine before it enters the outer one. That intermediate is where errors hide.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: two machines, four runs

$f(x) = x^2 \qquad g(x) = x + 3$

1. $f(g(1))$   *(g first: what does g hand to f?)*

   ::: answer
   $g(1) = 4$, then $f(4) = 16$. Move: work inside-out — innermost function ($g$) first.
   :::

2. $g(f(1))$

   ::: answer
   $f(1) = 1$, then $g(1) = 4$. Move: same inside-out rule, but now $f$ is innermost.
   :::

3. $f(g(-3))$

   ::: answer
   $g(-3) = 0$, then $f(0) = 0$.
   :::

4. $g(f(-3))$

   ::: answer
   $f(-3) = 9$, then $g(9) = 12$.
   :::

---

## Part B — Core: blueprints and decomposition

5. Same $f, g$. Build the combined blueprints $f(g(x))$ and $g(f(x))$, and expand both
   (Module 0.3 moves). Are they the same machine?

   ::: answer
   $f(g(x)) = (x+3)^2 = x^2 + 6x + 9$. $g(f(x)) = x^2 + 3$. Not the same machine —
   move: substitute the whole inner expression into the outer, don't just relabel.
   :::

6. $u(x) = 2x - 1$ and $v(x) = \dfrac{1}{x}$. Build $v(u(x))$ and $u(v(x))$.
   State the domain of each — *which input crashes which pipeline?*

   ::: answer
   $v(u(x)) = \dfrac{1}{2x - 1}$, domain $x \neq \tfrac{1}{2}$ (that's where the denominator hits 0).
   $u(v(x)) = \dfrac{2}{x} - 1$, domain $x \neq 0$ (division by $x$ crashes first, before $u$ even runs).
   :::

7. Decompose each machine into an inner and outer blueprint
   (write "inner: …, outer: …"):

   a) $h(x) = (3x + 2)^2$

   b) $k(x) = 2^{x - 4}$

   c) $m(x) = \dfrac{1}{x^2 + 1}$

   ::: answer
   a) inner: $3x + 2$, outer: $\square^2$.
   b) inner: $x - 4$, outer: $2^{\square}$.
   c) inner: $x^2 + 1$, outer: $\dfrac{1}{\square}$.
   Move: find what's "done last" reading the expression outside-in — that's the outer machine.
   :::

8. Three-deep: $a(x) = x + 1$, $b(x) = 2x$, $c(x) = x^2$. Compute $c(b(a(2)))$ step by step,
   writing each intermediate. Then build the full blueprint $c(b(a(x)))$.

   ::: answer
   $a(2) = 3$, $b(3) = 6$, $c(6) = 36$. Blueprint: $c(b(a(x))) = c(b(x+1)) = c(2x+2) = (2x+2)^2 = 4x^2 + 8x + 4$.
   Move: chain inside-out, one substitution at a time, then expand at the end.
   :::

---

## Part C — Spot the error

Each solution has exactly one broken step. Circle it and name the fix.

9. Claimed: with $f(x) = x^2$ and $g(x) = x + 3$, "$f(g(x)) = x^2 + 3$."

   ::: answer
   Broken: they squared $x$ alone and then bolted on $g$'s $+3$, instead of substituting the
   whole $g(x) = x+3$ into $f$. Correct: $f(g(x)) = (x+3)^2 = x^2 + 6x + 9$.
   :::

10. Claimed evaluation of $f(g(2))$ with $f(x) = 3x$, $g(x) = x - 5$:
    - line 1: $f(2) = 6$
    - line 2: $g(6) = 1$
    - line 3: so $f(g(2)) = 1$

    ::: answer
    Line 1 is broken — $f(g(2))$ means $g$ runs first, not $f$. Correct order:
    $g(2) = -3$, then $f(-3) = -9$. So $f(g(2)) = -9$. The move that broke: composition
    order reversed (they computed $g(f(2))$ instead).
    :::

11. Claimed: "$f(g(x)) = g(f(x))$ for all machines, because multiplication is commutative."

    ::: answer
    False. Composition is not multiplication — the reasoning conflates two different operations.
    Problem 5's counterexample proves it: $x^2 + 6x + 9 \neq x^2 + 3$. Order of machines matters.
    :::

---

## Part D — Deep end

*Beyond what was taught.*

12. The lesson's self-feeding machine: $f(x) = \dfrac{x}{2} + 1$. Starting at $x = 0$, apply $f$
    five times, writing every value. Where is it heading? Find the exact number it's creeping
    toward — *(hint: that special number $x^{\ast}$ doesn't move: solve $f(x^{\ast}) = x^{\ast}$ with
    Module 0 moves.)*

    ::: answer
    Values: $0, 1, 1.5, 1.75, 1.875, 1.9375, \ldots$ — creeping toward $2$.
    Move: solve $x^{\ast} = \dfrac{x^{\ast}}{2} + 1$ → $\dfrac{x^{\ast}}{2} = 1$ → $x^{\ast} = 2$.
    :::

13. Layers: with $\ell(x) = 2x + 1$, build $\ell(\ell(\ell(x)))$ and expand it fully.
    What species is the result? What does that suggest about stacking this kind of machine?
    *(Hold that thought — it's the whole point of unit 1.5.)*

    ::: answer
    $\ell(\ell(x)) = 2(2x+1)+1 = 4x+3$. $\ell(\ell(\ell(x))) = 2(4x+3)+1 = 8x+7$.
    Still a straight line ($ax+b$ form) — stacking linear machines only ever produces another
    linear machine. Linear composition stays linear.
    :::

14. Undo machines: $g(x) = x + 3$ and $u(x) = x - 3$. Compute $u(g(x))$.
    Now find the undo machine for $f(x) = 2x - 1$ — the machine $w$ with $w(f(x)) = x$.
    *(Solve it like a balance game: get $x$ back.)*

    ::: answer
    $u(g(x)) = (x+3) - 3 = x$ — $u$ perfectly undoes $g$. For $f$: let $y = 2x-1$ and solve for
    $x$ (balance-game moves: $+1$ both sides, then $\div 2$) → $x = \dfrac{y+1}{2}$, so
    $w(x) = \dfrac{x+1}{2}$.
    :::

15. Wiggle whisper: machine $b$ doubles any small change to its input; machine $c$ triples any
    small change. If a pipeline runs $x \to b \to c$, a small wiggle in $x$ comes out how many
    times bigger? What if the pipeline were ten machines, each doubling?

    ::: answer
    $2 \times 3 = 6$ times bigger — wiggle-multipliers compose by multiplying. Ten doubling
    machines: $2^{10} = 1024$ times bigger.
    :::

---

## Part E — Python check (at the computer, after the pen work)

16. Verify Parts A and B:

```python
def f(x): return x ** 2
def g(x): return x + 3

print(f(g(1)), g(f(1)))          # your problems 1 and 2
print(f(g(2)) == (2 + 3) ** 2)   # blueprint check for problem 5
```

17. Verify problem 12 with a loop — watch the machine feed itself:

```python
x = 0
for step in range(10):        # repeat 10 times
    x = f_half(x)             # you define f_half first: x/2 + 1
    print(step, x)
```

Does it creep toward your Part D answer?

> **Bonus thought:** change the self-feeding machine to $f(x) = 3.9 \, x \, (1 - x)$ and start at
> $x = 0.5$. Loop 30 times and look at the numbers. Settling? Cycling? …Or something else?
> The notebook has the full reveal.
