# Curriculum — Year 10 → Dangerous Enough for Deep Learning

One filter decides what's in: *does practical ML / CV / LLMs / diffusion need it?*
No trig identities for their own sake. No geometry proofs. Mastery-gated: move exactly as fast as
demonstrated skill allows.

**Mastery gate:** every module ends with a pen-and-paper **boss worksheet**, done cold, scanned in,
marked by Claude. ≥ ~85% with sound reasoning unlocks the next module; gaps go on the spaced-review queue.
After every boss fight: a **Wonder Interlude** as the reward.

---

## Module 0 — Algebra Bootcamp *(the fix for the old wound)*

The goal isn't "more algebra practice" — it's replacing memorised procedures with an understanding of
equations as a **balance game** with legal moves.

| # | Unit | Why (the ML hook) |
|---|---|---|
| 0.1 | Equations as a balance — legal moves that preserve truth | Every derivation you'll ever read is just chains of these moves |
| 0.2 | Rearranging & solving for *any* symbol | Rearranging loss/learning-rate formulas is daily ML life |
| 0.3 | Expanding & factoring — same expression, different shapes | "Simplify into a solvable structure" — the exact old struggle, made mechanical |
| 0.4 | Fractions, ratios & percentages fluency | Normalising data, probabilities, train/test splits |
| 0.5 | Exponents & logarithms | Loss curves, learning-rate schedules, log-probabilities |
| 0.6 | Σ summation notation — read it as a Python for-loop | Every ML paper equation; loss = a big Σ |

**Boss:** multi-step rearrangements + a "translate this Σ into Python" section.
**Interlude reward:** *The Fibonacci Spiral & the Golden Ratio* — one simple recurrence → sunflowers, shells, galaxies.

## Module 1 — Functions & Graphs

| # | Unit | Why |
|---|---|---|
| 1.1 | Functions as machines: input → output (= Python functions) | Neural nets ARE functions |
| 1.2 | The shape zoo: linear, quadratic, exp, log, 1/x | Reading loss curves and activation functions at a glance |
| 1.3 | Transforming graphs: shift, stretch, flip | Normalisation; what weights and biases *do* |
| 1.4 | Composing functions: machines feeding machines | Deep = composed. This is what "layers" means |
| 1.5 | Sigmoid & friends (preview) | Meet the activation functions early |

