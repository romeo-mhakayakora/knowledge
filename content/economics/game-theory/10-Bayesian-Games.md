---
title: Bayesian Games
---

# Module 10: Bayesian Games (Lectures 32–38)

This module introduces **Bayesian Games**, which model strategic interactions under **incomplete information**—scenarios where players are uncertain about other players' payoffs, strategies, or types.

---

## 1. The Harsanyi Transformation (Lectures 32–33)

In games of incomplete information, a player does not know the exact utility function of the opponent.
**John Harsanyi** solved this by transforming games of *incomplete information* into games of *imperfect information* using a new player called **Nature**:

1.  **Nature** moves first, selecting a **type** $\theta_i \in \Theta_i$ for each player $i$ according to a probability distribution $p(\theta_1, \ldots, \theta_n)$.
2.  Each player $i$ learns their own type $\theta_i$, but not the types of the other players. They only know the prior probability distribution $p$.
3.  Players choose actions simultaneously.

---

## 2. Bayesian Nash Equilibrium (BNE) Formal Definition

A **Bayesian Game** is defined by:
$$\{N, A, \Theta, p, u\}$$
*   $N$: Set of players.
*   $A = A_1 \times \cdots \times A_n$: Action spaces.
*   $\Theta = \Theta_1 \times \cdots \times \Theta_n$: Type spaces.
*   $p(\theta)$: Prior probability distribution over types.
*   $u_i(a, \theta)$: Utility functions.

### BNE Strategy Definition
A strategy for player $i$ is a function $s_i: \Theta_i \to A_i$ mapping each of their possible private types to an action.
A strategy profile $s^* = (s_1^*, \ldots, s_n^*)$ is a **Bayesian Nash Equilibrium (BNE)** if for every player $i$ and every type $\theta_i \in \Theta_i$ with $p(\theta_i) > 0$:
$$\max_{a_i \in A_i} \sum_{\theta_{-i} \in \Theta_{-i}} p(\theta_{-i} \mid \theta_i) \cdot u_i(a_i, s_{-i}^*(\theta_{-i}), \theta_i, \theta_{-i})$$

---

## 3. Bayesian Battle of the Sexes (Lectures 33–34)

Suppose Player 1 is unsure whether Player 2 wants to coordinate with them (Type 1: "Wish to Coordinate", prob $1-e$) or avoid them (Type 2: "Wish to Avoid", prob $e$).

*   **Player 1's payoffs (known):** Prefers Opera ($O$) to Football ($F$) but wants to coordinate.
*   **Player 2's payoffs depend on type:**
    *   **Type 1 (Coordinate):** Standard coordinator payoffs.
    *   **Type 2 (Avoid):** Prefers to choose the opposite of Player 1.

By utilizing BNE, we solve for Player 1's action and Player 2's type-dependent strategy. Player 2's action is a function:
$$s_2(\theta_2) = \begin{cases} s_2(\text{Coordinate}) \\ s_2(\text{Avoid}) \end{cases}$$

---

## 4. Yield vs. Fight Game (Lectures 35–36)

Two drivers meet at a narrow bridge. They can either **Yield ($Y$)** or **Fight ($F$)**.
Player 1 does not know if Player 2 is "Mild" (hates fighting, gets payoff $-10$ from Fight) or "Aggressive" (loves fighting, gets payoff $+5$ from Fight).
Let $p(\text{Aggressive}) = p$ and $p(\text{Mild}) = 1-p$.

*   **Mild Player 2** has a dominant strategy to **Yield** (to avoid the high negative payoff of fighting).
*   **Aggressive Player 2** has a dominant strategy to **Fight** (since $+5 > 0$).
*   Thus, Player 2's BNE strategy is fixed: $s_2^*(\text{Mild}) = Y$, $s_2^*(\text{Aggressive}) = F$.
*   **Player 1's Decision:** Player 1 (who has no private types, type is public) maximizes expected payoff:
    *   If Player 1 chooses Yield ($Y$): expected payoff is $0$.
    *   If Player 1 chooses Fight ($F$): expected payoff is:
        $$E[u_1(F)] = p(-100) + (1-p)(10) = 10 - 110p$$
    *   For Player 1 to choose Fight, we must have:
        $$10 - 110p > 0 \implies p < \frac{1}{11}$$

> **Conclusion:** Player 1 will choose to fight only if the probability of the opponent being aggressive is very low ($p < 9.09\%$). If the threat of aggression is higher, Player 1 yields.

---

## 5. Bayesian Cournot Competition (Lecture 37)

In a **Bayesian Cournot Duopoly**, Firm 1 has a known marginal cost $c$. Firm 2's cost is private information:
*   High cost $c_H$ with probability $p$.
*   Low cost $c_L$ with probability $1-p$.

We solve this using BNE: Firm 2 sets a cost-dependent quantity $q_2^*(c_H)$ and $q_2^*(c_L)$, while Firm 1 sets a single quantity $q_1^*$ based on expected reaction curves.
This illustrates how asymmetric information shifts market power and production quantities in oligopolies.
