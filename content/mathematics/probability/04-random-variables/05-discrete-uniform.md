---
title: Discrete Uniform Distribution
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

# Discrete Uniform Distribution

> *Introduction to Probability* — Blitzstein & Hwang

---

## Discrete Uniform Distribution

> **Story:** Let $C$ be a finite, nonempty set of numbers. Choose one uniformly at random — all values equally likely. Call the chosen number $X$.

$$X \sim \text{DUnif}(C)$$

**PMF:**
$$P(X = x) = \frac{1}{|C|} \quad \text{for } x \in C \quad (0 \text{ otherwise})$$

**Check — sums to 1:** $|C| \times \frac{1}{|C|} = 1$ ✓

**For any subset $A \subseteq C$:**
$$P(X \in A) = \frac{|A|}{|C|}$$

This is exactly the naive definition of probability — DUnif questions always reduce to counting problems.

**Special note on X:** When the sample space $C$ is already numeric, $X$ is the **identity function** — $X(s) = s$ for all $s \in C$. The sample space IS the support of $X$, so naive probability applies directly without the full pipeline.

---

## Worked Example — Slips of Paper (DUnif)

There are 100 slips of paper numbered $1, 2, \ldots, 100$, each number appearing once. Five slips are drawn one at a time.

### Sampling With Replacement

**(a) Distribution of how many drawn slips have value $\geq 80$:**
Each draw independently has probability $\frac{21}{100}$ of landing $\geq 80$. By the Binomial story: $\text{Bin}(5, 21/100)$.

**(b) Distribution of the value of the $j$-th draw:**
By symmetry, $X_j \sim \text{DUnif}(\{1, 2, \ldots, 100\})$ for any $j$.

**(c) $P(\text{number 100 drawn at least once})$:**
$$1 - \left(\frac{99}{100}\right)^5 \approx 0.049$$

### Sampling Without Replacement

**(d) Distribution of how many drawn slips have value $\geq 80$:**
Now $\text{HGeom}(21, 79, 5)$ — pool shrinks, $p$ changes, trials dependent.

**(e) Distribution of the value of the $j$-th draw:**
Still $Y_j \sim \text{DUnif}(\{1, 2, \ldots, 100\})$ by symmetry — each slip equally likely to be in any position when viewed in isolation.

**(f) $P(\text{number 100 is in the sample})$:**
$$\frac{5}{100} = \frac{1}{20} = 0.05$$

> **Key insight:** Sampling with and without replacement give the **same marginal distribution** for any single draw — $\text{DUnif}$ either way. The difference only shows up when looking at *multiple* draws together.

---

## Worked Example — Random Walk

A particle starts at 0. At each step it moves $+1$ or $-1$, each with probability $\frac{1}{2}$, independently. After $n$ steps, let $Y$ be the particle's position.

Let $X$ = number of right steps, so $X \sim \text{Bin}(n, 1/2)$. Net position: $Y = X - (n - X) = 2X - n$.

$$P(Y = k) = P\!\left(X = \frac{n+k}{2}\right) = \binom{n}{\frac{n+k}{2}} \left(\frac{1}{2}\right)^n$$

Valid for $k \in \{-n, -n+2, \ldots, n-2, n\}$ — values where $n+k$ is even.

---

## Worked Example — Distance from Origin

Let $D = |Y|$ = distance from origin after $n$ steps. Since $|k| = |-k|$, this is many-to-one:

$$P(D = 0) = P(Y = 0) = \binom{n}{n/2} \left(\frac{1}{2}\right)^n \quad \text{(only if } n \text{ is even)}$$

$$P(D = k) = 2\binom{n}{\frac{n+k}{2}}\left(\frac{1}{2}\right)^n \quad \text{for } k \geq 1$$

Two $y$ values ($+k$ and $-k$) collapse into one $d$ value ($k$) — a direct application of the many-to-one PMF formula.
