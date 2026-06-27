---
title: Connections Between Binomial and Hypergeometric
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

# Connections Between Binomial and Hypergeometric

> *Introduction to Probability* — Blitzstein & Hwang

---

## Connections Between Binomial and Hypergeometric

$$\text{Binomial} \xrightarrow{\text{condition on total}} \text{Hypergeometric}$$
$$\text{Hypergeometric} \xrightarrow{\text{population} \to \infty} \text{Binomial}$$

### Binomial → Hypergeometric by conditioning

Start with $X \sim \text{Bin}(n,p)$ and $Y \sim \text{Bin}(m,p)$ independent. Condition on the total $X+Y = K$. Once the total is fixed, the trials are no longer independent — asking for the distribution of $X$ given the total is exactly the Hypergeometric.

---

### Hypergeometric → Binomial by taking a limit

Start with $\text{HGeom}(w, b, n)$. Let $w + b \to \infty$ while keeping $\frac{w}{w+b} = p$ fixed. Drawing without replacement from an effectively infinite population is the same as drawing with replacement — dependence vanishes. In the limit, $\text{HGeom}(w, b, n) \to \text{Bin}(n, p)$.

> **Practical implication:** When sampling $n$ people from a large population $N$ where $n \ll N$, the Hypergeometric can be safely approximated by the Binomial. The approximation improves as $n/N \to 0$.

---

## Big Picture Flowchart

```
Two conditions: independence + constant p
        |
        ├── Both hold → BINOMIAL Bin(n,p)
        │       ├── Lens 1 Story: n indep. Bern(p) trials, count successes
        │       ├── Lens 2 Indicators: X = X₁ + ... + Xₙ, i.i.d. Bern(p)
        │       └── Lens 3 PMF: C(n,k) pᵏ qⁿ⁻ᵏ  [validated by Binomial Theorem]
        │
        └── Sampling without replacement → HYPERGEOMETRIC HGeom(w,b,n)
                ├── Story: draw n from w white + b black, count white
                └── PMF: C(w,k)C(b,n-k) / C(w+b,n)  [validated by Vandermonde]

Adding independent Binomials with same p:
    Bin(n,p) + Bin(m,p) = Bin(n+m,p)
    Proved 3 ways: Story | Indicators | PMF convolution (uses Vandermonde)

Vandermonde Identity: Σⱼ C(n,j)C(m,k-j) = C(n+m,k)
    Proved 3 times across the course:
        1. Story proof (combinatorics)
        2. Binomial convolution (PMF proof above)
        3. Hypergeometric PMF summing to 1

Random Variables: functions X: S → ℝ
    Described by CDF F(x) = P(X ≤ x)  [always]
    or PMF pⱼ = P(X = aⱼ)             [discrete only, usually easier]
```
