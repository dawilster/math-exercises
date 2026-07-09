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

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

12. The lesson's self-feeding machine: $f(x) = \dfrac{x}{2} + 1$. Starting at $x = 0$, apply $f$
    five times, writing every value. Where is it heading? Find the exact number it's creeping
    toward — *(hint: that special number $x^{\ast}$ doesn't move: solve $f(x^{\ast}) = x^{\ast}$ with
    Module 0 moves.)*

    ::: rephrase
    Two jobs bolted together. Job one: feed the machine its own output five times — the exact
    thing the lesson's calm-case picture did, homing in on a dashed line. Job two: name the number
    that line *is*. The magic: a machine parks where its input equals its output — a "fixed point" —
    so "find the $x^{\ast}$ that doesn't move" is just the balance game $f(x^{\ast}) = x^{\ast}$.
    :::

    ::: hint
    Start job one by hand: input $0$ gives $f(0) = \tfrac{0}{2} + 1 = 1$. Feed that $1$ back in.
    Keep a running list of all five values and watch where they crowd.
    :::

    ::: hint
    For job two, a fixed point is an input the machine hands straight back: $x^{\ast} = \tfrac{x^{\ast}}{2} + 1$.
    Solve it with Module 0 balance moves (subtract $\tfrac{x^{\ast}}{2}$, then double).
    :::

    ::: steps
    1. **Feed the output back in, five times.** $0 \to 1 \to 1.5 \to 1.75 \to 1.875 \to 1.9375$ — closing in on $2$.
    2. **Set up the fixed point (input = output).** $x^{\ast} = \dfrac{x^{\ast}}{2} + 1$
    3. **Balance-game: subtract $\tfrac{x^{\ast}}{2}$ from both sides.** $\dfrac{x^{\ast}}{2} = 1$
    4. **Double both sides.** $x^{\ast} = 2$ — matches where the values crowd.
    :::

13. Layers: with $\ell(x) = 2x + 1$, build $\ell(\ell(\ell(x)))$ and expand it fully.
    What species is the result? What does that suggest about stacking this kind of machine?
    *(Hold that thought — it's the whole point of unit 1.5.)*

    ::: rephrase
    "Build $\ell(\ell(\ell(x)))$" means bolt the same machine to itself three deep, then expand to
    a single blueprint — exactly problem 8's three-deep move, but with one machine reused. Work
    inside-out: do the innermost $\ell(x)$ first, feed that *whole* result into the next $\ell$, then
    again. "What species" asks: after expanding, what kind of expression is it — a line? a
    parabola? — and does it stay that kind when you stack more?
    :::

    ::: hint
    Start with just the inner two: $\ell(\ell(x))$. Feed the whole blueprint $2x+1$ into $\ell$'s
    slot — that's $\ell(2x+1)$, bracketed (the 1.1 rule).
    :::

    ::: hint
    Take your $\ell(\ell(x))$ result and feed that whole thing into one more $\ell$. Then expand and
    read off the highest power of $x$.
    :::

    ::: steps
    1. **Inner two: feed $2x+1$ into $\ell$.** $\ell(\ell(x)) = 2(2x+1)+1 = 4x+3$
    2. **Feed that whole result into one more $\ell$.** $\ell(\ell(\ell(x))) = 2(4x+3)+1 = 8x+7$
    3. **Read the species.** highest power of $x$ is $1$ → still a straight line ($ax+b$ form). Stacking linear machines only ever produces another linear machine.
    :::

14. Undo machines: $g(x) = x + 3$ and $u(x) = x - 3$. Compute $u(g(x))$.
    Now find the undo machine for $f(x) = 2x - 1$ — the machine $w$ with $w(f(x)) = x$.
    *(Solve it like a balance game: get $x$ back.)*

    ::: rephrase
    First part is a warm confidence-builder: run $u$ after $g$ and watch the $+3$ and $-3$ cancel —
    $u$ is $g$'s "undo". Second part is the real ask: given $f(x) = 2x-1$, invent the machine $w$
    that reverses it, so running $f$ then $w$ lands you back on the $x$ you started with. Finding an
    undo machine = solve $y = f(x)$ for $x$ (get $x$ alone), the same re-arranging as Module 0.
    :::

    ::: hint
    For $u(g(x))$: feed the whole $g(x) = x+3$ into $u(x) = x-3$, i.e. compute $(x+3) - 3$. For $f$'s
    undo, first write $y = 2x - 1$ and aim to get $x$ by itself.
    :::

    ::: hint
    Balance-game on $y = 2x-1$: add $1$ to both sides, then divide by $2$. Whatever $x$ equals in
    terms of $y$ is the recipe for $w$ — just rename $y$ back to $x$.
    :::

    ::: steps
    1. **Compose $u$ after $g$.** $u(g(x)) = (x+3) - 3 = x$ — $u$ perfectly undoes $g$.
    2. **Set $y = f(x)$ for the second machine.** $y = 2x - 1$
    3. **Balance-game: $+1$ both sides.** $y + 1 = 2x$
    4. **$\div 2$ both sides — $x$ alone.** $x = \dfrac{y+1}{2}$
    5. **Rename $y \to x$ to write the machine.** $w(x) = \dfrac{x+1}{2}$
    :::

15. Wiggle whisper: machine $b$ doubles any small change to its input; machine $c$ triples any
    small change. If a pipeline runs $x \to b \to c$, a small wiggle in $x$ comes out how many
    times bigger? What if the pipeline were ten machines, each doubling?

    ::: rephrase
    This is the lesson's chain-rule whisper in disguise. "Doubles any small change" means: nudge
    the input a tiny bit and the output moves *twice* as far — a multiplier of $2$. Run $x \to b \to c$
    and that nudge passes through $b$ ($\times 2$) then $c$ ($\times 3$). The question: what's the
    total stretch on the nudge? Then: ten machines each $\times 2$ in a row?
    :::

    ::: hint
    The nudge doesn't *add* through the pipeline, it gets *multiplied* at each machine — $b$ scales
    it by $2$, then $c$ scales that result by $3$.
    :::

    ::: hint
    So the total is $2$ then $\times 3 = 2 \times 3$. Ten doublings in a row is $2$ multiplied by
    itself ten times — write it as a power.
    :::

    ::: steps
    1. **Multiply the wiggle-factors along the chain** (each machine scales the nudge). $2 \times 3 = 6$ times bigger.
    2. **Ten doubling machines: multiply ten $2$'s.** $2^{10} = 1024$ times bigger — this multiplying-down-the-chain is exactly the chain rule the lesson promised.
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
