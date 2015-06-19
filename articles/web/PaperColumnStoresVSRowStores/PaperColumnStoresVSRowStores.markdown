# Paper Reading Notes: Column-Stores vs. Row-Stores: How Different Are They Really?

Link to paper: [ACM website for citations](http://dl.acm.org/citation.cfm?id=1376712), [full pdf](http://db.csail.mit.edu/projects/cstore/abadi-sigmod08.pdf).

## Overview

SQL databases are typically row-oriented. These row-stores (RS) are well suited for applications such as customer relationship management, but ill-suited for online analytical processing (OLAP) such as data mining.

This paper compares the performance of RS and column-stores (CS) databases for those workloads. The contributions are:

1. Comparison of RS and CS databases on a standard benchmark.
2. Lists, explain and measure gains of different optimizations in CS databases.
3. Address the question of whether adapting the schema of a RS to me more CS-like can yield similar performance gain as switching to a CS database.
4. Proposes and measures the performance of a novel optimization for CS databases: invisible join.

The __main findings__ are:

1. CS can outperform RS by about a factor 10 _for some workloads_. 
2. Performance gains: late materialization: 3x, compression: 2x.
3. Attempts to adapt RS schemas to be more CS-like by method such as vertical partitioning, creating indexes for every column and optimal materialized views did not improve performance of RS as much as switching to CS.
4. Invisible join improves performance by 50%.

Those results suggest that one should pick a database system that is well suited for the expected workload.

However, the reason RS optimizations to me more CS-like did not yield good result does not mean that it is not possible to build a RS database that can have similar performances under OLAP workload given CS-like optimizations are not done. The authors claim that _current_ RS databases are not coded in a way that can take advantage of those optimizations.

## 1. Introduction

### 1.1 Vocabulary:

- Record: unit of data stored in a database (e.g.: person: (Paul, CA, 25)).
- Attribute: sub-part of record (e.g.: person.age).
- Predicate: {true, false} function used to filter entities (e.g.: person.age > 25).
- Locality of reference: it is much faster to access data in a contiguous manner.

## 4. Row Oriented Execution

Section 4 discusses __optimizations__ that can be introduced to a __RS__ database to __mimic__ a __CS__ database.

Although those optimization seem like a good idea, the authors show that none of them perform particularly well.

### 4.1 Vertical Partitioning

Entities are split in tables, one table per attribute. 

Since entities are not necessarily stored in order (hence the need for IAM), each attribute table stores the value alongside its position id (~= primary key of row the attribute belong to).

For example, the name column of the example RS in 1.2.2 becomes a list of (position, value) tuples:

    (2, Mary)
    (1, Paul)
    (n, Jeanne)

When doing a query on m columns, m-1 joins on the record ID must be done. In order to speed-up joins, the authors tried to either cluster-index each table or use hash joins.

### 4.2 Index-Only Plans

Leave the data as in a RS, but create an index for every column.

### 4.3 Materialized View

Denormalize the data in tuples which fit the predicates that are often run on the database.

## 5. Column Oriented Execution

### 5.1 Compression

Data in a __column__ has __less variance__ than data across rows (less entropy), it can therefore be compressed more efficiently. The main __gain__ from compression is __reduced I/O__, rather than saving disk space. One must take care to select appropriate compression algorithms where speed of decompression is optimized at the cost of saving disk space. Another saving from compression is that some predicates can operate directly on (smaller) compressed data (think of binary comparison for example).

### 5.2 Early Materialization, Late Materialization

In a CS database, tuples that represent the data needed to run the query’s predicates for a row are materialized in a row-by-row order. Materialization is the creation of a tuple that represents the information required to complete an operation, which can be any of the columns in the row in addition data which is present in other table(s) (and that must be fetched with a join operation). Predicate are run in order of most to least selective: the next predicate to run is fetched, if any data is missing it is fetched using a join operation and appended to the tuple. Once the operation is done for a row, a n-tuple is kept in memory and the same steps are repeated on the next row until all rows are done.

In a CS database, the predicates can be run on the columns separately. Since entities in a column are at a fixed offset, that allows to keep a simple binary mask (bit at offset i represents delegate on record at offset i) for all entities that are true for a predicate, and doing a binary AND for the bitmasks of all predicates yields the entities that pass all predicates. Then, the tuple are materialized (hence ‘late materialization’). This avoids partial materialization for entities that eventually have a predicate that return false. It is also significantly faster to do things this way since no superfluous data is read. In a RS, the data is stored in row-order, which means that after the original seek (which is the slowest operation in a read -- sequential read is extremely fast), only a bit of data can be read (the column required to run the predicate for the row) before having to seek again. In CS, a large chunk of column information can be sequentially read, which is much more efficient.

### 5.3 Block Iteration

The last section of 5.2 covered block iteration and why it is faster. It is worth mentioning that CS can also take advantage of the fact that column data will either be all fixed width, or all variable width. This means that column that are fixed width can be processed much faster. In RS, if any of the column of an record is of variable width, the whole record become variable width and that does away with the possible optimizations.

### 5.4 Author’s Innovation: Invisible Join

See 5.2 for an overview of early and late materialization.

An issue with column late materialization is that data from the different columns is extracted out-of-order in the final tuple materialization, which has performance cost due to bad locality of reference.

An invisible join consist of the following steps:

- Apply predicates on dimension tables.
- Create 1 hash table per column. Hash is of key ? {0,1}.
- Do a binary AND on all keys (keep only keys that satisfy all predicates).

It is not clear to me how this is fundamentally different from late materialization. Also, after 3, the materialization will also be done out of order for all columns but the first one (assuming no correlation between column orders).
