---
title: The FLP Impossibility Proof
subject: distributed-systems
chapter: 06-dmst-flp
tags:
- distributed-systems
- systems
date: '2026-06-24'
updated: '2026-06-24'
status: complete
difficulty: advanced
---

# The FLP Impossibility Proof

The **FLP Impossibility Result** (published by Fischer, Lynch, and Paterson in 1985) is one of the most critical theorems in distributed computing. It establishes the absolute theoretical boundaries of consensus protocols in asynchronous networks.

---

## 1. The Impossibility Theorem

> **Theorem**: In an asynchronous network, no deterministic consensus protocol can guarantee both Safety and Liveness in the presence of even a single unannounced process crash.

*   **Safety (Agreement)**: No two processes decide on different values.
*   **Liveness (Termination)**: All non-faulty processes eventually decide.

---

## 2. Proof Architecture: Bivalence and Configurations

The proof uses graph-theoretic configurations of the distributed system:

### 2.1 System Configurations
A **Configuration** $C$ represents the global state of the system (states of all processes and messages currently in transit).

*   **Univalent**: A configuration is univalent if the decision value is locked.
    *   **0-valent**: All possible execution paths from $C$ lead to a decision of $0$.
    *   **1-valent**: All possible execution paths from $C$ lead to a decision of $1$.
*   **Bivalent**: The decision is not yet determined. From $C$, some execution paths lead to a decision of $0$, while others lead to $1$.

### 2.2 Proof Steps
1.  **Lemma 1 (Bivalent Initial State)**: There exists an initial configuration $C_0$ that is bivalent (depends on the starting inputs).
2.  **Lemma 2 (Preserving Bivalence)**: From any bivalent configuration $C$, there exists a step (a message delivery) that keeps the system in a bivalent state.
3.  **Infinite Loop**: Since the system is asynchronous, an adversarial scheduler can delay messages such that the system transitions from bivalent state to bivalent state infinitely, preventing termination.

---

## 3. Circumventing FLP in Practice

To build real-world systems, we must relax the asynchronous consensus assumptions:
*   **Partial Synchrony**: Assume boundaries on message delays (used by Paxos, Raft).
*   **Randomization**: Use probabilistic consensus (used in blockchains).
*   **Failure Detectors**: Use partially accurate oracle failure detectors (e.g., Chandra-Toueg).