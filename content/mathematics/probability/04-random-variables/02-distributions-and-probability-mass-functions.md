---
title: Distributions and Probability Mass Functions
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

# Distributions and Probability Mass Functions

> *Introduction to Probability* — Blitzstein & Hwang

---

## The Probability Mass Function (PMF)

> **Definition:** The *probability mass function* (PMF) of a discrete r.v. $X$ is the function $p_X$ given by:
> $$p_X(x) = P(X = x)$$
> This is positive if $x$ is in the support of $X$, and 0 otherwise.

The PMF is the complete blueprint of a discrete random variable. Once you know the PMF, you can answer any probability question about $X$ by summing:

$$P(X \in B) = \sum_{x \in B} p_X(x)$$

### Valid PMF — Two Conditions

Any PMF must satisfy:

1. **Nonnegative:** $p_X(x) > 0$ for $x$ in the support, and $p_X(x) = 0$ otherwise
2. **Sums to 1:** $\sum_j p_X(x_j) = 1$

These follow naturally: probability is always nonnegative, and X must take *some* value — certainty.

> **Practical habit:** Before using a PMF, always: (1) list the valid values of $k$, and (2) verify the sum equals 1. This catches errors early.

### What P(X = x) Really Means

$\{X = x\}$ is an **event** — the set of all outcomes $s$ in $S$ that X maps to $x$:

$$\{X = x\} = \{s \in S : X(s) = x\}$$

This set is a subset of $S$, so it is a legitimate event, and we can take its probability. Multiple different outcomes can map to the same value of $x$ — the event $\{X = x\}$ collects all of them.

> Note: Writing $P(X)$ makes no sense — you can only take the probability of an **event**, not of a random variable itself.

### What "Find the Distribution" Means

When a problem says *find the distribution of $X$*, it means: provide a complete mathematical description of the randomness of $X$. There are two valid answers:

1. **Give the PMF** $P(X = k)$ for all $k$ — works only for discrete RVs, but is usually far easier.
2. **Give the CDF** $F(x) = P(X \leq x)$ — works for any RV.

These are equally valid and carry the same information. In discrete settings, always prefer the PMF unless told otherwise.

---

## The PMF Pipeline

This is the core procedure for finding any PMF. Always follow it step by step.

**Step 0 — Is X discrete or continuous?**
If discrete, continue. Identify what X counts or measures.

**Step 1 — Find the support of X**
List all values x can actually take (where $P(X = x) > 0$).

**Step 2 — For each value x, find the event $\{X = x\}$**
$\{X = x\} = \{s \in S : X(s) = x\}$ — the set of all outcomes mapping to x.

**Step 3 — Calculate the probability of each individual outcome in that event**

**Step 4 — Add them up**
$p_X(x) = \sum_{s \in \{X=x\}} P(s)$

**Step 5 — Finish with:**
$p_X(x) = 0$ for all $x$ outside the support.

### Example — Two Coin Tosses

$X$ = number of Heads, $S = \{HH, HT, TH, TT\}$, each outcome probability $1/4$:

| Event | Outcomes | Calculation | PMF value |
|-------|---------|-------------|-----------|
| $\{X = 0\}$ | $\{TT\}$ | $1/4$ | $p_X(0) = 1/4$ |
| $\{X = 1\}$ | $\{HT, TH\}$ | $1/4 + 1/4$ | $p_X(1) = 1/2$ |
| $\{X = 2\}$ | $\{HH\}$ | $1/4$ | $p_X(2) = 1/4$ |
