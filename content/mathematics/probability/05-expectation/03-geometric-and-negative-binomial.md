---
title: Geometric and Negative Binomial Expectation
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

# Geometric and Negative Binomial Expectation

This section covers the expected values of the Geometric and Negative Binomial distributions.

## Geometric Distribution

For a random variable $X \sim \text{Geom}(p)$ representing the number of failures before the first success (support $\{0, 1, 2, \ldots\}$):

$$E(X) = \frac{1-p}{p} = \frac{q}{p}$$

For the First Success distribution $Y = X + 1$ representing the number of trials until the first success (support $\{1, 2, 3, \ldots\}$):

$$E(Y) = \frac{1}{p}$$

---

## Negative Binomial Distribution

For a random variable $X \sim \text{NBin}(r, p)$ representing the number of failures before the $r$-th success:

$$E(X) = r \cdot \frac{q}{p}$$