**Boss:** sketch-by-hand + predict-the-shape, then verify own answers in matplotlib.
**Interlude reward:** *The Logistic Map & Chaos* — one innocent quadratic function iterated → the edge of chaos (and the world's most beautiful bifurcation plot).

## Module 2 — Linear Algebra *(the heart of deep learning)*

| # | Unit | Why |
|---|---|---|
| 2.1 | Vectors: arrows AND lists of numbers | Data points, embeddings — everything is a vector |
| 2.2 | Vector arithmetic & scaling | "king − man + woman ≈ queen" |
| 2.3 | Dot product = similarity | The single most important operation in AI; powers attention |
| 2.4 | Matrices as data tables and as transformations | Weight matrices; batches of data |
| 2.5 | Matrix multiplication — why the weird row×column rule | It's function composition (Module 1.4 pays off) |
| 2.6 | Images ARE matrices — load a photo in numpy, manipulate pixels | First real computer vision |

**Boss:** hand-computed dots & matmuls + a numpy image-manipulation mini-project.
**Interlude reward:** *The Mandelbrot Set* — z² + c iterated over complex numbers → infinite beauty, computed by his own numpy code.

## Module 3 — Calculus *(just enough, gradient-first)*

| # | Unit | Why |
|---|---|---|
| 3.1 | Slope everywhere: derivative = sensitivity of output to input | "If I nudge this weight, how does the loss change?" |
| 3.2 | Derivative rules for the shape zoo | Enough fluency to read any ML derivation |
| 3.3 | Chain rule = pipelines of functions | Backpropagation IS the chain rule |
| 3.4 | Partial derivatives & the gradient | Loss surfaces; ∇ in every paper |
| 3.5 | Gradient descent — implement it by hand on a real curve | THE payoff moment: watch your own code learn |

**Boss:** derivatives & chain-rule by hand + a from-scratch gradient descent in Python.
**Interlude reward:** *Random Walks & Brownian Motion* — pure coin-flips → the wandering paths inside diffusion models and stock markets.

## Module 4 — Probability & Statistics

| # | Unit | Why |
|---|---|---|
| 4.1 | Probability as counting; simulation-first with numpy | Intuition by experiment, not formulas |
| 4.2 | Mean, variance, standard deviation | Why we normalise inputs; batch norm |
| 4.3 | Distributions & the normal (Gaussian) | The bell curve that powers diffusion models |
| 4.4 | Sampling & randomness | Why training is stochastic; temperature |
| 4.5 | Likelihood → cross-entropy loss | Why classifiers use that "weird" loss — it's just log-probability |

**Boss:** simulation experiments + interpret-the-distribution problems.
**Interlude reward:** *The Galton Board & Order from Chaos* — thousands of random bounces always build the same bell curve. Randomness has laws.

## Module 5 — The Math of a Neural Net *(capstone I)*

Build a tiny neural network **from scratch in numpy**, using only math from Modules 0–4:

1. Forward pass = matrix multiplications + activation functions (M1, M2)
2. Loss = cross-entropy (M4)
3. Backprop = the chain rule (M3)
4. Training loop = gradient descent (M3)
5. Convolutions = sliding dot-products over image matrices (M2 → computer vision)

**Boss:** the network works and he can explain every line's math on paper.
**Finishing Module 5 = ready for fast.ai Practical Deep Learning.**

## Module 6 — The Math of Modern AI: LLMs & Stable Diffusion *(capstone II)*

Almost everything here is *reuse* — modern AI isn't new math, it's Modules 2–4 composed cleverly.

**LLMs:**
| # | Unit | Reuses |
|---|---|---|
| 6.1 | Embeddings: words as vectors in space | M2 vectors |
| 6.2 | Attention = dot-product similarity + softmax | M2 dot product, M0 exp |
| 6.3 | Softmax & temperature: scores → probabilities | M0 exponents, M4 distributions |
| 6.4 | Next-token prediction = cross-entropy over a vocabulary | M4 likelihood |
| 6.5 | Build a toy attention head in numpy | everything |

**Stable Diffusion:**
| # | Unit | Reuses |
|---|---|---|
| 6.6 | Gaussian noise — the normal distribution, starring role | M4 |
| 6.7 | Noising/denoising images = vector arithmetic on matrices | M2 |
| 6.8 | Noise schedules: interpolation & exp curves | M0, M1 |
| 6.9 | The denoising loop — gradient descent's cousin | M3 |
| 6.10 | Latent spaces: compressed matrices | M2 |
| 6.11 | Experiment: progressively noise & denoise a real photo in numpy | everything |

**Interlude reward (finale):** *Fourier & Epicycles* — any drawing rebuilt from pure spinning circles; the math inside JPEG, audio, and vision models. Plus *Euler's identity*, e^{iπ} + 1 = 0 — the most beautiful equation ever written, and by then he'll understand every symbol in it.

## Module 7 — Read a Breakthrough Paper *(capstone III — the graduation test)*

Nobody teaches how to read CS papers. This module fixes that, live, as guided sessions with Claude
rather than pre-written worksheets — question-driven dissection suits how William learns.

| # | Unit | What happens |
|---|---|---|
| 7.1 | Anatomy of a paper | The three-pass method: skim (title/abstract/figures) → read (intro/conclusions) → dissect (method). Papers are written back-to-front; readers shouldn't read front-to-back |
| 7.2 | Notation survival kit | The Greek alphabet of ML: subscripts/superscripts, argmax, 𝔼 expectations, ‖·‖ norms, ∇, ⊙ — every symbol mapped to the module that taught it and to a line of Python |
| 7.3 | Dissect *Attention Is All You Need* | Section by section, equation by equation. The famous $\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right)V$ — by now he can hand-compute every piece (M2 dot products, M0 exp, M6 softmax). Translate each equation into numpy as we go |
| 7.4 | Reproduce something | Rebuild a toy version of one figure or result from the paper in a notebook — the moment a paper stops being scripture and becomes an engineering document |
| 7.5 | Solo flight | He picks the second paper (ResNet, U-Net, CLIP, DDPM…) and leads the dissection; Claude only answers questions. Pass = he explains the core equation on paper to Claude |

**Prerequisite:** Module 6. **Format:** live sessions, one pass per session — logged in `sessions/` like everything else.

---

## Wonder Interludes *(the beauty track — `modules/interludes/`)*

Optional any time, mandatory after boss fights. Each is a ≤30-min notebook where William generates
a genuinely beautiful image with his own code, and each secretly reinforces curriculum skills:

| Interlude | Beauty | Secretly drills |
|---|---|---|
| I.1 Fibonacci & the golden ratio | Spirals in sunflowers, shells, galaxies | Recurrences, ratios, loops |
| I.2 The logistic map | Bifurcation into chaos | Function iteration, quadratics |
| I.3 The Mandelbrot set | Infinite fractal coastline | Complex numbers, iteration, numpy arrays |
| I.4 Random walks | Brownian wandering | Randomness, cumulative sums |
| I.5 The Galton board | Order emerging from chaos | Distributions, the central limit theorem |
| I.6 Fourier epicycles | Drawings from spinning circles | Vectors, waves, composition |
| I.7 L-systems & fractal plants | Grow a fern from 3 rules | Recursion, geometry of nature |

The thread running through them: *simple rules, iterated, create the complexity of nature.*
That same idea — simple math, composed and repeated — is exactly what a neural network is.

---

## Progression map

```
M0 algebra ──▶ M1 functions ──▶ M2 linear algebra ──▶ M3 calculus ──▶ M4 probability
                                                                          │
                    fast.ai ready ◀── M5 neural net from scratch ◀────────┘
                                            │
                                            ▼
                              M6 LLMs & stable diffusion
                                            │
                                            ▼
                              M7 read a breakthrough paper
```
