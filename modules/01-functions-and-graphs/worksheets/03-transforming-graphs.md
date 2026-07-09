# Worksheet 1.3 — Transforming Graphs

*Pen and paper. Sketch FIRST, verify with matplotlib only in Part E after scanning.
For every transformation, name the move — "shift left 2", "flip over x-axis" — the way you
named balance-scale moves in Module 0. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: name the move

$f$ is any machine. Describe in words what each does to the graph of $y = f(x)$:

1. $y = f(x) + 4$

   ::: answer
   Shifts **up** 4 — move: add 4 to the output.
   :::

2. $y = f(x - 2)$   *(careful — inside the brackets is opposite day)*

   ::: answer
   Shifts **right** 2 — move: $x \to x - 2$ is added to the *input*, and input moves run
   backwards: $-2$ inside pushes the graph right, not left.
   :::

3. $y = 3f(x)$

   ::: answer
   Vertical stretch ×3 — move: multiply the output by 3.
   :::

4. $y = -f(x)$

   ::: answer
   Flips upside down (reflects over the $x$-axis) — move: flip the output.
   :::

5. $y = f(-x)$

   ::: answer
   Flips left-right (reflects over the $y$-axis) — move: flip the input.
   :::

---

## Part B — Core: sketch by moves

Start from the zoo animal, list the moves in order, then sketch. Mark the key point that moved
(vertex, crossing, or asymptote).

6. $y = x^2 - 3$   *(from $y = x^2$)*

   ::: answer
   Move: subtract 3 from the output → shift **down** 3. Vertex $(0,0) \to (0,-3)$.
   :::

7. $y = (x + 2)^2$   *(from $y = x^2$ — which way does the vertex go?)*

   ::: answer
   Move: $x \to x + 2$ added to the input → shift **left** 2 (opposite day). Vertex
   $(0,0) \to (-2, 0)$.
   :::

8. $y = -(x - 1)^2 + 4$   *(from $y = x^2$, three moves — do them in blueprint order)*

   ::: answer
   Blueprint order, innermost first: (1) $x \to x - 1$ — shift **right** 1, vertex
   $(0,0) \to (1,0)$; (2) leading $-$ — flip upside down, valley becomes a hill, vertex
   stays $(1,0)$; (3) $+4$ — shift **up** 4, vertex $(1,0) \to (1,4)$. Result: a
   downward-opening hill peaking at $(1, 4)$.
   :::

9. $y = 2^x + 3$   *(from $y = 2^x$ — where is the asymptote now? Draw it dashed.)*

   ::: answer
   Move: add 3 to the output → shift **up** 3. The asymptote moves with it, from $y = 0$
   to $y = 3$.
   :::

10. $y = \dfrac{1}{x - 2}$   *(from $y = \frac{1}{x}$ — your worksheet 1.2 deep-end, now official)*

    ::: answer
    Move: $x \to x - 2$ added to the input → shift **right** 2 (opposite day). Vertical
    asymptote moves from $x = 0$ to $x = 2$; horizontal asymptote stays at $y = 0$.
    :::

---

## Part C — Spot the error

Each claim has exactly one mistake. Circle and correct it.

11. "$y = (x + 5)^2$ is $y = x^2$ shifted **right** 5, because the 5 is positive."

    ::: answer
    Wrong — it's shifted **left** 5. The $+5$ sits inside the brackets, added to the
    *input*, and input moves run backwards: opposite day.
    :::

12. "$y = 2^x + 3$ still has its asymptote at $y = 0$, because shifts don't affect asymptotes."

    ::: answer
    Wrong — the asymptote moves to $y = 3$. The $+3$ is added to the *output*, so it
    lifts the whole graph, floor included. Vertical shifts always drag the horizontal
    asymptote with them.
    :::

13. "$y = 2f(x) + 1$ and $y = 2(f(x) + 1)$ are the same graph, because both stretch by 2 and
    shift by 1."

    ::: answer
    Wrong — different graphs. $y = 2f(x) + 1$ stretches by 2, *then* shifts up 1.
    $y = 2(f(x) + 1) = 2f(x) + 2$ shifts up 1, *then* stretches by 2 — landing as $+2$
    overall, not $+1$. Brackets set the order, and order changes the result.
    :::

---

## Part D — Deep end

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

14. Normalisation, the ML ritual: $z = \dfrac{x - 5}{2}$. Describe it as two graph-moves applied
    to data. If the original data was centred at 5 with spread 2, where is $z$ centred and what's
    its spread?

    ::: rephrase
    Read the formula as two graph-moves done to *every* data point. It's the lesson's
    normalisation ritual ($z = \frac{x-\mu}{\sigma}$: shift, then squash) with real numbers —
    here $\mu = 5$, $\sigma = 2$. "Centred at 5, spread 2" is just where the pile of data sits
    and how wide it is; the two moves relocate and resize that whole pile, exactly like the
    heights histogram in the lesson.
    :::

    ::: hint
    Read the formula in operation order: what happens to $x$ first (the top of the fraction),
    then what happens to that (the divide)? Name each as one of the four graph-moves.
    :::

    ::: hint
    The $-5$ on top is "add $-5$ to the input" — a shift. Ask: where does a pile centred at 5
    land after you subtract 5 from every value?
    :::

    ::: steps
    1. **Subtract 5** (shift by $-5$) — centres the pile at 0. $x - 5$
    2. **Divide by 2** (squash by $\div 2$) — halves the spread. $z = \dfrac{x-5}{2}$
    3. **Read off the result.** $z$ is centred at $0$ with spread $1$.
    :::

