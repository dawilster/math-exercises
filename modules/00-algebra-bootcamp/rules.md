# Module 0 — Algebra Bootcamp: Rules & Moves Reference

*Machine-parsed by `tools/rules_panel.py` into the on-page "Rules so far" panel. Each `##` section
must be headed `slug — Title` where `slug` matches the lesson/worksheet filename stem exactly
(e.g. `01-balance-game`). Bullets are `- **Name**: description`.*

## 01-balance-game — Equations as a Balance

- **Add/subtract both sides**: do the same add or subtract to both pans — $x-5=9 \to x=14$ (+5 both sides).
- **Multiply/divide both sides**: scale both pans by the same nonzero number — $3x=12 \to x=4$ (÷3 both sides).
- **A move hits the WHOLE side**: never apply a move to only part of one pan — $\frac{3x+6}{3}=x+2$, not $x+6$.
- **Peel outermost layer first**: strategy, not a law — undo whatever's furthest from the target variable first.

## 02-rearranging-any-symbol — Rearranging for Any Symbol

- **Any symbol not being solved for acts like a known number**: the same moves apply whether you're
  isolating $x$ or $a$ — $at=v \to a=\frac{v}{t}$ is the identical move as $3x=12 \to x=4$.
- **Square-root both sides**: legal for the same reason as +/−/×/÷ — mind the $\pm$ (both roots are
  candidates unless context rules one out).
- **Target in the basement (dividing something)**: multiply both sides by that symbol first, then re-solve —
  $\frac{k}{x}=5 \to k=5x$.
- **Never divide by a symbol that might be zero**: note the assumption (e.g. $t \neq 0$) and move on.

## 03-expand-and-factor — Expand & Factor

- **Distributive law**: $a(b+c)=ab+ac$ — read left-to-right to *expand*, right-to-left to *factor*.
  One law, two directions.
- **Two brackets, distribute twice**: every term in the first bracket times every term in the second —
  $(x+2)(x+3)=x^2+5x+6$.
- **Zero-product rule**: if two things multiply to give $0$, at least one of them IS $0$ — only works
  when the product equals zero, not any other number.
- **Reshape until a move you know applies**: expanding/factoring don't change what an expression *is*,
  only its *shape* — different shapes unlock different moves (e.g. factored form unlocks zero-product).
- **The freshman's dream trap**: $(a+b)^2 \neq a^2+b^2$ — it's $a^2+2ab+b^2$; the $2ab$ handshake term
  is real.

## 04-fractions-ratios-percentages — Fractions, Ratios & Percentages

- **Multiplying by 1 changes nothing**: since $\frac{5}{5}=1$, $\frac{3}{4}=\frac{3}{4}\times\frac{5}{5}=\frac{15}{20}$
  — the move behind every common-denominator trick.
- **Multiply fractions straight across**: $\frac{a}{b}\times\frac{c}{d}=\frac{ac}{bd}$.
- **Divide by flipping and multiplying**: $\frac{a}{b}\div\frac{c}{d}=\frac{a}{b}\times\frac{d}{c}$.
- **Add/subtract fractions needs a common denominator first**: you can only combine matching pieces.
- **Percent means per hundred**: $x\%$ of $y$ = $\frac{x}{100}\times y$.
- **Normalise = divide each value by the total**: guarantees the results sum to 1 (a probability
  distribution).
- **Cancel factors, never terms**: $\frac{x+4}{4}\neq x$ — you can only cancel things that are
  *multiplied*, not *added*.

## 05-exponents-and-logs — Exponents & Logarithms

- **Same base multiplied → add exponents**: $a^m \cdot a^n = a^{m+n}$.
- **Same base divided → subtract exponents**: $\frac{a^m}{a^n} = a^{m-n}$.
- **Power of a power → multiply exponents**: $(a^m)^n = a^{mn}$.
- **Anything to the power 0 is 1** (nonzero base): $a^0 = 1$.
- **Negative exponent → reciprocal**: $a^{-n} = \frac{1}{a^n}$.
- **Fractional exponent $\tfrac12$ → square root**: $a^{1/2} = \sqrt{a}$.
- **A log asks "to the what power?"**: $\log_a x$ is the exponent that turns $a$ into $x$.
- **Product inside a log → sum of logs**: $\log(ab) = \log a + \log b$.
- **Quotient inside a log → difference of logs**: $\log\frac{a}{b} = \log a - \log b$.
- **Undo a log by raising the base on both sides**: $\log_2 x = 6 \to x = 2^6$.
- **Undo an exponent by taking the log of both sides**: $2^x = 10 \to x = \log_2 10$.

## 06-sigma-notation — Σ Notation

- **Σ is a for-loop with an accumulator**: $\sum_{i=1}^{n} f(i)$ is `total=0; for i in range(1,n+1): total += f(i)`
  — note Σ's top limit is *inclusive*, unlike Python's `range`.
- **Subscripts are indexing**: $x_i$ is `x[i]`; double subscript $w_{ij}$ is `w[i][j]` (row $i$, column $j$).
- **A double Σ is nested loops**: $\sum_i\sum_j w_{ij}$ = loop over rows, loop over columns, add everything.
- **Σ obeys the distributive law**: constants factor out, sums split across $+$ —
  $\sum_i(2x_i+1) = 2\sum_i x_i + n$.
- **"Sum of squares" ≠ "square of sum"**: $\sum x_i^2 \neq \left(\sum x_i\right)^2$ — check which one a
  formula actually asks for.
