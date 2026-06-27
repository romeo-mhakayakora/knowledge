---
title: Recap
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

# Summary Cheatsheet

| Concept | Key Formula / Fact |
|---------|-------------------|
| Random variable | Deterministic function $X: S \to \mathbb{R}$; randomness lives in $P$, not $X$ |
| Support | $\{x : P(X=x) > 0\}$ — where probability mass actually lives |
| PMF | $p_X(x) = P(X=x)$; nonneg + sums to 1 |
| PMF pipeline | Support → event $\{X=x\}$ → add outcome probabilities → done |
| "Find the distribution" | Give PMF (discrete, easier) or CDF (universal) — both equally valid |
| Bernoulli | $P(X=1)=p$, $P(X=0)=1-p$; indicator r.v. of any event |
| Binomial — 3 lenses | Story (indep. trials) / Indicators (sum of Bern) / PMF formula |
| Binomial PMF | $\binom{n}{k}p^k(1-p)^{n-k}$; requires independent trials, same $p$ |
| Binomial as sum | $X = X_1 + \cdots + X_n$, $X_i \overset{\text{i.i.d.}}{\sim} \text{Bern}(p)$ |
| Binomial additivity | $\text{Bin}(n,p) + \text{Bin}(m,p) = \text{Bin}(n+m,p)$ (same $p$, independent) |
| NOT Binomial | If sampling without replacement or $p$ changes — use Hypergeometric |
| Hypergeometric PMF | $\frac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}$; without replacement, equally likely |
| Vandermonde Identity | $\sum_{j=0}^k \binom{n}{j}\binom{m}{k-j} = \binom{n+m}{k}$ — proved 3 ways |
| DUnif PMF | $\frac{1}{\vert C \vert}$ for $x \in C$; reduces to counting problems |
| CDF | $F(x) = P(X \leq x)$; non-decreasing, right-continuous, $0 \to 1$ |
| CDF shape | Continuous: smooth S-curve. Discrete: staircase, jumps = PMF values |
| PMF → CDF | $F(x) = \sum_{x' \leq x} p_X(x')$ (running total) |
| CDF → PMF | $P(X=x_0) = F(x_0) - F(x_0^-)$ (size of jump) |
| PMF of $g(X)$ | $P(g(X)=y) = \sum_{x: g(x)=y} P(X=x)$ |
| One-to-one $g$ | Probability passes down unchanged |
| Many-to-one $g$ | Probabilities of merging inputs add up |
| Independence | $P(X \leq x, Y \leq y) = P(X \leq x)P(Y \leq y)$ |
| Discrete independence | $P(X=x, Y=y) = P(X=x)P(Y=y)$ |
| i.i.d. | Independent AND identically distributed — two orthogonal properties |
| HGeom ≈ Binomial | When population $\gg$ sample size ($n/N \to 0$) |
| Convolution meta-insight | PMF proof of Bin additivity is simultaneously a proof of Vandermonde |
