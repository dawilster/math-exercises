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

   ::: answer
   $f'(x) = 7x^6$ — move: power rule ($x^n \to nx^{n-1}$).
   :::

2. $f(x) = 4x^3 - 6x^2 + x - 9$

   ::: answer
   $f'(x) = 12x^2 - 12x + 1$ — move: power rule term-by-term (sum rule lets each term
   differentiate separately); the constant $-9$ vanishes.
   :::

3. $f(x) = 2e^x + 3\ln x$

   ::: answer
   $f'(x) = 2e^x + \dfrac{3}{x}$ — move: $e^x$ differentiates to itself; $\ln x \to \frac{1}{x}$;
   constant multiples just ride along.
   :::

4. $f(x) = \dfrac{1}{x} + \sqrt{x}$   *(rewrite as powers first)*

   ::: answer
   Rewrite: $x^{-1} + x^{1/2}$. Move: power rule on each →
   $f'(x) = -x^{-2} + \tfrac{1}{2}x^{-1/2} = -\dfrac{1}{x^2} + \dfrac{1}{2\sqrt{x}}$.
   :::

5. $f(x) = x^2 - 10x$. Differentiate, then find the $x$ where $f'(x) = 0$ and say what that
   point *is* on the graph.

   ::: answer
   $f'(x) = 2x - 10$. Move: set $f'(x) = 0 \Rightarrow 2x = 10 \Rightarrow x = 5$.
   That's the vertex — the parabola's minimum (flat tangent, turning point).
   :::

---

## Section 2 — Chain rule, pipeline named

For each: name the pipeline (inner/outer), differentiate each stage, multiply along the pipe.

6. $h(x) = (5x - 2)^4$

   ::: answer
   $h'(x) = 4(5x-2)^3 \cdot 5 = 20(5x-2)^3$ — pipeline: outer $u^4$ (power rule),
   inner $5x-2$ (derivative $5$), multiply along the pipe.
   :::

7. $h(x) = e^{x^2}$

   ::: answer
   $h'(x) = e^{x^2} \cdot 2x = 2x\,e^{x^2}$ — pipeline: outer $e^u$ (its own derivative),
   inner $x^2$ (derivative $2x$), multiply along the pipe.
   :::

8. $h(x) = \ln(2x + 1)$

   ::: answer
   $h'(x) = \dfrac{1}{2x+1} \cdot 2 = \dfrac{2}{2x+1}$ — pipeline: outer $\ln u$
   (derivative $\frac{1}{u}$), inner $2x+1$ (derivative $2$), multiply along the pipe.
   :::

9. $h(x) = \left(e^x + x\right)^3$, then evaluate $h'(0)$.

   ::: answer
   $h'(x) = 3(e^x+x)^2(e^x+1)$ — pipeline: outer $u^3$, inner $e^x+x$ (derivative $e^x+1$).
   At $x=0$: inner value $= 1$, inner derivative $= 2$, so $h'(0) = 3(1)^2(2) = 6$.
   :::

10. In one or two sentences, using the exchange-rate or gears idea: why do the sensitivities
    of a pipeline *multiply*, and what does this have to do with how a deep neural network
    learns? (This is the "explain backprop to a mate at the pub" question.)

    ::: answer
    Each stage rescales a nudge by its own local rate before handing it to the next stage
    (like converting currency through several exchange rates, or one gear turning the next) —
    so the total rate is the product of the stage rates: $\frac{dy}{dx} = \frac{dy}{du}\cdot\frac{du}{dx}$.
    A deep network is just a long pipeline of layers, so backprop finds the gradient of the
    loss w.r.t. an early weight by multiplying the local derivatives of every layer back through
    the chain.
    :::

---

## Section 3 — One gradient

11. $L(w, b) = w^2 + 3wb + b^2$
    a. Find $\dfrac{\partial L}{\partial w}$ (state who's frozen).
    b. Find $\dfrac{\partial L}{\partial b}$ (state who's frozen).
    c. Write $\nabla L$ and evaluate it at $(w, b) = (1, 2)$.
    d. At that point, which parameter is the loss more sensitive to, and what direction would
       a gradient-descent step move $(w, b)$ — uphill or downhill?

    ::: answer
    a. $\dfrac{\partial L}{\partial w} = 2w + 3b$ — $b$ frozen (treated as constant).
    b. $\dfrac{\partial L}{\partial b} = 3w + 2b$ — $w$ frozen.
    c. $\nabla L = (2w+3b,\ 3w+2b)$. At $(1,2)$: $(2(1)+3(2),\ 3(1)+2(2)) = (8, 7)$.
    d. More sensitive to $w$ ($8 > 7$). A gradient-descent step moves *opposite* the gradient
       (downhill): direction $-\nabla L = (-8, -7)$ — decrease both $w$ and $b$.
    :::

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

    ::: answer
    a. Distance from centre to $(3,2)$ is $|2-(-1)| = 3$, so you're sitting exactly on the
       outermost contour, $L=9$ (matches $L=r^2$: $r=3 \Rightarrow L=9$), directly above the
       centre on the line $w_1=3$.
    b. $\nabla L$ points radially *outward* from the centre — at $(3,2)$ that's straight up
       (pure $+w_2$, zero $w_1$ component). It's perpendicular to the contour because moving
       *along* a contour doesn't change $L$ to first order — the direction of steepest increase
       must be at 90° to that flat direction.
    c. Gradient descent moves opposite the gradient: straight down, directly toward the centre
       $(3,-1)$.
    d. The surface is flattening as you approach the minimum at $(3,-1)$; for a bowl-shaped loss
       the gradient's length scales with distance from the minimum ($|\nabla L| = 2r$ here), so
       it's expected to shrink to zero right at the bottom.
    e. Overshooting produces a zig-zag (or an outward spiral if severe) instead of settling at
       the centre. Fix: shrink the learning rate.
    :::

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

    ::: answer
    (a, b are code-to-write — no single answer, verify against the below.)
    c. Converges to $x = 4$ — the minimum of $(x-4)^2$, where the true derivative
       $2(x-4)=0$; descent keeps stepping downhill until the slope flattens to zero there.
    d. Diverges. Update: $x \to x - 1.5\cdot 2(x-4) = x - 3(x-4)$, so the distance from $4$
       multiplies by $(1-3)=-2$ each step — flips sign and doubles in size every step.
       Failure mode: learning rate too large → oscillating blow-up, not convergence.
    e. Lands at $(w,b) = (2,-1)$ — the minimum of the bowl, found the same way: each
       nudge-based partial drives its own coordinate downhill until both flatten out.
    :::

---

*Done? Everything into `scans/inbox/`, then tell Claude it's boss-marking time.*
