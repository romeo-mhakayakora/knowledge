---
title: Start Here
---

# Chapter 12: Markov Chains

Welcome to the **Markov Chains** module. This chapter corresponds to **Chapter 11** of *Introduction to Probability* by Blitzstein & Hwang. 

A **Markov Chain** is a mathematical model for a sequence of random variables where the future depends only on the present state, not on the path taken to get there. It represents the perfect middle ground in probability modeling: it adds memory to a process without making computations intractable.

---

## 🗺️ Topic Map

Explore the chapter through the following modular notes:

| Topic | Description | Key Math / Concepts |
| :--- | :--- | :--- |
| **[[11.1-Markov-Property]]** | Foundations & Transition Matrix | $P(X_{n+1} \mid X_n, \ldots, X_0) = P(X_{n+1} \mid X_n)$, transition matrix $Q$, Chapman-Kolmogorov equations. |
| **[[11.1.6-Marginal-Distributions]]** | Evolving Distributions over Time | Spawn vector $t$, Law of Total Probability (LOTP) expansions, Proposition 11.1.6 ($tQ^n$). |
| **[[11.2-State-Classification]]** | Topology of State Spaces | Recurrent vs. Transient states, Geometric visits, Proposition 11.2.4 (Finite & Irreducible). |
| **[[11.2.8-Periodicity]]** | Rhythms of Return | Period $d(i) = \gcd\{n \ge 1: q_{ii}^{(n)} > 0\}$, Periodic vs. Aperiodic states, self-loop rule. |
| **[[11.3-Stationary-Distributions]]** | Long-Term Equilibrium | Definition of $\pi Q = \pi$, Dynamic Equilibrium (Water Fountain & City Apartment analogies). |
| **[[11.3.5-Existence-Uniqueness]]** | Solving for Equilibrium | Left Eigenvectors, flow balance equations ($as_1 = bs_2$), universal 2-state matrix shortcut. |
| **[[11.3.6-Convergence]]** | Convergence & Amnesia | $Q^\infty$ behavior, mathematical amnesia, reducible chain edge cases. |
| **[[Examples]]** | Worked Examples & Applications | Worked 2-step paths, Gambler's Ruin, Coupon Collector, Queueing Theory, and Reinforcement Learning connections. |
| **[[Questions]]** | Discussion & Inquiries | Focus questions and clarifications. |
| **[[Cheat-Sheet]]** | Reference Guide | Quick-lookup summary grids for definitions and properties. |

---

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:
1. **Apply the Markov Property** to model step-by-step processes and explain why the present state acts as an informational bottleneck.
2. **Compute $n$-step transition probabilities** using matrix multiplication ($Q^n$) and Chapman-Kolmogorov summations.
3. **Analyze marginal distributions** ($tQ^n$) given starting spawn vectors.
4. **Classify states** as recurrent or transient, and determine the period of a state using Greatest Common Divisors (GCD).
5. **Solve for the stationary distribution** ($\pi Q = \pi$) using flow balance and left eigenvector methods.
6. **Understand long-term convergence** and visual connections to Reinforcement Learning (value functions, Bellman equations).
