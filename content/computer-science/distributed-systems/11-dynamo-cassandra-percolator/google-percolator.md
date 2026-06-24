---
title: Google Percolator
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

# Google Percolator

Google Percolator provides distributed transactions with snapshot isolation over Google Bigtable. It is used to build the Google search index incrementally.

---

## 1. Two-Phase Commit (2PC) with Locks

Percolator implements a decentralized two-phase commit protocol using a centralized **Timestamp Oracle (TSO)** to provide strictly ordered transaction times.

### 1.1 Prewrite Phase
1.  Select one cell as the **Primary Lock**.
2.  Write data and locks to all participant cells (referencing the primary lock).
3.  If any lock conflict is detected, abort.

### 1.2 Commit Phase
1.  Request a commit timestamp from the TSO.
2.  Commit the Primary Lock.
3.  Once the primary is committed, asynchronously roll out commits to secondary cells.

---

## 2. Isolation Guarantees

Percolator guarantees **Snapshot Isolation (SI)**. Readers use a start timestamp from the TSO to read only committed data that was written before their transaction started, ignoring uncommitted locks.