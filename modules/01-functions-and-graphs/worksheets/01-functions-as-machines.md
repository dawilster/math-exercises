# Worksheet 1.1 — Functions as Machines

*Pen and paper. Show the substitution step — write the input going into the slot, brackets and all,
before simplifying. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: run the machines

The machine: $f(x) = 2x + 3$. Compute:

1. $f(5)$

2. $f(0)$

3. $f(-2)$   *(brackets around the input — the #1 sign-error defence)*

4. $f\!\left(\frac{1}{2}\right)$

---

## Part B — Core: slots take anything

5. $g(x) = x^2 - 4$. Compute $g(3)$, $g(-3)$ and $g(1)$.

6. Same $g$. Compute $g(a)$ and $g(2a)$ — symbols go in the slot whole, just like numbers.

7. $f(x) = 2x + 3$ again. Compute $f(x + 1)$, then separately compute $f(x) + 1$.
   Are they the same machine? One sentence: what's the difference in *where* the 1 enters the pipeline?

8. State the domain of each machine — i.e. which inputs crash it, if any:

   a) $p(x) = \dfrac{7}{x - 2}$

   b) $q(x) = \sqrt{x - 5}$

   c) $r(x) = \log(x)$

   d) $s(x) = 3x^2 - x + 1$

---

## Part C — Spot the error

Each claim below contains exactly one mistake. Circle it and name what went wrong.

9. "Given $f(x) = x^2$, we get $f(-4) = -4^2 = -16$."

10. "Given $f(x) = 3x$, we get $f(x + 2) = 3x + 2$."

11. "Given $f(x) = 5x + 1$, the expression $f(2)$ means $f \times 2$, so the answer depends on $f$."

---

## Part D — Deep end

*Beyond what was taught. Wrong attempts with visible reasoning beat blank space.*

12. Find the domain of $m(x) = \dfrac{1}{x^2 - 9}$.
    *(Which inputs make the basement zero? There's more than one.)*

13. Design your own machine whose domain is "every number except 7". Write its blueprint.

14. $f(x) = 2x + 3$. Compute $f(f(2))$ — feed the machine its own output.
    *(This move gets a whole unit soon.)*

15. The lesson's deep-end: $f(x) = (x+1)^2 - x^2$ and $g(x) = 2x + 1$. Expand $f$'s blueprint
    with Module 0 moves. Same machine as $g$, or not? What does this tell you about
    "different blueprint" vs "different machine"?

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
