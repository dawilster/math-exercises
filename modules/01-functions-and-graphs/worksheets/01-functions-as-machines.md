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

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

12. Find the domain of $m(x) = \dfrac{1}{x^2 - 9}$.
    *(Which inputs make the basement zero? There's more than one.)*

    ::: rephrase
    Same job as problem 8a — "which inputs crash it?" — but this machine has a *squared* basement.
    A fraction dies when its denominator hits 0, so the real question is: which $x$ make $x^2 - 9 = 0$?
    In 8a exactly one value crashed it; here the square means the danger can strike from two sides.
    :::

    ::: hint
    A fraction crashes only when the basement is zero. Ignore the top; set the bottom equal to 0.
    :::

    ::: hint
    You're solving $x^2 = 9$. Ask "what number squared gives 9?" — and remember a negative squared
    is still positive.
    :::

    ::: steps
    1. **Set the basement to zero** (a fraction crashes when its denominator is 0). $x^2 - 9 = 0$
    2. **Solve for the crashers.** $x^2 = 9 \Rightarrow x = \pm 3$
    3. **Exclude both from the domain.** all reals except $x = 3$ and $x = -3$
    :::

13. Design your own machine whose domain is "every number except 7". Write its blueprint.

    ::: rephrase
    This is problem 8a run *backwards*. There you were handed a machine and hunted for the input
    that crashes it; here you pick the crasher first — 7 — and build a machine around it. You need
    one ingredient that dies at exactly one input of your choosing. What crashes at a single value?
    :::

    ::: hint
    Fractions crash when the basement is 0 (that's the one-input crasher). What basement is zero
    *only* when $x = 7$?
    :::

    ::: steps
    1. **Put $x-7$ in the basement** — it's zero only at $x = 7$. $h(x) = \dfrac{1}{x - 7}$
    2. **Check it crashes at 7 and nowhere else.** $x - 7 = 0 \Rightarrow x = 7$; every other input runs
       fine → domain is every number except 7. (Any $(x-7)$ denominator works — verify yours the same way.)
    :::

14. $f(x) = 2x + 3$. Compute $f(f(2))$ — feed the machine its own output.
    *(This move gets a whole unit soon.)*

    ::: rephrase
    $f(f(2))$ means: run the machine on 2, then take whatever falls out the chute and run the machine
    on *that*. Work inside-out, exactly like nested brackets — innermost first. Only one of the two
    $f$'s has a number in its slot right now; the outer one is waiting for the inner one's output.
    :::

    ::: hint
    Deal with the *inner* $f(2)$ only — ignore the outer $f$ for a moment. Compute just $f(2)$.
    :::

    ::: hint
    Take that output number and drop it into the slot as a brand-new input: compute $f(\text{that number})$.
    :::

    ::: steps
    1. **Run the inner machine first.** $f(2) = 2(2)+3 = 7$
    2. **Feed that output back in.** $f(7) = 2(7)+3 = 17$
    :::

15. The lesson's deep-end: $f(x) = (x+1)^2 - x^2$ and $g(x) = 2x + 1$. Expand $f$'s blueprint
    with Module 0 moves. Same machine as $g$, or not? What does this tell you about
    "different blueprint" vs "different machine"?

    ::: rephrase
    This is the question the lesson told you to hold in your head. "Same machine?" means one precise
    thing: do both blueprints hand back the *same output for every input*? Plugging in a few numbers
    can only build suspicion; the honest test is to expand $f$'s blueprint with Module 0 moves until
    it's written in the same form as $g$, then read them side by side.
    :::

    ::: hint
    The obstacle is the $(x+1)^2$. Expand it first with Module 0's "square a binomial" —
    what is $(x+1)^2$ written out?
    :::

    ::: hint
    Substitute that expansion back into $f(x) = (x+1)^2 - x^2$ and collect like terms. Watch the
    $x^2$ terms — one is positive, one is negative.
    :::

    ::: steps
    1. **Expand the square** ($(x+1)^2 = x^2 + 2x + 1$). $f(x) = x^2 + 2x + 1 - x^2$
    2. **Cancel the $x^2$ terms.** $f(x) = 2x + 1$
    3. **Compare to $g$.** $2x + 1 = g(x)$ → same machine. Two blueprints can look completely
       different on paper yet produce identical output for every input — "different blueprint"
       doesn't mean "different machine".
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
