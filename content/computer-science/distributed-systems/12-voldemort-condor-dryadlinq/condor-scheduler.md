---
title: The Condor High Throughput Scheduler
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

# The Condor High Throughput Scheduler

Condor (now HTCondor) is a specialized workload management system designed for **High Throughput Computing (HTC)**. It manages large clusters of distributed workstations by harvesting idle CPU cycles.

---

## 1. ClassAds Matchmaking

Condor matches jobs to machines using a symmetric schema called **ClassAds**:

*   **Job ClassAd**: Describes job requirements (e.g., minimum RAM, OS type) and preferences.
*   **Machine ClassAd**: Describes machine capabilities and policies (e.g., "only run jobs when keyboard is idle for 15 minutes").
*   **Matchmaker**: A central daemon evaluates both ClassAds and creates bindings.

---

## 2. Checkpointing and Migration

To handle transient resource availability, Condor supports **Job Checkpointing**:
*   A job's execution state (memory stack, registers, file descriptors) is periodically saved to disk.
*   If a user returns to their workstation, Condor suspends the guest job, migrates the checkpoint to another idle node, and resumes execution seamlessly.