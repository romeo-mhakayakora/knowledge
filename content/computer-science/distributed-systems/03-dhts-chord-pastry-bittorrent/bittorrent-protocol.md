---
title: The BitTorrent P2P Protocol
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

# The BitTorrent P2P Protocol

BitTorrent is a highly popular peer-to-peer file distribution protocol. Unlike DHT overlays which focus on key routing, BitTorrent optimizes for high-throughput, parallel replication of large files across unstable networks.

---

## 1. BitTorrent Terminology and Components

BitTorrent splits files into small, equal-sized pieces (typically $256\text{ KB}$ to $2\text{ MB}$) to allow parallel downloading.

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
    $$d(x, y) = x \oplus y$$
    Peers store contacts in $k$-buckets based on their XOR distance.