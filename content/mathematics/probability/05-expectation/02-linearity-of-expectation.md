---
title: Linearity of Expectation
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

# Linearity of Expectation

Linearity of expectation is one of the most powerful and fundamental properties of expected value. 

## The Theorem

For **any** random variables $X$ and $Y$ (regardless of whether they are independent or dependent), and any constants $a$ and $b$:

$$E(aX + bY) = aE(X) + bE(Y)$$

More generally, for any finite collection of random variables $X_1, X_2, \ldots, X_n$ and constants $c_1, c_2, \ldots, c_n$:

$$E\left(\sum_{i=1}^n c_i X_i\right) = \sum_{i=1}^n c_i E(X_i)$$

> **CRITICAL IMPORTANCE:** Linearity of expectation does *not* require independence. It holds unconditionally. This makes it incredibly useful for finding expectations of sums of dependent random variables, such as in occupancy problems or matches.
