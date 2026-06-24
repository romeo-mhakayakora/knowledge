---
title: The LeLann-Chang-Roberts (LCR) Bound
subject: distributed-systems
chapter: 05-distributed-leader-election
tags:
- distributed-systems
- systems
date: '2026-06-24'
updated: '2026-06-24'
status: complete
difficulty: advanced
---

# The LeLann-Chang-Roberts (LCR) Bound

The LCR (LeLann-Chang-Roberts) algorithm is a classic comparison-based leader election algorithm for synchronous rings. It serves as a benchmark for analyzing the theoretical limits of distributed message complexity.

---

## 1. Algorithm Description

LCR operates in synchronous rounds on a unidirectional ring of size $N$:

*   In each round, every active node $i$ sends its ID (as a message) to its successor.
*   Upon receiving an ID $j$:
    *   If $j > i$: Node $i$ forwards $j$ to its successor.
    *   If $j < i$: Node $i$ discards the message.
    *   If $j = i$: Node $i$ has received its own ID. It declares itself leader and sends a termination message.

---

## 2. Theoretical Lower Bounds

LCR is highly simple but provides key proofs for distributed algorithm bounds:

*   **Message Complexity**: $O(N \log N)$ on average, and $O(N^2)$ in the worst case (when IDs are in decreasing order around the ring).
*   **Lower Bound Proof**: It is proven that for *comparison-based* election on a synchronous ring where node count $N$ is unknown, any algorithm must send at least:
    $$\Omega(N \log N) \quad \text{messages}$$
    Thus, LCR is asymptotically optimal in message complexity for comparison-based algorithms.