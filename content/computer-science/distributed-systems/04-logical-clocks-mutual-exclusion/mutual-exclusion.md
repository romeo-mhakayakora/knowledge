---
title: Distributed Mutual Exclusion Algorithms
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

# Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion ensures that multiple processes executing in a network can coordinate access to a shared resource (the **Critical Section** or CS) without conflicts.

---

## 1. Classifications of Mutex Algorithms

1.  **Permission-Based**: A process must request permission from a set of coordinator/peer nodes before entering the CS.
2.  **Token-Based**: A single virtual "token" circulates through the network. The process holding the token has the exclusive right to enter the CS.

---

## 2. Core Mutual Exclusion Algorithms

### 2.1 Lamport's Permission-Based Algorithm
*   **Mechanism**: Uses Lamport logical clocks. A process broadcasts a request with its timestamp. Peers place requests in local priority queues and reply. A process enters the CS when its request is at the head of its queue and it has received acknowledgments with larger timestamps from all peers.
*   **Message Complexity**: $3(N-1)$ messages per CS entry (Request, Reply, Release).

### 2.2 Ricart-Agrawala Algorithm
*   An optimization of Lamport's algorithm. Instead of sending explicit Release messages, processes defer replying to requests with timestamps smaller than their own pending request.
*   **Message Complexity**: $2(N-1)$ messages per CS entry.

### 2.3 Maekawa's Quorum Algorithm
*   Processes do not request permission from all peers. Instead, they request permission from a subset of processes called a **Quorum** ($S_i$).
*   **Rules**:
    *   Intersection: $\forall i, j, \ S_i \cap S_j \ne \emptyset$ (any two quorums must overlap by at least one node).
    *   Symmetry: $|S_i| = K \approx \sqrt{N}$.
*   **Message Complexity**: $3\sqrt{N}$ messages per CS entry.

---

## 3. Comparison Summary

| Algorithm | Message Complexity | Synchronization Delay | Single Point of Failure |
| :--- | :--- | :--- | :--- |
| **Centralized** | $3$ | $2$ | Yes (Coordinator) |
| **Ricart-Agrawala** | $2(N-1)$ | $1$ round-trip | Yes (Any node crash) |
| **Maekawa** | $3\sqrt{N}$ | $2$ | Yes (Quorum node crash) |
| **Token Ring** | $0$ to $N$ | $N/2$ average | Yes (Token loss) |