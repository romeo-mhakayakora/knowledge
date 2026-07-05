import os
import yaml

BASE_DIR = r"C:\Users\romeo\.gemini\antigravity-ide\scratch\knowledge\content\computer-science\distributed-systems"

# 1. Subject configuration
subject_meta = {
    "name": "Advanced Distributed Systems",
    "slug": "distributed-systems",
    "domain": "computer-science",
    "icon": "🌐",
    "color": "#10B981",
    "description": "Advanced topics in distributed systems: gossip protocols, DHTs, consensus, replication, and large-scale cloud architectures.",
    "chapters": [
        "01-epidemic-gossip",
        "02-napster-gnutella",
        "03-dhts",
        "04-logical-clocks-mutual-exclusion",
        "05-distributed-leader-election",
        "06-dmst-flp",
        "07-consistency-cap",
        "08-paxos-raft",
        "09-byzantine-virtual-synchrony",
        "10-bitcoin-blockchains",
        "11-dynamo-cassandra-percolator",
        "12-voldemort-condor-dryadlinq"
    ],
    "estimated_hours": 60,
    "difficulty": "advanced",
    "learning_outcomes": [
        "Explain the theoretical limits of distributed consensus (FLP, CAP, Byzantine bounds).",
        "Implement and analyze classic peer-to-peer architectures (Napster, Gnutella, Chord, Pastry).",
        "Compare modern consensus protocols (Multi-Paxos, Raft, PBFT, Nakamoto Consensus).",
        "Evaluate the trade-offs of key-value stores (Dynamo, Cassandra, Voldemort) and transactions (Percolator)."
    ],
    "prerequisites": ["operating-systems", "networks"]
}

