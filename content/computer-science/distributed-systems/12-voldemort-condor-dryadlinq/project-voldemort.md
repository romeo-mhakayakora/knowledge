---
title: Project Voldemort (LinkedIn)
subject: distributed-systems
chapter: 12-voldemort-condor-dryadlinq
tags:
- distributed-systems
- systems
date: '2026-06-24'
updated: '2026-06-24'
status: complete
difficulty: advanced
---

# Project Voldemort (LinkedIn)

Project Voldemort is LinkedIn's distributed key-value storage system, heavily inspired by the Amazon Dynamo paper.

---

## 1. Routing Architectures

Voldemort supports two routing strategies:

*   **Client-Side Routing**: The client maintains the partition map and routes requests directly to the correct storage nodes. This minimizes hop latency but increases client complexity.
*   **Server-Side Routing**: Clients send requests to a random node, which forwards it to the correct partition coordinator.

---

## 2. Comparison with Amazon Dynamo

While Voldemort mirrors Dynamo's architecture (consistent hashing, vector clocks, tunable quorums), it differs by focusing on modular storage engines (pluggable BDB, MySQL, or Read-Only storage) and separating the storage layer from the routing layer for easier maintenance.