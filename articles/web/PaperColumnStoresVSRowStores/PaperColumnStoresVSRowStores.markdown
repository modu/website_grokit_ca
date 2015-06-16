# Paper Reading Notes: Column-Stores vs. Row-Stores: How Different Are They Really?

## Overview

SQL databases are typically row-oriented. These row-stores (RS) are well suited for applications such as customer relationship management, but ill-suited for online analytical processing (OLAP) such as data mining.

This paper compares the performance of RS and column-stores (CS) databases for those workloads. The contributions are:

Comparison of RS and CS databases on a standard benchmark.
Lists, explain and measure gains of different optimizations in CS databases.
Address the question of whether adapting the schema of a RS to me more CS-like can yield similar performance gain as switching to a CS database.
Proposes and measures the performance of a novel optimization for CS databases: invisible join.

The main findings are:

CS can outperform RS by about a factor 10 _for some workloads_. 
Performance gains: late materialization: 3x, compression: 2x.
Attempts to adapt RS schemas to be more CS-like by method such as vertical partitioning, creating indexes for every column and optimal materialized views did not improve performance of RS as much as switching to CS.
Invisible join improves performance by 50%.

Those results suggest that one should pick a database system that is well suited for the expected workload.

However, the reason RS optimizations to me more CS-like did not yield good result does not mean that it is not possible to build a RS database that can have similar performances under OLAP workload given CS-like optimizations are not done. The authors claim that _current_ RS databases are not coded in a way that can take advantage of those optimizations.

## 1. Introduction

### 1.1 Vocabulary:

Entity: unit of data stored in a database (e.g.: person: (Paul, CA, 25)).
Attribute: Sub-part of entity (e.g.: person.age).
Predicate: {true, false} function used to filter entities (e.g.: person.age > 25).
Locality of reference: it is much faster to access data in a contiguous manner.

### 1.2 Review of RS / CS

#### 1.2.1 RS Typical Schema

                  (name)      (country)   (age)
                  column_1    column_2    column_3
    Entity_1      Paul        CA          25
    Entity_2      Mary        CA          95
    [...] 
    Entity_n      Jeanne      US          61

Data is stored on disk in a row-fashion: Paul, CA, 25; Mary, CA, 95; ... 61;.

Without any database administrator set constraint, the data is stored in an Index Allocation Map (IAM), which is basically a contigious array of data in no particular order alongside with an index ordered by id [Web_SQL_Datastructures, http://www.akadia.com/services/sqlsrv_data_structure.html]. This means that delegates operating on columns stored in IAM must scan the entire table.

Databases allow to create one clustered index per table, which structures the data in a B-Tree whose keys are one of the column of the table (where that column has the property to have guaranteed unique entries).

It is possible to have indexes on more than one index per table, but that necessitates that creation of another data structure (B-Tree again) containing a tuple of (b-tree-id, actual-data-ref). Of course, this comes at the cost of more disk-data and more work to maintain consistency.

#### 1.2.2 CS Typical Schema

The data is stored in disk in a column-fashion. The previous examples would have 3 columns: (names: Paul, Mary, Jeanne), (country: CA, CA, US), (ages: 25, 95, 61). The entity the data belongs to is identified by the index in the column at which the data is located [CStore_Paper, http://db.csail.mit.edu/projects/cstore/vldb.pdf].

## 4. Row Oriented Execution

Section 4 discusses optimizations that can be introduced to a RS database to mimic a CS database.

Although those optimization seem like a good idea, the authors show that none of them perform particularly well.

### 4.1 Vertical Partitioning

Entities are split in tables, one table per attribute. Since entities are not necessarily stored in order (hence the need for IAM), each attribute table stores the value alongside its position id (~= primary key of row the attribute belong to).

For example, the name column of the example RS in 1.2.2 becomes a list of (position, value) tuples:

    (2, Mary)
    (1, Paul)
    (n, Jeanne)

When doing a query on m columns, m-1 joins on the entity ID must be done. In order to speed-up joins, the authors tried to either cluster-index each table or use hash joins.

### 4.2 Index-Only Plans

Leave the data as in a RS, but create an index for every column.

### 4.3 Materialized View

Denormalize the data in tuples which fit the predicates that are often run on the database.

## 5. Column Oriented Execution

### 5.1 Compression

Data in a column has less variance than data across rows (less entropy), it can therefore be compressed more efficiently. The main gain from compression is reduced I/O, rather than saving disk space. One must take care to select appropriate compression algorithms where speed of decompression is optimized at the cost of saving disk space. Another saving from compression is that some predicates can operate directly on (smaller) compressed data (think of binary comparison for example).

### 5.2 Early Materialization, Late Materialization

In a CS database, tuples that represent the data needed to run the query’s predicates for a row are materialized in a row-by-row order. Materialization is the creation of a tuple that represents the information required to complete an operation, which can be any of the columns in the row in addition data which is present in other table(s) (and that must be fetched with a join operation). Predicate are run in order of most to least selective: the next predicate to run is fetched, if any data is missing it is fetched using a join operation and appended to the tuple. Once the operation is done for a row, a n-tuple is kept in memory and the same steps are repeated on the next row until all rows are done.

In a CS database, the predicates can be run on the columns separately. Since entities in a column are at a fixed offset, that allows to keep a simple binary mask (bit at offset i represents delegate on entity at offset i) for all entities that are true for a predicate, and doing a binary AND for the bitmasks of all predicates yields the entities that pass all predicates. Then, the tuple are materialized (hence ‘late materialization’). This avoids partial materialization for entities that eventually have a predicate that return false. It is also significantly faster to do things this way since no superfluous data is read. In a RS, the data is stored in row-order, which means that after the original seek (which is the slowest operation in a read -- sequential read is extremely fast), only a bit of data can be read (the column required to run the predicate for the row) before having to seek again. In CS, a large chunk of column information can be sequentially read, which is much more efficient.

### 5.3 Block Iteration

The last section of 5.2 covered block iteration and why it is faster. It is worth mentioning that CS can also take advantage of the fact that column data will either be all fixed width, or all variable width. This means that column that are fixed width can be processed much faster. In RS, if any of the column of an entity is of variable width, the whole entity become variable width and that does away with the possible optimizations.

### 5.4 Author’s Innovation: Invisible Join

See 5.2 for an overview of early and late materialization.

An issue with column late materialization is that data from the different columns is extracted out-of-order in the final tuple materialization, which has performance cost due to bad locality of reference.

An invisible join consist of the following steps:

Apply predicates on dimension tables.
Create 1 hash table per column. Hash is of <key →{0,1}>.
Do a binary AND on all keys (keep only keys that satisfy all predicates).

It is not clear to me how this is fundamentally different from late materialization. Also, after 3, the materialization will also be done out of order for all columns but the first one (assuming no correlation between column orders).