# 2. Structure data for each week
weeks_data = {
    "01-epidemic-gossip": {
        "title": "Epidemic and Gossip-based Algorithms",
        "description": "Information dissemination, anti-entropy, and scalable failure detection in dynamic groups.",
        "topics": {
            "epidemic-models": {
                "title": "Epidemic Models and Dissemination Dynamics",
                "content": """# Epidemic Models and Dissemination Dynamics

Epidemic algorithms model information dissemination in distributed networks by drawing a direct mathematical parallel to biological disease spreading. They are highly valued for their robustness, decentralized nature, and predictable scaling properties.

---

## 1. Epidemic Paradigms (SIR vs. SIS)

Distributed nodes transitions through states similar to epidemiological models:

*   **Susceptible ($S$)**: A node that does not yet know the updates but is open to receiving it.
*   **Infective ($I$)**: A node that holds the update and is actively actively transmitting it to others.
*   **Removed / Recovered ($R$)**: A node that holds the update but has stopped transmitting it (in gossip, this represents *losing interest*).

### 1.1 The SIR Model
In the **SIR model**, the population transitions unidirectionally: $S \to I \to R$.
The rate of transition depends on the contact rate $\beta$ and recovery rate $\gamma$:

$$\\frac{dS}{dt} = -\\beta S I$$
$$\\frac{dI}{dt} = \\beta S I - \\gamma I$$
$$\\frac{dR}{dt} = \\gamma I$$

*   **Key Characteristic**: Once a node enters the Removed state ($R$), it remains there forever. This model guarantees that the gossip will eventually die out naturally, preventing infinite routing cycles in the network.

### 1.2 The SIS Model
In the **SIS model**, there is no recovery to a permanent removed state; rather, nodes transition $S \to I \to S$:

$$\\frac{dS}{dt} = -\\beta S I + \\gamma I$$
$$\\frac{dI}{dt} = \\beta S I - \\gamma I$$

*   **Key Characteristic**: Nodes can become susceptible again. In distributed systems, this represents a node forgetting an update or needing to fetch periodic updates continuously.

---

## 2. Gossip Protocols (Anti-Entropy vs. Rumor Mongering)

Distributed databases use two primary styles of gossip:

### 2.1 Anti-Entropy
Anti-entropy protocols are designed for **state reconciliation**. Nodes periodically select a random peer and compare their full datasets to resolve differences.

*   **Push Mechanism**: Node $A$ sends its state $S_A$ to node $B$. $B$ updates its state: $S_B \\gets S_B \\cup S_A$.
*   **Pull Mechanism**: Node $A$ requests state from $B$. $B$ sends $S_B$. $A$ updates: $S_A \\gets S_A \\cup S_B$.
*   **Push-Pull Mechanism**: Node $A$ and $B$ exchange summaries (e.g., Merkle trees) and send only missing entries to each other.

> **Efficiency**: Pull and Push-Pull are mathematically proven to converge much faster than pure Push when most of the population is infected. In a system of size $N$, anti-entropy achieves complete convergence in $O(\\log N)$ rounds.

### 2.2 Rumor Mongering (Dissemination)
When a node receives a new update (rumor), it becomes *infective* and actively "hot-gossips" it to $k$ random peers every round. 

*   **Feedback & Termination**: In each round, if a peer chosen by the infective node already knows the rumor, the infective node loses interest and transitions to the *Removed* state with probability $1/k$.
*   **Coverage**: Rumor mongering is highly efficient but does not guarantee 100% coverage. The fraction of nodes $p$ that remain uninformed is given by the transcendental equation:
    $$p = e^{-(k+1)(1-p)}$$
    To eliminate this residual error, rumor mongering is typically combined with a slow background anti-entropy process.
"""
            },
            "membership-failure-detection": {
                "title": "Membership and Failure Detection (SWIM Protocol)",
                "content": """# Membership and Failure Detection (SWIM Protocol)

In large-scale distributed systems, maintaining a consistent membership list is challenging. The **SWIM (Structured Weakly-consistent Infection-style Process Group Membership) Protocol** provides an elegant, scalable solution for membership and failure detection.

---

## 1. SWIM Architecture

Traditional heartbeat-based membership protocols suffer from $O(N^2)$ message complexity, where every node sends heartbeats to all other nodes. SWIM decouples membership update dissemination from failure detection, reducing message load per node to $O(1)$.

```mermaid
graph TD
    A[Node A] -->|1. Ping| B(Node B - Unresponsive)
    A -->|2. Ping-Req| C[Node C]
    A -->|2. Ping-Req| D[Node D]
    C -->|3. Indirect Ping| B
    D -->|3. Indirect Ping| B
    C -->|4. No Ack| A
    D -->|4. No Ack| A
    A -->|5. Suspect B| E[SWIM Gossip Network]
```

---

## 2. Failure Detector Protocol

The SWIM failure detector operates in periods of duration $T$. In each period, Node $A$ performs the following:

1.  **Direct Ping**: $A$ randomly selects a node $B$ from its membership list and sends a `Ping`.
2.  **Ack Timeout**: If $A$ receives an `Ack` from $B$ within a timeout, the period ends.
3.  **Indirect Ping (Ping-Req)**: If no `Ack` is received, $A$ selects $k$ helper nodes (e.g., $C$ and $D$) and sends them a `Ping-Req(B)` message.
4.  **Indirect Probe**: The helper nodes attempt to ping $B$ directly. If they receive an `Ack`, they forward it to $A$.
5.  **Declare Unresponsive**: If $A$ receives no direct or indirect `Ack` before the end of period $T$, $B$ is marked as failed.

> **Rationale**: Using indirect pings avoids false positives caused by transient network congestion on the direct link between $A$ and $B$.

---

## 3. The SWIM Suspicion Mechanism

Directly declaring a node dead can cause churn if a node is merely slow. SWIM adds a **Suspicion Mechanism**:

*   Instead of immediately marking $B$ as dead, $A$ marks $B$ as **Suspect** and gossips a `{Suspect B, Incarnation i}` message.
*   If $B$ is alive, it will receive the suspect message. It refutes this claim by incrementing its incarnation number and gossiping `{Alive B, Incarnation i+1}`.
*   If the suspect timer expires without an `Alive` refutation, $B$ is officially declared dead and removed from membership lists.
"""
            }
        }
    },
    "02-napster-gnutella": {
        "title": "Napster and Gnutella",
        "description": "First and second generation Peer-to-Peer (P2P) systems, centralized indexes, flooding, and supernodes.",
        "topics": {
            "napster-architecture": {
                "title": "Napster: Centralized Index P2P",
                "content": """# Napster: Centralized Index P2P

Napster represents the first generation of Peer-to-Peer (P2P) file-sharing networks. It introduced the hybrid model of using a centralized index server alongside direct peer-to-peer data transfers.

---

## 1. Napster System Architecture

Napster is not a pure peer-to-peer system because it relies on a central coordinate server to locate resources.

```mermaid
sequenceDiagram
    participant Peer A
    participant Central Index Server
    participant Peer B
    
    Peer A->>Central Index Server: 1. Register shared files (IP, File List)
    Peer B->>Central Index Server: 2. Search query ("song.mp3")
    Central Index Server-->>Peer B: 3. Return IP address of Peer A
    Peer B->>Peer A: 4. Direct TCP connection (download file)
    Peer A-->>Peer B: 5. File transfer complete
```

---

## 2. Operational Workflow

1.  **Registration**: When a peer joins, it establishes a persistent connection to the Napster central server and uploads a list of files it is sharing.
2.  **Search**: To find a file, a peer sends a keyword query to the central server. The server searches its database and returns a list of matching peers (with IP addresses, ports, and connection speeds).
3.  **Download**: The requesting peer selects a target peer and opens a direct socket connection to download the file.

---

## 3. Architecture Trade-offs

| Advantage | Disadvantage |
| :--- | :--- |
| **High Search Efficiency**: Search is $O(1)$ and supports arbitrary complex regular expressions. | **Single Point of Failure**: If the central server crashes, no searches can be performed. |
| **Simple Directory Management**: Index state is held centrally, eliminating consistency overhead. | **Scalability Bottleneck**: Central server resources (RAM, bandwidth) limit network size. |
| **No Routing Overhead**: Peers do not forward queries. | **Vulnerable to Legal Action**: Easy targets for copyright enforcement (Napster was shut down in 2001). |
"""
            },
            "gnutella-flooding": {
                "title": "Gnutella: Decentralized Flooding P2P",
                "content": """# Gnutella: Decentralized Flooding P2P

Gnutella represents the second generation of Peer-to-Peer (P2P) systems. It was designed to be a fully decentralized, unstructured file-sharing network to overcome the single-point-of-failure and legal vulnerabilities of Napster.

---

## 1. Gnutella Protocol & Query Flooding

Since Gnutella lacks a central index, search queries must be broadcasted through the network. Peers establish random TCP connections to form an unstructured overlay.

```mermaid
graph LR
    A[Peer A] -->|Query, TTL=4| B[Peer B]
    A -->|Query, TTL=4| C[Peer C]
    B -->|Query, TTL=3| D[Peer D]
    B -->|Query, TTL=3| E[Peer E]
    C -->|Query, TTL=3| F[Peer F]
```

### 1.1 Messaging Protocols
Gnutella uses five core message types:

*   **Ping**: Probe the network to discover active peers.
*   **Pong**: Response to a Ping, containing peer IP, port, and shared files summary.
*   **Query**: Search request containing search keywords and a **TTL (Time To Live)** field.
*   **QueryHit**: Response to a Query, sent along the reverse path, containing file details.
*   **Push**: Request for firewalled peers to initiate the connection.

### 1.2 The Flooding Mechanism
1.  **Query Generation**: Peer $A$ broadcasts a `Query` with a transaction ID, search terms, and a `TTL` (typically 7) to all its connected neighbors.
2.  **Forwarding**: When a peer receives a `Query`, it checks if it has already processed it (via transaction ID cache).
    *   If yes, it drops the query to prevent loops.
    *   If no, it searches its local files. If a match is found, it sends a `QueryHit` back along the path the query arrived.
    *   It decrements the `TTL` by 1. If `TTL > 0`, it forwards the query to all its other neighbors.

---

## 2. Limits and Performance Issues

Gnutella's unstructured, flooding-based approach suffers from severe scaling constraints:

*   **Network Congestion**: Flooding causes exponential message growth:
    $$\\text{Total Messages} \\approx d \\cdot (d-1)^{\\text{TTL}-1}$$
    where $d$ is average node degree. This "broadcast storm" consumes massive bandwidth.
*   **Free Riding**: Up to 70% of peers do not share files, acting only as consumers.
*   **Incompleteness**: Rare files may exist but not be found if they lie beyond the TTL horizon.
"""
            },
            "hierarchical-p2p": {
                "title": "Hierarchical Peer-to-Peer (Supernodes)",
                "content": """# Hierarchical Peer-to-Peer (Supernodes)

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
| **Search Time** | $O(1)$ | $O(N)$ worst case | $O(S)$ where $S \\ll N$ |
| **Message Overhead** | $O(1)$ | $O(d^k)$ (exponential) | Limited to Supernode network |
| **Failure Vulnerability** | Critical (Server loss) | None (Very robust) | Minimal (Leaf reassignment) |
| **State Consistency** | Highly Consistent | N/A (Dynamic query) | Local consistency at Supernodes |
"""
            }
        }
    },
    "03-dhts": {
        "title": "DHTs: Pastry and Freenet",
        "description": "Structured peer-to-peer overlays, prefix matching, and adaptive anonymous datastores.",
        "topics": {
            "01-pastry": {
                "title": "The Pastry DHT Protocol",
                "content": """# Distributed Hash Tables and Pastry

*Lecture notes — Smruti R. Sarangi, IIT Delhi*
*Source paper: Rowstron & Druschel, "Pastry: Scalable, Decentralized Object Location and Routing for Large-Scale Peer-to-Peer Systems," Middleware 2001*

> **Structure:** Part I covers every concept and algorithm cleanly, with intuition and no proofs. Part II contains all the mathematics. Read Part I to understand the system; go to Part II when you want to derive the numbers.

---

## Table of Contents

**Part I — Concepts and Intuition**

- [1. From Napster to DHTs: The Motivation](#1-from-napster-to-dhts-the-motivation)
- [2. What Is a Hash Table? What Is a Distributed Hash Table?](#2-what-is-a-hash-table-what-is-a-distributed-hash-table)
  - [2.1 Normal Hash Tables](#21-normal-hash-tables)
  - [2.2 Why DHTs? The Scale Problem](#22-why-dhts-the-scale-problem)
  - [2.3 Advantages of DHTs](#23-advantages-of-dhts)
- [3. The Core Idea: Mapping Files and Nodes to the Same Space](#3-the-core-idea-mapping-files-and-nodes-to-the-same-space)
  - [3.1 The Problem of Finding Who Owns What](#31-the-problem-of-finding-who-owns-what)
  - [3.2 The Ring: Organizing the ID Space](#32-the-ring-organizing-the-id-space)
  - [3.3 The Fundamental Rule of DHT Storage](#33-the-fundamental-rule-of-dht-storage)
- [4. Pastry: Design and Overview](#4-pastry-design-and-overview)
  - [4.1 Node IDs and the Ring](#41-node-ids-and-the-ring)
  - [4.2 The Three Data Structures of a Pastry Node](#42-the-three-data-structures-of-a-pastry-node)
- [5. Prefix-Based Routing: The Core Algorithm](#5-prefix-based-routing-the-core-algorithm)
  - [5.1 The Intuition: Narrowing Down Digit by Digit](#51-the-intuition-narrowing-down-digit-by-digit)
  - [5.2 The Routing Table in Detail](#52-the-routing-table-in-detail)
  - [5.3 The Leaf Set: The Endgame](#53-the-leaf-set-the-endgame)
  - [5.4 The Neighborhood Set: Locality](#54-the-neighborhood-set-locality)
  - [5.5 The Full Routing Algorithm](#55-the-full-routing-algorithm)
  - [5.6 Performance and Reliability](#56-performance-and-reliability)
- [6. Node Arrival: Joining the Ring](#6-node-arrival-joining-the-ring)
  - [6.1 The Join Procedure](#61-the-join-procedure)
  - [6.2 Initializing the Three Tables](#62-initializing-the-three-tables)
  - [6.3 Maintaining Locality on Join](#63-maintaining-locality-on-join)
- [7. Node Departure and Failure: Keeping the Ring Alive](#7-node-departure-and-failure-keeping-the-ring-alive)
  - [7.1 Graceful vs Non-Graceful Departure](#71-graceful-vs-non-graceful-departure)
  - [7.2 Redundancy: Why Store at Neighbors?](#72-redundancy-why-store-at-neighbors)
  - [7.3 Repairing the Leaf Set](#73-repairing-the-leaf-set)
  - [7.4 Repairing the Routing Table](#74-repairing-the-routing-table)
  - [7.5 Repairing the Neighborhood Set](#75-repairing-the-neighborhood-set)
- [8. Tolerating Byzantine Failures](#8-tolerating-byzantine-failures)
- [9. Experimental Results](#9-experimental-results)

**Part II — Proofs and Mathematical Derivations**

- [P1. Why $O(\log_{2^b} N)$ Steps Suffice: The Prefix-Match Convergence Proof](#p1-why-olog_2b-n-steps-suffice-the-prefix-match-convergence-proof)
- [P2. Maintaining Locality on Join: The Induction Argument](#p2-maintaining-locality-on-join-the-induction-argument)

---

# Part I — Concepts and Intuition

## 1. From Napster to DHTs: The Motivation

Before DHTs, the P2P generations looked like this:

| Generation | System | Search Mechanism | Weakness |
|---|---|---|---|
| 1st | Napster | Central server index | Single point of failure — legal and technical |
| 2nd | Gnutella | Broadcast query to graph neighbors (TTL-bounded) | Floods the network; $O(N)$ messages in the worst case |
| 3rd | DHTs (Pastry, Chord, Tapestry…) | Structured routing via a hash ring | $O(\log N)$ messages, fully decentralized |

The core question motivating the 3rd generation: *can we find where a file is stored in $O(\log N)$ messages, without any central server and without flooding?*

The answer is yes — by storing information cleverly, so that the location of any piece of data can be *computed*, not searched for.

---

## 2. What Is a Hash Table? What Is a Distributed Hash Table?

### 2.1 Normal Hash Tables

A hash table is a dictionary storing **key–value pairs**. Supply the key, get the value back.

| Operation | What it does | Time complexity |
|---|---|---|
| `insert(key, value)` | Store the pair | $\approx \Theta(1)$ |
| `lookup(key)` | Return value, or null | $\approx \Theta(1)$ |
| `delete(key)` | Remove the pair | $\approx \Theta(1)$ |

A good hash function maps keys to unique locations to minimize collisions. Collisions are resolved via **chaining** (each slot is a linked list) or **rehashing** (probe alternative slots).

### 2.2 Why DHTs? The Scale Problem

A single machine's hash table cannot hold web-scale data. Consider two concrete examples:

**Banking (fits on one machine):**
- 0.1 billion customers × 8 KB per customer = **0.8 TB** — a modern laptop handles this.

**Music sharing (does not fit):**
- 0.1 billion users × 100 songs × 5 MB per song = **50 petabytes** — orders of magnitude larger, geographically distributed, and the system must survive regional outages.

The key transition: for web-scale data, a single machine is not just impractical — it's architecturally wrong. Facebook, LinkedIn, Google, Netflix, and Amazon are all built on DHT-like technology.

### 2.3 Advantages of DHTs

DHTs solve four problems simultaneously:

**Scale** — key-value pairs are distributed across thousands of machines; the system grows by simply adding nodes.

**Fault tolerance** — data is replicated; a regional outage (e.g., a power cut in one data center) does not take down the system.

**Elastic load balancing** — different keys hash to different nodes, spreading user requests naturally. Adding nodes during peak load (Diwali, Thanksgiving, Christmas) and removing them afterward is straightforward.

**Reduced legal liability** — in P2P contexts, with no central server knowing about all transfers, legal exposure is diffuse (though transferring unlicensed content remains illegal regardless).

Major DHT proposals: **Pastry**, **Chord**, **Tapestry**, **CAN**, **Fawn**.

---

## 3. The Core Idea: Mapping Files and Nodes to the Same Space

### 3.1 The Problem of Finding Who Owns What

Imagine node $Q$ has file $F_1$. It wants to tell the rest of the network "I have $F_1$" — not by broadcasting (expensive), but by storing that information at some node $E$ that anyone can find just by computing.

The question is: **where should $Q$ store the information "I have $F_1$"?** And how can any other node $A$ find $E$ without knowing the network topology?

The answer: use a **hash function** to map both file names and node identities into the same numerical space, then define a rule for who is responsible for what.

### 3.2 The Ring: Organizing the ID Space

Take an $m$-bit hash space: integers from $0$ to $2^m - 1$, arranged conceptually as a circle (ring). Both nodes and objects (files/keys) get mapped into this space:

- Each node gets a **node ID**: computed as the cryptographic hash of its IP address or public key.
- Each object/file gets an **object ID**: computed as the cryptographic hash of its name/content.

```mermaid
flowchart LR
    subgraph Ring["ID Space: 0 → 2^m − 1 (circular)"]
        N1((Node A)) --- N2((Node B)) --- N3((Node E)) --- N4((Node C)) --- N1
        F1[/Object: F1\] -. "closest node: E" .-> N3
        F2[/Object: F2\] -. "closest node: B" .-> N2
    end
```

Nodes are arranged in **ascending order of node ID** around the ring. This is a virtual/conceptual arrangement — not a physical network topology.

### 3.3 The Fundamental Rule of DHT Storage

> **The rule:** information about an object is stored at the node whose node ID is **numerically closest** to the object's hash value.

So:
- To **store** information about $F_1$: hash $F_1$, find the closest node on the ring, send "I have $F_1$" to that node.
- To **look up** $F_1$: hash $F_1$, route a query to the closest node on the ring, receive back "node $Q$ has it."

This is beautiful because the mapping is entirely deterministic — anyone can compute where to send a query without consulting any central directory. The hash function is public and agreed upon by all participants.

**Why use the same hash space for both?** If IP addresses were mapped directly to file IDs, IP address clusters (entire universities, ISPs) might map to the same region of the file ID space, overloading some nodes. Hashing both independently achieves a much more uniform distribution.

---

## 4. Pastry: Design and Overview

Pastry is a concrete DHT design by Rowstron and Druschel (Middleware 2001). It is a **scalable distributed object location service** using a ring-based overlay that accounts for network locality and automatically adapts to node arrivals, departures, and failures.

Applications built on top of Pastry: **PAST** (large-scale distributed file storage) and **SCRIBE** (scalable publish/subscribe system).

### 4.1 Node IDs and the Ring

Every node gets a unique **128-bit node ID**, generated by:
- Computing `SHA(IP address)` or using the node's public key, then taking the lower 128 bits.

With $b = 4$ (the standard choice), each 128-bit ID is represented as **32 hexadecimal digits** (since 1 hex digit = 4 bits, 128 / 4 = 32). All node IDs and keys are treated as base-$2^b = 16$ numbers.

**Key parameters:**
- $b = 4$: bits per digit (so base = $2^b = 16$, i.e. hexadecimal).
- $L$: leaf set size (typically 16 or 32).
- $M$: neighborhood set size (typically $2^{b+1} = 32$).

**Pastry's headline guarantee:** routing completes in $\lceil \log_{2^b}(N) \rceil$ steps. With $b=4$ and $N=1{,}000{,}000$ nodes: $\log_{16}(10^6) = \log_{16}(16^5) = 5$ steps. Five hops to find anything among a million nodes.

**Fault tolerance guarantee:** delivery is guaranteed unless $L/2$ nodes with adjacent node IDs fail simultaneously.

### 4.2 The Three Data Structures of a Pastry Node

Every Pastry node maintains three tables:

| Table | What it contains | Purpose |
|---|---|---|
| **Routing table** $\mathcal{R}$ | 32 rows × 15 columns; each cell = IP of a node with a specific prefix match | Prefix-based long-distance routing |
| **Leaf set** $\mathcal{L}$ | $L/2$ closest larger node IDs + $L/2$ closest smaller node IDs | Guaranteed final delivery to the numerically closest node |
| **Neighborhood set** $\mathcal{M}$ | $M$ nodes geographically/topologically close | Maintains network locality |

These three serve completely different roles: the routing table does the fast long-distance travel; the leaf set does the precise final delivery; the neighborhood set maintains physical proximity for efficiency. Understanding all three is essential.

---

## 5. Prefix-Based Routing: The Core Algorithm

### 5.1 The Intuition: Narrowing Down Digit by Digit

Here is the central insight of Pastry's routing, explained from first principles.

Suppose you want to find the node closest to hash value `F E 3 6 ...` (in hex). You are currently at some node and need to get progressively closer on the ring. The trick Pastry uses: **match one more hex digit of the key at each hop**.

Imagine the 32-digit hex key `F E 3 6 A 2 ...`. At the first node:
- If your node ID starts with `F`, great — you already share 1 digit.
- Look for a neighbor whose ID starts with `F E` (matching 2 digits).
- Forward the query there.

At the next node (starting with `F E`):
- Look for a neighbor starting with `F E 3`.
- Forward there.

Each hop increases the shared prefix by one digit. After $k$ hops, the query is at a node matching $k$ hex digits of the key — which means it is exponentially closer in the ID space. This is exactly like binary search, but in base 16: each step eliminates $15/16$ of the remaining search space.

```mermaid
flowchart LR
    A["Node: A7... \n(0 digits match key FE36...)"] -->|"forward: find FE"| B["Node: FE... \n(1 digit matches)"]
    B -->|"forward: find FE3"| C["Node: FE3... \n(2 digits match)"]
    C -->|"forward: find FE36"| D["Node: FE36... \n(3 digits match)"]
    D -->|"leaf set lookup"| E["Node: FE36A2... \n(closest — done)"]
```

**The key abstraction:** routing in Pastry is not happening at Layer 3 (the IP network layer). It's happening at the **application layer**, over the P2P overlay network. Each "hop" is one message forwarded between Pastry peers over an existing TCP connection.

### 5.2 The Routing Table in Detail

The routing table $\mathcal{R}$ is a $32 \times 15$ matrix (with $b=4$, base 16).

**Why 32 rows?** A node ID is 128 bits = 32 hex digits. At most, you need to match all 32 digits, one per hop.

**Why 15 columns?** At row $i$, you already share $(i-1)$ digits with the key. The $i$-th digit of the key is some hex value $d \in \{0, 1, \ldots, F\}$. Since your own $i$-th digit already accounts for one value, there are $2^b - 1 = 15$ other possible values to cover.

**What each cell contains:** $\mathcal{R}[i][d]$ holds the IP address of a node that shares the first $(i-1)$ digits of *your* node ID, but whose $i$-th digit is $d$. If you find a cell where $d$ matches the $i$-th digit of the key, that node shares one more digit of the key than you do — forward there.

**Mnemonic:** Row $i$ answers "given that I match $(i-1)$ digits, where can I find a node matching $i$ digits for each possible next digit?"

### 5.3 The Leaf Set: The Endgame

The leaf set $\mathcal{L}$ contains:
- $L/2$ nodes with numerically closest **larger** node IDs (clockwise neighbors on the ring).
- $L/2$ nodes with numerically closest **smaller** node IDs (counter-clockwise neighbors).

**Why the leaf set matters:** prefix routing gets you *close* to the target, but not necessarily to the single numerically closest node. The leaf set is what guarantees precision at the end. Once the key's hash falls within the range of the current node's leaf set, the node has a perfect local view of that region of the ring and can identify the single closest node with certainty.

**Intuition:** think of the leaf set as your "known neighborhood" on the ring. The routing table takes you to the right neighborhood; the leaf set finds the exact address within it.

**Fault tolerance via the leaf set:** if $L/2$ nodes in the leaf set are still alive, the message can always be passed to *some* neighbor — even if some have failed. This is the basis of Pastry's failure tolerance guarantee.

**Why $L > 2$?** If $L = 2$ (only one neighbor on each side), a single node failure on one side leaves you with no fallback. Having $L = 16$ or $L = 32$ gives you $L/2 - 1$ redundant fallbacks per side — much more robust.

**The critical question: how does a node know who its $L/2$ immediate ring neighbors are?**

This seems circular — to know your ring neighbors, you'd need to know the whole ring. Pastry solves it via the join procedure (Section 6): when node $X$ joins, it routes toward its own node ID. Every node $B_i$ along that path shares $i$ digits of prefix with $X$ and is therefore progressively closer on the ring. $X$ adds all of these path nodes to its leaf set. Because the routing path takes $O(\log N)$ hops, the leaf set ends up with $O(\log N)$ nodes that are **well-distributed** around the ring — not just the immediate neighbors, but also a spread of nodes at varying distances. This distribution is what makes the fast $O(\log N)$ routing work in practice.

**The $O(N)$ baseline — why distributed connections matter:**

To see why you need well-distributed leaf set entries, consider the degenerate case: each node knows *only* its immediate left and right ring neighbors (leaf set size 2, nothing else). Routing works — you'll always find the closest node eventually — but how many hops does it take?

With only immediate neighbors, routing from node $A$ to a target near node $E$ means hopping one step at a time around the ring: $A \to$ next $\to$ next $\to \cdots \to E$. This is $O(N)$ hops — linear in the number of nodes, catastrophically slow for large networks.

Pastry's routing table and well-distributed leaf set act like long-range "shortcuts": instead of stepping one node at a time, you can jump to a node that is already halfway across the ring (in ID space), then a quarter of the way, then an eighth — a classic halving-the-distance strategy that gives $O(\log N)$.

| Connectivity | Routing time | Why |
|---|---|---|
| Only immediate neighbors | $O(N)$ | Must step one node at a time |
| Well-distributed (Pastry) | $O(\log_{2^b} N)$ | Long-range jumps halve the search space each hop |

### 5.4 The Neighborhood Set: Locality

The neighborhood set $\mathcal{M}$ contains $M \approx 2^{b+1}$ nodes that are **geographically or topologically close** to the current node — e.g., nodes in the same data center, same ISP, or nearby in latency.

**What it's for:** locality. When initializing a new node, the neighborhood set seeds the routing table with nearby nodes, so that early routing hops don't unnecessarily cross the globe. It is *not* about closeness in the ID space — it's about closeness in the physical network.

**Key distinction:** the leaf set tracks proximity in the *ID space* (who is numerically close on the ring); the neighborhood set tracks proximity in the *physical network* (who is geographically/latency-close). A node might be your physical neighbor but have a node ID far from yours — that's normal.

### 5.5 The Full Routing Algorithm

```
Input:  key K, routing table R, hash of key D
Output: value V

if L_{-L/2} ≤ D ≤ L_{L/2}  then
    // Key is within the leaf set range — we know exactly who's closest
    forward K to leaf L_i minimizing |L_i − K|

else
    l ← length of common prefix between D and my node ID
    if R(l+1, D_{l+1}) ≠ null  then
        // Normal case: forward to a node matching one more digit
        forward to R(l+1, D_{l+1})
    else
        // Rare case: no routing table entry for the next digit
        // Fall back: find any known node that is at least as close
        // in prefix length but numerically closer to D
        forward to T ∈ (L ∪ R ∪ M) such that:
            prefix(T, K) ≥ l   AND   |T − K| < |nodeId − K|
```

**Three cases, in plain English:**

1. **Leaf set hit** (most precise): the key is in your immediate neighborhood on the ring. You have a complete picture — send directly to the closest node.

2. **Routing table hit** (normal case): look at the $(l+1)$-th row, the column corresponding to the next digit of the key. If that cell is populated, forward there — the next node shares one more digit.

3. **Routing table miss** (rare): your routing table has a gap. Scan all three data structures ($\mathcal{L}$, $\mathcal{R}$, $\mathcal{M}$) for any node that both (a) matches at least as many prefix digits as you do and (b) is numerically closer to the target. Forward there. Progress is still guaranteed — each hop strictly decreases the distance.

### 5.6 Performance and Reliability

**Routing complexity:** $O(\log_{2^b} N)$ hops. With $b=4$ and $N=100{,}000$: $\log_{16}(100{,}000) \approx 4$ hops. Experimentally confirmed:

| Hop count | Fraction of lookups |
|---|---|
| 2 hops | 1.5% |
| 3 hops | 16.4% |
| 4 hops | 64% |
| 5 hops | 17% |

Average: ~4 hops for 100,000 nodes (2.5 hops for 1,000 nodes). With a complete routing table, hop count would be 30% lower.

**Why so fast?** Each hop increases the prefix match by one base-$2^b$ digit. That means each hop reduces the search space by a factor of $2^b = 16$. The number of hops needed to reduce a space of $N$ to 1 is $\log_{16}(N)$ — logarithmic search by construction.

---

## 6. Node Arrival: Joining the Ring

### 6.1 The Join Procedure

When node $X$ wants to join:

1. $X$ locates a **nearby** node $A$ (bootstrapping). $A$ can be found via **expanding ring multicast**: $X$ broadcasts a "who is near me?" message with TTL=1, then TTL=2, expanding the search radius until it finds at least one responsive Pastry node. This avoids flooding the whole network while still guaranteeing discovery of a nearby peer.
2. $X$ routes a **join message** through the network toward the node $Z$ whose node ID is numerically closest to $X$'s own node ID.
3. Every node on the path from $A$ to $Z$ sends its routing table to $X$.
4. $X$ uses all this information to initialize its three tables.
5. $X$ transmits its state to all nodes in $\mathcal{L} \cup \mathcal{R} \cup \mathcal{M}$ so they can update their own tables.

```mermaid
sequenceDiagram
    participant X as New Node X
    participant A as Nearby Node A
    participant Bi as Path Nodes B₁…Bₙ
    participant Z as Closest Node Z

    X->>A: join message (route toward X's node ID)
    A->>Bi: forward join message
    Bi->>Z: forward join message
    A-->>X: send routing table row 1
    Bi-->>X: send routing table rows 2…n
    Z-->>X: send leaf set
    X->>Z: update: I have arrived
```

### 6.2 Initializing the Three Tables

**Neighborhood set:** $A$ is physically close to $X$ (that's how $X$ found it). So $X$ simply copies $A$'s neighborhood set. Geographic proximity is inherited.

**Leaf set:** $Z$ is the closest node to $X$ in the ID space. $X$ copies $Z$'s leaf set and adjusts it around its own position — these are the nodes immediately adjacent to $X$ on the ring.

**Routing table:** this is the clever part. Each node $B_i$ on the path from $A$ to $Z$ has exactly $i$ digits of its prefix matching $X$'s ID (because each step of routing increases the prefix match by one). So $B_i$'s $(i+1)$-th routing table row already covers nodes sharing $i$ digits with $X$ — exactly what $X$ needs for its $(i+1)$-th row. $X$ copies row $i+1$ from $B_i$'s table. The first row (no prefix match needed) comes from $A$.

**Why this is efficient:** $X$ does not need to contact the entire network. It only contacts the $O(\log N)$ nodes along the routing path, and each contributes exactly the right row of the routing table.

### 6.3 Maintaining Locality on Join

**The induction argument (intuition, not proof):** assume every existing node already has a well-localized routing table — i.e., all its routing table entries point to nearby nodes. When $X$ joins:

- $X$ starts from $A$, which is geographically close.
- The routing path $A \to B_1 \to \cdots \to Z$ stays "fairly close" to $X$ throughout, because each $B_i$ was close to $A$ (by the induction assumption applied to $B_i$'s own routing table).
- Since $X$ copies row $i+1$ from $B_i$, and $B_i$ is fairly close, $X$'s row $i+1$ also points to nearby nodes.
- Therefore $X$ inherits locality.

The induction base case holds trivially: when the network has one node, the property is vacuously true. New joins preserve it. **Induction hypothesis proved.**

---

## 7. Node Departure and Failure: Keeping the Ring Alive

### 7.1 Graceful vs Non-Graceful Departure

A node can leave the network in two fundamentally different ways:

- **Graceful departure**: the node knows it is leaving. It can notify its neighbors, transfer its stored records to the next-closest node, and update routing tables. This is clean but rare in practice — machines crash, connections drop, users close applications without warning.
- **Non-graceful departure (failure)**: the node simply disappears. No notification, no data transfer. This is the common case and the one the protocol must be designed for.

Pastry's design is specifically built around the assumption that departures are usually non-graceful. The redundancy mechanism below is the answer.

### 7.2 Redundancy: Why Store at Neighbors?

Suppose node $X$ holds the record "node $Q$ has file $F_1$." If $X$ fails without warning — which is the common case — that record is lost. The next query for $F_1$ will route to $Y$ (the next closest node), which knows nothing.

**The fix: each node stores a copy of what its neighbors would normally store.** Specifically, every node stores the key-value records that would belong to the $L/2$ nodes to its immediate left and right on the ring.

**Careful: this is not a full replication of everyone's data.** Node $Y$ only stores *what would be stored at $X$ by the DHT rule*, not what $X$ itself happens to hold for other reasons. This keeps the storage overhead bounded.

**Why $L/2$ copies?** The failure guarantee says delivery is possible unless $L/2$ adjacent nodes fail simultaneously. With $L/2$ redundant copies distributed around the neighborhood, you need to lose all of them at once before data becomes unavailable.

### 7.3 Repairing the Leaf Set

Nodes might fail or leave without notice. When node $\mathcal{L}_{-k}$ (a leaf at position $-k$, where $-L/2 < k < 0$) is detected as failed:

1. Contact the furthest-away leaf on the same side: $\mathcal{L}_{-L/2}$.
2. Get its leaf set.
3. Merge the received leaf set with your own.
4. For any new nodes discovered, **ping them** to verify they are actually alive before adding them.

**Why ping?** The received leaf set might itself be stale. A node that appears in $\mathcal{L}_{-L/2}$'s leaf set might also have failed. Always verify before trusting.

**Keep-alive messages:** every Pastry node periodically sends heartbeat messages to all nodes it is connected to. This gives early warning of failures, so repair can happen proactively rather than reactively.

### 7.4 Repairing the Routing Table

When routing table entry $\mathcal{R}(l, d)$ fails:

1. **Try a lateral replacement:** contact $\mathcal{R}(l, d')$ for some $d' \neq d$ (a different node in the same row, i.e., one that shares the same prefix length). Ask it for a node at the same position.
2. **If no lateral replacement works, look further:** ask $\mathcal{R}(l+1, d')$ — a node with an even longer prefix match. It likely has richer knowledge of that region of the ring.

**Intuition:** nodes with longer shared prefixes tend to know more about the detailed structure of that ID region — they're "deeper" into the same neighborhood of the ring.

### 7.5 Repairing the Neighborhood Set

The neighborhood set requires a different repair strategy because it tracks physical proximity, not ID proximity:

1. Each node **periodically pings** all nodes in its neighborhood set.
2. If a neighbor is found dead, contact the *remaining* neighbors and ask for *their* neighborhood sets.
3. Merge, verify, and repair.

**Why go to neighbors?** If your geographic neighbor is dead, your other geographic neighbors are likely to know about nearby nodes — they share the same physical region.

---

## 8. Tolerating Byzantine Failures

Byzantine failures — where nodes lie, corrupt messages, or behave maliciously — require additional mechanisms beyond fail-stop handling:

- **Multiple entries per routing table cell**: store several alternative nodes per cell so a single malicious/incorrect entry can be detected and bypassed.
- **Randomize the routing strategy**: don't always take the same route; randomization makes it harder for an adversary to reliably intercept queries.
- **Periodic IP broadcasts and expanding-ring multicasts**: reconnect network components that may have become disconnected due to failures or attacks.

---

## 9. Experimental Results

**Simulation setup:** 100,000 nodes, each running a Java-based VM, each assigned coordinates in a Euclidean plane (to model geographic distances).

**Key findings:**

- Hop count grows **linearly with $\log N$** — confirming the $O(\log_{2^b} N)$ prediction.
- At 1,000 nodes: ~2.5 hops average.
- At 100,000 nodes: ~4 hops average.
- With a complete routing table (no missing entries): hop count would be **30% lower**.
- Hop count distribution for 100,000 nodes and 200,000 lookups: 64% of queries complete in exactly 4 hops.

---

# Part II — Proofs and Mathematical Derivations

> Read this after Part I. All notation defined here is consistent with Part I.

## P1. Why $O(\log_{2^b} N)$ Steps Suffice: The Prefix-Match Convergence Proof

**What we want to show:** after $m = c + \log_{16}(N)$ hops (with $c$ a small constant), it is virtually certain that no other node exists that shares more than $m$ hex digits of prefix with the key. This means routing *must* have converged — there's no one further to forward to.

**Setup (with $b=4$, base $= 2^b = 16$):**

The probability that two randomly hashed IDs share the same first hex digit is $1/16$ (each digit is uniformly distributed). The probability they share the first $m$ digits is $16^{-m}$.

Therefore, the probability that a specific node does **not** share a prefix of length $m$ with the key is $1 - 16^{-m}$.

With $N$ nodes (all independent):

$$P(\text{no node shares a prefix of length } m \text{ with the key}) = (1 - 16^{-m})^N$$

**Setting $m = c + \log_{16}(N)$:**

$$P = (1 - 16^{-m})^N = (1 - 16^{-c} \cdot 16^{-\log_{16}(N)})^N = \left(1 - \frac{16^{-c}}{N}\right)^N$$

Let $\lambda = 16^{-c}$. Rewrite:

$$P = \left(1 - \frac{\lambda}{N}\right)^N = \left[\left(1 - \frac{\lambda}{N}\right)^{N/\lambda}\right]^\lambda$$

Applying the standard limit $\lim_{N \to \infty}(1 - \lambda/N)^{N/\lambda} = e^{-1}$:

$$\boxed{P = e^{-\lambda} = e^{-16^{-c}}}$$

**Reading the result:**

| $c$ | $\lambda = 16^{-c}$ | $P = e^{-\lambda}$ |
|---|---|---|
| 0 | 1 | $e^{-1} \approx 0.37$ |
| 1 | $1/16 \approx 0.063$ | $\approx 0.94$ |
| 2 | $1/256 \approx 0.004$ | $\approx 0.996$ |
| 3 | $\approx 2.4\times10^{-4}$ | $\approx 0.9998$ |

By $c = 2$: the probability that *any* node in the entire network shares more than $m = 2 + \log_{16}(N)$ digits of prefix with the key is essentially zero. So after $2 + \log_{16}(N)$ hops, prefix routing has converged with near certainty.

**The $O(\log N)$ conclusion:**

$$\text{routing hops} \leq m = c + \log_{16}(N) = O(\log_{16}(N)) = O(\log_{2^b}(N))$$

**Worked example** with $N = 1{,}000{,}000$:

$$\log_{16}(10^6) = \log_{16}(16^5) = 5$$

So $m = c + 5 \approx 7$ hops at most — even for a million-node network.

**Why does the search space shrink exponentially per hop?** Each hex digit of the key occupies 4 bits. Matching one more digit means you have narrowed the target region of the ring by a factor of $16 = 2^4$. After $k$ matched digits, you are looking at a region of size $N / 16^k$. Setting $N / 16^k = 1$ gives $k = \log_{16}(N)$ — exactly the number of routing hops needed.

---

## P2. Maintaining Locality on Join: The Induction Argument

**Claim:** if all existing nodes have well-localized routing tables (all entries point to nearby nodes), then when a new node $X$ joins using the Pastry join procedure, $X$'s routing table is also well-localized.

**Proof by induction on the join order:**

**Base case:** a network with one node trivially satisfies the property (no routing table entries to worry about).

**Inductive step:** assume all existing nodes have well-localized routing tables. Node $X$ joins via nearby node $A$.

The join message routes from $A$ toward $Z$ (the node closest to $X$'s node ID). Let $B_i$ be the $i$-th node along this path. By the routing protocol, $B_i$ shares $i$ digits of prefix with $X$.

The induction assumption says $B_i$'s routing table is well-localized — all its entries point to nearby nodes.

$X$ copies row $i+1$ of its routing table from $B_i$'s row $i+1$. We need to show those entries are near to $X$:

- $B_i$ shares $i$ prefix digits with $X$.
- $B_i$ was reached from $A$, which is geographically close to $X$.
- Each routing step stays "in the neighborhood" because the induction assumption guarantees $B_i$'s entries point to nearby nodes.
- Since $B_i$ is close to $X$ (transitively via $A$), $B_i$'s row $i+1$ entries are also close to $X$.

Therefore $X$'s row $i+1$ is populated with nearby nodes — locality is preserved.

Since this holds for all rows $i = 1, \ldots, 32$, $X$'s entire routing table is well-localized.

**Induction hypothesis proved.** $\square$

**The practical consequence:** locality is not an accident. The join procedure is explicitly designed so that routing-table rows are obtained from nodes that are simultaneously (a) ID-space-close (sharing prefix digits) and (b) network-space-close (reachable via short physical hops). The two notions of closeness are coupled by the join path, which ensures each $B_i$ is both.
"""
            },
            "02-freenet": {
                "title": "The Freenet Protocol",
                "content": """# Freenet: 3rd Generation Peer-to-Peer Networks

*Lecture notes — Smruti R. Sarangi, IIT Delhi*
*Source paper: Clarke et al., "Freenet: A Distributed Anonymous Information Storage and Retrieval System," Designing Privacy Enhancing Technologies, Springer, 2001*
*Course page: [COL 819 — Advanced Computer Networks, IIT Delhi (2021)](https://www.cse.iitd.ac.in/~srsarangi/courses/2021/col_819_2021/index.html)*

> **Academic purpose only.** Freenet is studied here purely as a computer science system. Understanding how anonymization networks work is necessary for anyone who wants to study, regulate, or investigate them. The discussion neither endorses nor promotes any misuse.

> **Structure:** Part I covers every concept and mechanism cleanly with intuition. No math, no proofs. Part II is a summary of the evaluation results. There is no heavy mathematics in this topic — the "proof" here is the protocol design itself and the anonymity argument.

---

## Table of Contents

- [1. Where Freenet Fits: The P2P Progression](#1-where-freenet-fits-the-p2p-progression)
- [2. Design Goals](#2-design-goals)
- [3. Freenet = Gnutella + Pastry + Anonymity](#3-freenet-gnutella-pastry-anonymity)
- [4. The Freenet Node](#4-the-freenet-node)
- [5. Querying: How You Find a File](#5-querying-how-you-find-a-file)
  - [5.1 Steps in a Query](#51-steps-in-a-query)
  - [5.2 Failure Handling During a Query](#52-failure-handling-during-a-query)
  - [5.3 Search Quality: How the Network Improves Over Time](#53-search-quality-how-the-network-improves-over-time)
- [6. Data Storage: How You Insert a File](#6-data-storage-how-you-insert-a-file)
  - [6.1 The Insert Procedure](#61-the-insert-procedure)
  - [6.2 Two Termination Strategies](#62-two-termination-strategies)
  - [6.3 Beating Security on Insert: Lying About Ownership](#63-beating-security-on-insert-lying-about-ownership)
  - [6.4 Advantages of This Storage Mechanism](#64-advantages-of-this-storage-mechanism)
- [7. Data Management: Finite Storage and LRU](#7-data-management-finite-storage-and-lru)
- [8. Encryption for Deniability](#8-encryption-for-deniability)
- [9. Message Format and Protocol Details](#9-message-format-and-protocol-details)
  - [9.1 Message Fields](#91-message-fields)
  - [9.2 The TTL Vulnerability and the Depth Field Fix](#92-the-ttl-vulnerability-and-the-depth-field-fix)
  - [9.3 Timers and Reliability](#93-timers-and-reliability)
  - [9.4 Message Types](#94-message-types)
- [10. Naming, Searching, and Security](#10-naming-searching-and-security)
  - [10.1 Organizing Files Without a Central Directory](#101-organizing-files-without-a-central-directory)
  - [10.2 Sender Anonymity](#102-sender-anonymity)
  - [10.3 Pre-routing and Layered Encryption](#103-pre-routing-and-layered-encryption)
- [11. Summary: The Four Pillars of Freenet Anonymity](#11-summary-the-four-pillars-of-freenet-anonymity)
- [12. Evaluation](#12-evaluation)
  - [12.1 Setup](#121-setup)
  - [12.2 Results: Successful Requests vs. Number of Queries](#122-results-successful-requests-vs-number-of-queries)
  - [12.3 Results: Hops vs. Number of Queries](#123-results-hops-vs-number-of-queries)

---

## 1. Where Freenet Fits: The P2P Progression

| Generation | System | Key Property | Main Weakness |
|---|---|---|---|
| 1st | Napster | Centralized index, P2P transfer | One legal and technical point of failure — the server |
| 2nd | Gnutella | Decentralized, broadcast search | No anonymity; IP addresses visible along the path |
| 3rd | DHTs (Pastry, Chord…) | Structured $O(\log N)$ routing | Nodes along the path know who is searching for what |
| 3rd+ | **Freenet** | DHT-like routing + anonymization | Still partial (not total) anonymity; no guaranteed delivery time |

Freenet's unique contribution is not speed or efficiency — it's **anonymity**. Both the requester and the original provider of a file are hidden from the rest of the network, to a degree not achieved by any of the earlier systems.

Freenet is a direct precursor to the modern **dark web** and influenced the design of networks like Tor.

---

## 2. Design Goals

Freenet was explicitly designed around four goals, in this priority order:

**Anonymity** — it must not be possible to determine the true origin of a file (who inserted it) or the identity of who is requesting it.

**Deniability of storers** — a node that is caching and forwarding data must be able to credibly deny that it knows what it is storing or who originally created the content. This is the legal protection layer.

**Efficient storage** — the system should organize data intelligently (similar keys cluster together) so lookups can succeed quickly.

**Reliability** — the system should deliver data consistently, even in a network where nodes join and leave unpredictably.

**A critical design consequence:** all storage in Freenet is explicitly **temporary**, not permanent. Data that is not frequently accessed eventually gets evicted (via LRU policy). This is partly a technical choice and partly a legal one — a node can claim it did not deliberately retain any specific content.

---

## 3. Freenet = Gnutella + Pastry + Anonymity

The cleanest way to understand Freenet is as a combination of two things you already know, plus a layer of deliberate obfuscation:

```
Freenet ≈ Gnutella (flooding-style neighbor queries)
        + Pastry (key-based routing toward numerically closer nodes)
        + Anonymity mechanisms (fake ownership, no origin tracing)
```

**From Gnutella:** queries are sent to neighbor nodes, which forward them onward. There's a TTL field to prevent infinite flooding. There's a pseudo-random query ID to prevent cycles.

**From Pastry:** each node maintains a routing table of key→address mappings. When forwarding a query, you don't just flood randomly — you forward to the neighbor whose known keys are *numerically closest* to the key you're looking for. This gives directional, informed routing rather than pure broadcast.

**What Freenet adds:** a deliberate system of fake ownership claims, origin hiding, and message obfuscation that makes it very difficult to identify who published or requested any particular file.

---

## 4. The Freenet Node

Each Freenet node maintains two local structures:

**Local data store** — actual cached copies of files (or file chunks) that this node holds. Storage is finite and managed via LRU eviction.

**Routing table** — a dynamic table with entries of the form:

| Key | Address | Content (?) |
|---|---|---|
| hash of some file | IP of a node that *might* have it | Optional cached content |

The `(?)` on content is important — the routing table records *where* data might be, but a node is not required to store the content itself. It may just know a pointer.

**Critical constraint: 1-hop visibility only.** A node knows only its *immediate* neighbors — it has no view of the wider network. This is a deliberate design choice for anonymity: you cannot reveal information about nodes you don't know. The routing table grows organically over time as queries traverse the network and new entries are created along successful paths.

There is also a **degree of trust** between a node and its direct neighbors — they know each other is *participating* in the protocol, but cannot verify whether the other is the original requester of any given query or just forwarding on someone else's behalf.

---

## 5. Querying: How You Find a File

### 5.1 Steps in a Query

Suppose you want to find a file named `song.mp3`.

```mermaid
flowchart LR
    A["Requester A"] -->|"1: hash(song.mp3) = key K\n lookup closest key in routing table"| B["Node B"]
    B -->|"2: forward toward closest key to K"| C["Node C"]
    C -->|"3: forward..."| E["Node E (has file)"]
    E -->|"4: Send.Data (claims to be owner)"| C
    C -->|"5: cache + create routing entry\n forward reply"| B
    B -->|"6: cache + create routing entry\n forward reply"| A
```

Step by step:

1. The requesting node hashes the file name to get key $K$.
2. In its routing table, it finds the entry whose key is *numerically closest* to $K$ and forwards the request to that node's address.
3. Each intermediate node repeats: find the routing table entry with the key closest to $K$, forward there.
4. When a node that has the file is found, it returns the file contents **and claims to be the owner** — even if it is not the original creator, just a caching intermediary.
5. The reply travels back hop by hop along the same path.
6. Every node on the return path **caches a copy of the file** and **creates a new routing table entry** pointing to whoever supplied it (which may be a fake owner — see §6.3).

**Why do intermediate nodes cache?** This is the mechanism by which popular data gets widely replicated. Every successful query spreads the file to all intermediate nodes. Future queries for the same file have a shorter path to travel — and more fake owners to confuse trackers.

**Why does every node claim to be the owner?** This is the core anonymity mechanism. If every node that has ever touched a file claims ownership, a legal investigator facing dozens of "owners" in a large network cannot determine which one actually created it.

### 5.2 Failure Handling During a Query

A query can fail for two reasons: the path creates a **cycle** (the pseudo-random query ID detects this — a node refuses to forward a query it has already seen), or a node simply has no further routing table entries to try.

When a node cannot forward:
- It first tries the **second-closest key** in its routing table instead of the closest.
- It can keep trying progressively further keys.
- The TTL field decrements at every hop regardless, so the query eventually dies if nothing is found.

**Dynamic TTL reduction:** if the network is congested (too many messages), nodes can reduce the TTL faster than one-per-hop to shed load. Nodes can also use the TTL value to prioritize which queued request to process next — higher remaining TTL = more urgent.

### 5.3 Search Quality: How the Network Improves Over Time

Freenet starts cold — routing tables are sparse and searches fail often. Over time:

**Information disseminates.** Every successful query plants routing table entries and cached files along its path. The more queries the network processes, the richer every node's routing table becomes.

**Nodes aggregate files with similar keys.** Because routing always moves toward numerically closer keys, a node tends to accumulate cached copies of files whose keys are numerically near its own routing table entries. Over time, a node becomes a de-facto specialist for a neighborhood of the key space.

**Popular data replicates widely.** A heavily-requested file gets cached by every node that ever handled a query for it. This makes popular data easy to find and extremely hard to eradicate.

**Routing tables grow without revealing identities.** New entries get created whenever a query path passes through a node, but the node only learns the next hop — not the full path. The network map is discovered incrementally and anonymously.

---

## 6. Data Storage: How You Insert a File

### 6.1 The Insert Procedure

To insert a file into the Freenet network:

1. The user creates a key: `key = hash(filename)`.
2. The user sends an `insert` message to their own local node, containing: `(file, key, TTL)`.
3. The local node checks its routing table:
   - If `key` is already there → it returns the existing contents (collision — see below).
   - If not → it finds the closest key in its routing table and **forwards the insert message** in that direction.
4. This forwarding continues, hop by hop, toward the node whose routing table entry is closest to `key`.
5. The file eventually lands at a node that cannot find anyone closer — and that node stores it.

**The crucial anonymity property of insertion:** the original owner does **not** keep a copy. The file is sent away into the network, routed toward a node with numerically similar keys, and stored there. The inserter's connection to the content is immediately severed — the file is now geographically and topologically far from whoever created it.

### 6.2 Two Termination Strategies

There are two ways an insert can legitimately end:

**Strategy 1 — Closest key:** the insert propagates until it reaches a node where no neighbor has a closer key. That node stores the file. This is the more intelligent approach — the file lands as close as possible to its "correct" position in the key space, which makes future lookups efficient.

**Strategy 2 — TTL exhaustion:** the insert is forwarded $k$ hops in the direction of the closest key, and when the TTL reaches 0, whatever node currently holds it stores it. This is simpler but less precise about placement.

In both cases, on success:
- The terminal node (and possibly the inserter's own node) add the file and key to their stores.
- Every node on the path adds the key and a routing entry to its table.
- Every node caches a copy of the file.
- The original inserter is notified via back-propagation.

### 6.3 Beating Security on Insert: Lying About Ownership

When a node on the insertion path caches the file and creates a routing table entry, what address does it record as the "source"?

It has two options, both of which add anonymity:

- **Claim itself as the owner**: record its own IP address in the routing entry. Anyone querying this node in the future will be told "I am the owner."
- **Point to a neighbor**: record the address of whichever neighbor it forwarded to (or received from). This creates a further layer of indirection.

Both strategies create **fake owners**. In a large network, dozens or hundreds of nodes along the paths of all queries that have ever touched this file will all claim ownership. An investigator faces an impossible signal-to-noise problem: who among all these claimants actually created the file?

**The hash collision case:** if during insertion the target node already has a file with the same key (hash collision), it passes the data *back upstream* to the node that sent it, which then caches it locally. This also means the file gets stored, just at a different node.

### 6.4 Advantages of This Storage Mechanism

**Files land near nodes with similar keys.** This is not accidental — the routing always moves toward numerically closer keys, so the file naturally lands in a neighborhood of the key space where future lookups will also naturally arrive. Insertion and retrieval use the same routing logic, so they converge to the same location.

**Information about new files disseminates quickly.** Every node on the insert path gets a routing entry. From the moment of insertion, $O(\text{TTL})$ nodes already know where the file is.

**Deliberate hash collision attacks are difficult.** An attacker trying to spam the network with fake inserts to displace legitimate files would need to predict hash outputs — cryptographically hard. Legitimate collisions are handled gracefully by bouncing the file to the upstream node.

---

## 7. Data Management: Finite Storage and LRU

Both the routing table and the data store are **finite structures**. They cannot grow indefinitely. The management policy is **LRU (Least Recently Used)**:

- When a new file or routing entry must be stored and there's no space, the oldest, least-recently-accessed entry is evicted.
- This ensures old, unpopular data gradually disappears from the network.

**Legal implication of LRU:** a node can claim it did not deliberately retain any specific content — files it once held may have been silently evicted to make room for newer traffic. The node had no editorial control over what it stored. This is the **deniability of storers** design goal in action.

This also means Freenet provides **no guarantee of permanence**. Files that are not actively requested will eventually fall out of the network. Popular files self-replicate (via caching on query paths) and effectively become permanent. Rare files gradually disappear.

---

## 8. Encryption for Deniability

Deniability can be strengthened further using encryption. The mechanism:

- When inserting a file, the original owner **encrypts the file content using the file key** (or a derived key).
- The encrypted content circulates through the network — nodes store and forward it without being able to read it.
- Any node that knows the key can **decrypt** the content; nodes that don't know the key cannot.

**The deniability argument:** a node storing an encrypted file can honestly say it had no idea what content it held — it could not distinguish an illegal file from a legal one because everything was encrypted ciphertext. The "I didn't know what I was storing" defense has real legal weight in some jurisdictions.

**The catch:** the final consumer must know the decryption key, and that key cannot be distributed via Freenet itself (that would defeat the encryption). Key sharing must happen through some other out-of-band channel. This is a significant practical limitation of the encryption approach.

**Participation alone may be illegal:** in many jurisdictions, merely running a Freenet node that routes and caches content — even without knowing what that content is — may be sufficient for legal liability depending on local law. The encryption argument provides a defense but not a guarantee.

---

## 9. Message Format and Protocol Details

### 9.1 Message Fields

Freenet messages are self-contained packets, sent over either TCP (reliable) or UDP (unreliable). Every message — whether a query or an insert — contains three mandatory fields:

| Field | Size | Purpose |
|---|---|---|
| Transaction ID | 64 bits | Uniquely identifies this transaction; prevents cycles (a node won't forward a transaction ID it has already seen) |
| TTL counter | Variable | Decremented at every hop; kills the message when it reaches 0 |
| Depth field | Variable | Starts at a random value, **incremented** at every hop; used to defeat TTL-based tracing attacks |

### 9.2 The TTL Vulnerability and the Depth Field Fix

**The attack:** an eavesdropper (e.g., a law enforcement node) inside the network can observe the TTL value on a passing message. If TTL was initialized to 10 and the eavesdropper sees TTL=5, it deduces the requester is exactly 5 hops away — and can use triangulation to narrow down the source.

There are two defenses:

**Defense 1 — Random TTL propagation:** when the TTL field reaches 1 (about to die), instead of stopping, the node probabilistically continues forwarding the message to other nodes. This adds random noise to the apparent "distance" of the source.

**Defense 2 — The depth field (the main fix):**

The depth field starts at a **random positive value** (not zero) and is incremented at every hop. When the destination node (the one that has the file) is about to send the reply back, it sets:

$$\text{TTL}_{\text{return}} = \text{depth}_{\text{current}}$$

**Why this works:**

Say the true distance from requester to destination is $k$ hops. The depth field started at some random value $r > 0$ and was incremented $k$ times, so at the destination it equals $r + k$.

The return TTL is set to $r + k$, which is guaranteed to be $\geq k$ (the message won't die in transit) but is not *equal* to $k$ (an eavesdropper can't measure the exact distance). How much greater than $k$ it is depends on $r$, which is unknown to any eavesdropper.

**The three constraints satisfied:**
- TTL must be $\geq k$: otherwise the reply dies before reaching the requester.
- TTL must not be exactly $k$: otherwise an eavesdropper learns the exact distance.
- The excess above $k$ must be random: otherwise the eavesdropper could infer $k$ from the TTL anyway.

The depth field with a random initialization satisfies all three.

```mermaid
sequenceDiagram
    participant R as Requester
    participant M as Middle Node (eavesdropper)
    participant D as Destination

    R->>M: query, TTL=10, depth=5 (random start)
    Note over M: sees TTL=9, depth=6. Knows it's ≥1 hop from source. Cannot tell exact distance.
    M->>D: query, TTL=8, depth=7
    Note over D: distance from R = 2 hops. depth=7. Sets return TTL=7.
    D-->>M: reply, TTL=6
    Note over M: sees TTL=6. Cannot determine if R is 1 or 6 hops away.
    M-->>R: reply, TTL=5
```

### 9.3 Timers and Reliability

For every request, the requester starts an **absolute timer**. If the timer expires with no reply:
- It infers failure.
- It may try again with a different routing path.

Downstream nodes that are still processing (congestion, slow search) can send a **`Reply.Restart`** message to the requester. On receiving this, the requester **extends its timer** — it knows the request is still in flight, just delayed. This prevents premature failure declarations in a slow but functioning network.

### 9.4 Message Types

| Message | When sent | Meaning |
|---|---|---|
| `Send.Data` | File found | Success; includes file content and (possibly fake) source ID |
| `Reply.NotFound` | TTL reached 0 with no result | No file found within the TTL radius |
| `Request.Continue` | No more paths, TTL > 0 | Stuck — requester should try other routing table entries |
| `Reply.Restart` | Downstream node congested | "Still working, extend your timer" |

---

## 10. Naming, Searching, and Security

### 10.1 Organizing Files Without a Central Directory

**The problem:** in a large anonymous network, how does a user find files without a central search engine?

A central directory or Google-like search engine is incompatible with anonymity — whoever maintains the index becomes a legal target, and the index itself reveals what content exists in the network.

**The solution — distributed metadata files:**

Indirect files containing metadata are scattered throughout the network. A directory is itself a file in Freenet, with a key. It contains a mapping from keywords to the keys of actual files.

For complex searches, multiple keyword-index files can exist independently. Searching for a file by multiple terms means:
1. Query the network for the keyword-A index file → get a set of keys.
2. Query for the keyword-B index file → get another set of keys.
3. Take the intersection → keys of files matching both terms.

This is a fully distributed search with no central coordinator.

**Content integrity:** to ensure a file has not been tampered with in transit, a **content hash** can accompany the file. Any node receiving the file can verify the hash; if it doesn't match, the file was corrupted or deliberately altered.

**Bookmark lists:** in jurisdictions where operating a Freenet directory is legally safe, node operators can publish bookmark lists — collections of keys to notable files, shared via the same Freenet mechanisms.

### 10.2 Sender Anonymity

Sender anonymity means a neighbor cannot tell whether the node it is talking to is the original requester or merely a forwarding relay.

**Why this holds:** since every node participates in forwarding queries on behalf of others, any given query arriving at node $B$ from node $A$ could have originated at $A$, or it could have originated at some unknown node further back in the chain that asked $A$ to forward it. There is no way for $B$ to distinguish these cases.

**The 1-hop visibility rule is the key:** a node only knows its immediate neighbors. It cannot see two hops back. This structural constraint — not any cryptographic trick — is what provides sender anonymity at the routing level.

**Message-level eavesdroppers:** a passive attacker who can read messages between specific pairs of nodes can potentially correlate timing and content to infer who is requesting what. Defense: encrypt all messages between node pairs. This prevents eavesdroppers from learning which key is being requested even if they can observe traffic volume.

### 10.3 Pre-routing and Layered Encryption

If a requester has a detailed enough routing table (knows the full path to the destination), it can use **pre-routing**: it decides the entire routing path in advance and encrypts the message in successive layers, one per hop.

```
Message for destination D, path: A → B → C → D

Encrypted as: Encrypt_A( Encrypt_B( Encrypt_C( Encrypt_D( payload ) ) ) )
```

At each hop, the node peels one layer of encryption (using its private key), revealing only the address of the next hop. No node can see further than one hop ahead, and no node can determine who the original sender is.

**Limitation:** this only works if the requester knows the full path, which requires a detailed routing table. In practice, routing tables are incomplete and pre-routing is used selectively.

---

## 11. Summary: The Four Pillars of Freenet Anonymity

Everything in Freenet's design reduces to four mechanisms working together:

**Pillar 1 — Request denial (1-hop visibility):** a node can never verify whether its neighbor is the original requester or just a relay. Every node plausibly deniable as "just forwarding."

**Pillar 2 — Sender denial (fake ownership):** every node that touches a file during a successful query claims to be the owner. Multiple fake owners across the network make it impossible to identify the true original creator.

**Pillar 3 — Insertion anonymity:** the original inserter does not keep the file. It is routed away to a remote node. The inserter's causal link to the content is severed as soon as the insert is complete.

**Pillar 4 — TTL obfuscation via the depth field:** the depth field with a random initial value prevents an eavesdropper from inferring the number of hops to the source from the TTL value.

```mermaid
flowchart TD
    A["Freenet Anonymity"] --> B["Request Denial\n(1-hop visibility only)"]
    A --> C["Sender Denial\n(fake ownership claims)"]
    A --> D["Insertion Anonymity\n(file sent away from creator)"]
    A --> E["TTL Obfuscation\n(randomized depth field)"]
    B --> F["Requester identity hidden"]
    C --> F
    C --> G["Provider identity hidden"]
    D --> G
    E --> F
```

No single pillar is sufficient alone. Together, they make Freenet substantially more anonymous than any previous P2P system — though not perfectly so. Timing attacks, traffic analysis, and infiltration by adversarial nodes can still yield partial information.

---

## 12. Evaluation

### 12.1 Setup

| Parameter | Value |
|---|---|
| Network size | 500 to 900 nodes |
| Items per node | 40 |
| Routing table size | 50 addresses max |
| Network topology | Linear chain (worst case — not a realistic best-case topology) |
| Query load tested | 50 to 1200 queries |

The chain topology is deliberately conservative — it forces messages to travel long paths and gives fewer routing shortcuts than a realistic random-graph topology. Results should be interpreted as lower bounds.

### 12.2 Results: Successful Requests vs. Number of Queries

**The key finding: success rate rises rapidly with query volume due to information dissemination.**

| Node count | Success at low query rate | Success at high query rate |
|---|---|---|
| 500 nodes | ~20% (at 50 queries) | ~100% (at 300 queries) |
| 600–900 nodes | ~10% (at start) | ~100% (at 400–500 queries) |

**Interpretation:** the "warm-up" period reflects the cold-start problem — a fresh network has sparse routing tables and low replication. As queries run, information spreads, routing tables fill in, and popular files get replicated widely. After warm-up, essentially all queries succeed.

**The trade-off with node count:** larger networks have lower initial success rates (more nodes = harder to find any one file before information disseminates) and a longer warm-up. But they reach the same ~100% ceiling eventually.

The important practical takeaway: **Freenet is not a fast-start system.** It is designed for steady-state operation in a mature network, not immediate responsiveness in a fresh one.

### 12.3 Results: Hops vs. Number of Queries

**The key finding: hop count drops quadratically as query volume increases.**

- At 20 queries: ~50 hops average.
- At 600+ queries: ~10 hops average.
- More nodes = more hops (larger network = more distance to cover).

**Why hops decrease with more queries:** as more queries run, routing tables fill in with entries closer to the keys being requested. The informed routing (forward toward the closest key) becomes more effective as the routing tables become richer. What was a 50-hop grope through an unfamiliar network becomes a 10-hop directed walk through a well-mapped one.

The quadratic decrease is faster than linear — each additional query improves routing quality not just for itself but for all future queries that travel similar paths. The benefit of each query compounds.

**The limitation of the chain topology:** in a real network with richer connectivity, both the initial hop counts and the warm-up time would be substantially lower. The chain is a stress test, not a representative deployment scenario.
"""
            }
        }
    },
    "04-logical-clocks-mutual-exclusion": {
        "title": "Logical Clocks and Mutual Exclusion",
        "description": "Event ordering, causal consistency, vector timestamps, and distributed critical sections.",
        "topics": {
            "logical-clocks": {
                "title": "Lamport Logical Clocks",
                "content": """# Lamport Logical Clocks

In distributed systems, physical clocks can drift due to hardware variance, making it impossible to rely on physical wall-clock timestamps to order events. Leslie Lamport introduced **Logical Clocks** to define a consistent chronological order of events based on causality.

---

## 1. The Happens-Before Relation ($a \\to b$)

The happens-before relation (denoted $\\to$) defines a strict causal ordering of events:

1.  **Local Ordering**: If event $a$ and event $b$ occur within the same process, and $a$ occurs before $b$ locally, then $a \\to b$.
2.  **Message Passing**: If event $a$ is the sending of a message by one process, and event $b$ is the receipt of that same message by another process, then $a \\to b$.
3.  **Transitivity**: If $a \\to b$ and $b \\to c$, then $a \\to c$.

> **Concurrence ($a \\parallel b$)**: If neither $a \\to b$ nor $b \\to a$, the events are said to be concurrent.

---

## 2. Lamport Clock Update Rules

Each process $P_i$ maintains a local integer counter $L_i$ (initialized to 0). The clock is updated using two rules:

*   **Rule 1 (Local Event)**: Before executing a local event, process $P_i$ increments its local clock:
    $$L_i \\gets L_i + 1$$
*   **Rule 2 (Message Passing)**:
    *   When process $P_i$ sends a message $m$, it attaches its current clock value: $(m, L_i)$.
    *   Upon receiving message $(m, L_{msg})$, the receiving process $P_j$ updates its clock and increments it:
        $$L_j \\gets \\max(L_j, L_{msg}) + 1$$

```mermaid
sequenceDiagram
    participant P1
    participant P2
    
    Note over P1: L1=0
    Note over P2: L2=0
    P1->>P1: Event a (L1=1)
    P1->>P2: Send Message m1 (L1=2)
    Note over P2: Receive m1 (max(0, 2) + 1 = 3)
    P2->>P2: Event b (L2=4)
```

---

## 3. Total Ordering of Events

Lamport clocks only provide a partial order: if $a \\to b$, then $L(a) < L(b)$. However, $L(a) < L(b)$ does **not** imply $a \\to b$ (events could be concurrent).

To resolve ties and create a **Total Order** (denoted $\\implies$), we use process identifiers as tie-breakers. Event $a$ at process $P_i$ occurs before event $b$ at process $P_j$ if:

$$a \\implies b \\iff (L(a) < L(b)) \\quad \\text{or} \\quad (L(a) = L(b) \\ \\text{and} \\ i < j)$$
"""
            },
            "vector-clocks": {
                "title": "Vector Clocks and Causality",
                "content": """# Vector Clocks and Causality

While Lamport clocks generate a total order, they cannot detect concurrent events. If $L(a) < L(b)$, we cannot distinguish whether $a \\to b$ or if they are concurrent ($a \\parallel b$). **Vector Clocks** overcome this limitation, allowing processes to detect causal violations and concurrent updates.

---

## 1. Vector Clock Update Rules

For a system of $N$ processes, each process $P_i$ maintains an integer array $V_i$ of size $N$ (initialized to all zeros).

*   **Rule 1 (Local Event)**: Before executing a local event, process $P_i$ increments its own component:
    $$V_i[i] \\gets V_i[i] + 1$$
*   **Rule 2 (Message Passing)**:
    *   When process $P_i$ sends a message $m$, it attaches its vector: $(m, V_i)$.
    *   Upon receiving $(m, V_{msg})$, process $P_j$ merges the vectors element-wise, increments its own component, and records the receipt:
        $$\\forall k \\in [1, N], \\quad V_j[k] \\gets \\max(V_j[k], V_{msg}[k])$$
        $$V_j[j] \\gets V_j[j] + 1$$

---

## 2. Comparing Vector Timestamps

A vector timestamp $V(a)$ causally precedes $V(b)$ if and only if every element in $V(a)$ is less than or equal to the corresponding element in $V(b)$, and at least one element is strictly smaller:

$$V(a) \\le V(b) \\iff \\forall k \\in [1, N], \\ V(a)[k] \\le V(b)[k]$$
$$V(a) < V(b) \\iff V(a) \\le V(b) \\quad \\text{and} \\quad \\exists k \\ \\text{s.t.} \\ V(a)[k] < V(b)[k]$$

### 2.1 Causal Equivalence
Using vector clocks, the logical order matches the causal order exactly:

$$a \\to b \\iff V(a) < V(b)$$

### 2.2 Concurrency Detection
If neither $V(a) \\le V(b)$ nor $V(b) \\le V(a)$, then the events are **concurrent**:

$$a \\parallel b \\iff \\neg(V(a) \\le V(b)) \\ \\wedge \\ \\neg(V(b) \\le V(a))$$

This property is crucial for detecting conflicts in distributed replication systems (such as Amazon Dynamo).
"""
            },
            "mutual-exclusion": {
                "title": "Distributed Mutual Exclusion Algorithms",
                "content": """# Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion ensures that multiple processes executing in a network can coordinate access to a shared resource (the **Critical Section** or CS) without conflicts.

---

## 1. Classifications of Mutex Algorithms

1.  **Permission-Based**: A process must request permission from a set of coordinator/peer nodes before entering the CS.
2.  **Token-Based**: A single virtual "token" circulates through the network. The process holding the token has the exclusive right to enter the CS.

---

## 2. Core Mutual Exclusion Algorithms

### 2.1 Lamport's Permission-Based Algorithm
*   **Mechanism**: Uses Lamport logical clocks. A process broadcasts a request with its timestamp. Peers place requests in local priority queues and reply. A process enters the CS when its request is at the head of its queue and it has received acknowledgments with larger timestamps from all peers.
*   **Message Complexity**: $3(N-1)$ messages per CS entry (Request, Reply, Release).

### 2.2 Ricart-Agrawala Algorithm
*   An optimization of Lamport's algorithm. Instead of sending explicit Release messages, processes defer replying to requests with timestamps smaller than their own pending request.
*   **Message Complexity**: $2(N-1)$ messages per CS entry.

### 2.3 Maekawa's Quorum Algorithm
*   Processes do not request permission from all peers. Instead, they request permission from a subset of processes called a **Quorum** ($S_i$).
*   **Rules**:
    *   Intersection: $\\forall i, j, \\ S_i \\cap S_j \\ne \\emptyset$ (any two quorums must overlap by at least one node).
    *   Symmetry: $|S_i| = K \\approx \\sqrt{N}$.
*   **Message Complexity**: $3\\sqrt{N}$ messages per CS entry.

---

## 3. Comparison Summary

| Algorithm | Message Complexity | Synchronization Delay | Single Point of Failure |
| :--- | :--- | :--- | :--- |
| **Centralized** | $3$ | $2$ | Yes (Coordinator) |
| **Ricart-Agrawala** | $2(N-1)$ | $1$ round-trip | Yes (Any node crash) |
| **Maekawa** | $3\\sqrt{N}$ | $2$ | Yes (Quorum node crash) |
| **Token Ring** | $0$ to $N$ | $N/2$ average | Yes (Token loss) |
"""
            }
        }
    },
    "05-distributed-leader-election": {
        "title": "Distributed Leader Election",
        "description": "Coordination in dynamic groups: ring-based election, bully algorithms, and LeLann-Chang-Roberts limits.",
        "topics": {
            "ring-election": {
                "title": "Ring-Based Election Algorithms",
                "content": """# Ring-Based Election Algorithms

Leader election is a fundamental coordination problem where a group of processes must agree on a single coordinator node. In **Ring-based Election**, nodes are logically organized in a unidirectional circle, and messages can only be forwarded to a node's immediate successor.

---

## 1. The Chang-Roberts Algorithm

The Chang-Roberts algorithm is designed for a ring of size $N$ where nodes have unique numeric identifiers. All nodes are initially in a `Non-Participant` state.

```mermaid
graph TD
    N1((Node 17)) -->|Election 17| N2((Node 4))
    N2 -->|Election 17| N3((Node 23))
    N3 -->|Election 23| N4((Node 12))
    N4 -->|Election 23| N1
    style N3 fill:#f9f,stroke:#333
```

### 1.1 Execution Rules
1.  **Initiation**: Any node that detects the leader has failed starts an election. It marks itself as a `Participant`, creates an `Election(ID)` message containing its own ID, and sends it to its successor.
2.  **Receiving Election(incoming_ID)**: When node $i$ receives an `Election(incoming_ID)`:
    *   If $\\text{incoming_ID} > i$: Forward `Election(incoming_ID)` and set state to `Participant`.
    *   If $\\text{incoming_ID} < i$:
        *   If not a `Participant`, change ID in the message to $i$, forward it, and set state to `Participant`.
        *   If already a `Participant`, drop the message.
    *   If $\\text{incoming_ID} = i$: Node $i$ has received its own message back. It is the coordinator! It changes state to `Non-Participant` and sends a `Coordinator(i)` message around the ring.
3.  **Receiving Coordinator(leader_ID)**: Nodes update their record of the leader, set state to `Non-Participant`, and forward the message.

---

## 2. Complexity Analysis

*   **Best Case**: Nodes are ordered such that the election initiator is immediately followed by nodes with decreasing IDs. The election message circles the ring once:
    $$\\text{Messages} = 2N - 1$$
*   **Worst Case**: Initiator is immediately preceded by the largest ID. The message must circle multiple times:
    $$\\text{Messages} = O(N^2)$$
*   **Average Case**: If IDs are distributed randomly:
    $$\\text{Messages} = O(N \\log N)$$
"""
            },
            "bully-algorithm": {
                "title": "The Bully Election Algorithm",
                "content": """# The Bully Election Algorithm

The Bully Algorithm (proposed by Hector Garcia-Molina) is a classic leader election protocol for synchronous distributed systems. It assumes that processes have unique IDs and that any process can communicate directly with any other process via point-to-point links.

---

## 1. Core Messaging Protocol

The algorithm uses three message types:

1.  **Election**: Initiates an election process.
2.  **Answer (OK)**: Sent by a higher-ID node to cancel a lower-ID node's bid.
3.  **Coordinator**: Sent by the winning node to announce its leadership.

---

## 2. Operational Phases

When a process $P_i$ detects that the coordinator has failed:

1.  **Challenge Higher Nodes**: $P_i$ sends an `Election` message to all processes with larger IDs: $P_{i+1}, P_{i+2}, \\ldots, P_N$.
2.  **Wait for Answer**: $P_i$ waits for an `Answer` message for a timeout period $T$.
    *   **Case A (No Answer)**: If no higher node answers, $P_i$ "bullies" its way into leadership. It sends a `Coordinator(i)` message to all processes with lower IDs and becomes the leader.
    *   **Case B (Answer Received)**: If any higher node answers with `Answer`, $P_i$ stands down and waits for a `Coordinator` message from the new leader.
3.  **Higher Node Action**: When a higher process $P_h$ ($h > i$) receives `Election` from $P_i$, it replies with `Answer` and immediately starts its own election by sending `Election` messages to nodes with IDs greater than $h$.

```mermaid
sequenceDiagram
    participant P1 (ID=1)
    participant P2 (ID=2)
    participant P3 (ID=3)
    
    Note over P1: Detects Leader Fail
    P1->>P2: Election
    P1->>P3: Election
    P2-->>P1: Answer (OK)
    Note over P2: Starts own election
    P2->>P3: Election
    Note over P2: No Answer from P3 (failed)
    P2->>P1: Coordinator (2)
```

---

## 3. Complexity & Evaluation

*   **Message Complexity**:
    *   Worst case: Lower-ID node starts the election when all nodes are alive. The complexity is $O(N^2)$ messages.
    *   Best case: The second-highest node detects failure and immediately becomes leader. Requires $N-2$ messages.
*   **Limitation**: Relies on strict synchronization. If network delays exceed timeout $T$, a slow process might incorrectly think higher nodes are dead, causing election churn.
"""
            },
            "lcr-algorithm": {
                "title": "The LeLann-Chang-Roberts (LCR) Bound",
                "content": """# The LeLann-Chang-Roberts (LCR) Bound

The LCR (LeLann-Chang-Roberts) algorithm is a classic comparison-based leader election algorithm for synchronous rings. It serves as a benchmark for analyzing the theoretical limits of distributed message complexity.

---

## 1. Algorithm Description

LCR operates in synchronous rounds on a unidirectional ring of size $N$:

*   In each round, every active node $i$ sends its ID (as a message) to its successor.
*   Upon receiving an ID $j$:
    *   If $j > i$: Node $i$ forwards $j$ to its successor.
    *   If $j < i$: Node $i$ discards the message.
    *   If $j = i$: Node $i$ has received its own ID. It declares itself leader and sends a termination message.

---

## 2. Theoretical Lower Bounds

LCR is highly simple but provides key proofs for distributed algorithm bounds:

*   **Message Complexity**: $O(N \\log N)$ on average, and $O(N^2)$ in the worst case (when IDs are in decreasing order around the ring).
*   **Lower Bound Proof**: It is proven that for *comparison-based* election on a synchronous ring where node count $N$ is unknown, any algorithm must send at least:
    $$\\Omega(N \\log N) \\quad \\text{messages}$$
    Thus, LCR is asymptotically optimal in message complexity for comparison-based algorithms.
"""
            }
        }
    },
    "06-dmst-flp": {
        "title": "Distributed MST and the FLP Result",
        "description": "Gallager-Humblet-Spira (GHS) distributed MST, and the limits of asynchronous consensus.",
        "topics": {
            "distributed-mst": {
                "title": "Distributed Minimum Spanning Tree (GHS)",
                "content": """# Distributed Minimum Spanning Tree (GHS)

The Gallager-Humblet-Spira (GHS) algorithm is a classic distributed protocol for finding a Minimum Spanning Tree (MST) in an arbitrary connected network. It allows decentralized nodes to find the optimal network routing backbone using localized message passing.

---

## 1. GHS Core Concepts and States

Nodes start as single-node tree **fragments**. Fragments merge iteratively by finding their **Minimum Weight Outgoing Edge (MWOE)**.

*   **Edge States**:
    *   `Basic`: Unexplored edges.
    *   `Branch`: Edges selected to be part of the MST.
    *   `Rejected`: Edges confirmed to connect nodes within the same fragment (creating cycles).
*   **Levels**: Each fragment has a Level $L$ (initially 0).

---

## 2. Fragment Merging Rules

When two fragments $F_1$ and $F_2$ identify a common MWOE, they merge based on their levels:

### 2.1 Merge ($L_1 < L_2$)
If fragment $F_1$ has a lower level than $F_2$, $F_1$ merges into $F_2$. $F_1$ updates its level to $L_2$.

### 2.2 Friendly Merge ($L_1 = L_2$)
If levels are equal, the fragments merge and form a new fragment at level $L+1$. The shared MWOE becomes a `Branch` edge, and the node with the higher ID becomes the leader of the new fragment.

---

## 3. Complexity

*   **Message Complexity**: Finding MWOE requires $O(E + N \\log N)$ messages.
*   **Time Complexity**: Runs in $O(N \\log N)$ time.
"""
            },
            "flp-impossibility": {
                "title": "The FLP Impossibility Proof",
                "content": """# The FLP Impossibility Proof

The **FLP Impossibility Result** (published by Fischer, Lynch, and Paterson in 1985) is one of the most critical theorems in distributed computing. It establishes the absolute theoretical boundaries of consensus protocols in asynchronous networks.

---

## 1. The Impossibility Theorem

> **Theorem**: In an asynchronous network, no deterministic consensus protocol can guarantee both Safety and Liveness in the presence of even a single unannounced process crash.

*   **Safety (Agreement)**: No two processes decide on different values.
*   **Liveness (Termination)**: All non-faulty processes eventually decide.

---

## 2. Proof Architecture: Bivalence and Configurations

The proof uses graph-theoretic configurations of the distributed system:

### 2.1 System Configurations
A **Configuration** $C$ represents the global state of the system (states of all processes and messages currently in transit).

*   **Univalent**: A configuration is univalent if the decision value is locked.
    *   **0-valent**: All possible execution paths from $C$ lead to a decision of $0$.
    *   **1-valent**: All possible execution paths from $C$ lead to a decision of $1$.
*   **Bivalent**: The decision is not yet determined. From $C$, some execution paths lead to a decision of $0$, while others lead to $1$.

### 2.2 Proof Steps
1.  **Lemma 1 (Bivalent Initial State)**: There exists an initial configuration $C_0$ that is bivalent (depends on the starting inputs).
2.  **Lemma 2 (Preserving Bivalence)**: From any bivalent configuration $C$, there exists a step (a message delivery) that keeps the system in a bivalent state.
3.  **Infinite Loop**: Since the system is asynchronous, an adversarial scheduler can delay messages such that the system transitions from bivalent state to bivalent state infinitely, preventing termination.

---

## 3. Circumventing FLP in Practice

To build real-world systems, we must relax the asynchronous consensus assumptions:
*   **Partial Synchrony**: Assume boundaries on message delays (used by Paxos, Raft).
*   **Randomization**: Use probabilistic consensus (used in blockchains).
*   **Failure Detectors**: Use partially accurate oracle failure detectors (e.g., Chandra-Toueg).
"""
            },
            "consensus-bounds": {
                "title": "Theoretical Bounds on Consensus",
                "content": """# Theoretical Bounds on Consensus

Distributed consensus bounds vary dramatically depending on system assumptions (synchronous vs. asynchronous, crash-stop vs. Byzantine faults).

---

## 1. Synchronous System Bounds

In a synchronous system (where message delays have a known upper bound $D$):

*   **Round Complexity**: If up to $f$ processes can crash, any deterministic consensus protocol requires at least:
    $$f + 1 \\quad \\text{rounds}$$
    to guarantee agreement.
*   **Fault Tolerance**:
    *   Under **Crash-Stop (Fail-Stop)** faults: Consensus is possible for any $f < N$.
    *   Under **Byzantine** faults: Consensus is possible if and only if $f < N/3$.

---

## 2. Asynchronous System Bounds

*   Under **Crash-Stop** faults: FLP Impossibility proves that deterministic consensus is impossible for $f \\ge 1$.
*   **Randomized Consensus**: If protocols can toss coins (randomized steps), consensus terminates in $O(1)$ expected rounds with probability 1.
"""
            }
        }
    },
    "07-consistency-cap": {
        "title": "Consistency Models and the CAP Theorem",
        "description": "Linearizability, causal systems, the formal CAP theorem proof, and PACELC trade-offs.",
        "topics": {
            "consistency-models": {
                "title": "Data Consistency Models",
                "content": """# Data Consistency Models

In replicated storage systems, the consistency model defines the rules governing the ordering and visibility of read and write operations.

---

## 1. Strong Consistency (Linearizability)

**Linearizability** is the strongest consistency model for single-object operations.

*   **Rule**: Every operation must appear to take effect instantaneously at some point in time between its invocation and its response.
*   **Implication**: Once a write completes, all subsequent reads (in real time) must return the new value or a newer one.

```mermaid
sequenceDiagram
    participant Client A
    participant DB (Linearizable)
    participant Client B
    
    Client A->>DB: Write(x=5)
    DB-->>Client A: Ok
    Note right of Client B: Read starts after Write returns
    Client B->>DB: Read(x)
    DB-->>Client B: 5 (Must return 5)
```

---

## 2. Sequential Consistency

Proposed by Lamport, **Sequential Consistency** relaxes the real-time constraint of linearizability:

*   **Rule**: The result of any execution is the same as if the operations of all processors were executed in some sequential order, and the operations of each individual processor appear in this sequence in the order specified by its program.
*   **Difference**: Operations do not need to take effect instantly in real-time, but all clients must agree on the *exact same order* of updates.

---

## 3. Causal Consistency

A weaker, highly scalable model that only orders causally related events:

*   **Rule**: Operations that are causally related must be seen by every node in the same order. Operations that are concurrent may be seen in different orders by different nodes.
*   **Detection**: Uses vector clocks to track causal relationships.
"""
            },
            "cap-theorem": {
                "title": "The CAP Theorem and Proof",
                "content": """# The CAP Theorem and Proof

The **CAP Theorem** (Brewer's Conjecture, formalized by Seth Gilbert and Nancy Lynch in 2002) states that a distributed read-write register can guarantee at most two of three properties simultaneously.

---

## 1. CAP Definitions

*   **Consistency (C)**: Equivalent to **Linearizability**. Every read returns the most recent write or an error.
*   **Availability (A)**: Every non-failing node returns a non-error response to every request (without guaranteeing it contains the most recent write).
*   **Partition Tolerance (P)**: The system continues to operate despite arbitrary message loss or network partitions.

---

## 2. Formal Proof (Gilbert & Lynch)

The proof constructs a network partition scenario:

```mermaid
graph LR
    subgraph Cluster Side G1
        A[Node A]
    end
    subgraph Cluster Side G2
        B[Node B]
    end
    A -.-x B[Network Partition]
```

1.  Assume a system of two nodes, $A$ and $B$, separated by a network partition (Property $P$).
2.  Client 1 writes a new value $v_1$ to Node $A$.
    *   To be **Available (A)**, Node $A$ must accept the write and return `Ok`.
3.  Because of the partition, Node $A$ cannot send the update to Node $B$.
4.  Client 2 reads from Node $B$.
    *   To be **Available (A)**, Node $B$ must respond without waiting.
    *   Node $B$ only knows the old value $v_0$.
5.  Node $B$ returns $v_0$, violating **Consistency (C)**.

> **Conclusion**: In the presence of a partition (P), a distributed system must choose either Consistency (CP) or Availability (AP).

---

## 3. Architectural Choices

*   **CP Systems**: Deny reads/writes during partitions to guarantee consistency (e.g., Google Spanner, HBase, ZooKeeper).
*   **AP Systems**: Accept writes locally and resolve conflicts later, sacrificing consistency (e.g., DynamoDB, Cassandra).
"""
            },
            "pacelc-theorem": {
                "title": "The PACELC Theorem Extension",
                "content": """# The PACELC Theorem Extension

While the CAP theorem describes system behavior during partitions, systems spend most of their time operating normally. Daniel Abadi formulated the **PACELC Theorem** in 2012 to describe the trade-offs during normal operations.

---

## 1. PACELC Formulation

The theorem states:

$$\\text{If there is a } \\mathbf{P} \\text{artition, trade off } \\mathbf{A} \\text{vailability vs. } \\mathbf{C} \\text{onsistency};$$
$$\\text{E} \\text{lse, trade off } \\mathbf{L} \\text{atency vs. } \\mathbf{C} \\text{onsistency}.$$

---

## 2. Trade-off Analysis

Even when there are no network faults, a database must make a choice:

*   **PC/EC**: High consistency during partitions, high consistency during normal operations (e.g., Spanner).
*   **PA/EL**: High availability during partitions, low latency during normal operations (e.g., Dynamo, Cassandra). Writes return immediately without waiting for replicas to acknowledge.
"""
            }
        }
    },
    "08-paxos-raft": {
        "title": "Paxos and Raft Consensus Protocols",
        "description": "Multi-Paxos round dynamics, consensus safety, and Raft leader election invariants.",
        "topics": {
            "paxos-consensus": {
                "title": "Paxos Consensus Protocol",
                "content": """# Paxos Consensus Protocol

Paxos is the foundational consensus protocol for fault-tolerant distributed systems. It allows a set of nodes to agree on a single value despite node crashes and network delays.

---

## 1. Roles in Paxos

*   **Proposers**: Advocate for client values by initiating proposals.
*   **Acceptors**: Vote on proposals and form the quorum memory.
*   **Learners**: Read the agreed-upon consensus value.

---

## 2. Single-Decree Paxos Protocol

Paxos operates in two distinct phases:

### Phase 1 (Prepare)
1.  **Phase 1a (Prepare)**: A Proposer selects a unique proposal number $n$ and broadcasts `Prepare(n)` to a majority of Acceptors.
2.  **Phase 1b (Promise)**: If $n$ is greater than any proposal number the Acceptor has seen, it promises not to accept any proposals numbered less than $n$, and returns the highest-numbered proposal it has already accepted (if any): `Promise(n, accepted_num, accepted_val)`.

### Phase 2 (Accept)
1.  **Phase 2a (Accept)**: If the Proposer receives promises from a majority of Acceptors, it selects a value $v$ (the value of the highest-numbered proposal among the promises, or its own value if no proposals were returned). It sends `Accept(n, v)` to the Acceptors.
2.  **Phase 2b (Accepted)**: If an Acceptor receives `Accept(n, v)`, it accepts the proposal unless it has already made a promise to a higher proposal number. It sends `Accepted(n, v)` to the Proposer and Learners.

```mermaid
sequenceDiagram
    participant Proposer
    participant Acceptor A
    participant Acceptor B
    
    Proposer->>Acceptor A: Prepare(n=1)
    Proposer->>Acceptor B: Prepare(n=1)
    Acceptor A-->>Proposer: Promise(n=1, null, null)
    Acceptor B-->>Proposer: Promise(n=1, null, null)
    Proposer->>Acceptor A: Accept(n=1, v="val")
    Proposer->>Acceptor B: Accept(n=1, v="val")
    Acceptor A-->>Proposer: Accepted(n=1, v="val")
    Acceptor B-->>Proposer: Accepted(n=1, v="val")
```
"""
            },
            "raft-consensus": {
                "title": "The Raft Consensus Protocol",
                "content": """# The Raft Consensus Protocol

Raft is a consensus algorithm designed to be easy to understand compared to Paxos. It decomposes consensus into three subproblems: Leader Election, Log Replication, and Safety.

---

## 1. Raft Roles and Terms

A Raft node is in one of three states: **Leader**, **Follower**, or **Candidate**. Time is divided into **Terms** of arbitrary length, acting as logical clocks.

```mermaid
stateDiagram-v2
    Follower --> Candidate: Timeout (Start Election)
    Candidate --> Candidate: Timeout (New Election)
    Candidate --> Leader: Receives Majority Votes
    Candidate --> Follower: Discovers Leader / Higher Term
    Leader --> Follower: Discovers Higher Term
```

---

## 2. Core Mechanisms

### 2.1 Leader Election
1.  Followers increment their term and transition to Candidates if they receive no heartbeat within an election timeout.
2.  Candidates vote for themselves and send `RequestVote` RPCs to peers.
3.  If a candidate receives votes from a majority of nodes, it becomes the Leader.

### 2.2 Log Replication
The leader coordinates client writes:
1.  Leader appends command to local log.
2.  Leader sends `AppendEntries` RPCs to followers.
3.  Once a majority of followers acknowledge the entry, the leader commits it and applies it to its local state machine.

---

## 3. Raft Safety Invariants

Raft guarantees five safety properties:

*   **Election Safety**: At most one leader can be elected per term.
*   **Leader Append-Only**: A leader never overwrites or truncates its log; it only appends.
*   **Log Matching**: If two logs contain an entry with the same index and term, then they are identical up to that index.
*   **Leader Completeness**: If a log entry is committed in a given term, that entry will be present in the logs of the leaders for all higher-numbered terms.
*   **State Machine Safety**: If a server has applied a log entry at a given index to its state machine, no other server will ever apply a different log entry for the same index.
"""
            },
            "consensus-comparison": {
                "title": "Paxos vs. Raft Comparison",
                "content": """# Paxos vs. Raft Comparison

| Feature | Paxos | Raft |
| :--- | :--- | :--- |
| **Understandability** | Low (Difficult to conceptualize) | High (Decomposed into clean states) |
| **Leader Model** | Symmetric (Any proposer can write) | Strong Leader (Only leader can replicate) |
| **Log Gaps** | Allowed (Requires filling null values) | Prohibited (Logs must remain sequential) |
| **Safety Logic** | Derived from intersection of quorums | Enforced by strict leader election rules |
| **Performance** | High (Multi-Paxos avoids Phase 1) | Equal to Multi-Paxos under normal loads |
"""
            }
        }
    },
    "09-byzantine-virtual-synchrony": {
        "title": "Byzantine Generals and Virtual Synchrony",
        "description": "Consensus under malicious faults, group communication membership, and view deliveries.",
        "topics": {
            "byzantine-generals": {
                "title": "The Byzantine Generals Problem",
                "content": """# The Byzantine Generals Problem

The Byzantine Generals Problem (formalized by Lamport, Shostak, and Pease in 1982) models consensus in systems where nodes can fail arbitrarily, including sending conflicting information, lying, or acting maliciously.

---

## 1. Problem Formulation

Let there be $N$ generals coordinating an attack. Some generals may be traitors.
*   **Agreement**: All loyal generals must agree on the same action (Attack or Retreat).
*   **Validity**: If the commander is loyal, all loyal generals must follow the commander's order.

---

## 2. Limits of Byzantine Agreement

### 2.1 The $3m + 1$ Impossibility Rule
> **Theorem**: No consensus is possible if $N \\le 3m$, where $m$ is the number of traitors.

For $m=1$, agreement is impossible with $N=3$ nodes:

```mermaid
graph LR
    C[Commander - Loyal] -->|1. Attack| G1[General 1 - Loyal]
    C -->|2. Attack| G2[General 2 - Traitor]
    G2 -->|3. Commander said Retreat| G1
```

General 1 cannot distinguish whether the Commander is loyal and General 2 is a traitor, or if the Commander is a traitor who sent conflicting messages.

---

## 3. Practical Byzantine Fault Tolerance (PBFT)

PBFT is a state machine replication protocol designed for Byzantine environments:

*   **Message Phases**: `Pre-Prepare` $\\to$ `Prepare` $\\to$ `Commit`.
*   Requires a quorum of $2f + 1$ matches out of $3f + 1$ total nodes to progress, guaranteeing safety even if $f$ nodes are malicious.
"""
            },
            "virtual-synchrony": {
                "title": "Virtual Synchrony",
                "content": """# Virtual Synchrony

Virtual Synchrony is a programming model for group communication. It guarantees that membership changes (view changes) and message multicasts are delivered in a coordinated, atomic manner.

---

## 1. Group Views

Nodes are organized into a **Group**. The state of the group at any time is represented by a **View** $V_i = \\{\\text{list of active nodes}\\}$.

*   When a node joins or fails, a **View Change** is triggered, producing a new view $V_{i+1}$.

---

## 2. Synchronization Guarantees

*   **Atomic Delivery**: If two nodes transition from View $V_i$ to $V_{i+1}$, they must have received the exact same set of multicast messages while in View $V_i$.
*   **Flush Protocol**: Before a new view can be installed, all pending messages in the current view must be acknowledged and "flushed" to all active members.
"""
            }
        }
    },
    "10-bitcoin-blockchains": {
        "title": "Bitcoin and Blockchains",
        "description": "Nakamoto consensus, Proof of Work, Merkle trees, UTXO validation, and smart contracts.",
        "topics": {
            "proof-of-work": {
                "title": "Nakamoto Consensus and Proof of Work",
                "content": """# Nakamoto Consensus and Proof of Work

Bitcoin introduced **Nakamoto Consensus**, a breakthrough in distributed systems that solves Byzantine consensus at global scale without relying on a fixed, known set of validators.

---

## 1. Proof of Work (PoW) Mechanism

To prevent Sybil attacks (where a malicious actor creates millions of virtual nodes to dominate votes), voting power is tied to physical computation.

*   **The Cryptographic Puzzle**: Nodes (miners) must find a nonce value such that the hash of the block header is less than a target value $T$:
    $$\\text{SHA256}(\\text{SHA256}(\\text{BlockHeader})) < T$$
*   **Difficulty Adjustment**: Every 2016 blocks, the target $T$ is adjusted based on hash rate to keep block generation times stable (approximately 10 minutes).

---

## 2. Nakamoto Routing Rules

*   **Longest-Chain Rule**: Nodes always accept and build on the chain with the most accumulated Proof of Work (the longest valid chain).
*   **Double-Spend Protection**: If two blocks are mined simultaneously, a fork occurs. The fork is resolved when miners build on one of the branches, making it longer. The other branch is orphaned.
"""
            },
            "blockchain-mechanics": {
                "title": "Blockchain Data Structures",
                "content": """# Blockchain Data Structures

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

*   **Benefit**: Allows lightweight clients to verify if a transaction is included in a block using only $O(\\log N)$ hash proofs (the Merkle Path).

---

## 2. UTXO Model

Bitcoin uses the **Unspent Transaction Output (UTXO)** model:
*   Transactions do not update account balances. Instead, they consume existing UTXOs (inputs) and create new UTXOs (outputs).
*   **Verification**: A transaction is valid if the inputs are currently unspent and are signed by the rightful owner.
"""
            }
        }
    },
    "11-dynamo-cassandra-percolator": {
        "title": "Amazon Dynamo, Facebook Cassandra, and Google Percolator",
        "description": "Industrial distributed data stores: masterless replication, vector clocks, LSM trees, and 2-phase transactions.",
        "topics": {
            "amazon-dynamo": {
                "title": "Amazon Dynamo",
                "content": """# Amazon Dynamo

Amazon Dynamo is a highly available, masterless key-value store. It is designed to prioritize write availability over consistency (an AP system under CAP).

---

## 1. Core Architectural Pillars

Dynamo combines several distributed techniques:

*   **Consistent Hashing**: Data is distributed across a hash ring using virtual nodes.
*   **Tunable Quorums ($N, R, W$)**:
    *   $N$: Number of replicas.
    *   $R$: Number of nodes that must respond to a read.
    *   $W$: Number of nodes that must acknowledge a write.
    *   If $R+W > N$, the system guarantees read-your-writes consistency.
*   **Sloppy Quorums and Hinted Handoff**: If preferred nodes are down, writes are accepted by temporary healthy nodes which forward them once the primary recovers.
*   **Vector Clocks**: Used to detect concurrent updates and capture version branching.

---

## 2. Conflict Resolution

Because Dynamo prioritizes availability, writes can branch during partitions. When the partition heals, readers must resolve conflicts. Dynamo uses **vector clocks** to detect these conflicts, forcing the application client to merge divergent branches.
"""
            },
            "facebook-cassandra": {
                "title": "Facebook Cassandra",
                "content": """# Facebook Cassandra

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
"""
            },
            "google-percolator": {
                "title": "Google Percolator",
                "content": """# Google Percolator

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
"""
            }
        }
    },
    "12-voldemort-condor-dryadlinq": {
        "title": "Voldemort, Condor, and Microsoft DryadLINQ",
        "description": "Industrial key-value routing, high-throughput scheduling, and compiler-integrated dataflow graphs.",
        "topics": {
            "project-voldemort": {
                "title": "Project Voldemort (LinkedIn)",
                "content": """# Project Voldemort (LinkedIn)

Project Voldemort is LinkedIn's distributed key-value storage system, heavily inspired by the Amazon Dynamo paper.

---

## 1. Routing Architectures

Voldemort supports two routing strategies:

*   **Client-Side Routing**: The client maintains the partition map and routes requests directly to the correct storage nodes. This minimizes hop latency but increases client complexity.
*   **Server-Side Routing**: Clients send requests to a random node, which forwards it to the correct partition coordinator.

---

## 2. Comparison with Amazon Dynamo

While Voldemort mirrors Dynamo's architecture (consistent hashing, vector clocks, tunable quorums), it differs by focusing on modular storage engines (pluggable BDB, MySQL, or Read-Only storage) and separating the storage layer from the routing layer for easier maintenance.
"""
            },
            "condor-scheduler": {
                "title": "The Condor High Throughput Scheduler",
                "content": """# The Condor High Throughput Scheduler

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
"""
            },
            "dryadlinq-execution": {
                "title": "Microsoft DryadLINQ",
                "content": """# Microsoft DryadLINQ

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
"""
            }
        }
    }
}

