# Worksheet 0.6 — Σ Notation

*Pen and paper. For every problem, show your working — when you unroll a Σ, write the
unrolled sum before computing it, and **name the move** ("unroll the loop", "constant out
of the Σ", …). Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: unroll the loop

Unroll each Σ into an explicit sum, then compute it.

1. $\displaystyle\sum_{i=1}^{5} i$

2. $\displaystyle\sum_{i=1}^{4} 2i$

3. $\displaystyle\sum_{i=1}^{3} i^2$

4. $\displaystyle\sum_{i=1}^{4} 3$   *(no $i$ in the body — what does each loop pass add?)*

---

## Part B — Core: subscripts, means and both directions

Use the list $x = (2, 5, 5, 8)$, so $x_1 = 2,\; x_2 = 5,\; x_3 = 5,\; x_4 = 8$.

5. Compute $\displaystyle\sum_{i=1}^{4} x_i$ and then the mean $\bar{x} = \frac{1}{4}\sum_{i=1}^{4} x_i$.

6. Compute $\displaystyle\sum_{i=2}^{4} x_i$   *(mind the starting line)*

7. Compute $\displaystyle\sum_{i=1}^{4} (x_i - \bar{x})$ using your mean from problem 5.
   *(The answer should surprise you — and it's not a coincidence. Any hunch why?)*

8. Write in Σ notation: "the sum of the squares of the first ten counting numbers."

9. Write in Σ notation: $\;x_1 y_1 + x_2 y_2 + x_3 y_3 + x_4 y_4$
   *(Remember this one — in Module 2 it turns out to run all of modern AI.)*

10. For the grid $w = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, where $w_{ij}$ means
    row $i$, column $j$: write out and compute $\displaystyle\sum_{i=1}^{2}\sum_{j=1}^{2} w_{ij}$,
    showing the four terms in loop order.

---

## Part C — Spot the illegal move

Circle the broken line and name the rule it broke.

11. Claimed evaluation, with $x = (1, 2, 3)$:
    - line 1: $\sum_{i=1}^{3} x_i^2$
    - line 2: $(1 + 2 + 3)^2 = 36$   *(added, then squared)*

12. Claimed Python translation of $\sum_{i=1}^{10} i$:
    - line 1: `total = 0`
    - line 2: `for i in range(1, 10):`
    - line 3: `    total = total + i`
    *(Run it in your head: what does it actually compute?)*

13. Claimed simplification:
    - line 1: $\sum_{i=1}^{n} 2 x_i = 2 \sum_{i=1}^{n} x_i$   *(pulled the constant out)*
    - line 2: $\sum_{i=1}^{n} (x_i + 3) = 3 + \sum_{i=1}^{n} x_i$   *(pulled the constant out)*
    *(One of these two lines is legal, one is broken. Which, and why? Unroll a tiny case
    with $n = 2$ to find out.)*

---

## Part D — Deep end

*Beyond what was taught. Struggle is the workout — unroll tiny cases whenever stuck.*

14. The **MSE loss** — how wrong a model is, averaged over $N$ examples, where $y_i$ is the
    true answer and $\hat{y}_i$ the model's guess:
    $$L = \frac{1}{N}\sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$
    Compute $L$ by hand for $y = (3, 5, 7)$, $\hat{y} = (2, 5, 9)$. Then answer: why square
    the differences instead of just summing them? *(Hint: problem 7.)*

15. Little Gauss, age 8, computed $1 + 2 + \dots + 100$ in seconds by pairing the first and
    last numbers. Find his trick, then write the formula for $\displaystyle\sum_{i=1}^{n} i$ and
    check it against your problem 1.

16. Using the distributive law (0.3), show step by step that
    $\displaystyle\sum_{i=1}^{n}(x_i - \bar{x}) = 0$ for ANY list — proving your problem-7 surprise.
    *(Moves: split the Σ over the minus, then ask what $\sum \bar{x}$ adds up to when
    $\bar{x}$ is the same constant every pass… and what $n\bar{x}$ equals by the definition
    of the mean.)*

17. Write the lesson's neural-net loss $L = -\frac{1}{N}\sum_{i=1}^{N} \log p_i$ as a Python
    loop, on paper. Every symbol in it is now yours: the fraction (0.4), the log (0.5),
    the Σ (0.6). Then answer: the $p_i$ are probabilities the model gives to correct
    answers. Why does the minus sign make $L$ a number worth *minimising*?

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
