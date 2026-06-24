---
title: Facebook Cassandra
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

# Facebook Cassandra

Cassandra is a wide-column distributed database that combines the distributed systems features of Amazon Dynamo (gossip, consistent hashing, masterless) with the data model of Google Bigtable.

---

## 1. Storage Engine (LSM Trees)

Cassandra avoids random disk I/O by utilizing **Log-Structured Merge (LSM) Trees**:

1.  **Memtable**: Incoming writes are appended to a commit log (for durability) and written to an in-memory buffer called a Memtable.
2.  **SSTable (Sorted String Table)**: When the Memtable is full, it is flushed to disk as an immutable SSTable, sorted by key.
3.  **Compaction**: Background threads merge immutable SSTables, removing deleted items and duplicate updates.

---

## 2. Tunable Consistency

Like Dynamo, Cassandra allows clients to specify the consistency level on a per-request basis:
*   `ANY`: Write succeeds if written to at least one node (even a hinted handoff).
*   `ONE`: Write/read must acknowledge from at least one replica.
*   `QUORUM`: Requires majority agreement ($N/2 + 1$).