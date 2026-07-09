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

    ::: rephrase
    "Solve for $x$" means get $x$ alone. But $x$ is downstairs in a fraction $\frac{k}{x}$ (the
    **basement**), and there's a spare $+c$ cluttering that side. You can't reach into the
    basement while $c$ is bolted on top — so this is problem 5's "clear the clutter first" move
    followed by the lesson-table basement move. First sweep $c$ off, *then* deal with the fraction.
    :::

    ::: hint
    The $+c$ is the outermost layer, and it isn't touching $x$ at all. Peel it off first to get
    the fraction $\frac{k}{x}$ sitting alone on one pan.
    :::

    ::: hint
    Now $x$ is stranded in the denominator. The basement move (lesson table): multiply both pans
    by $x$ to lift it upstairs — then $x$ is free to isolate.
    :::

    ::: steps
    1. **$-c$ both sides** — clears the clutter. $\dfrac{k}{x} = y - c$
    2. **$\times x$ both sides** — lifts $x$ out of the basement. $k = x(y-c)$
    3. **$\div (y-c)$ both sides** ($y \neq c$) — frees $x$. $x = \dfrac{k}{y - c}$
    :::

11. Solve for $\mathbf{a}$: $\;y = \frac{a+b}{a}$   *(the target appears TWICE. Hint: multiply
    out first, then herd every $a$-term onto one pan and factor — 0.3 will make this
    mechanical, but have a go now)*

    ::: rephrase
    The snag: $a$ shows up in **two** places — on top *and* on the bottom of the fraction. You
    can never isolate a symbol while it's split across two spots. So the whole game is: gather
    every $a$ into one place, then treat that clump as a single thing you can divide away. First
    clear the fraction (the basement move), *then* herd the $a$'s together.
    :::

    ::: hint
    Start by killing the fraction: multiply both pans by the $a$ downstairs. That turns
    $y = \frac{a+b}{a}$ into a plain equation with no denominator.
    :::

    ::: hint
    Now every $a$ is on one side, but there are two $a$-terms. Collect them onto one pan, then
    **factor $a$ out** — pulling $a$ outside a bracket turns two $a$'s back into one, which you
    can finally divide away.
    :::

    ::: steps
    1. **$\times a$ both sides** — clears the fraction. $ya = a + b$
    2. **$-a$ both sides** — herds the $a$-terms onto the left. $ya - a = b$
    3. **Factor $a$ out** — two $a$'s become one. $a(y-1) = b$
    4. **$\div (y-1)$ both sides** ($y \neq 1$) — frees $a$. $a = \dfrac{b}{y - 1}$
    :::

12. The learning-rate schedule $\eta = \frac{\eta_0}{1 + kt}$ says how a network's step size
    shrinks over time. Solve for $\mathbf{t}$: *given a target learning rate, when do we reach it?*
    (Treat $\eta_0$ and $k$ as knowns. Read $\eta$ as just another symbol — "eta". Once you clear
    the basement you'll have a bracket to multiply out — arriving early is 0.3's distributive law,
    $a(b+c) = ab+ac$: multiply the outside term onto *every* term inside.)

    ::: rephrase
    Read $\eta$ as just another number ("eta"). The target $t$ is buried in the **basement** —
    down in the denominator $1+kt$ — with $\eta$ multiplying the whole fraction out front. Same
    opening as problem 10: get $t$ out of the basement first (multiply both sides by $1+kt$).
    That leaves a bracket to multiply out, and from there it's a straight peel like problem 7.
    :::

    ::: hint
    $t$ sits inside the denominator $1+kt$. The basement move: multiply both pans by $(1+kt)$ to
    lift that whole bracket up out of the fraction.
    :::

    ::: hint
    Now you have $\eta(1+kt) = \eta_0$. Expand the bracket — distribute $\eta$ onto **every** term
    inside ($a(b+c)=ab+ac$) — then peel the leftover pieces off $t$ one legal move at a time.
    :::

    ::: steps
    1. **$\times(1+kt)$ both sides** — lifts $t$ out of the basement. $\eta(1+kt) = \eta_0$
    2. **Expand** ($\eta \cdot 1 + \eta \cdot kt$). $\eta + \eta k t = \eta_0$
    3. **$-\eta$ both sides** — isolates the $t$-term. $\eta k t = \eta_0 - \eta$
    4. **$\div (\eta k)$ both sides** ($\eta \neq 0$, $k \neq 0$) — frees $t$. $t = \dfrac{\eta_0 - \eta}{\eta k}$
    :::

13. From 0.1's deep end: $y = mx + b$ rearranged for $m$, then that result rearranged for $y$.
    Do you land back on the original? What does that tell you about legal moves?

    ::: rephrase
    This one asks for a **round trip**, not a number. Step 1: rearrange $y = mx + b$ to make $m$
    the subject. Step 2: take *that* result and rearrange it back to make $y$ the subject. Then
    ask: did you land on the original equation? The real point isn't the algebra — it's noticing
    that every move you made had a partner move that undid it.
    :::

    ::: hint
    First leg: solve $y = mx + b$ for $m$. Same peel as always — clear the $+b$ off the right
    side, then free $m$ from what's multiplying it.
    :::

    ::: hint
    Second leg: take your $m = \frac{y-b}{x}$ and run it *forward* for $y$, reversing each move you
    just made. You divided by $x$ — so now multiply by $x$; you subtracted $b$ — so now add $b$.
    Watch where you end up.
    :::

    ::: steps
    1. **Rearrange for $m$** ($-b$ both sides, then $\div x$). $m = \dfrac{y - b}{x}$
    2. **Rearrange that for $y$** ($\times x$ both sides, then $+b$). $y = mx + b$
    3. **Read the meaning.** You landed exactly back on the original. Each move ($-b$, $\div x$) was undone by its **inverse** ($+b$, $\times x$) — that's what makes a move *legal*: it's reversible, so no truth is lost either way.
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
