# Worksheet 0.4 — Fractions, Ratios & Percentages

*Pen and paper. For every problem, write the **move you're making** next to each step, like
"× by 3/3 to match denominators" or "÷ by total to normalise". The moves are the point,
not the answers. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: costume changes

1. Write $\frac{3}{4}$ as a decimal and as a percentage.

   ::: answer
   $\frac{3}{4} = 0.75 = 75\%$ — move: divide numerator by denominator for the decimal,
   then $\times 100$ for the percentage.
   :::

2. Write $0.2$ as a fraction (simplest form) and as a percentage.

   ::: answer
   $0.2 = \frac{1}{5} = 20\%$ — move: write over $10$ ($\frac{2}{10}$), cancel the common
   factor $2$ to simplify, and $\times 100$ for the percentage.
   :::

3. Simplify $\frac{18}{24}$ by cancelling common factors. Name the factor(s) you cancel.

   ::: answer
   $\frac{18}{24} = \frac{3}{4}$ — move: cancel the common factor $6$ (top and bottom both $\div 6$).
   :::

4. What is $25\%$ of $80$?

   ::: answer
   $20$ — move: convert percentage to decimal ($25\% = 0.25$), multiply: $0.25 \times 80 = 20$.
   :::

---

## Part B — Core: the moves

Name every move.

5. $\frac{2}{3} \times \frac{9}{10}$   *(simplify before multiplying if you can — less arithmetic)*

   ::: answer
   $\frac{3}{5}$ — move: cancel the common factor $3$ between the $9$ and the $3$ first
   ($\frac{2}{1}\times\frac{3}{10}$), then multiply tops and bottoms: $\frac{6}{10}=\frac{3}{5}$.
   :::

6. $\frac{3}{4} \div \frac{1}{2}$   *(and sanity-check: should the answer be bigger or smaller than $\frac{3}{4}$?)*

   ::: answer
   $\frac{3}{4} \div \frac{1}{2} = \frac{3}{4}\times\frac{2}{1} = \frac{3}{2} = 1.5$ — move: flip
   the second fraction and multiply (keep, flip, change). Bigger than $\frac{3}{4}$, because
   dividing by a number less than $1$ grows the result.
   :::

7. $\frac{1}{4} + \frac{2}{3}$   *(matching pieces first)*

   ::: answer
   $\frac{11}{12}$ — move: common denominator $12$ ($\frac{1}{4}=\frac{3}{12}$,
   $\frac{2}{3}=\frac{8}{12}$), then add tops: $\frac{3+8}{12}=\frac{11}{12}$.
   :::

8. $\frac{5}{6} - \frac{1}{2}$

   ::: answer
   $\frac{1}{3}$ — move: common denominator $6$ ($\frac{1}{2}=\frac{3}{6}$), subtract tops:
   $\frac{5-3}{6}=\frac{2}{6}$, then cancel the common factor $2$ to get $\frac{1}{3}$.
   :::

9. A dataset has 1,200 images. You want an 80/20 train/test split.
   How many images in each part?

   ::: answer
   $960$ train, $240$ test — move: convert each percentage to a decimal, multiply by the total
   ($0.8\times1200=960$, $0.2\times1200=240$).
   :::

10. Normalise the scores $(6, 10, 4)$: divide each by the total, simplify each fraction,
    and confirm the three results sum to exactly 1.

    ::: answer
    $\frac{6}{20}=\frac{3}{10}$, $\frac{10}{20}=\frac{1}{2}$, $\frac{4}{20}=\frac{1}{5}$ — move:
    divide each by the shared total $20$, then cancel common factors. Check with a common
    denominator: $\frac{3}{10}+\frac{5}{10}+\frac{2}{10}=\frac{10}{10}=1$.
    :::

11. Solve for $x$ (balance moves on a fraction equation): $\;\frac{x}{5} = \frac{12}{20}$

    ::: answer
    $x=3$ — move: multiply both sides by $5$ (balance move): $x = 5\times\frac{12}{20} = \frac{60}{20}=3$.
    (Or spot directly that $\frac{12}{20}=\frac{3}{5}$.)
    :::

---

## Part D — Deep end

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

12. A jacket is discounted 30%, then the sale price gets 10% tax added.
    What single percentage of the original do you pay? Does the order
    (discount-then-tax vs tax-then-discount) matter? Test both.

    ::: rephrase
    You never *add or subtract* percentages here — you chain them as **multiply-by-a-factor**
    moves. "30% off" means you keep 70% of the price → $\times 0.7$. "10% tax added" means you
    pay 110% → $\times 1.1$. The question is: what single factor equals doing both? First move —
    turn each percentage change into its multiplier.
    :::

    ::: hint
    A percentage *change* becomes a multiplier: 30% off → $\times 0.7$ (you keep 70%); 10% added
    → $\times 1.1$ (you pay 110%). Write both multipliers before you do anything else.
    :::

    ::: hint
    Apply them one after the other to the original — that's just multiplying the two factors
    together. For the "does order matter?" part, swap which factor goes first and compare.
    :::

    ::: steps
    1. **Turn each change into a multiplier.** 30% off $\to \times 0.7$; 10% tax $\to \times 1.1$
    2. **Chain them (discount then tax).** $0.7 \times 1.1 = 0.77 = 77\%$
    3. **Swap the order (tax then discount).** $1.1 \times 0.7 = 0.77 = 77\%$ — identical, because multiplication commutes.
    :::

