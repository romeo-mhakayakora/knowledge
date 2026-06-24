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
        "03-dhts-chord-pastry-bittorrent",
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
    "03-dhts-chord-pastry-bittorrent": {
        "title": "DHTs: Chord, Pastry, and BitTorrent",
        "description": "Structured peer-to-peer overlays, consistent hashing, finger tables, prefix routing, and parallel transfer protocols.",
        "topics": {
            "chord-protocol": {
                "title": "The Chord DHT Protocol",
                "content": """# The Chord DHT Protocol

Chord is a classic **Structured Peer-to-Peer** protocol implementing a Distributed Hash Table (DHT). It guarantees that finding a key in a network of $N$ nodes requires at most $O(\\log N)$ messages.

---

## 1. Consistent Hashing and Identifier Ring

Chord maps both nodes and keys into an $m$-bit identifier space using a cryptographic hash function (like SHA-1). The space is organized as a modulo-$2^m$ circle known as the **Chord Ring**.

*   **Node ID**: Hash of node's IP address.
*   **Key ID**: Hash of the data key.
*   **Successor Node**: Key $k$ is assigned to the first node whose ID is equal to or greater than $k$ in the ring. This node is called $\\text{successor}(k)$.

```mermaid
graph LR
    N0((Node 0)) --- N1((Node 1))
    N1 --- N3((Node 3))
    N3 --- N8((Node 8))
    N8 --- N14((Node 14))
    N14 --- N0
    style N0 fill:#f9f,stroke:#333
    style N3 fill:#ccf,stroke:#333
    style N8 fill:#ccf,stroke:#333
```

For example, on an $m=4$ ring (sizes $0-15$), key $k=5$ would be stored at node $N=8$ if the active nodes are $0, 1, 3, 8, 14$.

---

## 2. Chord Finger Table Routing

To avoid routing hops of $O(N)$ around the ring, each node $n$ maintains a routing table called the **Finger Table** with at most $m$ entries. The $i$-th entry of node $n$'s finger table points to:

$$\\text{Finger}[i] = \\text{successor}((n + 2^{i-1}) \\pmod{2^m})$$

### 2.1 Finger Table Example (Node 0, $m=4$)
For node $n=0$ on a ring with active nodes $\{0, 1, 3, 8, 14\}$:

| Index $i$ | Formula $n + 2^{i-1}$ | Target successor | Finger Node |
| :---: | :---: | :---: | :---: |
| 1 | $0 + 1 = 1$ | $\\text{successor}(1)$ | **1** |
| 2 | $0 + 2 = 2$ | $\\text{successor}(2)$ | **3** |
| 3 | $0 + 4 = 4$ | $\\text{successor}(4)$ | **8** |
| 4 | $0 + 8 = 8$ | $\\text{successor}(8)$ | **8** |

### 2.2 Routing Algorithm
When node $n$ queries for key $k$:
1.  Check if $k$ lies between $n$ and $\\text{successor}(n)$. If so, return $\\text{successor}(n)$.
2.  Otherwise, search the finger table for the closest predecessor node $n'$ to $k$.
3.  Forward the query to $n'$. The distance to the key is halved in each hop, yielding $O(\\log N)$ lookup time.

---

## 3. Node Joins and Stabilization

To maintain correct pointers under network churn, Chord nodes run a periodic **Stabilization** protocol:

1.  **stabilize()**: Node $n$ queries its successor for its predecessor $p$. If $p$ lies between $n$ and successor, $n$ updates its successor to $p$.
2.  **notify()**: Node $n$ tells its successor about its existence. If successor's predecessor is empty or $n$ is closer, successor updates predecessor to $n$.
"""
            },
            "pastry-protocol": {
                "title": "The Pastry DHT Protocol",
                "content": """# The Pastry DHT Protocol

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

> **Complexity**: Lookups complete in $O(\\log_{2^b} N)$ routing steps.

---

## 3. Proximity Routing (Network Locality)

Pastry leverages the Neighborhood Set to achieve **Proximity Routing**. During routing table initialization, a joining node requests states from nearby nodes. It copies routing rows from nodes that match its prefix digits and are physically close, ensuring that each routing hop travels the minimum physical network distance possible.
"""
            },
            "bittorrent-protocol": {
                "title": "The BitTorrent P2P Protocol",
                "content": """# The BitTorrent P2P Protocol

BitTorrent is a highly popular peer-to-peer file distribution protocol. Unlike DHT overlays which focus on key routing, BitTorrent optimizes for high-throughput, parallel replication of large files across unstable networks.

---

## 1. BitTorrent Terminology and Components

BitTorrent splits files into small, equal-sized pieces (typically $256\\text{ KB}$ to $2\\text{ MB}$) to allow parallel downloading.

*   **Torrent File**: Metadata containing piece hashes, file sizes, and the tracker URL.
*   **Tracker**: A centralized HTTP/HTTPS server that maintains a list of peers downloading the torrent.
*   **Seeder**: A peer that has a complete copy of the file and is only uploading.
*   **Leecher**: A peer that is actively downloading and uploading pieces.
*   **Swarm**: The group of all peers participating in sharing a specific torrent.

---

## 2. Swarm Dynamics and Algorithms

To maximize download speeds and prevent "freeriding," BitTorrent employs decentralized auction-like algorithms:

### 2.1 Rarest-First Selection
To prevent pieces from dying out in the swarm, leechers query their connected neighbors for their piece maps and download the **rarest pieces first**. This ensures high piece diversity in the swarm.

### 2.2 Choking Algorithm (Tit-for-Tat)
Each peer limits the number of concurrent uploads (typically to 4) by "choking" (refusing to send data to) other peers. It updates these decisions every 10 seconds:

1.  **Symmetric Exchange**: The peer measures the download rates from all connected neighbors. It unchokes the **4 peers** that are currently providing the highest download rates.
2.  **Optimistic Unchoking**: Every 30 seconds, the peer unchokes a **random peer**, regardless of its upload contribution. This allows new peers to acquire their first pieces and discovers faster uploaders.

---

## 3. Trackerless Torrents (Kademlia DHT)

Modern BitTorrent clients do not rely on central trackers. Instead, they use a structured Kademlia DHT overlay:

*   **Nodes as Trackers**: The swarm information is mapped to a key (the torrent's *InfoHash*).
*   **Kademlia Routing**: Routing is based on the XOR metric:
    $$d(x, y) = x \\oplus y$$
    Peers store contacts in $k$-buckets based on their XOR distance.
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
        
    # Write README.md for the chapter
    readme_content = f"""---
title: {week_info["title"]}
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
