---
title: Cumulative Distribution Functions
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

# Cumulative Distribution Functions (CDF)

> *Introduction to Probability* — Blitzstein & Hwang

---

## Cumulative Distribution Functions (CDF)

> **Definition:** The *cumulative distribution function* (CDF) of an r.v. $X$ is:
> $$F_X(x) = P(X \leq x)$$

Unlike the PMF (discrete only), the CDF is defined for **all** random variables — discrete and continuous. It is the universal tool for describing distributions.

Think of the CDF as a running total — it accumulates all PMF values from $-\infty$ up to $x$.

**Three properties every valid CDF must satisfy:**

### Property 1 — Increasing
$$x_1 \leq x_2 \implies F(x_1) \leq F(x_2)$$
$P(X \leq x_2)$ includes everything in $P(X \leq x_1)$ plus more. Probability can only accumulate, never decrease.

---

### Property 2 — Right-continuous
$$F(a) = \lim_{x \to a^+} F(x)$$
For discrete r.v.s, the CDF is completely flat between support values and jumps *at* each support value. The jump size equals the PMF value there. For integer-valued X this is even stronger — $F$ is literally constant between integers, not just right-continuous.

```
F(x)
|              ___________
|         ____|
|    ____|
|___|
|_________________________ x
   0    1    2    3    4
```

---

### Property 3 — Convergence to 0 and 1
$$\lim_{x \to -\infty} F(x) = 0 \qquad \text{and} \qquad \lim_{x \to +\infty} F(x) = 1$$

As $x \to -\infty$: no values of $X$ are $\leq x$, so probability = 0.
As $x \to +\infty$: all values of $X$ are $\leq x$, so:
$$\lim_{x \to \infty} F(x) = \lim_{x \to \infty} \sum_{n=0}^{x} P(X=n) = \sum_{n=0}^{\infty} P(X=n) = 1$$

The third property is just the PMF axiom expressed through the CDF — the boundary conditions are the PMF properties in disguise.

---

### What CDF Graphs Look Like

* **Discrete distributions**: The CDF is a **staircase function** (step function). It is flat between support values, and has a vertical jump at each support value. The height of the jump at $x$ is equal to $P(X = x)$.
* **Continuous distributions**: The CDF is a **smooth, continuous curve** with no jumps (since $P(X = x) = 0$ for all $x$).

---

## PMF vs CDF

| | PMF | CDF |
|---|---|---|
| Formula | $P(X = x)$ | $P(X \leq x)$ |
| What it gives | Probability at one exact point | Accumulated probability up to $x$ |
| Shape (discrete) | Spikes at support values | Staircase — flat then jump |
| Jump size | — | Equals PMF value at that point |
| Defined for | Discrete r.v.s only | All r.v.s |

The CDF and PMF carry the same information — you can always recover one from the other. The jump in the CDF at any point equals the PMF value there: $P(X = x_0) = F(x_0) - F(x_0^-)$.
