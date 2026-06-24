---
title: Theoretical Bounds on Consensus
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

# Theoretical Bounds on Consensus

Distributed consensus bounds vary dramatically depending on system assumptions (synchronous vs. asynchronous, crash-stop vs. Byzantine faults).

---

## 1. Synchronous System Bounds

In a synchronous system (where message delays have a known upper bound $D$):

*   **Round Complexity**: If up to $f$ processes can crash, any deterministic consensus protocol requires at least:
    $$f + 1 \quad \text{rounds}$$
    to guarantee agreement.
*   **Fault Tolerance**:
    *   Under **Crash-Stop (Fail-Stop)** faults: Consensus is possible for any $f < N$.
    *   Under **Byzantine** faults: Consensus is possible if and only if $f < N/3$.

---

## 2. Asynchronous System Bounds

*   Under **Crash-Stop** faults: FLP Impossibility proves that deterministic consensus is impossible for $f \ge 1$.
*   **Randomized Consensus**: If protocols can toss coins (randomized steps), consensus terminates in $O(1)$ expected rounds with probability 1.