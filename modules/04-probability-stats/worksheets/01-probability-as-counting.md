# Worksheet 4.1 — Probability as Counting

*Pen and paper. For each answer, show the count: favourable ÷ total. Fractions are fine —
don't reach for a calculator. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: straight counting

1. One fair die. $P(\text{rolling a 5}) = ?$

2. One fair die. $P(\text{rolling an even number}) = ?$

3. A standard 52-card deck, one card drawn. $P(\text{it's a heart}) = ?$

4. A bag holds 3 red and 7 blue marbles. $P(\text{red}) = ?$

---

## Part B — Core: count at the right level

5. Two fair coins are flipped. List all equally likely outcomes, then find
   $P(\text{exactly one head})$.

6. Two fair dice. $P(\text{sum} = 11) = ?$ *(List the pairs.)*

7. Two fair dice. $P(\text{both dice show the same number}) = ?$

8. Two fair dice. Which is more likely: sum = 9 or sum = 4? Show the counts that decide it.

9. A die is rolled 3,000 times. Roughly how many 6s do you expect? Will it be exactly that?
   One sentence on the difference between those two answers.

---

## Part C — Spot the error

Each claim contains one broken idea. Name it.

10. "Two coins can land: two heads, two tails, or one of each. Three outcomes, so
    $P(\text{one of each}) = \frac{1}{3}$."

11. "This coin has landed heads 6 times straight. Tails is due — it's now more likely than heads."

12. "I simulated 100 rolls and got 21 sixes, so $P(6) = 0.21$, not $\frac{1}{6}$. The formula
    is wrong."

---

## Part D — Deep end

*Not covered yet. Attempt anyway — reason from counting.*

13. Two fair dice. $P(\text{at least one six}) = ?$
    *(Hint: sometimes it's easier to count the outcomes where it DOESN'T happen.)*

14. A fair coin is flipped 3 times. $P(\text{at least one head}) = ?$ Use the same trick.

15. Three fair coins. Which is more likely: all three match, or they don't all match?
    By how much?

16. An LLM assigns the next token: "the" 0.40, "a" 0.25, "his" 0.15, everything else shares 0.20.
    If it samples 1,000 completions of this sentence, roughly how many start with "the" or "a"?
    What rule did you just use about combining probabilities of *different* outcomes?

---

## Part E — Python check (at the computer, after the pen work)

17. Verify problem 6 by simulation:

```python
import numpy as np
rng = np.random.default_rng(42)
rolls = rng.integers(1, 7, size=(100_000, 2))
sums = rolls[:, 0] + rolls[:, 1]
print((sums == 11).mean())        # close to your fraction from problem 6?
```

18. Change the line to check problem 13 (`at least one six`).
    *(Hint: `(rolls == 6).any(axis=1)` asks "any six in each pair?")* Write ✓ next to each
    problem the simulation confirmed.
