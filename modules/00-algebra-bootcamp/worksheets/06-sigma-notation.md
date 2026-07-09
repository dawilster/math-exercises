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
   Deviations from the mean always cancel to zero (proved in problem 13).
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

## Part D — Deep end

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

11. The **MSE loss** — how wrong a model is, averaged over $N$ examples, where $y_i$ is the
    true answer and $\hat{y}_i$ the model's guess:
    $$L = \frac{1}{N}\sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$
    Compute $L$ by hand for $y = (3, 5, 7)$, $\hat{y} = (2, 5, 9)$. Then answer: why square
    the differences instead of just summing them? *(Hint: problem 7.)*

    ::: rephrase
    The scary fraction-with-a-Σ is just "the **average of the squared errors**." It's a Part A
    unroll with a $\frac{1}{N}$ out front (the mean, 0.4): for each example take *true minus guess*,
    square it, add them all, divide by how many. The second question — "why square?" — is
    problem 7 in disguise: remember what happened when you added *raw* deviations there.
    :::

    ::: hint
    Ignore the "why" for now. $\frac{1}{N}\sum$ is just "the mean of" — same as problem 5. The
    mean of *what* list? Build it term by term: for each $i$, compute $(y_i - \hat y_i)^2$.
    :::

    ::: hint
    First move: line up the pairs and subtract, $y_i - \hat y_i$ for $i = 1, 2, 3$, *before* you
    square anything.
    :::

    ::: steps
    1. **Unroll the loop — differences $y_i - \hat y_i$.** $3-2 = 1,\quad 5-5 = 0,\quad 7-9 = -2$
    2. **Square each term.** $1^2 = 1,\quad 0^2 = 0,\quad (-2)^2 = 4$
    3. **Average them ($\tfrac{1}{N}$, here $N=3$).** $L = \frac{1}{3}(1+0+4) = \frac{5}{3} \approx 1.67$
    4. **Why square — it stops errors cancelling.** Like problem 7's surprise, raw differences sum to (near) zero even when guesses are badly wrong; squaring makes every error positive, and punishes big misses harder than small ones.
    :::

12. Little Gauss, age 8, computed $1 + 2 + \dots + 100$ in seconds by pairing the first and
    last numbers. Find his trick, then write the formula for $\displaystyle\sum_{i=1}^{n} i$ and
    check it against your problem 1.

    ::: rephrase
    Two jobs: (1) *find* the shortcut Gauss used, then (2) turn it into a formula for any $n$.
    He didn't add $1+2+\dots+100$ one at a time — he paired numbers from the two *ends*. Try the
    trick on a tiny case first, say $1+2+3+4$: pair the outer two and the inner two, and notice
    what each pair totals.
    :::

    ::: hint
    Pair the first with the last, the second with the second-last, and so on. In $1\dots100$,
    what does $1+100$ make? And $2+99$?
    :::

    ::: hint
    Every pair totals the same $101$, and $100$ numbers make $50$ pairs. To generalise to
    $1\dots n$: each pair totals $n+1$, and there are $n/2$ pairs.
    :::

    ::: steps
    1. **Pair from both ends.** $1+100 = 101,\quad 2+99 = 101,\quad \dots$ — every pair totals $101$.
    2. **Count the pairs.** $100$ numbers $\Rightarrow 50$ pairs $\Rightarrow 50 \times 101 = 5050$.
    3. **Generalise to $1\dots n$** ($n+1$ per pair, $n/2$ pairs). $\displaystyle\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$
    4. **Check against problem 1.** $n=5$: $\frac{5\cdot 6}{2} = 15$. ✓
    :::

