## Column-Store Relational Database

@@@read more about that

The data is stored in disk in a column-fashion. The previous examples would have 3 columns: (names: Paul, Mary, Jeanne), (country: CA, CA, US), (ages: 25, 95, 61). The Record the data belongs to is identified by the index in the column at which the data is located [CStore_Paper, http://db.csail.mit.edu/projects/cstore/vldb.pdf].

# Misc

“ An index can be used to efficiently find all row matching some column in your query and then walk through only that subset of the table to find exact matches. If you don't have indexes on any column in the WHERE clause, the SQL server have to walk through the whole table and check every row to see if it matches, which may be a slow operation on big tables.”

http://dev.mysql.com/doc/refman/5.0/en/mysql-indexes.html

http://odetocode.com/articles/70.aspx
^^ this suggests that by default there are no index, but that index are created on demand. A normal index in a B-Tree that stores references to the row. This can be created on-demand on any column. A clustered index

https://msdn.microsoft.com/en-us/library/ms190457.aspx
“The only time the data rows in a table are stored in sorted order is when the table contains a clustered index. When a table has a clustered index, the table is called a clustered table. If a table has no clustered index, its data rows are stored in an unordered structure called a heap.”

https://msdn.microsoft.com/en-us/library/ms190457.aspx
“If a table is a heap and does not have any nonclustered indexes, then the entire table must be examined (a table scan) to find any row. This can be acceptable when the table is tiny, such as a list of the 12 regional offices of a company.”
^^ the lesson here is that you really have to optimize your SQL schema to the queries that will come-in.


## Editorial: Planetary Systems Implemented on SQL?

ACID: can you prevent locking the whole DB for all queries?

How would you deal with distributing the data? Can it be done in-schema?
Overview of SQL multi-site (see facebook paper).

KVP is too loose and necessitates writing modules on top of KVP to provide things like n-ary indexes and transaction support. CAP theorem is a fact, we have yet to find a good middle-ground between ACID and NoSQL.

It is foolish to bet against researchers and compilers, new SQL-like languages will emerge on top of KVP-like stores for “planetary-scale” applications.

Until then, you must learn the jungle of databases and what they are good at and what they are not. 

SQL will optimize the differences between RS / CS depending on the typical data flows. New implementation and compiler optimization will eat away at the CS advantage, will probably emerge a new implementation that will be flexible enough for those two.
SQL has its niche applications that will not go away, but supporting ACID limits how scalable SQL can be and how distributed the database can be.

SQL vs NoSQL: sometimes it is worth to stand back, review assumptions, and solve an _easier_ problem better.

## Discussion: CAP theorem, availability, scalability, …
https://en.wikipedia.org/wiki/MySQL#Limitations
Ensuring high availability requires a certain amount of redundancy in the system. For database systems, the redundancy traditionally takes the form of having a primary server acting as a master, and using replication to keep secondaries available to take over in case the primary fails. This means that the "server" that the application connects to is in reality a collection of servers, not a single server. In a similar manner, if the application is using a sharded database, it is in reality working with a collection of servers, not a single server. In this case, a collection of servers is usually referred to as a farm.[50] One of the projects aiming to provide high availability for MySQL is MySQL Fabric, an integrated system for managing a collection of MySQL servers, and a framework on top of which high availability and database sharding is built. MySQL Fabric is open-source and is intended to be extensible, easy to use, and to support procedure execution even in the presence of failure, providing an execution model usually called resilient execution. MySQL client libraries are extended so they are hiding the complexities of handling failover in the event of a server failure, as well as correctly dispatching transactions to the shards. As of September 2013, there is currently support for Fabric-aware versions of Connector/J, Connector/PHP, Connector/Python, as well as some rudimentary support for Hibernate and Doctrine. As of May 2014, MySQL Fabric is in the general availability stage of development.[51]
^^ SQL does not come with “high availability” in the box.

https://en.wikipedia.org/wiki/Codd%27s_12_rules
Rule 7: High-level insert, update, and delete:
The system must support set-at-a-time insert, update, and delete operators. This means that data can be retrieved from a relational database in sets constructed of data from multiple rows and/or multiple tables. This rule states that insert, update, and delete operations should be supported for any retrievable set rather than just for a single row in a single table.
^^ oh, oh: fundamentally can’t scale that?


## Read Stack

http://dba.stackexchange.com/questions/607/what-is-a-key-value-store-database
https://en.wikipedia.org/wiki/Database_normalization
https://en.wikipedia.org/wiki/Denormalization
https://en.wikipedia.org/wiki/Star_schema
https://en.wikipedia.org/wiki/Database
https://en.wikipedia.org/wiki/Join_(SQL)
https://en.wikipedia.org/wiki/Select_(SQL)
https://en.wikipedia.org/wiki/Column-oriented_DBMS
http://hepburndata.blogspot.com/2011/12/perspective-is-everything-why-even-most.html
http://www.toadworld.com/platforms/oracle/b/weblog/archive/2015/04/07/rise-and-fall-of-the-nosql-empire.aspx
http://dataconomy.com/sql-vs-nosql-need-know/
http://blogs.msdn.com/b/windowsazurestorage/archive/2010/11/06/how-to-get-most-out-of-windows-azure-tables.aspx
http://www.fullstackpython.com/no-sql-datastore.html

https://en.wikipedia.org/wiki/Database_index

[GoogleBigTable] http://static.googleusercontent.com/media/research.google.com/en/us/archive/bigtable-osdi06.pdf
