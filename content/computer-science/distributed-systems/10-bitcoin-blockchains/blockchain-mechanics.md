---
title: Blockchain Data Structures
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

# Blockchain Data Structures

A blockchain organizes transactions into a tamper-evident linked list using cryptographic hashes.

---

## 1. Merkle Trees

Transactions inside a block are organized into a **Merkle Tree** (a binary hash tree).

```mermaid
graph TD
    Root[Merkle Root] --> H12[Hash 1-2]
    Root --> H34[Hash 3-4]
    H12 --> H1[Hash 1]
    H12 --> H2[Hash 2]
    H34 --> H3[Hash 3]
    H34 --> H4[Hash 4]
```

*   **Benefit**: Allows lightweight clients to verify if a transaction is included in a block using only $O(\log N)$ hash proofs (the Merkle Path).

---

## 2. UTXO Model

Bitcoin uses the **Unspent Transaction Output (UTXO)** model:
*   Transactions do not update account balances. Instead, they consume existing UTXOs (inputs) and create new UTXOs (outputs).
*   **Verification**: A transaction is valid if the inputs are currently unspent and are signed by the rightful owner.