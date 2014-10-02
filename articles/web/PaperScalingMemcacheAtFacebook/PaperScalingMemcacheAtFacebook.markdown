
# Paper Reading Notes: Scaling Memcache At Facebook

Facebook uses memcache as a key-value cache in between frontend instances and MySQL databases. It is optimized for read-heavy scenarios where heavy read on SQL databases would be prohibitive. Memcache in itself is an in-memory, single computer, key-value cache; this paper explains how Facebook scaled this out to a multi-computer, multi-region key-value cache with a SQL-backed permanent store.

Typically, a client connects to a front-end through a load-balancer, the frontend requests data needed to render the client's request (let's say a friend's feed) to many different memcache instances, aggregates all the results and returns the result to the client. This is done through an _all-to-all_ communication pattern, where frontends fetch data from many memcache instances (in theory, one frontend instance could be connected to all memcache instances; memcache instances do not communicate with each-other). 

**Read**:

When a get issued to a memcache instance is successful ({key, value} pair in memory), the value is simply returned to the client. On a cache miss, the client is responsible for fetching the data from the MySQL database and then updating the read key in the memcache instances (see figure 1).

**Write**:

On a write (or delete), 

**???**:

Facebook is organized in _regions_ (machines geographically located togeter) and _clusters_ (set of machines in a region). Data is organized in one master MySQL database, and a number of replicas that can be in different regions / clusters (5.0).

A cluster contains a set of frontends (web servers that the client directly connects to), memcache instances and MySQL database instances. Each frontend is connected to a number (up to all) of memcache instances through a proxy named _mcrouter_. The memcache instances do not communicate with each other.

Key can be replicated to mutiple _clusters_ (Facebook's term for a geographically close cluster of computers), but I can't find any details on the criteria and how a frontend instance gets > 1 cache location from hashing a key.

When a write / delete occurs on a database (MySQL), a notification broadcaster (called "McSqueal") is notified and will notify each memcache instance containing the key of the change. The master / replica MySQL servers are kept in sync using MySQL's replication mechanism.

**Keywords**: key-value stores, memcache, large scale distributed systems, distributed cache.

**Link to paper**: [https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala](https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala).

## Key Concepts

- All-to-all communication pattern.
- Sliding window to avoid response overload on massive-keys-requests.
- Leases to avoid stale sets.
- UDP used for gets (fetch from cache miss on UDP packet lost), TCP for write and deletes.
- Gutter pool: using a fast-expiring cache that is used only temporarily if a main cache fails to alleviate cascading failures (3.3).
- Eventual consistency as a tradeoff to provide greater availability.

## Details



### Performance

Gets are performed using UDP, but writes and delete use a long-lived TCP connection proxy (called _mcrouter_ internally) which is shared between all threads on a machine.

The paper discussed TCP vs. UDP, with UDP having a ~20% latency benefit using a "try, if fail try again later" model where the client implements the retry logic. AAA section??

### ?? how they scaled and how they partitioned their keys ??







