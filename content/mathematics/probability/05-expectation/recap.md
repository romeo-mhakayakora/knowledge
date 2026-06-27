---
title: Recap
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

# Expectation and Variance Recap

A quick summary of key formulas and concepts covered in this chapter:

## Key Formulas

| Concept | Discrete Formula | Continuous Formula |
|---|---|---|
| **Expectation $E(X)$** | $\sum_{x} x P(X = x)$ | $\int_{-\infty}^{\infty} x f(x) \, dx$ |
| **LOTUS $E(g(X))$** | $\sum_{x} g(x) P(X = x)$ | $\int_{-\infty}^{\infty} g(x) f(x) \, dx$ |
| **Variance $\text{Var}(X)$** | $E(X - EX)^2 = E(X^2) - (EX)^2$ | $E(X^2) - (EX)^2$ |
| **Standard Deviation** | $\text{SD}(X) = \sqrt{\text{Var}(X)}$ | $\text{SD}(X) = \sqrt{\text{Var}(X)}$ |

---

## Important Properties

* **Linearity of Expectation**: 
  $$E(aX + bY) = aE(X) + bE(Y) \quad \text{(always holds)}$$
* **Variance Properties**:
  * $\text{Var}(X + c) = \text{Var}(X)$
  * $\text{Var}(cX) = c^2 \text{Var}(X)$
  * $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) \quad \text{(only if } X \text{ and } Y \text{ are independent)}$
* **Poisson Distribution $\text{Pois}(\lambda)$**:
  * PMF: $P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}$
  * $E(X) = \lambda$
  * $\text{Var}(X) = \lambda$
* **Poisson Approximation**:
  * $\text{Bin}(n, p) \approx \text{Pois}(np)$ when $n$ is large and $p$ is small.
