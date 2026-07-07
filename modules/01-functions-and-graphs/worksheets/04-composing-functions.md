# Worksheet 1.4 — Composing Functions

*Pen and paper. When evaluating compositions, write the intermediate value — show the output of the
inner machine before it enters the outer one. That intermediate is where errors hide.
Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: two machines, four runs

$f(x) = x^2 \qquad g(x) = x + 3$

1. $f(g(1))$   *(g first: what does g hand to f?)*

2. $g(f(1))$

3. $f(g(-3))$

4. $g(f(-3))$

---

## Part B — Core: blueprints and decomposition

5. Same $f, g$. Build the combined blueprints $f(g(x))$ and $g(f(x))$, and expand both
   (Module 0.3 moves). Are they the same machine?

6. $u(x) = 2x - 1$ and $v(x) = \dfrac{1}{x}$. Build $v(u(x))$ and $u(v(x))$.
   State the domain of each — *which input crashes which pipeline?*

7. Decompose each machine into an inner and outer blueprint
   (write "inner: …, outer: …"):

   a) $h(x) = (3x + 2)^2$

   b) $k(x) = 2^{x - 4}$

   c) $m(x) = \dfrac{1}{x^2 + 1}$

8. Three-deep: $a(x) = x + 1$, $b(x) = 2x$, $c(x) = x^2$. Compute $c(b(a(2)))$ step by step,
   writing each intermediate. Then build the full blueprint $c(b(a(x)))$.

---

## Part C — Spot the error

Each solution has exactly one broken step. Circle it and name the fix.

9. Claimed: with $f(x) = x^2$ and $g(x) = x + 3$, "$f(g(x)) = x^2 + 3$."

10. Claimed evaluation of $f(g(2))$ with $f(x) = 3x$, $g(x) = x - 5$:
    - line 1: $f(2) = 6$
    - line 2: $g(6) = 1$
    - line 3: so $f(g(2)) = 1$

11. Claimed: "$f(g(x)) = g(f(x))$ for all machines, because multiplication is commutative."

---

## Part D — Deep end

*Beyond what was taught.*

12. The lesson's self-feeding machine: $f(x) = \dfrac{x}{2} + 1$. Starting at $x = 0$, apply $f$
    five times, writing every value. Where is it heading? Find the exact number it's creeping
    toward — *(hint: that special number $x^{\ast}$ doesn't move: solve $f(x^{\ast}) = x^{\ast}$ with
    Module 0 moves.)*

13. Layers: with $\ell(x) = 2x + 1$, build $\ell(\ell(\ell(x)))$ and expand it fully.
    What species is the result? What does that suggest about stacking this kind of machine?
    *(Hold that thought — it's the whole point of unit 1.5.)*

14. Undo machines: $g(x) = x + 3$ and $u(x) = x - 3$. Compute $u(g(x))$.
    Now find the undo machine for $f(x) = 2x - 1$ — the machine $w$ with $w(f(x)) = x$.
    *(Solve it like a balance game: get $x$ back.)*

15. Wiggle whisper: machine $b$ doubles any small change to its input; machine $c$ triples any
    small change. If a pipeline runs $x \to b \to c$, a small wiggle in $x$ comes out how many
    times bigger? What if the pipeline were ten machines, each doubling?

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
