# 7.1 — How to Read a Paper (the three-pass method)

*≤4 min read. This module runs as live sessions with Claude — this lesson is the field manual.*

## Why this matters

Nobody is taught to read CS papers, so everyone secretly reads them like novels — front to back,
drowning by page 3. But papers aren't novels. They're **written back-to-front** (results first,
then the story is reverse-engineered) — so reading them front-to-back is playing the game on hard mode.

## The one big idea

**Three passes, never one.** Each pass has a different mission, and you're allowed — *expected* —
to bail after any pass.

| Pass | Read | Mission | Time |
|---|---|---|---|
| 1 — Skim | Title, abstract, section headings, **every figure + caption**, conclusion | "What did they claim, and do I care?" | 10 min |
| 2 — Read | Intro, method *prose* (skip equation guts), results | "How does the idea work, roughly?" | 1 hour |
| 3 — Dissect | The equations, line by line, translated to numpy | "Could I rebuild a toy of this?" | days, and that's normal |

The figures are the paper's real abstract. Authors sweat over them most — start there.

## The dissection rules (pass 3)

1. **Every symbol gets named.** Meet $\mathbb{E}$, $\nabla$, $\|x\|$, $\odot$? Stop, identify it,
   map it to the module that taught it. An equation is just Module 0's balance game wearing a costume.
2. **Every equation becomes numpy.** If you can't write it as code, you don't understand it yet —
   and that's the *test*, not a failure.
3. **Small numbers first.** Hand-trace with a 2×3 matrix before believing anything about a 512×64 one.
4. **Questions are the method.** "Why √d?" "Why softmax and not just normalise?" — the paper makes
   sense exactly as fast as you generate questions at it.

## The plan for this module

- **7.3:** we dissect *Attention Is All You Need* (2017) together — the paper behind ChatGPT, Claude,
  and modern AI. By the time you get here, its scariest equation is made entirely of things you know:
  $$\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
  dot products (M2.3) · matrix multiplication (M2.5) · exp (M0.5) · softmax (M6.3).
- **7.4:** we rebuild a toy version of one of its figures in a notebook.
- **7.5:** you pick paper #2 and lead; Claude only answers questions.

> Drop any paper PDF into `modules/07-reading-papers/papers/` and start a session with
> *"let's dissect this"* — any paper, any time, even before officially reaching this module.

**Deep-end question:** why would a field's papers be written back-to-front? What does that tell you
about what reviewers (and readers) actually reward?
