---
title: Discussion and Questions
---

# Discussion and Questions

This page compiles the core conceptual questions, insights, and structural clarifications raised during the study of Markov Chains.

---

## 🙋 Conceptual Questions & Answers

### Q1: If the stationary distribution $s$ is not changing, why are we multiplying it by the transition matrix $Q$ in the equation $sQ = s$?

**Answer:** 
Multiplying a distribution vector by $Q$ is the mathematical equivalent of pressing the **"Play"** button on time to advance the system by one step. We must press "Play" to *prove* that the system is immune to it. 
- For any random starting distribution (e.g., $[0.90, 0.10]$), pressing Play changes the distribution (e.g., to $[0.85, 0.15]$). It is not stationary.
- For the stationary distribution (e.g., $[0.60, 0.40]$), pressing Play yields the exact same distribution $[0.60, 0.40]$. 

The equation $sQ = s$ proves we have found the unique balance where the incoming flows to each state perfectly cancel out the outgoing flows.

---

### Q2: Is the stationary distribution $s$ the probability distribution after $n$ steps?

**Answer:** 
No. The distribution after $n$ steps is given by $tQ^n$ (which depends on the initial spawn vector $t$ and varies with each step $n$). 

The stationary distribution $s$ is the **infinite-step limit** ($\lim_{n\to\infty} tQ^n$). It is the final, locked-in equilibrium that the system converges to as $n$ approaches infinity, regardless of where it started.

---

### Q3: Why doesn't each starting state get its own stationary distribution $s$?

**Answer:** 
In the short term ($Q^2$ or $Q^{10}$), your starting state matters, so each row of the matrix is different. 

At infinity, the system develops **total mathematical amnesia**. The chain has been shuffling around for so long that all traces of the starting state are completely erased. Therefore, $Q^\infty$ collapses into a matrix where every single row is identical to the universal vector $s$. 

*(Note: This holds true for **irreducible** chains. If the chain is **reducible**—i.e., has disconnected islands—the rows of $Q^\infty$ cannot be identical, and a single universal stationary distribution does not exist. See **[[11.3.6-Convergence]]** for details).*

---

### Q4: To find the long-run distribution, do we evolve the row vector step-by-step ($t \to tQ \to tQ^2 \to \ldots$) or evolve the matrix $Q$ first ($Q \to Q^n \to Q^\infty$)?

**Answer:** 
Both methods yield the exact same mathematical result. This is due to the **associative property** of matrix multiplication:

$$\left( (t \times Q) \times Q \right) \times Q = t \times (Q \times Q \times Q)$$

- Evolving the row step-by-step is a real-time simulation.
- Evolving the matrix first is like building a time machine ($Q^n$) and teleporting directly to the destination.

---

### Q5: Is the marginal distribution $s$ "short-sighted" compared to the conditional probabilities in $Q$?

**Answer:** 
Actually, the exact opposite is true:
- **Conditional probabilities ($Q$):** Zoomed in and short-sighted. They only look at the immediate next step, given where the system is *right now* ($P(X_{n+1} \mid X_n)$).
- **Marginal distribution ($s$):** Zoomed out and far-sighted. It represents the infinite, long-run average of the entire system across eternity.

---

### Q6: If a chain is recurrent, shouldn't the expected amount of time spent in each state be equal?

**Answer:** 
No. While the chain will visit every recurrent state infinitely many times, it does not visit them with equal frequency. 
- States that are easy to enter but hard to leave will pool more of the "crowd" and have a higher $s_j$.
- Equal time across states ($s_j = 1/M$ for all $j$) only occurs if the transition matrix is **doubly stochastic** (both rows and columns sum to 1.0), which represents a perfectly symmetric system.

---

### Q7: How does the Policy Gradient objective in Reinforcement Learning connect to these concepts?

**Answer:** 
The RL objective function $J(\theta) = \sum_{s_0} p(s_0) \cdot V^{\pi_\theta}(s_0)$ is structurally identical to the Law of Total Probability $P(X_n = j) = \sum_i t_i q_{ij}^{(n)}$. 
- The spawn probability $p(s_0)$ maps to the initial vector $t_i$.
- The value function $V^{\pi}(s_0)$ (sum of expected future rewards) maps to the transition probabilities $q_{ij}^{(n)}$ weighted by state rewards.
- The Bellman Equation is a recursive form of the Chapman-Kolmogorov equations.
