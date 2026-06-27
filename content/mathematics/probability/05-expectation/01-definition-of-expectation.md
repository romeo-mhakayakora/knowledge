---
title: Definition of Expectation
subject: probability
chapter: 05-expectation
tags:
- probability
- mathematics
date: '2026-06-18'
updated: '2026-06-19'
status: complete
difficulty: intermediate
---

# Definition of Expectation

> *Introduction to Probability* — Blitzstein & Hwang

---

## The Journey: Arithmetic Mean → Weighted Mean → Expectation

These three concepts are the same idea, progressively generalized.

### 1. Arithmetic Mean

The familiar average — all values treated equally:

$$\bar{x} = \frac{1}{n} \sum_{j=1}^{n} x_j = \frac{x_1 + x_2 + \cdots + x_n}{n}$$

Every data point $x_j$ gets the **same weight**: $\frac{1}{n}$.

---

### 2. Weighted Mean

Used when you already know how much each value should contribute:

$$\text{weighted-mean}(x) = \sum_{j=1}^{n} x_j p_j$$

Where the weights $p_1, \ldots, p_n$ must satisfy:

$$p_j \geq 0 \quad \text{and} \quad \sum_{j=1}^{n} p_j = 1$$

**Key insight:** The arithmetic mean is just a special case of the weighted mean where all weights are equal: $p_j = \frac{1}{n}$ for all $j$.

**Example** — Exam worth 70%, homework worth 30%:
$$\text{weighted mean} = 0.7 \times 80 + 0.3 \times 90 = 83$$
$$\text{arithmetic mean} = \frac{80 + 90}{2} = 85 \quad \leftarrow \text{wrong, ignores weights}$$

---

### 3. Expectation (Weighted Mean with Probabilities)

> "The definition of expectation for a discrete r.v. is inspired by the weighted mean of a list of numbers, with weights given by probabilities."

**Definition 4.1.1:** The *expected value* of a discrete r.v. $X$ with distinct possible values $x_1, x_2, \ldots$ is:

$$E(X) = \sum_{j=1}^{\infty} x_j \cdot P(X = x_j)$$

Same structure as the weighted mean — but now the weights $p_j$ are replaced by **probabilities** $P(X = x_j)$.

| | Arithmetic Mean | Weighted Mean | Expectation |
|---|---|---|---|
| Weight of each $x_j$ | $\frac{1}{n}$ (same for all) | $p_j$ (assigned manually) | $P(X = x_j)$ (from distribution) |
| Weights sum to | $1$ ✓ | $1$ ✓ | $1$ ✓ |
| Number of values | finite | finite | can be infinite |

---

## Cleaner Notation

Instead of indexing with $j$, you can sum directly over the **support** of $X$:

$$E(X) = \sum_{x} x \cdot P(X = x)$$

The **support** is the set of values $X$ can actually take (where the PMF is non-zero).

**Why this works:** For any $x$ not in the support, $P(X = x) = 0$, so:
$$x \cdot P(X = x) = x \cdot 0 = 0$$
Those terms contribute nothing, so it's safe to sum over everything — non-support values vanish automatically.

**The two notations are identical** — same numbers, same arithmetic:
$$\sum_{j=1}^{3} x_j \cdot P(X = x_j) = \sum_{x} x \cdot P(X = x)$$

The index $j$ is just a mechanical counter. The value notation skips the middleman.

**Example** — $X$ has support $\{3, 7, 10\}$ with probabilities $0.2, 0.5, 0.3$:
$$E(X) = 3(0.2) + 7(0.5) + 10(0.3) = 0.6 + 3.5 + 3.0 = 7.1$$

---

## Special Case: Equally Likely Outcomes

When all outcomes are equally likely, $P(X = x_j) = \frac{1}{n}$ for all $j$, so:

$$E(X) = \sum_{j=1}^{n} x_j \cdot \frac{1}{n} = \frac{x_1 + x_2 + \cdots + x_n}{n}$$

This is just the **arithmetic mean** — the average you learned in school.

> The arithmetic mean is a special case of expectation where every outcome is equally probable.

**Die example:** $X \in \{1, 2, 3, 4, 5, 6\}$, each with probability $\frac{1}{6}$:
$$E(X) = 1 \cdot \frac{1}{6} + 2 \cdot \frac{1}{6} + \cdots + 6 \cdot \frac{1}{6} = \frac{21}{6} = 3.5$$

Note: $X$ *never* equals 3.5 — but 3.5 is the long-run average. This is like the average number of children per household being 1.8 — no household actually has 1.8 children.

---

## Worked Examples {#worked-examples-expectation}

### Example 1 — Bernoulli R.V.

Let $X \sim \text{Bern}(p)$, with $q = 1 - p$. Then $X$ takes value 1 (success) with probability $p$ and value 0 (failure) with probability $q$:

$$E(X) = 1 \cdot p + 0 \cdot q = p$$

The expected value of a Bernoulli r.v. is simply $p$ — the probability of success. This makes intuitive sense: $E(X)$ sits between 0 and 1, compromising based on how likely each outcome is.

