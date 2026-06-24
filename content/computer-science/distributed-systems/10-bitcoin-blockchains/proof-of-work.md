---
title: Nakamoto Consensus and Proof of Work
subject: distributed-systems
chapter: 10-bitcoin-blockchains
tags:
- distributed-systems
- systems
date: '2026-06-24'
updated: '2026-06-24'
status: complete
difficulty: advanced
---

# Nakamoto Consensus and Proof of Work

Bitcoin introduced **Nakamoto Consensus**, a breakthrough in distributed systems that solves Byzantine consensus at global scale without relying on a fixed, known set of validators.

---

## 1. Proof of Work (PoW) Mechanism

To prevent Sybil attacks (where a malicious actor creates millions of virtual nodes to dominate votes), voting power is tied to physical computation.

*   **The Cryptographic Puzzle**: Nodes (miners) must find a nonce value such that the hash of the block header is less than a target value $T$:
    $$\text{SHA256}(\text{SHA256}(\text{BlockHeader})) < T$$
*   **Difficulty Adjustment**: Every 2016 blocks, the target $T$ is adjusted based on hash rate to keep block generation times stable (approximately 10 minutes).

---

## 2. Nakamoto Routing Rules

*   **Longest-Chain Rule**: Nodes always accept and build on the chain with the most accumulated Proof of Work (the longest valid chain).
*   **Double-Spend Protection**: If two blocks are mined simultaneously, a fork occurs. The fork is resolved when miners build on one of the branches, making it longer. The other branch is orphaned.