---
title: Paxos vs. Raft Comparison
subject: distributed-systems
chapter: 08-paxos-raft
tags:
- distributed-systems
- systems
date: '2026-06-24'
updated: '2026-06-24'
status: complete
difficulty: advanced
---

# Paxos vs. Raft Comparison

| Feature | Paxos | Raft |
| :--- | :--- | :--- |
| **Understandability** | Low (Difficult to conceptualize) | High (Decomposed into clean states) |
| **Leader Model** | Symmetric (Any proposer can write) | Strong Leader (Only leader can replicate) |
| **Log Gaps** | Allowed (Requires filling null values) | Prohibited (Logs must remain sequential) |
| **Safety Logic** | Derived from intersection of quorums | Enforced by strict leader election rules |
| **Performance** | High (Multi-Paxos avoids Phase 1) | Equal to Multi-Paxos under normal loads |