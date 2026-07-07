# Boss Worksheet — Module 3: Calculus

*The mastery gate. Rules:*

- *Paper parts (Sections 1–4) are done **cold** — no notes, no lessons open, no Python until Section 5.*
- *Name your moves at every step, as always. Reasoning earns marks; bare answers don't.*
- *Photograph everything into `scans/inbox/` for marking.*
- *≥85% with sound reasoning unlocks Module 4 (Probability & Statistics) — and your Wonder
  Interlude reward: Random Walks & Brownian Motion.*

---

## Section 1 — Derivatives, moves named

Differentiate. Name each rule as it fires.

1. $f(x) = x^7$

2. $f(x) = 4x^3 - 6x^2 + x - 9$

3. $f(x) = 2e^x + 3\ln x$

4. $f(x) = \dfrac{1}{x} + \sqrt{x}$   *(rewrite as powers first)*

5. $f(x) = x^2 - 10x$. Differentiate, then find the $x$ where $f'(x) = 0$ and say what that
   point *is* on the graph.

---

## Section 2 — Chain rule, pipeline named

For each: name the pipeline (inner/outer), differentiate each stage, multiply along the pipe.

6. $h(x) = (5x - 2)^4$

7. $h(x) = e^{x^2}$

8. $h(x) = \ln(2x + 1)$

9. $h(x) = \left(e^x + x\right)^3$, then evaluate $h'(0)$.

10. In one or two sentences, using the exchange-rate or gears idea: why do the sensitivities
    of a pipeline *multiply*, and what does this have to do with how a deep neural network
    learns? (This is the "explain backprop to a mate at the pub" question.)

---

## Section 3 — One gradient

11. $L(w, b) = w^2 + 3wb + b^2$
    a. Find $\dfrac{\partial L}{\partial w}$ (state who's frozen).
    b. Find $\dfrac{\partial L}{\partial b}$ (state who's frozen).
    c. Write $\nabla L$ and evaluate it at $(w, b) = (1, 2)$.
    d. At that point, which parameter is the loss more sensitive to, and what direction would
       a gradient-descent step move $(w, b)$ — uphill or downhill?

---

## Section 4 — Read the loss surface

12. A loss surface $L(w_1, w_2)$ has circular contours centred at $(3, -1)$, labelled
    $L = 1$ (innermost), $L = 4$, $L = 9$ (outermost). You are standing at $(3, 2)$.
    a. Sketch the contours and your position.
    b. Draw the direction of $\nabla L$ at your position. How do you know it's perpendicular
       to your contour?
    c. Draw the direction a gradient-descent step actually moves.
    d. Training runs for a while and the gradient's length keeps shrinking. What is happening,
       and why is that expected near $(3, -1)$?
    e. Your learning rate is set so large that each step *overshoots* the centre. Sketch two
       or three steps of the resulting path. What would you change, and in which direction?

---

## Section 5 — From-scratch gradient descent (at the computer)

*Write this yourself in a fresh notebook or .py file — no copying from the module notebooks.
Photograph/screenshot your code AND its output.*

13. Implement gradient descent on $f(x) = (x - 4)^2$:
    a. Write `f(x)` and a `derivative(f, x, h=1e-6)` nudge function — your slope must come
       from the nudge, not a hand-coded formula.
    b. Loop 50 update steps from `x = 0.0` with `lr = 0.1`, printing `x` every 10 steps.
    c. State what value it converged to and why that value was inevitable.
    d. Rerun with `lr = 1.5`. Describe what happened and name the failure mode.
    e. Stretch (bonus marks): descend the two-parameter bowl $L(w, b) = (w-2)^2 + (b+1)^2$
       using two nudge-based partials. Report where it lands.

---

*Done? Everything into `scans/inbox/`, then tell Claude it's boss-marking time.*
