---
title: Amazon Dynamo
subject: distributed-systems
chapter: 11-dynamo-cassandra-percolator
tags:
- distributed-systems
- systems
date: '2026-06-24'
updated: '2026-06-24'
status: complete
difficulty: advanced
---

# Amazon Dynamo

Amazon Dynamo is a highly available, masterless key-value store. It is designed to prioritize write availability over consistency (an AP system under CAP).

---

## 1. Core Architectural Pillars

Dynamo combines several distributed techniques:

*   **Consistent Hashing**: Data is distributed across a hash ring using virtual nodes.
*   **Tunable Quorums ($N, R, W$)**:
    *   $N$: Number of replicas.
    *   $R$: Number of nodes that must respond to a read.
    *   $W$: Number of nodes that must acknowledge a write.
    *   If $R+W > N$, the system guarantees read-your-writes consistency.
*   **Sloppy Quorums and Hinted Handoff**: If preferred nodes are down, writes are accepted by temporary healthy nodes which forward them once the primary recovers.
*   **Vector Clocks**: Used to detect concurrent updates and capture version branching.

---

## 2. Conflict Resolution

Because Dynamo prioritizes availability, writes can branch during partitions. When the partition heals, readers must resolve conflicts. Dynamo uses **vector clocks** to detect these conflicts, forcing the application client to merge divergent branches.