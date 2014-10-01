
# Paper Reading Notes: Scaling Memcache At Facebook

Facebook uses memcache as a key-value cache in between an internal server and a MySQL database. It is optimized for read-heavy scenarios where costly SQL queries are cached. Memcache in itself is an in-memory, single computer, key-value cache; this paper explains how Facebook scaled this out to a multi-computer SQL-databased backed permanent store with a caching layer. 

?? how they scaled and how they partitioned their keys ??

Their overarching architecture is a client connects to a front-end through a load-balancer, the frontend requests data needed to render the client request (let's say a friend's feed) to many different memcache instances, aggregates all the results and returns the request to the client. This is done through an _all-to-all_ communication pattern, where a typical request will require a frontend to fetch data from many memcache instances. Gets are performed using UDP, but writes and delete use a long-lived TCP connection proxy (called _mcrouter_ internally) which is shared between all threads on a machine.

## ?? diagram of server / memcache / SQL


## Get (success), get (cache miss) and write (figure 1)

?? to get a chunk of data, the frontend 


## ...

?? collocation of data ??
?? how do you invalidate perimated data ??

Keywords: key-value stores, large scale distributed systems, distributed cache

Link to paper: [https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala](https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala).

Key Concepts:
- All-to-all communication pattern.
- McSqueal thingie.

## Discussion

The paper discussed TCP vs. UDP, with UDP having a ~20% latency benefit using a "try, if fail try again later" model where the client implements the retry logic. AAA section??

