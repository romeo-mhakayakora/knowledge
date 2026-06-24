---
title: Virtual Synchrony
subject: distributed-systems
chapter: 09-byzantine-virtual-synchrony
tags:
- distributed-systems
- systems
date: '2026-06-24'
updated: '2026-06-24'
status: complete
difficulty: advanced
---

# Virtual Synchrony

Virtual Synchrony is a programming model for group communication. It guarantees that membership changes (view changes) and message multicasts are delivered in a coordinated, atomic manner.

---

## 1. Group Views

Nodes are organized into a **Group**. The state of the group at any time is represented by a **View** $V_i = \{\text{list of active nodes}\}$.

*   When a node joins or fails, a **View Change** is triggered, producing a new view $V_{i+1}$.

---

## 2. Synchronization Guarantees

*   **Atomic Delivery**: If two nodes transition from View $V_i$ to $V_{i+1}$, they must have received the exact same set of multicast messages while in View $V_i$.
*   **Flush Protocol**: Before a new view can be installed, all pending messages in the current view must be acknowledged and "flushed" to all active members.