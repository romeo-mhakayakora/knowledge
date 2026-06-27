---
title: R
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

# R Programming for Expectation and Poisson

Below are the R functions and code snippets related to expectation, variance, and the Poisson distribution.

## Poisson Functions in R

R has four built-in functions for the Poisson distribution:

* `dpois(x, lambda)`: Probability Mass Function $P(X = x)$.
* `ppois(q, lambda)`: Cumulative Distribution Function $P(X \leq q)$ (or $P(X > q)$ if `lower.tail = FALSE`).
* `qpois(p, lambda)`: Quantile function (finds $x$ such that $P(X \leq x) \geq p$).
* `rpois(n, lambda)`: Generates $n$ random observations from the Poisson distribution.

### Examples

```R
# Probability of exactly 3 events when lambda is 2
dpois(3, lambda = 2)

# Probability of 3 or fewer events when lambda is 5
ppois(3, lambda = 5)

# Generate 10 random samples from Pois(3.5)
rpois(10, lambda = 3.5)
```

---

## Calculating Expectation and Variance Numerically

If you have a custom discrete probability distribution with outcomes `x` and corresponding probabilities `p`:

```R
# Define support and probabilities
x <- c(1, 2, 5, 10)
p <- c(0.1, 0.4, 0.3, 0.2)

# Expectation E(X) = sum(x * p)
expectation <- sum(x * p)
print(paste("Expectation:", expectation))

# Variance Var(X) = sum((x - E(X))^2 * p)
variance <- sum((x - expectation)^2 * p)
print(paste("Variance:", variance))

# Standard Deviation
sd <- sqrt(variance)
print(paste("SD:", sd))
```