> Think of it as the balancing point on a seesaw with a pebble of mass $q$ at 0 and a pebble of mass $p$ at 1 — the fulcrum must be at $p$.

---

### Example 2 — Frequentist / Simulation Interpretation

Let $X$ have three possible values $a_1, a_2, a_3$ with probabilities $p_1, p_2, p_3$.

Imagine running $n$ independent draws of $X$. In the long run:
- About $p_1 n$ draws will produce $a_1$
- About $p_2 n$ draws will produce $a_2$
- About $p_3 n$ draws will produce $a_3$

The arithmetic mean of those $n$ simulation results is approximately:

$$\frac{p_1 n \cdot a_1 + p_2 n \cdot a_2 + p_3 n \cdot a_3}{n} = p_1 a_1 + p_2 a_2 + p_3 a_3 = E(X)$$

**Key takeaway:** The formula for $E(X)$ isn't arbitrary — it is exactly what you'd get by running the experiment many times and averaging the results. Expectation *is* the long-run average.

> For the Bernoulli case: writing 1 for "success" and 0 for "failure", the long-run proportion of 1's converges to $p$. The average of a long list of 0's and 1's is just the fraction of 1's — which is $p$.

---

## When Expectation is Undefined

$E(X)$ is only defined when:

$$\sum_{j=1}^{\infty} |x_j| \cdot P(X = x_j) < \infty$$

The sum of **absolute values**, weighted by probabilities, must be finite (must **converge**).

### What does "converge" vs "diverge" mean?

- **Converge** — as you add more and more terms, the sum settles toward a fixed finite number.
  $$\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots = 1 \quad \checkmark$$

- **Diverge** — the sum keeps growing forever, never settling.
  $$1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots = \infty \quad \times$$

### Two problems when $E(X)$ diverges:

1. **The series blows up** — the sum goes to $+\infty$ or $-\infty$. No finite answer.

2. **The answer depends on the order you add terms** — if there are large positive and large negative terms, rearranging them can give different sums (Riemann rearrangement theorem). The expectation wouldn't be well-defined.

Using $|x_j|$ (absolute values) checks that even ignoring signs, the sum stays finite — guaranteeing the answer is stable regardless of ordering.

| Condition | Result |
|---|---|
| $\sum |x_j| \cdot P(X = x_j) < \infty$ | $E(X)$ exists, finite, unambiguous ✓ |
| $\sum |x_j| \cdot P(X = x_j) = \infty$ | $E(X)$ undefined — diverges or order-dependent ✗ |

> In practice, most textbook distributions have well-defined expectations. But it's important to know it isn't automatically guaranteed.

---

## Key Properties and Warnings

### Proposition 4.1.2 — Same Distribution → Same Expectation

If $X$ and $Y$ are discrete r.v.s with the **same distribution** (same PMF), then:
$$E(X) = E(Y)$$

This follows directly from the definition — expectation is computed purely from the PMF.

### The Converse is FALSE

**Same expectation does NOT mean same distribution.**

$E(X)$ is just one number. It only tells you the "balancing point" — the center. It says nothing about:
- How spread out the values are
- The shape of the distribution
- How likely positive vs negative values are

**Example:** Both distributions below have $E(X) = 5$, but are completely different:

| Distribution A | Distribution B |
|---|---|
| $\{4, 5, 6\}$ equally likely | $\{1, 5, 9\}$ equally likely |
| Narrow spread | Wide spread |

Think of a seesaw — two differently shaped seesaws can still balance at the same point.

---

### Warning 4.1.3 — Never Replace an R.V. with Its Expectation

> "A common mistake is to replace an r.v. by its expectation without justification."

| | $X$ | $E(X)$ |
|---|---|---|
| What it is | A **function** — maps outcomes to values | A **constant** — one fixed number |
| Is it random? | Yes — varies across outcomes | No — completely fixed |

Replacing $X$ with $E(X)$ is wrong:
- **Mathematically** — $X$ is a function, $E(X)$ is a constant. They are different objects.
- **Statistically** — it ignores all the variability and randomness in $X$.

**Only exception:** If $X$ is a constant (e.g., $X = 5$ always with probability 1), then $X = E(X)$. But that's a degenerate r.v. — no randomness at all.

---

### Notation 4.1.4

We often abbreviate $E(X^2)$ to $EX^2$, and $E(X^n)$ to $EX^n$.

> $E(X^2)$ is the expectation of the r.v. $X^2$ — **not** the square of the number $EX$. These are generally different!

---

## Expectation Summary

$$\text{Arithmetic Mean} \longrightarrow \text{Weighted Mean} \longrightarrow \text{Expectation}$$

Each step just generalizes how weights are assigned:

- **Arithmetic mean** — all values weighted equally by $\frac{1}{n}$
- **Weighted mean** — values weighted by manually assigned $p_j$'s that sum to 1
- **Expectation** — values weighted by their probabilities $P(X = x_j)$

> **Core intuition:** $E(X)$ is the *long-run average* value of $X$ over many independent repetitions of the experiment. It is a one-number summary of the center — but does not determine the full distribution.
