---
title: The Pastry DHT Protocol
subject: distributed-systems
chapter: 03-dhts-chord-pastry-bittorrent
tags:
- distributed-systems
- systems
date: '2026-06-24'
updated: '2026-06-24'
status: complete
difficulty: advanced
---

# The Pastry DHT Protocol

Pastry is a structured peer-to-peer overlay network designed to implement a Distributed Hash Table (DHT). Unlike Chord's ring-based numeric distance, Pastry routes messages based on **Prefix Matching** and incorporates physical network topology to optimize routing latency.

---

## 1. Identifier Space and Routing Table

Pastry identifiers (both Node IDs and Key IDs) are $128$-bit numbers, typically represented in base $2^b$ (usually $b=4$, representing hexadecimal).

### 1.1 Node State
Each Pastry node maintains three key data structures:

1.  **Routing Table**: Organized into $128/b$ rows and $2^b$ columns.
    *   Row $r$ contains contacts whose IDs match the current node's ID in the first $r$ digits, but differ at digit $r+1$.
2.  **Leaf Set ($L$)**: A set of $L$ closest nodes in the identifier space (typically $L/2$ numerically smaller, $L/2$ numerically larger). Used for final delivery.
3.  **Neighborhood Set ($M$)**: A list of $M$ nodes that are physically closest in the network (based on ping latency/RTT). Used to maintain locality.

---

## 2. Pastry Routing Algorithm

When a node receives a message with key $D$:

1.  **Check Leaf Set**: If $D$ falls within the range of the Leaf Set, forward the message directly to the node in the Leaf Set numerically closest to $D$.
2.  **Check Routing Table**: If not in the Leaf Set, find the length of the common prefix between the current node ID and $D$. Let this prefix length be $l$.
    *   Look up the routing table entry at row $l$, column $d$ (where $d$ is the $(l+1)$-th digit of $D$).
    *   If the entry exists, forward to that node.
3.  **Fallback**: If no such entry exists, forward to a node from all available sets (Routing, Leaf, Neighborhood) that matches prefix length $l$ and is numerically closer to $D$ than the current node.

> **Complexity**: Lookups complete in $O(\log_{2^b} N)$ routing steps.

---

## 3. Proximity Routing (Network Locality)

Pastry leverages the Neighborhood Set to achieve **Proximity Routing**. During routing table initialization, a joining node requests states from nearby nodes. It copies routing rows from nodes that match its prefix digits and are physically close, ensuring that each routing hop travels the minimum physical network distance possible.