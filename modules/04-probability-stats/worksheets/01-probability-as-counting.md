# Worksheet 4.1 — Probability as Counting

*Pen and paper. For each answer, show the count: favourable ÷ total. Fractions are fine —
don't reach for a calculator. Photograph into `scans/inbox/` when done.*

---

## Part A — Warm-up: straight counting

1. One fair die. $P(\text{rolling a 5}) = ?$

   ::: answer
   $\frac{1}{6}$ — move: favourable outcomes / total outcomes = $1/6$.
   :::

2. One fair die. $P(\text{rolling an even number}) = ?$

   ::: answer
   $\frac{3}{6} = \frac{1}{2}$ — move: count favourable outcomes $\{2,4,6\}$, divide by total $6$.
   :::

3. A standard 52-card deck, one card drawn. $P(\text{it's a heart}) = ?$

   ::: answer
   $\frac{13}{52} = \frac{1}{4}$ — move: favourable (13 hearts) / total (52 cards).
   :::

4. A bag holds 3 red and 7 blue marbles. $P(\text{red}) = ?$

   ::: answer
   $\frac{3}{10}$ — move: favourable (3 red) / total (10 marbles).
   :::

---

## Part B — Core: count at the right level

5. Two fair coins are flipped. List all equally likely outcomes, then find
   $P(\text{exactly one head})$.

   ::: answer
   Outcomes: $\{HH, HT, TH, TT\}$ (4, equally likely). Exactly one head: $HT, TH$ → $\frac{2}{4} = \frac{1}{2}$.
   Move: count at the level of *ordered* outcomes, not "0, 1, or 2 heads" as if those were equally likely.
   :::

6. Two fair dice. $P(\text{sum} = 11) = ?$ *(List the pairs.)*

   ::: answer
   Pairs: $(5,6), (6,5)$ → 2 favourable out of 36 total. $P = \frac{2}{36} = \frac{1}{18}$.
   Move: count ordered pairs out of all 36, not just distinct sums.
   :::

7. Two fair dice. $P(\text{both dice show the same number}) = ?$

   ::: answer
   Pairs: $(1,1), (2,2), \dots, (6,6)$ → 6 favourable out of 36. $P = \frac{6}{36} = \frac{1}{6}$.
   Move: favourable outcomes / total outcomes.
   :::

8. Two fair dice. Which is more likely: sum = 9 or sum = 4? Show the counts that decide it.

   ::: answer
   Sum = 9: $(3,6),(4,5),(5,4),(6,3)$ → 4 outcomes. Sum = 4: $(1,3),(2,2),(3,1)$ → 3 outcomes.
   Sum = 9 is more likely ($\frac{4}{36}$ vs $\frac{3}{36}$). Move: count the pairs for each sum, compare counts directly.
   :::

9. A die is rolled 3,000 times. Roughly how many 6s do you expect? Will it be exactly that?
   One sentence on the difference between those two answers.

   ::: answer
   Expect $3000 \times \frac{1}{6} = 500$. Won't be exactly 500 most of the time — the *expected value*
   is a long-run average, individual runs bounce around it by chance (that scatter shrinks
   proportionally as the number of rolls grows).
   :::

---

## Part C — Spot the error

Each claim contains one broken idea. Name it.

10. "Two coins can land: two heads, two tails, or one of each. Three outcomes, so
    $P(\text{one of each}) = \frac{1}{3}$."

    ::: answer
    Broken idea: those three outcomes aren't equally likely. "One of each" is really two
    outcomes ($HT$ and $TH$) bundled together. Counting at the coin-by-coin level gives 4 equally
    likely outcomes, so $P(\text{one of each}) = \frac{2}{4} = \frac{1}{2}$, not $\frac{1}{3}$.
    :::

11. "This coin has landed heads 6 times straight. Tails is due — it's now more likely than heads."

    ::: answer
    Broken idea: the gambler's fallacy. Coin flips are independent — the coin has no memory of
    past results. $P(\text{tails})$ on the next flip is still $\frac{1}{2}$.
    :::

12. "I simulated 100 rolls and got 21 sixes, so $P(6) = 0.21$, not $\frac{1}{6}$. The formula
    is wrong."

    ::: answer
    Broken idea: confusing a small-sample empirical frequency with the true probability. $100$
    rolls is too few for the frequency to settle down; $21$ vs the expected $\approx 16.7$ is
    normal random scatter. The true $P(6) = \frac{1}{6}$ still holds — frequency converges to it
    as the number of rolls grows (law of large numbers), it doesn't equal it exactly at $n=100$.
    :::

---

## Part D — Deep end

*Beyond what was taught — you're **not** expected to see these cold. Each one gives you a ladder: tap **🔍 In plain words** if the question won't land, then **💡 Hints** one at a time (each says the least next thing), and only **✅ Worked solution** once you've wrestled. Take the fewest rungs you can — the struggle before each tap is where the learning happens. Always name your moves, even when guessing.*

13. Two fair dice. $P(\text{at least one six}) = ?$
    *(Hint: sometimes it's easier to count the outcomes where it DOESN'T happen.)*

    ::: rephrase
    "At least one six" is a wide net — it catches one six, or two. Counting all those cases
    directly is fiddly. So flip the question to the *one* thing you don't want: **no six
    anywhere**. That's the hint printed under the problem — count when it DOESN'T happen. Same
    "count at the easy level" move as Part B, just applied to the opposite event.
    :::

    ::: hint
    Reach for the **complement**: instead of adding up every "at least one" case, count the
    single opposite event (no six at all) and subtract from 1.
    :::

    ::: hint
    First move: find $P(\text{no six on one die})$, then both dice have to miss at once.
    :::

    ::: steps
    1. **Flip to the complement.** $P(\text{at least one six}) = 1 - P(\text{no six on either die})$
    2. **Count "no six" on each die, both must miss (multiply).** $P(\text{no six}) = \frac{5}{6} \times \frac{5}{6} = \frac{25}{36}$
    3. **Subtract from 1.** $P(\text{at least one six}) = 1 - \frac{25}{36} = \frac{11}{36}$
    :::

14. A fair coin is flipped 3 times. $P(\text{at least one head}) = ?$ Use the same trick.

    ::: rephrase
    Same shape as problem 13 — "at least one" again, so reach for the same trick. The opposite
    of "at least one head" is "**zero heads**", i.e. all three land tails. There's exactly one
    way for that to happen, so it's the easy side to count.
    :::

    ::: hint
    Use the **complement** again: what's the single opposite of "at least one head"?
    :::

    ::: hint
    First move: that opposite is "all three tails" — compute $P(\text{all tails}) = \left(\frac{1}{2}\right)^3$.
    :::

    ::: steps
    1. **Flip to the complement.** $P(\text{at least one head}) = 1 - P(\text{no heads})$
    2. **"No heads" = all three tails (multiply the three $\frac12$'s).** $P(\text{no heads}) = \left(\frac{1}{2}\right)^3 = \frac{1}{8}$
    3. **Subtract from 1.** $P(\text{at least one head}) = 1 - \frac{1}{8} = \frac{7}{8}$
    :::

15. Three fair coins. Which is more likely: all three match, or they don't all match?
    By how much?

    ::: rephrase
    "All three match" means $HHH$ or $TTT$ — only 2 of the 8 possible outcomes. That's the small,
    easy side to count (just like the complement trick you just used twice). "Don't all match"
    is everything else. So count the easy side, get the other by subtracting from 1, then compare
    the two.
    :::

    ::: hint
    Which side is easier to count directly — "all match" or "don't all match"? List the 8 equally
    likely outcomes and pick off the matching ones.
    :::

    ::: hint
    $P(\text{all match}) = P(HHH) + P(TTT)$. Once you have that, the other side is its **complement**,
    $1 - P(\text{all match})$.
    :::

    ::: steps
    1. **Count the easy side: all match is $HHH$ or $TTT$.** $P(\text{all match}) = \frac{1}{8} + \frac{1}{8} = \frac{2}{8} = \frac{1}{4}$
    2. **Complement gives the other side.** $P(\text{don't all match}) = 1 - \frac{1}{4} = \frac{3}{4}$
    3. **Compare — subtract for the gap.** $\frac{3}{4} - \frac{1}{4} = \frac{1}{2}$, so "don't all match" is three times as likely
    :::

16. An LLM assigns the next token: "the" 0.40, "a" 0.25, "his" 0.15, everything else shares 0.20.
    If it samples 1,000 completions of this sentence, roughly how many start with "the" or "a"?
    What rule did you just use about combining probabilities of *different* outcomes?

    ::: rephrase
    Two moves stacked. First: the first token is "the" or "a" — two *different* outcomes that
    can't both happen at once, so you need $P(\text{"the" or "a"})$. Second: turning that into a
    count over 1,000 samples is exactly problem 9 (die rolled 3,000 times $\to$ 500 sixes) —
    expected count $=$ probability $\times$ number of tries.
    :::

    ::: hint
    The first token is either "the" or "a" — never both at once. When two outcomes can't co-occur,
    how do you get the probability of "one **or** the other"?
    :::

    ::: hint
    Add the two probabilities to get $P(\text{"the" or "a"})$, then scale it to 1,000 completions
    the same way as problem 9 ($\times$ number of tries).
    :::

    ::: steps
    1. **Add the two probabilities (mutually exclusive $\to$ addition rule).** $P(\text{"the" or "a"}) = 0.40 + 0.25 = 0.65$
    2. **Scale to 1,000 completions (expected count, like problem 9).** $0.65 \times 1{,}000 = 650$
    :::

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
