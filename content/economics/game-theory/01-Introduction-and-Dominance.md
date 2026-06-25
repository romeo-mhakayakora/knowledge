---
title: Introduction and Dominant Strategies
---

# Module 01: Introduction and Dominant Strategies (Lectures 1–6)

This module introduces the mathematical foundations of game theory and strategic formulation, focusing on simultaneous games, dominated strategies, and Pareto optimality.

---

## 1. Practical Examples of Game Theory (Lectures 1–2)

Game theory is applicable in any setting where agents make decisions that affect one another:

*   **Markets:** Firms setting prices (Bertrand) or quantities (Cournot). A firm's profit depends not just on its price/quantity, but on competitor prices/quantities.
*   **Politics:** Candidates choosing platforms or spending limits. Voters' decisions depend on candidate promises and expected behavior of other voters.
*   **Wireless Communications:** Nodes choosing transmission power. If too many transmit at high power, interference ruins the signal for everyone.

---

## 2. Formal Game Representation: Normal Form

A simultaneous game in **Normal Form** is defined by the triple $\{N, S, U\}$:

1.  **Players ($N$):** The set of decision-makers:
    $$N = \{1, 2, \ldots, n\}$$
2.  **Strategies ($S$):** The strategy space of all players:
    $$S = S_1 \times S_2 \times \cdots \times S_n$$
    Where $S_i$ is player $i$'s set of possible strategies.
3.  **Payoffs ($U$):** The utility functions for each player:
    $$u_i: S \to \mathbb{R}$$
    Where $u_i(s_1, \ldots, s_n)$ represents player $i$'s payoff under strategy profile $s \in S$.

---

## 3. The Prisoner's Dilemma (Lecture 3)

The classic baseline model for strategic conflict. Two players choose to either Cooperate ($C$) or Defect ($D$):

| Player 1 \ Player 2 | Cooperate ($C$) | Defect ($D$) |
| :--- | :---: | :---: |
| **Cooperate ($C$)** | $(-1, -1)$ | $(-3, 0)$ |
| **Defect ($D$)** | $(0, -3)$ | $(-2, -2)$ |

### Solution Concept: Dominant Strategies
Regardless of whether Player 2 cooperates or defects:
*   If Player 2 plays $C$, Player 1 prefers $D$ ($0 > -1$).
*   If Player 2 plays $D$, Player 1 prefers $D$ ($-2 > -3$).

Thus, Defect ($D$) is a **dominant strategy** for both players. The unique equilibrium outcome is $(D, D)$.

---

## 4. Pareto Optimality (Lecture 4)

A strategy profile $s \in S$ is **Pareto Optimal** (or Pareto Efficient) if there is no other strategy profile $s' \in S$ that makes at least one player strictly better off without making any other player worse off.

*   Formally, $s$ is Pareto optimal if there does **not** exist an $s' \in S$ such that:
    $$\forall i \in N, \quad u_i(s') \ge u_i(s) \quad \text{and} \quad \exists j \in N \ \text{s.t.} \ u_j(s') > u_j(s)$$

### The Dilemma
In the Prisoner's Dilemma:
*   The Nash Equilibrium $(D, D)$ yields payoffs of $(-2, -2)$.
*   The profile $(C, C)$ yields $(-1, -1)$.
*   Since $(C, C)$ is strictly better for both players than $(D, D)$, $(D, D)$ is **Pareto inefficient**.

This shows that individual optimization does not necessarily lead to socially optimal outcomes.

---

## 5. Dominant Strategies (Lectures 5–6)

Let $s_i \in S_i$ be a strategy for player $i$, and let $S_{-i}$ be the set of all strategy profiles for the remaining players.

### 5.1 Strict Dominance
Strategy $s_i^*$ **strictly dominates** strategy $s_i$ for player $i$ if:
$$\forall s_{-i} \in S_{-i}, \quad u_i(s_i^*, s_{-i}) > u_i(s_i, s_{-i})$$

> **Rule of Rationality:** A rational player will never play a strictly dominated strategy.

### 5.2 Weak Dominance
Strategy $s_i^*$ **weakly dominates** strategy $s_i$ for player $i$ if:
$$\forall s_{-i} \in S_{-i}, \quad u_i(s_i^*, s_{-i}) \ge u_i(s_i, s_{-i})$$
and there exists at least one $s_{-i}' \in S_{-i}$ such that:
$$u_i(s_i^*, s_{-i}') > u_i(s_i, s_{-i}')$$
