---
title: Bargaining Theory
---

# Module 14: Bargaining Theory (Lectures 53–54)

This module explores **Bargaining Theory**, covering both non-cooperative sequential models (Rubinstein's alternating offers) and cooperative axiomatic models (Nash bargaining).

---

## 1. Rubinstein's Alternating-Offers Model (Lecture 53)

Two players bargain over a pie of size 1. The game has sequential, alternating rounds:
*   **Round 1:** Player 1 proposes a split $(x, 1-x)$. Player 2 accepts or rejects. If accepted, the game ends. If rejected, we move to Round 2.
*   **Round 2:** Player 2 proposes a split $(1-y, y)$. Player 1 accepts or rejects.
*   The game continues until an offer is accepted. Payoffs are discounted by $\delta \in (0, 1)$ each round.

### Subgame Perfect Equilibrium (SPNE)
Because the game has infinite horizon, the subgame starting at Round 3 is identical to the game starting at Round 1.
Let $V$ be the maximum payoff Player 1 can expect to get in the game at the start of any round where they are the proposer.
*   When Player 2 proposes in Round 2, the most they have to offer Player 1 to make them accept is the discounted value of what Player 1 would get by waiting for Round 3:
    $$\text{Offer to Player 1} = \delta V$$
    This leaves Player 2 with $1 - \delta V$. Thus, at the start of Round 2, Player 2's maximum payoff is $V_2 = 1 - \delta V$.
*   By the same logic, when Player 1 proposes in Round 1, they only need to offer Player 2 the discounted value of what Player 2 would get in Round 2:
    $$\text{Offer to Player 2} = \delta V_2 = \delta (1 - \delta V)$$
    This leaves Player 1 with:
    $$V = 1 - \delta (1 - \delta V) = 1 - \delta + \delta^2 V$$

Now, solve for $V$:
$$V(1 - \delta^2) = 1 - \delta \implies V(1 - \delta)(1 + \delta) = 1 - \delta \implies V = \frac{1}{1 + \delta}$$

### Unique SPNE Outcome
Player 1 proposes a split immediately in Round 1, and Player 2 accepts.
*   **Player 1 gets:** $x^* = \frac{1}{1 + \delta}$
*   **Player 2 gets:** $1 - x^* = \frac{\delta}{1 + \delta}$

> **Intuition:** The proposer has a first-mover advantage. If players are extremely patient ($\delta \to 1$), the split approaches $(0.5, 0.5)$. If players are impatient ($\delta \to 0$), the proposer takes the entire pie ($x^* \to 1$).

---

## 2. Nash's Axiomatic Cooperative Bargaining (Lecture 54)

Rather than modeling the step-by-step negotiations, **John Nash** proposed an **axiomatic approach** to cooperative bargaining.

Let $S \subset \mathbb{R}^2$ be the set of feasible payoff pairs, and $d = (d_1, d_2)$ be the **disagreement point** (what players receive if bargaining fails).
Nash proved that a unique solution exists satisfying four reasonable axioms:

1.  **Pareto Efficiency:** The solution lies on the boundary of the feasible set.
2.  **Symmetry:** If the feasible set is symmetric and $d_1 = d_2$, then $x_1^* = x_2^*$.
3.  **Independence of Irrelevant Alternatives (IIA):** If the solution to a large set of options is chosen, and we restrict the options to a subset containing that solution, the solution remains the same.
4.  **Scale Invariance:** The solution is invariant under linear transformations of utility.

### The Nash Bargaining Solution
The unique solution $(x_1^*, x_2^*)$ satisfying these axioms is the profile that maximizes the **Nash Product** of net utilities:
$$\max_{(x_1, x_2) \in S} (x_1 - d_1)(x_2 - d_2)$$
subject to $x_1 \ge d_1$ and $x_2 \ge d_2$.
