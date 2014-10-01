
# Paper Reading Notes: Scaling Memcache At Facebook

Facebook uses memcache as a key-value cache in between frontend instances and MySQL databases. It is optimized for read-heavy scenarios where heavy read on SQL databases would be prohibitive. Memcache in itself is an in-memory, single computer, key-value cache; this paper explains how Facebook scaled this out to a multi-computer key-value cache with a SQL-backed permanent store.

Typically, a client connects to a front-end through a load-balancer, the frontend requests data needed to render the client's request (let's say a friend's feed) to many different memcache instances, aggregates all the results and returns the result to the client. This is done through an _all-to-all_ communication pattern, where frontends fetch data from many memcache instances (in theory, one frontend instance could be connected to all memcache instances; memcache instances do not communicate with each-other). 

Keywords: key-value stores, large scale distributed systems, distributed cache

Link to paper: [https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala](https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala).

## Key Concepts
- All-to-all communication pattern.
- McSqueal thingie.
- 

## Details

### Performance

Gets are performed using UDP, but writes and delete use a long-lived TCP connection proxy (called _mcrouter_ internally) which is shared between all threads on a machine.

The paper discussed TCP vs. UDP, with UDP having a ~20% latency benefit using a "try, if fail try again later" model where the client implements the retry logic. AAA section??

### ?? how they scaled and how they partitioned their keys ??

### ?? diagram of server / memcache / SQL

### Get (success), get (cache miss) and write (figure 1)

?? to get a chunk of data, the frontend 

### ...

?? collocation of data ??
?? how do you invalidate perimated data ??





