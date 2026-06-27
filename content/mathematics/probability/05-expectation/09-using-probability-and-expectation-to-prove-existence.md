---
title: Using Probability and Expectation to Prove Existence
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

# Using Probability and Expectation to Prove Existence

The probabilistic method is a non-constructive method for proving the existence of a mathematical object with a certain property. It was pioneered by the mathematician Paul Erdős.

## The Core Concept

To prove that an object with property $P$ exists:
1. Define a probability space of candidate objects.
2. Show that if we choose an object $X$ at random from this space, the probability that $X$ has property $P$ is strictly positive:
   $$P(X \text{ has property } P) > 0$$
3. Since the probability is greater than zero, there must exist at least one object in the sample space that has property $P$. (If no such object existed, the probability would be exactly 0.)

## Using Expectations (The First Moment Method)

Expectations can also be used to prove existence:

- If the expected value of a random variable $X$ is $E(X) = \mu$, then there must exist:
  * At least one outcome in the sample space where $X \geq \mu$.
  * At least one outcome in the sample space where $X \leq \mu$.

If this were not true (for example, if $X < \mu$ everywhere), then the expectation $E(X)$ would have to be strictly less than $\mu$, a contradiction.

This simple but elegant idea is used to prove many bounds in graph theory, combinatorics, and computer science.
