# Worksheet 0.2 — Rearranging for ANY Symbol

*Pen and paper. For every problem, write the **move you're making** next to each step, like
"÷ t both sides (t ≠ 0)". The moves are the point, not the answers. Photograph into
`scans/inbox/` when done.*

---

## Part A — Warm-up: numbers wearing letter costumes

Solve for the **bold** symbol. One or two moves each. Name every move.

1. Solve for $\mathbf{t}$: $\;v = at$

   ::: answer
   $t = \dfrac{v}{a}$ — move: $\div a$ both sides ($a \neq 0$).
   :::

2. Solve for $\mathbf{b}$: $\;y = x + b$

   ::: answer
   $b = y - x$ — move: $-x$ both sides.
   :::

3. Solve for $\mathbf{w}$: $\;p = 4w$

   ::: answer
   $w = \dfrac{p}{4}$ — move: $\div 4$ both sides.
   :::

4. Solve for $\mathbf{d}$: $\;s = \frac{d}{t}$

   ::: answer
   $d = st$ — move: $\times t$ both sides ($t \neq 0$).
   :::

---

## Part B — Core: multi-move rearrangements

Same strategy as 0.1: peel the outermost layer first. Name every move, and note any
"can't be zero" assumptions.

5. Solve for $\mathbf{x}$: $\;y = mx + b$

   ::: answer
   $x = \dfrac{y - b}{m}$ — moves: $-b$ both sides → $y - b = mx$, then $\div m$ both sides ($m \neq 0$).
   :::

6. Solve for $\mathbf{h}$: $\;A = \frac{1}{2}bh$

   ::: answer
   $h = \dfrac{2A}{b}$ — moves: $\times 2$ both sides → $2A = bh$, then $\div b$ both sides ($b \neq 0$).
   :::

7. Solve for $\mathbf{C}$: $\;F = \frac{9}{5}C + 32$   *(the actual Celsius↔Fahrenheit formula)*

   ::: answer
   $C = \dfrac{5}{9}(F - 32)$ — moves: $-32$ both sides → $F - 32 = \frac{9}{5}C$, then $\times \frac{5}{9}$ both sides.
   :::

8. Solve for $\mathbf{r}$: $\;A = \pi r^2$   *(state which root you keep, and why)*

   ::: answer
   $r = \sqrt{\dfrac{A}{\pi}}$ — moves: $\div \pi$ both sides → $\frac{A}{\pi} = r^2$, then $\sqrt{\phantom{x}}$ both sides.
   Keep the **positive** root only — $r$ is a physical length, and lengths aren't negative.
   :::

9. Solve for $\mathbf{t}$: $\;d = \frac{1}{2}at^2$   *(assume $t > 0$)*

   ::: answer
   $t = \sqrt{\dfrac{2d}{a}}$ — moves: $\times 2$ both sides → $2d = at^2$, then $\div a$ both sides ($a \neq 0$) → $t^2 = \frac{2d}{a}$,
   then $\sqrt{\phantom{x}}$ both sides. Keep the **positive** root since we're told $t > 0$.
   :::

---

## Part D — Deep end

*These go beyond what was taught. Struggling here IS the workout — wrong attempts with
named moves are worth more than blank space.*

10. Solve for $\mathbf{x}$: $\;\frac{k}{x} + c = y$   *(the target is in the basement AND there's clutter)*

    ::: answer
    $x = \dfrac{k}{y - c}$ — moves: $-c$ both sides → $\frac{k}{x} = y - c$, then $\times x$ both sides → $k = x(y-c)$,
    then $\div (y-c)$ both sides ($y \neq c$).
    :::

11. Solve for $\mathbf{a}$: $\;y = \frac{a+b}{a}$   *(the target appears TWICE. Hint: multiply
    out first, then herd every $a$-term onto one pan and factor — 0.3 will make this
    mechanical, but have a go now)*

    ::: answer
    $a = \dfrac{b}{y - 1}$ — moves: $\times a$ both sides → $ya = a + b$, then $-a$ both sides → $ya - a = b$,
    factor the left: $a(y-1) = b$, then $\div (y-1)$ both sides ($y \neq 1$).
    :::

12. The learning-rate schedule $\eta = \frac{\eta_0}{1 + kt}$ says how a network's step size
    shrinks over time. Solve for $\mathbf{t}$: *given a target learning rate, when do we reach it?*
    (Treat $\eta_0$ and $k$ as knowns. Read $\eta$ as just another symbol — "eta". Once you clear
    the basement you'll have a bracket to multiply out — arriving early is 0.3's distributive law,
    $a(b+c) = ab+ac$: multiply the outside term onto *every* term inside.)

    ::: answer
    $t = \dfrac{\eta_0 - \eta}{\eta k}$ — moves: $\times(1+kt)$ both sides → $\eta(1+kt) = \eta_0$, expand → $\eta + \eta k t = \eta_0$,
    then $-\eta$ both sides → $\eta k t = \eta_0 - \eta$, then $\div (\eta k)$ both sides ($\eta \neq 0$, $k \neq 0$).
    :::

13. From 0.1's deep end: $y = mx + b$ rearranged for $m$, then that result rearranged for $y$.
    Do you land back on the original? What does that tell you about legal moves?

    ::: answer
    Yes — rearranging $y = mx+b$ for $m$ gives $m = \dfrac{y-b}{x}$; rearranging *that* for $y$ ($\times x$ both sides, then $+b$
    both sides) hands back $y = mx + b$ exactly. Every legal move has an inverse move that undoes it ($+$/$-$, $\times$/$\div$),
    so walking the moves forward then backward always returns you to where you started.
    :::

---

## Part E — Python check (at the computer, after the pen work)

14. Verify problems 5–9 the way the lesson showed — random numbers, round trip:

```python
# problem 5 example: y = m*x + b, and your rearrangement x = ???
m, b, x = 2.5, 1.0, 7.0          # invent any numbers you like
y = m * x + b                     # forwards, with the original formula
x_check = (y - b) / m             # backwards, with YOUR rearrangement
print(x_check == x)               # True → your algebra survived real numbers
```

Write ✓ next to each Part B problem Python confirms.

15. Check your Part D answers with the sympy referee (see the notebook), e.g.:

```python
import sympy as sp
k, x, c, y = sp.symbols("k x c y")
print(sp.solve(sp.Eq(k/x + c, y), x))   # problem 10
```

> **Bonus thought:** in problem 14, try `b = 0.1` and print `x_check` — you may see
> something like `6.999999999999999`. Floating-point numbers are *slightly* fuzzy.
> This is why real ML code compares with `abs(a - b) < 1e-9` instead of `==`.
