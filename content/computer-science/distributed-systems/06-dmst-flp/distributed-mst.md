---
title: Distributed Minimum Spanning Tree (GHS)
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

# Distributed Minimum Spanning Tree (GHS)

The Gallager-Humblet-Spira (GHS) algorithm is a classic distributed protocol for finding a Minimum Spanning Tree (MST) in an arbitrary connected network. It allows decentralized nodes to find the optimal network routing backbone using localized message passing.

---

## 1. GHS Core Concepts and States

Nodes start as single-node tree **fragments**. Fragments merge iteratively by finding their **Minimum Weight Outgoing Edge (MWOE)**.

*   **Edge States**:
    *   `Basic`: Unexplored edges.
    *   `Branch`: Edges selected to be part of the MST.
    *   `Rejected`: Edges confirmed to connect nodes within the same fragment (creating cycles).
*   **Levels**: Each fragment has a Level $L$ (initially 0).

---

## 2. Fragment Merging Rules

When two fragments $F_1$ and $F_2$ identify a common MWOE, they merge based on their levels:

### 2.1 Merge ($L_1 < L_2$)
If fragment $F_1$ has a lower level than $F_2$, $F_1$ merges into $F_2$. $F_1$ updates its level to $L_2$.

### 2.2 Friendly Merge ($L_1 = L_2$)
If levels are equal, the fragments merge and form a new fragment at level $L+1$. The shared MWOE becomes a `Branch` edge, and the node with the higher ID becomes the leader of the new fragment.

---

## 3. Complexity

*   **Message Complexity**: Finding MWOE requires $O(E + N \log N)$ messages.
*   **Time Complexity**: Runs in $O(N \log N)$ time.