# 1.1 — Functions as Machines

*≤5 min read. Then straight to the worksheet.*

## Why this matters (the real reason)

GPT is a function. Stable Diffusion is a function. An image classifier is a function.
Not "like" a function — each one literally IS a single function: input goes in (text, noise, pixels),
output comes out (next-word probabilities, an image, "cat: 94%"). Billions of internal knobs, sure —
but still one machine with an input slot and an output chute. Learn to read machines and you can
read all of modern AI.

## The one big idea

A function is a **machine**: feed it an input, it follows its rule, it hands back an output.
Same input in → same output out, *every single time*. That's the whole contract.

You already know this machine — you've been writing them in Python:

$$f(x) = 3x + 2 \qquad \equiv \qquad \texttt{def f(x): return 3*x + 2}$$

The scary notation is just naming the parts:

| Notation | What it actually says | Python |
|---|---|---|
| $f$ | the machine's name | the function's name |
| $x$ | the input slot (a placeholder, not a mystery) | the parameter |
| $f(5)$ | "feed 5 into machine $f$" | `f(5)` |
| $f(x) = 3x + 2$ | the machine's blueprint: what it does to *whatever* lands in the slot | the `def` line + `return` |

**$f(x)$ is NOT "$f$ times $x$".** It's a machine name with its input slot shown. This one
misreading causes years of confusion — kill it now.

## Watch one machine run

Blueprint: $g(x) = x^2 - 1$.

$$g(3) = 3^2 - 1 = 8 \qquad g(-3) = (-3)^2 - 1 = 8 \qquad g(0) = -1$$

The slot takes *whatever* you shove in — including symbols, shoved in **whole**:

$$g(a + 1) = (a+1)^2 - 1$$

Everywhere the blueprint says $x$, the entire input gets stamped in. That's the rule.

## Domain: what won't crash the machine

Some inputs crash some machines. $h(x) = \dfrac{10}{x - 4}$ runs fine on almost anything —
but feed it $x = 4$ and it divides by zero. In Python: `ZeroDivisionError`. In math: *undefined*.

The **domain** is simply *the set of inputs that won't crash the machine*. Three classic crashers:

| Machine part | Crashes when | Python error |
|---|---|---|
| $\frac{1}{\text{something}}$ | something $= 0$ | `ZeroDivisionError` |
| $\sqrt{\text{something}}$ | something $< 0$ | `math domain error` |
| $\log(\text{something})$ | something $\le 0$ | `math domain error` |

So the domain of $h$ is: every number except 4. Finding a domain = asking
"what would make this blueprint divide by zero, root a negative, or log a non-positive?"

## The Python connection

```python
def h(x):
    return 10 / (x - 4)

print(h(9))    # 2.0 — machine runs fine
print(h(4))    # ZeroDivisionError — input outside the domain, machine crashes
```

A math function and a Python function are the same species. When a mathematician writes
"the domain of $h$ is $x \ne 4$", a programmer writes "calling `h(4)` raises an exception".
Identical idea, different dialect.

## Classic traps

- **$f(x)$ read as multiplication.** It never is. It's machine-name + input-slot.
- **$f(x+1)$ treated as $f(x) + 1$.** No: $f(x+1)$ feeds $x+1$ *into the slot*; $f(x)+1$ adds 1 to
  the *output*. Different pipes, different results. (This distinction becomes a superpower in unit 1.3.)
- **Substituting only part of the input.** $g(a+1)$ means $(a+1)$ replaces $x$ *everywhere, in brackets*.
  Forgetting the brackets around a negative input — $g(-3) = -3^2 - 1$ ✗ — is the #1 sign error.

> **Deep-end question to hold in your head during the worksheet:**
> $f(x) = (x+1)^2 - x^2$ and $g(x) = 2x + 1$ have completely different blueprints.
> Are they the same machine or different machines? What would "same machine" even mean —
> and how could Python help you decide?

**Now: worksheet `01-functions-as-machines` — pen and paper. Photograph into `scans/inbox/` when done.**
