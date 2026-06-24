---
title: Markov Chains Cheat Sheet
---

# Markov Chains Cheat Sheet

A quick-reference guide for Markov Chain properties, classifications, and formulas.

---

## 🗺️ Topology Cheat Sheet

| Property | Definition | Scope | Key Intuition |
| :--- | :--- | :--- | :--- |
| **Recurrent State** | $P(\text{eventual return}) = 1$ | Single State | Inescapable loop. Given infinite time, visited infinitely many times. |
| **Transient State** | $P(\text{eventual return}) < 1$ | Single State | Has an escape hatch. Visited a finite number of times, then left forever. |
| **Absorbing State** | $q_{ii} = 1.0$ | Single State | Special case of recurrent. Once entered, the chain can never leave. |
| **Irreducible Chain** | All states communicate ($i \leftrightarrow j$) | Whole Chain | The map is fully connected; you can get from any state to any other. |
| **Reducible Chain** | Some states do not communicate | Whole Chain | The map contains isolated islands or one-way doors. |
| **Periodic State** | Return steps have $\gcd > 1$ | Single State | Returns only possible on a strict rhythmic grid (multiples of $d$). |
| **Aperiodic State** | Return steps have $\gcd = 1$ | Single State | Timing of returns is fluid. *(Self-loop $q_{ii} > 0$ guarantees aperiodicity).* |

---

## 📐 Core Formulas

### The Markov Property
$$P(X_{n+1} = j \mid X_n = i, X_{n-1} = i_{n-1}, \ldots, X_0 = i_0) = P(X_{n+1} = j \mid X_n = i)$$
*Future and past are conditionally independent given the present.*

### Transition Matrix Q
- $q_{ij} = P(X_{n+1} = j \mid X_n = i)$
- Row sum condition: $\sum_{j} q_{ij} = 1.0$ for all $i$.

### n-Step Transitions (Chapman-Kolmogorov)
- Matrix equation: $Q^{(n)} = Q^n$
- Summation form (2-step): $q_{ij}^{(2)} = \sum_{k} q_{ik} q_{kj}$

### Marginal Distributions (Law of Total Probability)
- $P(X_n = j) = \sum_{i} t_i q_{ij}^{(n)}$
- Vector form: $t^{(n)} = t Q^n$ (where $t$ is the initial spawn vector).

### Stationary Distributions
- Equation: $sQ = s \quad (\text{or } \pi Q = \pi)$
- Probability constraints: $s_i \ge 0$ and $\sum_{i} s_i = 1$.

### Universal 2-State Formula
For a transition matrix $Q = \begin{pmatrix} 1-a & a \\ b & 1-b \end{pmatrix}$:
- Flow balance: $a s_1 = b s_2$
- Stationary vector: $s = \left(\frac{b}{a+b}, \; \frac{a}{a+b}\right)$
