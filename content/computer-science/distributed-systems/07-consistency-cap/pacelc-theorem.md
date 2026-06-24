---
title: The PACELC Theorem Extension
subject: distributed-systems
chapter: 07-consistency-cap
tags:
- distributed-systems
- systems
date: '2026-06-24'
updated: '2026-06-24'
status: complete
difficulty: advanced
---

# The PACELC Theorem Extension

While the CAP theorem describes system behavior during partitions, systems spend most of their time operating normally. Daniel Abadi formulated the **PACELC Theorem** in 2012 to describe the trade-offs during normal operations.

---

## 1. PACELC Formulation

The theorem states:

$$\text{If there is a } \mathbf{P} \text{artition, trade off } \mathbf{A} \text{vailability vs. } \mathbf{C} \text{onsistency};$$
$$\text{E} \text{lse, trade off } \mathbf{L} \text{atency vs. } \mathbf{C} \text{onsistency}.$$

---

## 2. Trade-off Analysis

Even when there are no network faults, a database must make a choice:

*   **PC/EC**: High consistency during partitions, high consistency during normal operations (e.g., Spanner).
*   **PA/EL**: High availability during partitions, low latency during normal operations (e.g., Dynamo, Cassandra). Writes return immediately without waiting for replicas to acknowledge.