13. Using the distributive law (0.3), show step by step that
    $\displaystyle\sum_{i=1}^{n}(x_i - \bar{x}) = 0$ for ANY list — proving your problem-7 surprise.
    *(Moves: split the Σ over the minus, then ask what $\sum \bar{x}$ adds up to when
    $\bar{x}$ is the same constant every pass… and what $n\bar{x}$ equals by the definition
    of the mean.)*

    ::: rephrase
    "Show it's $0$ for ANY list" means: start from the sum and make legal Σ moves until $0$ falls
    out — a proof, like the one you did in 0.5. This is problem 7's surprise made *general*: there
    you saw the deviations cancel for one particular list; here you show it *must* happen for every
    list. The lever is the distributive law (0.3): a Σ splits over a minus.
    :::

    ::: hint
    Split the Σ over the subtraction: $\sum(x_i - \bar x)$ becomes *two* separate sums. Write them.
    :::

    ::: hint
    In $\sum \bar x$ the same constant $\bar x$ is added $n$ times, so it equals $n\bar x$. Now use
    the *definition* of the mean to see what $n\bar x$ is really equal to.
    :::

    ::: steps
    1. **Split the Σ over the minus (distributive law, 0.3).** $\displaystyle\sum_{i=1}^{n}(x_i - \bar x) = \sum_{i=1}^{n} x_i - \sum_{i=1}^{n} \bar x$
    2. **Sum a constant — $\bar x$ added $n$ times.** $\displaystyle\sum_{i=1}^{n} \bar x = n\bar x$
    3. **Use the definition of the mean.** $\bar x = \tfrac{1}{n}\sum_{i=1}^{n} x_i \;\Rightarrow\; n\bar x = \sum_{i=1}^{n} x_i$
    4. **Substitute back — the two sums are identical.** $\sum x_i - \sum x_i = 0 \;\blacksquare$
    :::

14. Write the lesson's neural-net loss $L = -\frac{1}{N}\sum_{i=1}^{N} \log p_i$ as a Python
    loop, on paper. Every symbol in it is now yours: the fraction (0.4), the log (0.5),
    the Σ (0.6). Then answer: the $p_i$ are probabilities the model gives to correct
    answers. Why does the minus sign make $L$ a number worth *minimising*?

    ::: rephrase
    Two jobs. (1) "Write the Σ as a Python loop" is exactly the costume-change from the lesson,
    same as every Part A problem: an accumulator starting at $0$, a `for` that adds one term each
    pass, then the $-\frac{1}{N}$ applied at the end. (2) The "why minus" question: think about the
    *size* of $\log p_i$ when $p_i$ is a probability (between $0$ and $1$) — positive or negative?
    :::

    ::: hint
    For the loop: start `total = 0`, loop `i` over the examples adding `log(p[i])` each pass, and
    handle the $-\frac{1}{N}$ *after* the loop finishes.
    :::

    ::: hint
    For the minus: probabilities satisfy $0 < p_i \le 1$, so (from 0.5) $\log p_i$ is negative. That
    makes the raw sum negative — so what does the leading minus sign do to it?
    :::

    ::: steps
    1. **Unroll the Σ into an accumulating loop (same as Part A).** `total = 0` then `for i in range(N): total = total + log(p[i])`
    2. **Apply the $-\tfrac{1}{N}$ after the loop.** `L = -total / N`
    3. **Sign of each term.** $0 < p_i \le 1 \Rightarrow \log p_i \le 0$, so the raw sum is negative; the leading minus flips $L$ to $\ge 0$.
    4. **Why it's worth minimising.** confident + correct $\Rightarrow p_i \to 1 \Rightarrow \log p_i \to 0$ (tiny loss); wrong or unsure $\Rightarrow p_i \to 0 \Rightarrow \log p_i \to -\infty$ (huge loss). Minimising $L$ forces the model toward high probability on the correct answers.
    :::

---

## Part E — Python check (at the computer, after the pen work)

15. Referee Parts A and B:

```python
x = [2, 5, 5, 8]

print(sum(range(1, 6)))                  # problem 1 — range(1, 6) is 1,2,3,4,5 (stops BEFORE 6)
print(sum(2 * i for i in range(1, 5)))   # problem 2
print(sum(x), sum(x) / len(x))           # problem 5
xbar = sum(x) / len(x)
print(sum(xi - xbar for xi in x))        # problem 7 — surprised on paper, confirmed here?
```

16. Check the double Σ (problem 10) as nested loops:

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
