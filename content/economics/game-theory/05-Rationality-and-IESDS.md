---
title: Rationality and IESDS
---

# Module 05: Rationality and IESDS (Lectures 17–18)

This module examines the assumptions of rationality and common knowledge in game theory, and details the **Iterated Elimination of Dominated Strategies (IESDS)** solution method.

---

## 1. Assumptions: Rationality and Common Knowledge (Lecture 17)

To solve games, game theory relies on two core assumptions:

1.  **Rationality:** Each player is an expected-utility maximizer. Given their beliefs, they will choose the strategy that maximizes their expected payoff.
2.  **Common Knowledge:** A fact $X$ is common knowledge if:
    *   Everyone knows $X$.
    *   Everyone knows that everyone knows $X$.
    *   Everyone knows that everyone knows that everyone knows $X$ (ad infinitum).

In game theory, **Rationality is Common Knowledge (RCK)**. This means:
*   I am rational.
*   I know you are rational.
*   You know I know you are rational.
*   This mutual expectation allows us to reason about each other's decisions.

---

## 2. Iterated Elimination of Dominated Strategies (IESDS) (Lecture 18)

Since rational players will never choose strictly dominated strategies, we can systematically simplify games by deleting dominated options.

### IESDS Step-by-Step Example
Consider the following 3x3 normal form game:

| Player 1 \ Player 2 | Left ($L$) | Center ($C$) | Right ($R$) |
| :--- | :---: | :---: | :---: |
| **Top ($T$)** | $(4, 3)$ | $(2, 7)$ | $(0, 4)$ |
| **Middle ($M$)** | $(5, 5)$ | $(5, -1)$ | $(1, 2)$ |
| **Bottom ($B$)** | $(3, 2)$ | $(2, 1)$ | $(0, 2)$ |

#### Step 1: Eliminate strictly dominated strategies for Player 1
Compare Player 1's strategies:
*   Comparing $M$ and $B$:
    *   Against $L$: $u_1(M,L) = 5 > 3 = u_1(B,L)$
    *   Against $C$: $u_1(M,C) = 5 > 2 = u_1(B,C)$
    *   Against $R$: $u_1(M,R) = 1 > 0 = u_1(B,R)$
*   Therefore, Bottom ($B$) is **strictly dominated** by Middle ($M$). We eliminate row $B$.

The reduced matrix is:

| Player 1 \ Player 2 | Left ($L$) | Center ($C$) | Right ($R$) |
| :--- | :---: | :---: | :---: |
| **Top ($T$)** | $(4, 3)$ | $(2, 7)$ | $(0, 4)$ |
| **Middle ($M$)** | $(5, 5)$ | $(5, -1)$ | $(1, 2)$ |

#### Step 2: Eliminate strictly dominated strategies for Player 2
Now, looking only at the remaining rows $\{T, M\}$, analyze Player 2's options:
*   Compare $L$ and $R$:
    *   Against $T$: $u_2(T,L) = 3 < 4 = u_2(T,R)$
    *   Against $M$: $u_2(M,L) = 5 > 2 = u_2(M,R)$
    *   No dominance here.
*   Compare $C$ and $R$:
    *   Against $T$: $u_2(T,C) = 7 > 4 = u_2(T,R)$
    *   Against $M$: $u_2(M,C) = -1 < 2 = u_2(M,R)$
    *   No dominance here.
*   Compare $L$ and $C$:
    *   Wait, is $R$ dominated?
    *   Let's check if $R$ is dominated by $L$ or $C$. No.
    *   Let's compare $L$ and $C$ again:
        *   Against $T$: $u_2(T,C) = 7 > 3 = u_2(T,L)$
        *   Against $M$: $u_2(M,C) = -1 < 5 = u_2(M,L)$
    *   Let's check if $R$ is dominated. Look at $R$: payoffs are $(4, 2)$. Look at $L$: payoffs are $(3, 5)$. Look at $C$: payoffs are $(7, -1)$.
    *   Wait, what if Player 2 randomizes? Or does a pure strategy dominate another?
    *   Let's check: $u_2(T, L) = 3$ and $u_2(M, L) = 5$. $u_2(T, R) = 4$ and $u_2(M, R) = 2$.
    *   Wait, let's look at $R$ vs. a mixture of $L$ and $C$.
    *   Let's check if $R$ is dominated by $L$:
        *   Against $T$: $u_2(T, L) = 3 < u_2(T, R) = 4$ (No)
    *   Let's look at the remaining choices. If we cannot find strict dominance in pure strategies, let's re-examine:
        *   For Player 2: $R$ vs $L$. Against $T$: $4 > 3$. Against $M$: $2 < 5$.
        *   What about $C$? Against $T$: $u_2(T, C) = 7$. Against $M$: $u_2(M, C) = -1$.
        *   Wait, is $C$ strictly dominated by a mix? No, because $7$ is the maximum.
        *   Wait! Let's compare $L$ and $R$. Against $M$, $L$ is better ($5 > 2$). Against $T$, $R$ is better ($4 > 3$).
        *   Let's check if we can eliminate anything else.
        *   Ah! Let's check if $T$ is dominated. For Player 1, compare $T$ and $M$ in the reduced matrix:
            *   Against $L$: $u_1(T,L) = 4 < 5 = u_1(M,L)$
            *   Against $C$: $u_1(T,C) = 2 < 5 = u_1(M,C)$
            *   Against $R$: $u_1(T,R) = 0 < 1 = u_1(M,R)$
        *   Yes! $T$ is strictly dominated by $M$! We eliminate $T$.

The reduced matrix is now a single row:

| Player 1 \ Player 2 | Left ($L$) | Center ($C$) | Right ($R$) |
| :--- | :---: | :---: | :---: |
| **Middle ($M$)** | $(5, 5)$ | $(5, -1)$ | $(1, 2)$ |

#### Step 3: Player 2 maximizes given Row M
Since Player 1 will definitely play $M$:
*   Player 2 compares $u_2(M,L) = 5$, $u_2(M,C) = -1$, and $u_2(M,R) = 2$.
*   Since $5$ is the highest payoff, Player 2 chooses $L$.

The unique IESDS equilibrium is:
$$(M, L) \quad \text{yielding payoffs } (5, 5)$$
