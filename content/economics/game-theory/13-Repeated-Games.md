---
title: Repeated Games
---

# Module 13: Repeated Games (Lectures 49–52)

This module explores **Repeated Games**, where the same stage game is played multiple times by the same players, introducing dynamic incentives for trust, punishment, and long-term cooperation.

---

## 1. Finitely Repeated Games (Lectures 49–51)

Suppose the standard Prisoner's Dilemma is repeated exactly $T$ periods. The total payoff is the sum of payoffs in each stage.

### The Backward Induction Breakdown (Lecture 50)
If RCK (Rationality is Common Knowledge) holds:
1.  **Period $T$ (The Final Round):** Since there is no future round to punish defection, the game collapses to a one-shot game. Both players have a dominant strategy to **Defect ($D$)**.
2.  **Period $T-1$:** Knowing that defection is guaranteed in period $T$ regardless of what happens in $T-1$, there is no future punishment incentive. Thus, both players **Defect** in $T-1$.
3.  **By Induction:** The game collapses completely. The unique SPNE is to **Defect in every single round**.

---

### The Chain-Store Paradox (Lecture 51)
A monopolist has stores in $T$ sequential markets. In each market, a different competitor decides to enter or stay out. If entry occurs, the monopolist can fight (costly price war) or acquiesce.
*   By backward induction, the monopolist will acquiesce in the final round, and thus in all rounds.
*   **Paradox:** In reality, monopolists frequently fight early entries aggressively to build a "reputation for toughness" to deter future entrants. This shows that standard backward induction assumes perfect information and complete rationality in a way that doesn't capture realistic reputation dynamics.

---

## 2. Infinitely Repeated Games (Lecture 52)

When games are repeated infinitely, cooperation can be sustained. Since players do not know when the game ends, the future always matters.

### Discount Factor $\delta$
We discount future payoffs using the discount factor $\delta \in [0, 1)$, which represents the time value of money or the probability that the game continues to the next round:
$$\text{Expected Total Payoff} = \sum_{t=0}^\infty \delta^t u_t$$

---

### The Grim Trigger Strategy
In the Prisoner's Dilemma, consider the **Grim Trigger** strategy:
*   Start by playing Cooperate ($C$).
*   Cooperate as long as the opponent has cooperated.
*   If the opponent defects even once, play Defect ($D$) **forever**.

### Checking for SPNE
Let's see if Grim Trigger forms an equilibrium. Suppose both players are currently cooperating.
*   **If I Cooperate:** I receive $-1$ in every period. My expected payoff is:
    $$U_{\text{coop}} = -1 - \delta - \delta^2 - \dots = -\frac{1}{1 - \delta}$$
*   **If I Defect (deviate):** I get $0$ this period (defecting against cooperation), but my opponent will defect forever, giving me $-2$ in every future round:
    $$U_{\text{defect}} = 0 - 2\delta - 2\delta^2 - \dots = -\frac{2\delta}{1 - \delta}$$

For cooperation to be optimal, we must have $U_{\text{coop}} \ge U_{\text{defect}}$:
$$-\frac{1}{1 - \delta} \ge -\frac{2\delta}{1 - \delta} \implies 1 \le 2\delta \implies \delta \ge \frac{1}{2}$$

> **Conclusion:** Cooperation is sustainable in an infinitely repeated Prisoner's Dilemma if players are sufficiently patient ($\delta \ge 0.5$).

---

## 3. The Folk Theorem

> **Folk Theorem (Abridged):** In an infinitely repeated game, any feasible payoff vector that yields each player at least their minimax (reservation) payoff can be sustained as a Subgame Perfect Nash Equilibrium, provided players are sufficiently patient ($\delta$ is close enough to $1$).