13. Normalise the symbols $(a, b, c)$: what does each become, and — using 0.4's common-
    denominator move with pure symbols — prove the three results sum to exactly 1.

    ::: rephrase
    This is problem 10 (normalise $(6,10,4)$) with **letters where the numbers were** — same
    moves exactly. "Normalise" = divide each by the total; here the total is $a+b+c$ (add them
    all). "Prove they sum to 1" = add the three fractions — and because they already share the
    denominator $a+b+c$, you just add the tops.
    :::

    ::: hint
    "Normalise" means divide each thing by the total. What's the total of $a$, $b$, and $c$?
    :::

    ::: hint
    To add the three normalised fractions, notice they already share one denominator — so add
    the tops straight over that common denominator (0.4's "add matching pieces" move).
    :::

    ::: steps
    1. **Sum everything for the total.** total $= a+b+c$
    2. **Divide each by the total (normalise).** $\dfrac{a}{a+b+c},\ \dfrac{b}{a+b+c},\ \dfrac{c}{a+b+c}$
    3. **Add the tops over the shared denominator.** $\dfrac{a+b+c}{a+b+c}=1$
    :::

14. In one class of 20 students, 15 passed. In another class of 80 students, 44 passed.
    What percentage passed **overall**? Why is the answer NOT the average of 75% and 55%?
    *(This trap — averaging averages — corrupts real ML evaluations all the time.)*

    ::: rephrase
    "Percentage passed overall" means **one big fraction**: everyone who passed over everyone
    total — pool the two classes into a single pile first, don't compute two separate rates.
    The trap: averaging $75\%$ and $55\%$ secretly pretends both classes are the same size, but
    the 80-student class dwarfs the 20-student one, so the true rate leans toward its $55\%$.
    :::

    ::: hint
    Don't work with the two percentages. Go back to raw counts: how many students passed in
    total, and how many students are there in total?
    :::

    ::: hint
    Overall rate $=\dfrac{\text{all passers}}{\text{all students}}$; turn that fraction into a
    percentage. Then compare it to the naive $\frac{75\%+55\%}{2}$ to see the size effect.
    :::

    ::: steps
    1. **Pool the passers and the totals.** passed $= 15+44 = 59$; students $= 20+80 = 100$
    2. **One big fraction → percentage.** $\dfrac{59}{100} = 59\%$
    3. **Name why the average fails.** $\dfrac{75\%+55\%}{2}=65\%$ ignores that the 80-student class outweighs the 20-student one — the correct figure is a *size-weighted* average, so it leans toward the bigger class's $55\%$.
    :::

15. Solve for $x$: $\;\frac{2}{x} + \frac{1}{3} = 1$
    *(A 0.2 basement problem wearing 0.4 clothes. Clear the clutter first.)*

    ::: rephrase
    The $x$ is hiding in a **basement** (a denominator) — you can't do balance moves on it while
    it's stuck down there. So the whole first job is to lift every term out of its basement by
    multiplying through by the LCD; the equation then collapses into an ordinary linear one like
    0.2's. That's what "clear the clutter first" is telling you to do.
    :::

    ::: hint
    You can't solve while $x$ sits in a denominator. What do you multiply *every* term by to
    clear all the denominators at once? (Find the LCD of $x$ and $3$.)
    :::

    ::: hint
    Multiply all three terms by $3x$. Each fraction's denominator cancels, leaving a plain linear
    equation — then gather the $x$'s onto one side.
    :::

    ::: steps
    1. **Multiply every term by the LCD $3x$** — clears both basements. $2(3) + x(1) = 1(3x)$
    2. **Simplify each term.** $6 + x = 3x$
    3. **Gather the $x$'s (subtract $x$ from both sides).** $6 = 2x$
    4. **Divide by 2.** $x = 3$ &nbsp; (check: $\frac{2}{3}+\frac{1}{3}=1$ ✓)
    :::

---

## Part E — Python check (at the computer, after the pen work)

16. Python has exact fractions — let them referee Part B:

```python
from fractions import Fraction         # exact fractions, no decimal fuzz

print(Fraction(2, 3) * Fraction(9, 10))    # problem 5 — Fraction(a, b) means a/b
print(Fraction(3, 4) / Fraction(1, 2))     # problem 6
print(Fraction(1, 4) + Fraction(2, 3))     # problem 7
```

17. Check your normalisation (problem 10) the ML way:

```python
scores = [6, 10, 4]
props = [s / sum(scores) for s in scores]   # divide each by the total
print(props, sum(props))                    # must end in 1.0
```

Write ✓ next to each problem Python confirms.

> **Bonus thought:** run `print(0.1 + 0.2)`. Surprised? Now
> `print(Fraction(1, 10) + Fraction(2, 10))`. This is why `Fraction` exists —
> and why ML code (which uses fast decimals anyway) never tests floats with `==`.
