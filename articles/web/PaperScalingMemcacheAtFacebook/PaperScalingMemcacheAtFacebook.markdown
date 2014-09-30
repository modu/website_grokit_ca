
# Paper Reading Notes: Scaling Memcache At Facebook

Facebook uses memcache as a key-value cache in between an internal server and a MySQL database. It is optimized for read-heavy scenarios where costly SQL queries are cached. Memcache in itself is an in-memory, single computer, key-value cache; this paper explains how Facebook scaled this out to a multi-computer SQL-databased backed permanent store with a caching layer. 

?? how do you invalidate perimated data ??
?? diagram of server / memcache / SQL

Keywords: key-value stores, large scale distributed systems, distributed cache

Link to paper: [https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala](https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala).

Key Concepts:


## Discussion

The paper discussed TCP vs. UDP, with UDP having a ~20% latency benefit using a "try, if fail try again later" model where the client implements the retry logic. AAA section??

