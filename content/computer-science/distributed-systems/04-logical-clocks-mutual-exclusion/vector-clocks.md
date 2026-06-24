---
title: Vector Clocks and Causality
subject: distributed-systems
chapter: 04-logical-clocks-mutual-exclusion
tags:
- distributed-systems
- systems
date: '2026-06-24'
updated: '2026-06-24'
status: complete
difficulty: advanced
---

# Vector Clocks and Causality

While Lamport clocks generate a total order, they cannot detect concurrent events. If $L(a) < L(b)$, we cannot distinguish whether $a \to b$ or if they are concurrent ($a \parallel b$). **Vector Clocks** overcome this limitation, allowing processes to detect causal violations and concurrent updates.

---

## 1. Vector Clock Update Rules

For a system of $N$ processes, each process $P_i$ maintains an integer array $V_i$ of size $N$ (initialized to all zeros).

*   **Rule 1 (Local Event)**: Before executing a local event, process $P_i$ increments its own component:
    $$V_i[i] \gets V_i[i] + 1$$
*   **Rule 2 (Message Passing)**:
    *   When process $P_i$ sends a message $m$, it attaches its vector: $(m, V_i)$.
    *   Upon receiving $(m, V_{msg})$, process $P_j$ merges the vectors element-wise, increments its own component, and records the receipt:
        $$\forall k \in [1, N], \quad V_j[k] \gets \max(V_j[k], V_{msg}[k])$$
        $$V_j[j] \gets V_j[j] + 1$$

---

## 2. Comparing Vector Timestamps

A vector timestamp $V(a)$ causally precedes $V(b)$ if and only if every element in $V(a)$ is less than or equal to the corresponding element in $V(b)$, and at least one element is strictly smaller:

$$V(a) \le V(b) \iff \forall k \in [1, N], \ V(a)[k] \le V(b)[k]$$
$$V(a) < V(b) \iff V(a) \le V(b) \quad \text{and} \quad \exists k \ \text{s.t.} \ V(a)[k] < V(b)[k]$$

### 2.1 Causal Equivalence
Using vector clocks, the logical order matches the causal order exactly:

$$a \to b \iff V(a) < V(b)$$

### 2.2 Concurrency Detection
If neither $V(a) \le V(b)$ nor $V(b) \le V(a)$, then the events are **concurrent**:

$$a \parallel b \iff \neg(V(a) \le V(b)) \ \wedge \ \neg(V(b) \le V(a))$$

This property is crucial for detecting conflicts in distributed replication systems (such as Amazon Dynamo).