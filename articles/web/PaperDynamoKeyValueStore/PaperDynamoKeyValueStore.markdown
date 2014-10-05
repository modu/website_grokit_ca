
# Paper Reading Note: Dynamo: Amazon's Highly Available Key-value Store

Dynamo is a key-value NoSQL database service that is designed for high availability and elastic scalability at the cost of lenient consistency. It offers an alternative to relational databases who are constrained by their requirement to support ACID properties which do not scale well horizontally.

The paper goes over a number of concepts that are useful to generic large-scale distributed systems. It is interesting even if you are not interested in using Dynamo because it explains a lot of themes present in most distributed computing problems.

**Link to paper**: [http://dl.acm.org/citation.cfm?id=1294281](http://dl.acm.org/citation.cfm?id=1294281), [full pdf](http://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf).

**Keywords**: key-value stores, large scale distributed systems

**Advantages**:

- Higher throughput for read/writes than relational database. 
 
    This is mainly due to using “eventual consistency” where a write returns before its data has been replicated to all N copies, allows to return from a read even if the queried node does not have the most recent copy of the data. This is a tradeoff for more availability at the cost of consistency.

- Can use nodes of heterogeneous capabilities (will only handle the load it can, allows multiple hardware generations in the same cloud).

- Elastic by default. You can add/remove nodes to the system without affecting the unchanged nodes or system's availability.
Distributed by default. Across heterogeneous nodes and distributed to different data centers by default.

**Drawbacks**:

- Only supports get() and set(key, metadata, data) operations (as opposed to complex query in relational databases).
- Requires that client implements merge logic because of the lax consistency requirements.

**Key Concepts**:

- Eventual consistency as a trade-off for higher availability (2.1).
- Consistent hashing to achieve elastic scalability (4.2).
  - Seeds nodes known to all nodes from configuration are used for initial state (4.8.2). 
- Key partitioning and key-data replication on nodes based on preference lists (4.3).
- Vector clocks for conflict resolution (4.4).
- Quorum and quorum parametrization (4.5, 4.6).
  - Sloppy quorum: skip over unhealthy nodes on read / write to avoid node starvation on outage (4.6).
  - Hinted handoff to copy keys to the temporary "next in hash ring" node when a node fails (4.6).
- Merkle trees (fancy term for a hash list implemented in a tree to be log(n), and hash list being simply a hash of every chunk of m bytes of data) to check which data needs to be synced between two nodes (4.7).
- Gossip-based protocol to keep track node's membership to a hash ring (4.8).

## Gossip-Based Protocol

In a network of N nodes that want to know each other state, a naive approach is for all nodes to broadcast its status to all node for all status changes. However, as the number of nodes grows, this approach does not scale.

A gossip approach uses statistical propagation; for example, every second, every node selects another node randomly and sends its state. There are thorough mathematical underpinnings to consider (see [8]), but intuitively this generates a finite amount of traffic as N increases (N communications every second, instead of N square for the previous algorithm). Also intuitively, if the rate of change is slow enough, all nodes end-up with up-to date information on all nodes. Of course, this is another case of eventual consistency as it can take a lot of time for information to propagate to other nodes.

## Unclear

It was not clear to me at first the difference between Dynamo and Amazon S3. Dynamo is for storing/retrieving small objects at very high throughput rates whereas Amazon S3 is used for huge objects that are not queried very frequently.

How to structure data for a service when relational queries are not available. Dynamo does support relational and non-relational DB for storage, when it uses SQL does it offer queries? Aren't SQL queries fundamentally incompatible with the consistent-hashing-node-partition used in Dynamo?
