---
title: Subgame Perfect Equilibrium
---

# Module 08: Subgame Perfect Equilibrium (Lectures 27–31)

This module explains **Subgame Perfect Nash Equilibrium (SPNE)** and **Backward Induction**, solution refinements designed to eliminate equilibria that rely on non-credible threats in sequential games.

---

## 1. Subgames and SPNE Definition (Lecture 27)

A **subgame** is a subset of an extensive form game that:

1.  Begins at a single decision node (that is in a singleton information set).
2.  Contains all successors of that node.
3.  Does not contain any nodes that belong to an information set starting outside the subgame.

### Subgame Perfect Nash Equilibrium (SPNE)
A strategy profile $s^*$ is a **Subgame Perfect Nash Equilibrium (SPNE)** if it induces a Nash Equilibrium in **every** subgame of the original game (including the game itself).

---

## 2. Backward Induction (Lectures 27–29)

For finite games of perfect information, SPNE is solved using **backward induction**:

1.  Find the optimal actions for players at the terminal decision nodes (at the very bottom/end of the tree).
2.  Replace those nodes with the resulting equilibrium payoff vectors.
3.  Move one step backward up the tree and repeat the process until the root node is reached.

### Eliminating Non-Credible Threats
Recall the sequential Entry Game:
*   Normal form Nash Equilibria: **(Enter, Acquiesce)** and **(Stay Out, Fight)**.

Let's test **(Stay Out, Fight)** using backward induction:
*   If the Entrant actually plays **Enter**, the Incumbent faces a choice:
    *   Fight: payoff $-1$
    *   Acquiesce: payoff $1$
*   Since $1 > -1$, a rational Incumbent will play **Acquiesce**.
*   Therefore, the threat of "Fight" is **non-credible**.
*   The only subgame perfect equilibrium is **(Enter, Acquiesce)**.

---

## 3. The Ultimatum Game (Lecture 30)

The **Ultimatum Game** is a classic sequential game showing the contrast between game-theoretic predictions and human behavior.

### Game Structure
*   **Player 1 (Proposer)** is given a sum of money $V$ (say $100) and proposes a split $x \in [0, V]$ to Player 2.
*   **Player 2 (Responder)** can either **Accept** or **Reject** the offer.
*   If Responder accepts, they get $x$ and Proposer gets $V - x$.
*   If Responder rejects, both players get $0$.

### SPNE Analysis (Backward Induction)
1.  **Responder's Decision:**
    If Proposer offers $x > 0$:
    *   Accept yields $x$.
    *   Reject yields $0$.
    *   Since $x > 0$, Responder should always accept.
    *   If $x = 0$, Responder is indifferent between Accept and Reject.
2.  **Proposer's Decision:**
    Knowing Responder will accept any $x > 0$, Proposer offers the smallest possible unit of money $\epsilon > 0$ (e.g. $1) and keeps $V - \epsilon$ ($99).
3.  **Unique SPNE:** Proposer offers $\epsilon$ (or $0$), and Responder accepts all offers $\ge \epsilon$.

### Behavioral Contrast
In experimental settings, human Responders frequently reject unfair offers (splits below 30%) due to reciprocity and fairness concerns, and Proposers usually offer around 40-50% splits to avoid rejection. This highlights the limits of assuming pure self-interest.
