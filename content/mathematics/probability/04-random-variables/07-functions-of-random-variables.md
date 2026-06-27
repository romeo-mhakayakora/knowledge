---
title: Functions of Random Variables
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

# Functions of Random Variables

> *Introduction to Probability* — Blitzstein & Hwang

---

## Functions of Random Variables

If $X$ is a random variable, then any function of $X$ is also a random variable.

$X^2$, $e^X$, $\sin(X)$, $g(X)$ for any $g : \mathbb{R} \to \mathbb{R}$ — all are random variables. Why? A random variable is a deterministic function on a random input. Applying another deterministic function on top still gives a deterministic function on a random input — still a random variable. Randomness flows from the original sample space through every transformation.

> **Definition 3.7.1:** For an experiment with sample space $S$, an r.v. $X$, and a function $g : \mathbb{R} \to \mathbb{R}$, $g(X)$ is the r.v. that maps $s$ to $g(X(s))$ for all $s \in S$.

$$s \xrightarrow{X} X(s) \xrightarrow{g} g(X(s))$$

This is function composition: $g(X) = g \circ X$. $g$ uses $X$'s output set as its own input — but the randomness always traces back to $S$.

---

### PMF of g(X) — The Master Formula

$$P(g(X) = y) = \sum_{x \,:\, g(x) = y} P(X = x)$$

Find every $x$ in the support of $X$ that maps to $y$ under $g$, then add up their probabilities.

**One-to-one g:** Only one $x$ maps to each $y$ → probability passes down unchanged:
$$P(Y = g(x)) = P(X = x)$$
The support just gets relabeled; probabilities are inherited directly.

**Many-to-one g:** Multiple $x$ values map to the same $y$ → probabilities merge and add up. This is the only interesting case requiring real work.

The formula handles both cases with one expression — one-to-one is just a special case where every sum has exactly one term.

> **Key insight:** Since random variables are deterministic, probability is born in $S$ and travels down through every function. One-to-one guarantees it arrives unchanged. Many-to-one is the only case where something interesting happens — probabilities of merging inputs add up.

---

### Two Common Mistakes

**Mistake 1 — Multiplying the PMF to get PMF of $2X$:**

Wrong: $P(2X = y) = 2 \times P(X = x)$. This makes probabilities sum to 2, violating the axiom.

Correct: $P(2X = y) = P(X = y/2)$. Since $g(x) = 2x$ is one-to-one, probability passes down unchanged. The PMF of $2X$ is a **horizontal stretch** of the PMF of $X$ — same heights, doubled support values. Not a vertical stretch.

**Mistake 2 — Same distribution means always equal:**

Wrong: if $X$ and $Y$ have the same distribution, then $P(X = Y) = 1$.

The PMF describes probability behaviour. Two r.v.s can have identical PMFs while mapping individual sample outcomes to completely different numbers.

| Situation | $P(X = Y)$ |
|---|---|
| $X$ and $Y = 1-X$ (coin) | 0 — never equal |
| $X$ and $Z$ (independent flip) | 1/2 — sometimes equal |
| $X$ and itself | 1 — always equal |

All three cases can share the same Bern$(1/2)$ distribution. Same distribution $\neq$ same r.v.
