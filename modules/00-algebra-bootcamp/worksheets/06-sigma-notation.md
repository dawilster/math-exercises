# Worksheet 0.6 — Σ Notation

*Pen and paper. For every problem, show your working — when you unroll a Σ, write the
unrolled sum before computing it, and **name the move** ("unroll the loop", "constant out
of the Σ", …). Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: unroll the loop

Unroll each Σ into an explicit sum, then compute it.

1. $\displaystyle\sum_{i=1}^{5} i$

   ::: answer
   $1+2+3+4+5 = 15$ — move: unroll the Σ, $i$ takes each integer value from $1$ to $5$ in turn.
   :::

2. $\displaystyle\sum_{i=1}^{4} 2i$

   ::: answer
   $2+4+6+8 = 20$ — move: unroll the loop, $i = 1,2,3,4$, each doubled before adding.
   :::

3. $\displaystyle\sum_{i=1}^{3} i^2$

   ::: answer
   $1 + 4 + 9 = 14$ — move: unroll, square each $i$ before adding.
   :::

4. $\displaystyle\sum_{i=1}^{4} 3$   *(no $i$ in the body — what does each loop pass add?)*

   ::: answer
   $3+3+3+3 = 12$ — move: with no $i$ in the body, each of the 4 loop passes just adds the constant $3$.
   :::

---

## Part B — Core: subscripts, means and both directions

Use the list $x = (2, 5, 5, 8)$, so $x_1 = 2,\; x_2 = 5,\; x_3 = 5,\; x_4 = 8$.

5. Compute $\displaystyle\sum_{i=1}^{4} x_i$ and then the mean $\bar{x} = \frac{1}{4}\sum_{i=1}^{4} x_i$.

   ::: answer
   $\sum_{i=1}^4 x_i = 2+5+5+8 = 20$; mean $\bar x = 20/4 = 5$ — move: unroll and add, then divide by the count.
   :::

6. Compute $\displaystyle\sum_{i=2}^{4} x_i$   *(mind the starting line)*

   ::: answer
   $x_2+x_3+x_4 = 5+5+8 = 18$ — move: the lower index tells you where the loop starts; $x_1$ is left out.
   :::

7. Compute $\displaystyle\sum_{i=1}^{4} (x_i - \bar{x})$ using your mean from problem 5.
   *(The answer should surprise you — and it's not a coincidence. Any hunch why?)*

   ::: answer
   $(2-5)+(5-5)+(5-5)+(8-5) = -3+0+0+3 = 0$ — move: unroll each deviation, then add.
   Deviations from the mean always cancel to zero (proved in problem 16).
   :::

8. Write in Σ notation: "the sum of the squares of the first ten counting numbers."

   ::: answer
   $\displaystyle\sum_{i=1}^{10} i^2$ — move: "first ten counting numbers" fixes the bounds
   $i=1$ to $10$; "squares" goes in the body as $i^2$.
   :::

9. Write in Σ notation: $\;x_1 y_1 + x_2 y_2 + x_3 y_3 + x_4 y_4$
   *(Remember this one — in Module 2 it turns out to run all of modern AI.)*

   ::: answer
   $\displaystyle\sum_{i=1}^{4} x_i y_i$ — move: spot the repeated pattern $x_i y_i$ and read
   the bounds off how many terms are written out.
   :::

10. For the grid $w = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, where $w_{ij}$ means
    row $i$, column $j$: write out and compute $\displaystyle\sum_{i=1}^{2}\sum_{j=1}^{2} w_{ij}$,
    showing the four terms in loop order.

    ::: answer
    $w_{11}+w_{12}+w_{21}+w_{22} = 1+2+3+4 = 10$ — move: the outer loop $i$ is slow (row), the
    inner loop $j$ is fast (column): for each $i$, run through every $j$ before moving to the next $i$.
    :::

---

## Part C — Spot the illegal move

Circle the broken line and name the rule it broke.

11. Claimed evaluation, with $x = (1, 2, 3)$:
    - line 1: $\sum_{i=1}^{3} x_i^2$
    - line 2: $(1 + 2 + 3)^2 = 36$   *(added, then squared)*

    ::: answer
    Line 2 is broken — a power doesn't distribute over a sum: $\left(\sum x_i\right)^2 \neq \sum x_i^2$
    in general. Correct: $1+4+9 = 14$, not $36$.
    :::

12. Claimed Python translation of $\sum_{i=1}^{10} i$:
    - line 1: `total = 0`
    - line 2: `for i in range(1, 10):`
    - line 3: `    total = total + i`
    *(Run it in your head: what does it actually compute?)*

    ::: answer
    It actually computes $\sum_{i=1}^{9} i = 45$, not $\sum_{i=1}^{10} i = 55$ — Python's
    `range(1, 10)` stops **before** 10, so $i=10$ never runs. Off-by-one; should be `range(1, 11)`.
    :::

13. Claimed simplification:
    - line 1: $\sum_{i=1}^{n} 2 x_i = 2 \sum_{i=1}^{n} x_i$   *(pulled the constant out)*
    - line 2: $\sum_{i=1}^{n} (x_i + 3) = 3 + \sum_{i=1}^{n} x_i$   *(pulled the constant out)*
    *(One of these two lines is legal, one is broken. Which, and why? Unroll a tiny case
    with $n = 2$ to find out.)*

    ::: answer
    Line 1 is legal — a multiplicative constant factors out of every term the same way (each
    term is literally $2$ times $x_i$). Line 2 is broken — the $+3$ is added **once per term**,
    $n$ times total, not once: with $n=2$, $(x_1+3)+(x_2+3) = x_1+x_2+6$, not $x_1+x_2+3$.
    Correct: $\sum_{i=1}^{n}(x_i+3) = n\cdot 3 + \sum_{i=1}^{n} x_i$.
    :::

---

## Part D — Deep end

*Beyond what was taught. Struggle is the workout — unroll tiny cases whenever stuck.*

14. The **MSE loss** — how wrong a model is, averaged over $N$ examples, where $y_i$ is the
    true answer and $\hat{y}_i$ the model's guess:
    $$L = \frac{1}{N}\sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$
    Compute $L$ by hand for $y = (3, 5, 7)$, $\hat{y} = (2, 5, 9)$. Then answer: why square
    the differences instead of just summing them? *(Hint: problem 7.)*

    ::: answer
    Differences: $1, 0, -2$; squared: $1, 0, 4$; $L = \frac{1}{3}(1+0+4) = \frac{5}{3} \approx 1.67$.
    Squaring (instead of summing raw differences) stops positive and negative errors from
    cancelling — like problem 7's surprise, raw deviations sum to (near) zero even when
    individual guesses are badly wrong. Squaring also punishes big misses harder than small ones.
    :::

15. Little Gauss, age 8, computed $1 + 2 + \dots + 100$ in seconds by pairing the first and
    last numbers. Find his trick, then write the formula for $\displaystyle\sum_{i=1}^{n} i$ and
    check it against your problem 1.

    ::: answer
    Pair first+last: $1+100 = 101$, $2+99 = 101$, … 50 pairs of $101$ = $5050$. Formula:
    $\displaystyle\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$ — move: the pairing trick, generalised.
    Check: $n=5$ gives $\frac{5\cdot 6}{2} = 15$, matching problem 1.
    :::

16. Using the distributive law (0.3), show step by step that
    $\displaystyle\sum_{i=1}^{n}(x_i - \bar{x}) = 0$ for ANY list — proving your problem-7 surprise.
    *(Moves: split the Σ over the minus, then ask what $\sum \bar{x}$ adds up to when
    $\bar{x}$ is the same constant every pass… and what $n\bar{x}$ equals by the definition
    of the mean.)*

    ::: answer
    $\sum_{i=1}^{n}(x_i - \bar x) = \sum_{i=1}^{n} x_i - \sum_{i=1}^{n} \bar x$ — move: split the
    Σ over the minus. Since $\bar x$ is the same constant every pass, $\sum_{i=1}^{n} \bar x = n\bar x$.
    By definition $\bar x = \frac{1}{n}\sum_{i=1}^{n} x_i$, so $n\bar x = \sum_{i=1}^{n} x_i$.
    Substituting: $\sum x_i - \sum x_i = 0$.
    :::

17. Write the lesson's neural-net loss $L = -\frac{1}{N}\sum_{i=1}^{N} \log p_i$ as a Python
    loop, on paper. Every symbol in it is now yours: the fraction (0.4), the log (0.5),
    the Σ (0.6). Then answer: the $p_i$ are probabilities the model gives to correct
    answers. Why does the minus sign make $L$ a number worth *minimising*?

    ::: answer
    Loop: `total = 0`; `for i in range(N): total = total + log(p[i])`; then `L = -total / N`.
    Move: unroll the Σ into an accumulating loop, same as every problem in Part A. Why the minus:
    probabilities satisfy $0 < p_i \le 1$, so $\log p_i \le 0$ and the raw sum is negative —
    flipping the sign makes $L \ge 0$. A confident, correct model pushes $p_i \to 1$, so
    $\log p_i \to 0$ (tiny loss); a wrong or unsure model pushes $p_i \to 0$, so $\log p_i \to -\infty$
    (huge loss). Minimising $L$ therefore forces the model toward high probability on the correct answers.
    :::

---

## Part E — Python check (at the computer, after the pen work)

18. Referee Parts A and B:

```python
x = [2, 5, 5, 8]

print(sum(range(1, 6)))                  # problem 1 — range(1, 6) is 1,2,3,4,5 (stops BEFORE 6)
print(sum(2 * i for i in range(1, 5)))   # problem 2
print(sum(x), sum(x) / len(x))           # problem 5
xbar = sum(x) / len(x)
print(sum(xi - xbar for xi in x))        # problem 7 — surprised on paper, confirmed here?
```

19. Check the double Σ (problem 10) as nested loops:

```python
w = [[1, 2],
     [3, 4]]         # a list of lists: w[i][j] is row i, column j (counting from 0!)
total = 0
for i in range(2):
    for j in range(2):
        total = total + w[i][j]
print(total)
```

Write ✓ next to each problem Python confirms.

> **Bonus thought:** Python's `sum(x)/len(x)` and numpy's `np.mean(x)` — one of them is a
> Σ you can now read, the other is the same Σ hidden inside a library. All of numpy is
> like this: loops you can already read, pre-written and fast.
