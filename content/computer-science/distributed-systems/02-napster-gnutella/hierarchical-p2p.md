---
title: Hierarchical Peer-to-Peer (Supernodes)
subject: distributed-systems
chapter: 02-napster-gnutella
tags:
- distributed-systems
- systems
date: '2026-06-24'
updated: '2026-06-24'
status: complete
difficulty: advanced
---

# Hierarchical Peer-to-Peer (Supernodes)

To balance the efficiency of Napster's centralized model with Gnutella's decentralized robustness, third-generation P2P networks (like FastTrack/KaZaA and Gnutella 0.6) introduced a **hierarchical architecture** utilizing **Supernodes** (or Ultrapeers).

---

## 1. Supernode System Architecture

Hierarchical networks classify peers based on resources (bandwidth, CPU, and uptime):

*   **Leaf Nodes**: Low-resource, transient client peers. Each leaf node connects to a single Supernode.
*   **Supernodes (Ultrapeers)**: High-performance, stable peers. Supernodes form an unstructured Gnutella-like network among themselves.

```mermaid
graph TD
    subgraph Supernode Overlay
        S1[Supernode 1] --- S2[Supernode 2]
        S2 --- S3[Supernode 3]
        S1 --- S3
    end
    subgraph Client Clusters
        S1 --- L1[Leaf 1]
        S1 --- L2[Leaf 2]
        S2 --- L3[Leaf 3]
        S2 --- L4[Leaf 4]
        S3 --- L5[Leaf 5]
    end
```

---

## 2. Query Routing and Execution

1.  **Registration**: A Leaf node uploads its list of shared files to its assigned Supernode. The Supernode indexes the contents of all its connected leaves.
2.  **Query Submission**: A Leaf node sends a search query directly to its Supernode.
3.  **Supernode Flood**: The Supernode processes the search against its client database. If not resolved, it floods the query only to other **Supernodes** in the overlay.
4.  **Reverse Path**: Results are returned back through the Supernode path to the requesting Leaf node.

---

## 3. Comparison of P2P Architectures

| Metric | Centralized (Napster) | Decentralized (Gnutella) | Hierarchical (KaZaA) |
| :--- | :--- | :--- | :--- |
| **Search Time** | $O(1)$ | $O(N)$ worst case | $O(S)$ where $S \ll N$ |
| **Message Overhead** | $O(1)$ | $O(d^k)$ (exponential) | Limited to Supernode network |
| **Failure Vulnerability** | Critical (Server loss) | None (Very robust) | Minimal (Leaf reassignment) |
| **State Consistency** | Highly Consistent | N/A (Dynamic query) | Local consistency at Supernodes |