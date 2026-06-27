---
title: Hypergeometric Distribution
subject: probability
chapter: 04-random-variables
tags:
- probability
- mathematics
date: '2026-06-18'
updated: '2026-06-19'
status: complete
difficulty: intermediate
---

# Hypergeometric Distribution

> *Introduction to Probability* — Blitzstein & Hwang

---

## Hypergeometric Distribution

> **Story:** A population of $w + b$ objects: $w$ white and $b$ black. Draw $n$ objects **without replacement**. $X$ = number of white objects in the sample.

$$X \sim \text{HGeom}(w, b, n)$$

**PMF:**
$$P(X = k) = \frac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}$$

for integers $k$ satisfying $0 \leq k \leq w$ and $0 \leq n-k \leq b$, and $P(X=k) = 0$ otherwise. By convention $\binom{a}{b} = 0$ when $b < 0$ or $b > a$, so the formula self-zeros outside the valid range.

**Where the formula comes from:**

| Part | Meaning |
|------|---------|
| $\binom{w}{k}$ | Ways to choose $k$ white objects from $w$ white objects |
| $\binom{b}{n-k}$ | Ways to choose $n-k$ black objects from $b$ black objects |
| $\binom{w+b}{n}$ | Total ways to choose $n$ objects from the full population |

**Why $\binom{b}{n-k} \neq 1$:** Unlike Binomial where failures are automatically determined once successes are chosen, here the black balls come from a **separate pool**. There are genuinely multiple ways to choose which black balls you get.

**Check — sums to 1:** $\sum_k \binom{w}{k}\binom{b}{n-k} = \binom{w+b}{n}$ by the **Vandermonde Identity** ✓ — this constitutes a third independent proof of Vandermonde.

**Two-tag interpretation:** Every item in the population gets two labels simultaneously — first tag (white/black) and second tag (sampled/not sampled). $X$ counts items that are **twice-tagged**: white AND sampled. This interpretation generalizes far beyond urns: tagged elk in a forest, aces in a card hand, defective items in batch inspection — all are the same story with different labels.

**Key difference from Binomial:** Sampling without replacement means $p$ changes after each draw — the pool shrinks and probabilities shift. The trials are **dependent**.

**Symmetry:** $\text{HGeom}(w, b, n)$ and $\text{HGeom}(n, w+b-n, w)$ are identical distributions — swapping which tag is "first" counts the same twice-tagged items.

### Hypergeometric vs. Binomial — Full Comparison

| Property | Binomial | Hypergeometric |
|---|---|---|
| Sampling method | With replacement (or independent trials) | Without replacement |
| Trial independence | ✅ Yes | ❌ No |
| Probability of success $p$ | ✅ Constant across trials | ❌ Changes after each draw |
| Parameters | $n$, $p$ | $w$, $b$, $n$ |
| PMF | $\binom{n}{k}p^k(1-p)^{n-k}$ | $\dfrac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}$ |
| Approx. relationship | — | $\approx \text{Bin}\!\left(n,\, \frac{w}{w+b}\right)$ when $w+b \gg n$ |
