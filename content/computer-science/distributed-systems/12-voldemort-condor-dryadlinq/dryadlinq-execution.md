---
title: Microsoft DryadLINQ
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

# Microsoft DryadLINQ

Microsoft DryadLINQ is a compiler-integrated system for executing data-parallel programs over distributed clusters. It translates sequential .NET queries into distributed execution graphs.

---

## 1. Programming Model (LINQ)

Developers write standard sequential queries using LINQ (Language Integrated Query) operators (such as `Select`, `Where`, `GroupBy`). The DryadLINQ compiler translates these operators into a distributed execution plan.

---

## 2. Dryad Execution Engine

The underlying **Dryad** execution engine manages dataflow:

```mermaid
graph LR
    Input[Input Files] --> Vertex1[Map Vertex]
    Vertex1 --> Channel[TCP/File Channel]
    Channel --> Vertex2[Reduce Vertex]
    Vertex2 --> Output[Output Files]
```

*   **Execution Graph**: Programs are modeled as a Directed Acyclic Graph (DAG), where vertices represent processing code and edges represent data transmission channels (shared memory, files, or TCP pipes).
*   **Fault Tolerance**: If a vertex fails, Dryad schedules a replacement vertex and reruns only the failed partition of the graph.