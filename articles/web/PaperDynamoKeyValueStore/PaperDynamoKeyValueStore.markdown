
# Paper Reading Note: Dynamo: Amazon's Highly Available Key-value Store

Dynamo is a key-value NoSQL database service that is designed for high availability and elastic scalability at the cost of lenient consistency. It offers an alternative to relational databases who are constrained by their requirement to support ACID properties which do not scale well horizontally.

The paper goes over a number of concepts that are useful to generic large-scale distributed systems.

Link to paper: [http://dl.acm.org/citation.cfm?id=1294281](http://dl.acm.org/citation.cfm?id=1294281)

Advantages:

* Higher throughput for read/writes than relational database. This is mainly due to using “eventual consistency” where a write returns before its data has been replicated to all N copies, allows to return from a read even if the queried node does not have the most recent copy of the data. This is a tradeoff for more availability at the cost of consistency.

* Can use nodes of heterogeneous capabilities (will only handle the load it can, allows multiple hardware generations in the same cloud).

* Elastic by default. You can add/remove nodes to the system without affecting the unchanged nodes or system’s availability.
Distributed by default. Across heterogeneous nodes and distributed to different data centers by default.

Drawbacks:

* Only supports get() and set(key, metadata, data) operations (as opposed to complex query in relational databases).
** Not clear from the paper how to structure data for a service when relational queries are not available.
* Requires that client implements merge logic because of the lax consistency requirements. This is somewhat alleviated by the use of vector clocks.

Key Concepts:

* Consistent hashing to achieve elastic scalability.
* Eventual consistency as a tradeoff for higher availability.
* Vector clocks for conflict resolution.
* Quorum, sloppy quorum (hinted handoff) and quorum parametrization.
* Merkle trees
* Gossip-based membership protocol.

