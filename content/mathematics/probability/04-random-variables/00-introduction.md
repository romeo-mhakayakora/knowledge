---
title: Random Variables and Their Distributions
---

# Chapter 3: Random Variables and Their Distributions

Standard probability notation gets unwieldy fast. For example, in the Gambler's Ruin problem, tracking exact amounts using event notation like $A_{jk}$ and $B_{jk}$ becomes a long, tangled string of unions and intersections.

The fix: random variables let us work with *numbers* instead of raw events — unlocking clean algebra and compact notation.

> "Instead of having convoluted notation that obscures how the quantities of interest are related, wouldn't it be nice if we could say something like: Let $X_k$ be the wealth of gambler A after $k$ rounds..."

Random variables also let us simplify a complex sample space. The sample space of an experiment is often incredibly complicated or high-dimensional, and the outcomes $s \in S$ may be non-numeric. A random variable maps those messy outcomes to numbers — so we can do mathematics on them.

> *Introduction to Probability* — Blitzstein & Hwang

---

## Topics

- [[01-random-variables]] — Definition, support, and classification of random variables
- [[02-distributions-and-probability-mass-functions]] — Blueprint of discrete random variables
- [[03-bernoulli-and-binomial]] — Success/failure trials and their sums
- [[04-hypergeometric]] — Sampling without replacement
- [[05-discrete-uniform]] — Equally likely outcomes in a finite set
- [[06-cumulative-distribution-functions]] — The universal distribution tool
- [[07-functions-of-random-variables]] — Deterministic transformations of random inputs
- [[08-independence-of-rvs]] — Decoupled behavior and sums of independent Binomials
- [[09-connections-between-binomial-and-hypergeometric]] — Limits and conditioning parallels
- [[10-recap]] — Concept and formula cheatsheet
- [[11-r]] — *(Empty - yet to be studied)* R programming for random variables
- [[12-exercises]] — Solved and unsolved exercises
