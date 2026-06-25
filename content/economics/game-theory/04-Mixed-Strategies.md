---
title: Mixed Strategies and MSNE
---

# Module 04: Mixed Strategies and MSNE (Lectures 12–16)

This module formalizes **Mixed Strategy Nash Equilibria (MSNE)**, where players choose probability distributions over their available pure strategies to achieve strategic equilibrium.

---

## 1. Mixed Strategy Definition (Lecture 12)

Let $S_i = \{s_{i1}, s_{i2}, \ldots, s_{ik}\}$ be player $i$'s set of finite pure strategies.
A **mixed strategy** for player $i$ is a probability distribution $p_i = (p_{i1}, p_{i2}, \ldots, p_{ik})$ over $S_i$, where:
$$\sum_{j=1}^k p_{ij} = 1 \quad \text{and} \quad p_{ij} \ge 0 \ \forall j$$

The set of all mixed strategies for player $i$ is denoted by $\Delta(S_i)$.

### Expected Payoffs
If players choose mixed strategies $p = (p_1, \ldots, p_n)$, player $i$'s expected payoff is the weighted sum of payoffs across all possible pure strategy profiles:
$$E[u_i(p)] = \sum_{s \in S} \left( \prod_{j=1}^n p_j(s_j) \right) u_i(s)$$

---

## 2. Solving Battle of the Sexes (Lectures 13–14)

Consider the Battle of the Sexes matrix:

| Player 1 \ Player 2 | Opera ($O$) | Football ($F$) |
| :--- | :---: | :---: |
| **Opera ($O$)** | $(2, 1)$ | $(0, 0)$ |
| **Football ($F$)** | $(0, 0)$ | $(1, 2)$ |

Let Player 1 choose $O$ with probability $p$ and $F$ with probability $1-p$.
Let Player 2 choose $O$ with probability $q$ and $F$ with probability $1-q$.

### Expected Payoffs & The Indifference Principle
A player is willing to randomize between multiple pure strategies if and only if all those strategies yield the **same expected payoff** given the opponent's mixed strategy.

For Player 1:
*   $E[u_1(O, q)] = q(2) + (1-q)(0) = 2q$
*   $E[u_1(F, q)] = q(0) + (1-q)(1) = 1 - q$

Equating the expected payoffs to solve for $q$:
$$2q = 1 - q \implies 3q = 1 \implies q^* = \frac{1}{3}$$

For Player 2:
*   $E[u_2(p, O)] = p(1) + (1-p)(0) = p$
*   $E[u_2(p, F)] = p(0) + (1-p)(2) = 2(1-p) = 2 - 2p$

Equating these:
$$p = 2 - 2p \implies 3p = 2 \implies p^* = \frac{2}{3}$$

The Mixed Strategy Nash Equilibrium is:
$$(p^*, q^*) = \left(\frac{2}{3}, \frac{1}{3}\right)$$
The equilibrium payoffs are $E[u_1] = \frac{2}{3}$ and $E[u_2] = \frac{2}{3}$.

---

## 3. Mixed Strategy Examples (Lectures 15–16)

### 3.1 Paying Taxes Game (Auditing)
A citizen chooses to pay taxes ($T$) or cheat ($C$). The government chooses to audit ($A$) or trust ($R$).

| Citizen \ Govt | Audit ($A$) | Trust ($R$) |
| :--- | :---: | :---: |
| **Tax ($T$)** | $(v - t, \ t - c)$ | $(v - t, \ t)$ |
| **Cheat ($C$)** | $(v - t - f, \ t + f - c)$ | $(v, \ 0)$ |

Where $t$ is tax rate, $f$ is fine for cheating, $c$ is cost of auditing, and $v$ is utility of keeping income.
*   If Govt trusts, Citizen cheats. If Citizen cheats, Govt audits. If Govt audits, Citizen pays taxes. If Citizen pays taxes, Govt prefers to trust (to save cost $c$).
*   This cycle yields a **Mixed Strategy Nash Equilibrium** representing the frequency of audits and tax evasion.

### 3.2 Portfolio Management Game
A fund manager decides between Safe ($S$) and Risky ($R$) assets, competing against a market state (High vs. Low volatility) where relative performance determines rewards. Mixed strategies optimize long-term expected returns under uncertainty.
