---
title: Evolutionary Game Theory
---

# Module 12: Evolutionary Game Theory (Lectures 45–48)

This module introduces **Evolutionary Game Theory (EGT)**, which replaces the classical assumption of rational players with evolutionary selection pressures in biological populations.

---

## 1. The Hawk-Dove Game (Lecture 45)

The **Hawk-Dove Game** models animal conflicts over resources. Two individuals compete for a resource of value $V$. They can choose one of two behaviors:
*   **Hawk ($H$):** Fight aggressively until injured or the opponent retreats.
*   **Dove ($D$):** Display peacefully and retreat if attacked.

If two Hawks fight, the loser suffers an injury cost $C$. Assume $V < C$.

| Player 1 \ Player 2 | Hawk ($H$) | Dove ($D$) |
| :--- | :---: | :---: |
| **Hawk ($H$)** | $\left(\frac{V - C}{2}, \ \frac{V - C}{2}\right)$ | $(V, \ 0)$ |
| **Dove ($D$)** | $(0, \ V)$ | $\left(\frac{V}{2}, \ \frac{V}{2}\right)$ |

### Nash Equilibria (Rational Analysis)
Since $V < C$, the term $\frac{V-C}{2}$ is negative.
*   Pure Strategy Nash Equilibria: $(H, D)$ and $(D, H)$.
*   Mixed Strategy Nash Equilibrium: A combination of Hawk and Dove behavior.

---

## 2. Evolutionary Game Theory Concepts (Lecture 46)

EGT shifts the vocabulary from classical game theory:
*   **Players $\to$ Members of a Population:** Agents drawn from a large population.
*   **Strategies $\to$ Phenotypes (Behaviors):** Inherited traits that determine behavior in interactions.
*   **Utility $\to$ Fitness (Reproductive Success):** Payoffs represent the change in expected offspring.
*   **Dynamics $\to$ Replicator Dynamics:** Phenotypes with higher-than-average fitness grow in population share.

---

## 3. Evolutionary Stable Strategy (ESS) (Lectures 47–48)

An **Evolutionary Stable Strategy (ESS)** is a strategy which, if adopted by a whole population, cannot be invaded by a small, mutant strategy group.

Let $E(s, s')$ represent the payoff (fitness) of strategy $s$ playing against $s'$.
Suppose a population plays strategy $p$. A small fraction $\epsilon$ of mutants playing strategy $q$ enters the population.
The expected fitness of the resident strategy $p$ is:
$$F(p) = (1-\epsilon)E(p, p) + \epsilon E(p, q)$$
The expected fitness of the mutant strategy $q$ is:
$$F(q) = (1-\epsilon)E(q, p) + \epsilon E(q, q)$$

For $p$ to be an ESS, it must outperform the mutant strategy $q$ for sufficiently small $\epsilon$:
$$F(p) > F(q)$$

### The Formal ESS Conditions
By taking the limit as $\epsilon \to 0$, $p$ is an ESS if and only if for every mutant strategy $q \ne p$:

1.  **Nash Equilibrium Condition:**
    $$E(p, p) \ge E(q, p)$$
2.  **Stability Condition (if $E(p,p) = E(q,p)$):**
    $$E(p, q) > E(q, q)$$

> **Relation to Nash Equilibrium:** Every ESS is a Nash Equilibrium, but not every Nash Equilibrium is an ESS. ESS is a strict refinement of Nash Equilibrium.

---

## 4. Beetles' World Example (Lecture 47)

Suppose a population of beetles consists of two sizes: Large and Small.
*   Large beetles win resources but have high energy maintenance costs.
*   Small beetles gather food efficiently with low costs but retreat in direct fights.
By modeling payoffs in terms of food acquired minus calorie expenditure, we solve for whether a purely "Large" population or a purely "Small" population is an ESS, illustrating how ecological constraints drive physical evolution.