15. The lesson's deep-end: show with an exponent rule (Module 0.5) that $e^{x+1} = e \cdot e^x$.
    So "shift left 1" and "stretch vertically by $e$" are the *same move* for this machine.
    Try the same trick on $y = x^2$: is $(x+1)^2$ a vertical stretch of $x^2$? Why not?

    ::: rephrase
    Two tasks in one. First: use a single Module 0.5 exponent rule to rewrite $e^{x+1}$ as
    *a number* $\times\, e^x$ — and "a number times the output" is a vertical stretch, so the
    one curve is both "shift left 1" and "stretch". Second: try the same trick on $(x+1)^2$ —
    expand it and check whether it comes out as just $a \cdot x^2$. This is the lesson's
    hold-in-your-head deep-end question, now on paper.
    :::

    ::: hint
    For $e^{x+1}$: which exponent rule splits a *sum in the exponent* into a *product*? It's
    $a^{m+n} = a^m \cdot a^n$ — apply it with $m = x$, $n = 1$.
    :::

    ::: hint
    For $(x+1)^2$: don't eyeball it, expand it fully. A genuine vertical stretch of $x^2$ has
    to look like $a \cdot x^2$ and nothing else. Does your expansion?
    :::

    ::: steps
    1. **Split the exponent** ($a^{m+n} = a^m a^n$). $e^{x+1} = e^x \cdot e^1 = e \cdot e^x$
    2. **Name it.** the constant $e$ multiplying $e^x$ *is* a vertical stretch $\times e$ — so shift-left-1 and stretch-$\times e$ are the same move for this machine.
    3. **Test $x^2$: expand.** $(x+1)^2 = x^2 + 2x + 1$
    4. **Compare to $a \cdot x^2$.** the leftover $2x + 1$ can't be absorbed into any constant $a$, so $(x+1)^2$ is **not** a vertical stretch of $x^2$. The trick works only because $e^{x+c}$ factors into $e^c \cdot e^x$; polynomials don't factor that way under a shift.
    :::

16. Write the blueprint for: "$\frac{1}{x}$, flipped upside down, then shifted up 1."
    Then sketch it. Bonus: what are its two asymptotes?

    ::: rephrase
    "Write the blueprint" means: build the equation by stacking the named moves onto the zoo
    animal $y = \frac1x$, in the stated order (flip first, then up 1) — exactly the "watch one
    build" from the lesson. "Flipped upside down" is a flip of the *output*; "shifted up 1"
    adds 1 to the *output*. Then track where the two asymptotes of $\frac1x$ (from worksheet
    1.2) end up.
    :::

    ::: hint
    Start from $y = \frac1x$. "Flipped upside down" (over the $x$-axis) is which of the four
    moves — and does its minus sign go inside or outside the fraction?
    :::

    ::: hint
    Now apply "up 1": add 1 to the whole output. For the asymptotes, remember output-moves
    leave the vertical asymptote ($x = 0$) alone; the horizontal one rides along with the flip
    and the $+1$.
    :::

    ::: steps
    1. **Flip the output** ($-$ outside). $y = -\dfrac{1}{x}$
    2. **Add 1 to the output** (shift up 1). $y = -\dfrac{1}{x} + 1$
    3. **Locate the asymptotes.** vertical $x = 0$ (untouched by output moves); horizontal starts at $y = 0$, the flip keeps it at $0$, then $+1$ lifts it to $y = 1$.
    :::

17. A machine's graph is a valley with vertex at $(-3, 7)$, opening downward… wait, valleys don't
    open downward. Fix the sentence, then write a blueprint whose graph is a *hill* with peak
    at $(-3, 7)$.

    ::: rephrase
    Two small tasks. First a vocabulary fix: the sentence calls something a "valley" that
    "opens downward" — one of those two words is wrong, because valley and hill each have a
    fixed opening direction. Second, build a blueprint (from $y = x^2$) whose graph is a hill
    peaking at $(-3, 7)$ — the same three-move build as problem 8 and the lesson's "watch one
    build".
    :::

    ::: hint
    A parabola that opens **downward** is a hill (peak on top); one that opens **upward** is a
    valley. Which word in the sentence contradicts the other?
    :::

    ::: hint
    For the hill at $(-3, 7)$: to slide the vertex to $x = -3$ you need $x \to x + 3$ (opposite
    day, inside the brackets); the leading $-$ makes it open downward; the $+7$ lifts the peak.
    :::

    ::: steps
    1. **Fix the vocabulary.** a valley opens **upward** — a downward-opening parabola is a hill, so either call it a hill or say it opens upward.
    2. **Shift the vertex to $x = -3$** ($x \to x + 3$, opposite day). $y = (x + 3)^2$
    3. **Flip to a hill** ($-$ outside). $y = -(x + 3)^2$
    4. **Lift the peak to 7** ($+7$). $y = -(x + 3)^2 + 7$
    :::

---

## Part E — Python check (at the computer, after scanning)

18. Verify Part B by plotting each transformed machine **on the same axes as its zoo original**:

```python
import sys; sys.path.append("../../tools")
import numpy as np
import matplotlib.pyplot as plt
from plots import plot_functions

plot_functions({
    "y = x^2":          lambda x: x**2,
    "y = -(x-1)^2 + 4": lambda x: -(x - 1)**2 + 4,
}, xlim=(-6, 6), ylim=(-8, 8))
plt.show()
```

Do the rest of Part B the same way. ✓ or a miss-note next to each sketch.

> **Bonus thought:** plot problem 15's pair — `np.e * np.exp(x)` and `np.exp(x + 1)`.
> If the lesson is right, how many curves should you see on the screen?
