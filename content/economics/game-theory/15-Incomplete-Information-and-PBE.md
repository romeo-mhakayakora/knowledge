---
title: Incomplete Information and PBE
---

# Module 15: Incomplete Information and PBE (Lectures 55–58)

This module introduces **Perfect Bayesian Equilibrium (PBE)**, the standard solution concept for sequential extensive form games with incomplete information.

---

## 1. Sequential Games of Incomplete Information (Lecture 55)

When games are both sequential (extensive form) and have incomplete information, subgame perfection (SPNE) is no longer sufficient.

### The Problem
Subgame perfection requires checking equilibria in every subgame. However, in games of incomplete or imperfect information, decision nodes often belong to multi-node information sets (because players do not know what type the opponent is or what action they took).
Since a subgame cannot cut across an information set, these games have **no proper subgames** other than the entire game itself. Thus, SPNE collapses back to standard Nash equilibrium and fails to eliminate unreasonable threats.

---

## 2. Perfect Bayesian Equilibrium (PBE) Definition (Lectures 56–57)

A **Perfect Bayesian Equilibrium (PBE)** specifies a strategy profile $s^*$ and a **system of beliefs** $\mu$ (assigning a probability to each node in every information set) such that:

1.  **Sequential Rationality:** At each information set, the player's action must maximize their expected utility, given their beliefs $\mu$ and the strategies of the other players.
2.  **Consistent Beliefs (Bayes' Rule):** Whenever possible, beliefs must be updated using **Bayes' Rule**, given the equilibrium strategies:
    $$P(\text{node } x \mid \text{info set } I) = \frac{P(x \text{ is reached under } s^*)}{P(I \text{ is reached under } s^*)}$$
    *   **On-equilibrium path:** Bayes' rule is mandatory.
    *   **Off-equilibrium path:** If an information set is never reached in equilibrium ($P(I) = 0$), Bayes' rule is undefined. Any system of beliefs is mathematically permitted, but actions must still be sequentially rational given these off-equilibrium beliefs.

---

## 3. Signaling Games and the Gift Game (Lecture 58)

A classic application of PBE is a **Signaling Game**:
1.  **Sender** has a private type $\theta \in \{\theta_H, \theta_L\}$.
2.  Sender sends a message/signal $m$ (e.g. gets a college degree, gives a gift).
3.  **Receiver** observes $m$ (but not $\theta$) and chooses an action $a$.

### The Gift Game Example
*   **Sender** can be a "Friend" or "Foe".
*   **Friend** wants to give a gift. **Foe** might give a gift to deceive the Receiver.
*   **Receiver** wants to accept the gift if Sender is a Friend, and reject if they are a Foe.

### Types of PBE
Signaling games have three types of equilibria:

1.  **Pooling Equilibrium:** Senders of all types send the **same** signal. The signal carries zero information. Receiver's beliefs remain equal to their prior probabilities:
    $$\mu(\text{Friend} \mid \text{Gift}) = P(\text{Friend})$$
2.  **Separating Equilibrium:** Senders of different types send **different** signals. The signal is fully revealing. Receiver updates beliefs to certainty:
    $$\mu(\text{Friend} \mid \text{Gift}) = 1 \quad \text{and} \quad \mu(\text{Friend} \mid \text{No Gift}) = 0$$
3.  **Semi-Pooling (Hybrid) Equilibrium:** One type plays a pure strategy, while the other type randomizes (plays a mixed strategy). The signal is partially revealing.