# 3. Create folders and files
for week_folder, week_info in weeks_data.items():
    week_path = os.path.join(BASE_DIR, week_folder)
    os.makedirs(week_path, exist_ok=True)
    os.makedirs(os.path.join(week_path, "lectures"), exist_ok=True)
    
    # Write _chapter.yml
    chapter_meta = {
        "title": week_info["title"],
        "chapter": week_folder,
        "description": week_info["description"],
        "topics": list(week_info["topics"].keys())
    }
    with open(os.path.join(week_path, "_chapter.yml"), "w", encoding="utf-8") as f:
        yaml.dump(chapter_meta, f, default_flow_style=False, sort_keys=False)
        
    readme_content = f"""---
title: "{week_info["title"]}"
---

# {week_info["title"]}

{week_info["description"]}

## Topics

"""
    for topic_slug, topic_info in week_info["topics"].items():
        readme_content += f"- [[{topic_slug}]] — {topic_info['title']}\n"
        
    readme_content += """
## Learning Objectives

- [ ] Master core concepts in this week's scope.
- [ ] Understand key protocol rules and edge cases.
- [ ] Complete exercises and self-evaluation.
"""
    with open(os.path.join(week_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)
        
    # Write each topic file
    for topic_slug, topic_info in week_info["topics"].items():
        fm = {
            "title": topic_info["title"],
            "subject": "distributed-systems",
            "chapter": week_folder,
            "tags": ["distributed-systems", "systems"],
            "date": "2026-06-24",
            "updated": "2026-06-24",
            "status": "complete",
            "difficulty": "advanced"
        }
        fm_str = "---\n" + yaml.dump(fm, default_flow_style=False, sort_keys=False) + "---\n"
        file_path = os.path.join(week_path, f"{topic_slug}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(fm_str + "\n" + topic_info["content"].strip())
            
    print(f"Generated {week_folder} ({week_info['title']})")

print("All weeks successfully scaffolded!")
