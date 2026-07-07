# Worksheet 1.1 — Functions as Machines

*Pen and paper. Show the substitution step — write the input going into the slot, brackets and all,
before simplifying. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: run the machines

The machine: $f(x) = 2x + 3$. Compute:

1. $f(5)$

   ::: answer
   $f(5) = 13$ — move: substitute $x = 5$ into $2x+3$: $2(5)+3 = 13$.
   :::

2. $f(0)$

   ::: answer
   $f(0) = 3$ — move: substitute $x = 0$: $2(0)+3 = 3$.
   :::

3. $f(-2)$   *(brackets around the input — the #1 sign-error defence)*

   ::: answer
   $f(-2) = -1$ — move: substitute $x = -2$ with brackets: $2(-2)+3 = -4+3 = -1$.
   :::

4. $f\!\left(\frac{1}{2}\right)$

   ::: answer
   $f\!\left(\frac{1}{2}\right) = 4$ — move: substitute $x = \frac{1}{2}$: $2\left(\frac{1}{2}\right)+3 = 1+3 = 4$.
   :::

---

## Part B — Core: slots take anything

5. $g(x) = x^2 - 4$. Compute $g(3)$, $g(-3)$ and $g(1)$.

   ::: answer
   $g(3) = 5$, $g(-3) = 5$, $g(1) = -3$ — move: substitute each value, square first (brackets
   handle the sign): $3^2-4=5$, $(-3)^2-4=5$, $1^2-4=-3$.
   :::

6. Same $g$. Compute $g(a)$ and $g(2a)$ — symbols go in the slot whole, just like numbers.

   ::: answer
   $g(a) = a^2 - 4$; $g(2a) = 4a^2 - 4$ — move: the whole symbol goes in the slot,
   then $(2a)^2 = 4a^2$ (square applies to the 2 as well as the $a$).
   :::

7. $f(x) = 2x + 3$ again. Compute $f(x + 1)$, then separately compute $f(x) + 1$.
   Are they the same machine? One sentence: what's the difference in *where* the 1 enters the pipeline?

   ::: answer
   $f(x+1) = 2x+5$ (move: substitute $x+1$ into the slot: $2(x+1)+3 = 2x+2+3$); $f(x)+1 = 2x+4$
   (move: run $f$ first, then add 1 outside). Not the same machine — $f(x+1)$ feeds the extra 1
   in *before* doubling, $f(x)+1$ adds it *after*.
   :::

8. State the domain of each machine — i.e. which inputs crash it, if any:

   a) $p(x) = \dfrac{7}{x - 2}$

   b) $q(x) = \sqrt{x - 5}$

   c) $r(x) = \log(x)$

   d) $s(x) = 3x^2 - x + 1$

   ::: answer
   a) all reals except $x = 2$ — move: denominator can't be 0, so exclude the value that makes $x-2=0$.
   b) $x \geq 5$ — move: the basement of a square root can't be negative, so require $x-5 \geq 0$.
   c) $x > 0$ — move: $\log$ is only defined for a strictly positive argument.
   d) all reals — move: a polynomial has no basement and no root, so nothing to crash it.
   :::

---

## Part C — Spot the error

Each claim below contains exactly one mistake. Circle it and name what went wrong.

9. "Given $f(x) = x^2$, we get $f(-4) = -4^2 = -16$."

   ::: answer
   Broken move: missing brackets around the input. It should be $(-4)^2 = 16$, not $-4^2 = -(4^2) = -16$.
   Correct: $f(-4) = 16$.
   :::

10. "Given $f(x) = 3x$, we get $f(x + 2) = 3x + 2$."

    ::: answer
    Broken move: didn't feed the *whole* input through the machine — only added the $2$ outside
    instead of substituting $x+2$ for $x$: $3(x+2) = 3x+6$. Correct: $f(x+2) = 3x+6$.
    :::

11. "Given $f(x) = 5x + 1$, the expression $f(2)$ means $f \times 2$, so the answer depends on $f$."

    ::: answer
    Broken move: $f(2)$ is notation for "run the machine $f$ on input 2", not multiplication —
    $f$ is the machine's name, not a variable. Correct: $f(2) = 5(2)+1 = 11$.
    :::

---

## Part D — Deep end

*Beyond what was taught. Wrong attempts with visible reasoning beat blank space.*

12. Find the domain of $m(x) = \dfrac{1}{x^2 - 9}$.
    *(Which inputs make the basement zero? There's more than one.)*

    ::: answer
    All reals except $x = 3$ and $x = -3$ — move: solve $x^2 - 9 = 0 \Rightarrow x^2 = 9 \Rightarrow x = \pm 3$,
    then exclude both.
    :::

13. Design your own machine whose domain is "every number except 7". Write its blueprint.

    ::: answer
    Sample blueprint: $h(x) = \dfrac{1}{x - 7}$ — move: put $x-7$ in the basement so it's the only
    value that zeroes it out. (Any machine with a $(x-7)$ denominator, or $\sqrt{x-7}$ shifted
    appropriately, also works — check yours crashes at 7 and nowhere else.)
    :::

14. $f(x) = 2x + 3$. Compute $f(f(2))$ — feed the machine its own output.
    *(This move gets a whole unit soon.)*

    ::: answer
    $f(f(2)) = 17$ — move: inside-out. $f(2) = 2(2)+3 = 7$, then feed that output back in:
    $f(7) = 2(7)+3 = 17$.
    :::

15. The lesson's deep-end: $f(x) = (x+1)^2 - x^2$ and $g(x) = 2x + 1$. Expand $f$'s blueprint
    with Module 0 moves. Same machine as $g$, or not? What does this tell you about
    "different blueprint" vs "different machine"?

    ::: answer
    Same machine. Move: expand $(x+1)^2 = x^2+2x+1$, so $f(x) = x^2+2x+1-x^2 = 2x+1 = g(x)$.
    Two blueprints can look completely different on paper yet produce identical output for every
    input — "different blueprint" doesn't mean "different machine".
    :::

---

## Part E — Python check (at the computer, after the pen work)

16. Define your Part A machine and check your answers:

```python
def f(x):
    return 2 * x + 3

print(f(5), f(0), f(-2), f(0.5))
```

17. Crash a machine on purpose — confirm your domain answer for problem 8a:

```python
def p(x):
    return 7 / (x - 2)

print(p(3))    # fine
print(p(2))    # what error do you get? Write its name next to problem 8a.
```

> **Bonus thought:** for problem 15, how would you get Python to give evidence that two blueprints
> are the same machine? (Hint: same input → same output, *every time*. Try a loop over many inputs…)
