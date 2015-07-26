# Paper Reading Notes: Column-Stores vs. Row-Stores: How Different Are They Really?

Link to paper: [ACM website for citations](http://dl.acm.org/citation.cfm?id=1376712), [full pdf](http://db.csail.mit.edu/projects/cstore/abadi-sigmod08.pdf).

## Overview

SQL databases are typically row-oriented. These row-stores (RS) are well suited for applications such as _customer relationship management_, but ill-suited for online _analytical processing_ (OLAP) such as data mining.

This paper compares the performance of RS and column-stores (CS) databases. The contributions are:

1. Comparison of RS and CS databases on a standard benchmark.
2. Lists, explain and measure _gains_ of different _optimizations_ in _CS_ databases.
3. Address the question of whether _adapting_ the schema of a _RS_ to me more CS-like can yield similar performance gain as _switching_ to a CS database.
4. Proposes and measures the performance of a _novel optimization_ for CS databases: _invisible join_.

The _main findings_ are:

1. CS can outperform RS by about a factor 10 _for some workloads_. 
2. Performance gains: late materialization: 3x, compression: 2x.
3. Attempts to adapt RS schemas to be more CS-like by method such as _vertical partitioning_, creating _indexes for every column_ and _optimal materialized views_ did not improve performance of RS as much as switching to CS.
4. Invisible join improves performance by 50%.

Those results suggest that one should pick a database system that is well suited for the expected workload.

However, the reason RS optimizations did not yield good result does not mean that it is not possible to build a RS database that can have _similar performances under OLAP workload given CS-like optimizations_. The authors claim that _current_ RS databases are _not coded in a way_ that can take advantage of those optimizations.

## 1. Introduction

### 1.1 Vocabulary:

- Record: unit of data stored in a database (e.g.: person: (Paul, CA, 25)).
- Attribute: sub-part of record (e.g.: person.age).
- Predicate: {true, false} function used to filter entities (e.g.: person.age > 25).
- Locality of reference: it is much faster to access data in a contiguous manner.

## 4. Row Oriented Execution

Section 4 discusses _optimizations_ that can be introduced to a _RS_ database to _mimic_ a _CS_ database.

Although those optimization seem like a good idea, the authors show that _none_ of them _perform_ particularly _well_.

### 4.1 Vertical Partitioning

Vertical partitioning: _entities are split in tables_, one table per attribute. 

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

This section reviews optimization that a CS can use. Most of those optimizations hinge on the idea that in CS, you can do thing faster since you do not need to read / process unrelated data (that you necessarily have to skip over if processing row-by-row).

### 5.1 Compression

Data in a _column_ has _less variance_ than data across rows (less entropy), it can therefore be compressed more efficiently. The main _gain_ from compression is _reduced I/O_, rather than saving disk space. One must take care to select appropriate compression algorithms where speed of decompression is optimized at the cost of saving disk space. Another saving from compression is that some predicates can operate directly on (smaller) compressed data (think of binary comparison for example).

### 5.2 Early Materialization, Late Materialization

**Materialization** is the creation of a tuple that represents information required to complete an operation, which can be any of the attribute from any of the tables (attribute in dimension tables must be fetched with a join operation). 

#### Early Materialization

To complete a query, it is necessary to fetch the information from the SELECT statement in addition to all information necessary to run all the predicates.

For example, in a typical SQL query:

        SELECT <column_1, column_2, ..., column_n>
        FROM   <table_1, table_2, ..., table_n>
        WHERE  <predicate_1>
        AND    <predicate_2>
        [...]
        AND    <predicate_n>

... all predicates must return true for the engine to have to return the data from the SELECT line to the user. This means that it can skip fetching some of the data if a predicate is false. Therefore, the data is fetched in a _pipeline join_ in order of _predicate selectivity_.

This means that the SQL engine will progressively build a tuple of data as it processes the predicates. When it needs data from another table, it does an implicit join, applies the predicate, if the predicate return true it appends the data to the tuple and keep going.

This process is called _early materialization_ because the tuple is materialized from the moment the first predicate is run. If all predicates are run and the last one return false, the partially built tuple is simply discarded.

#### Late Materialization

Assuming CS (data in a column is stored sequentially), it is very efficient to apply predicates column-by-column instead of row-by-row. Since in a CS, _entities in a column are at a fixed offset_, that allows to keep a simple _binary mask_ (bit at offset i represents delegate on record at offset i) for all entities that are true for a predicate. Doing a binary AND for the bitmasks of all predicates yields the entities that pass all predicates. After this is done, the final output n-tuple can be materialized.

This has the potential to be faster than _early materialization_ since:

##### No superfluous data is read

Is a RS, some of the fields for a row might not be needed, but they need to be read anyways. Using CS / late materialization, no superfluous data is read.

##### Locality of Reference

In a RS, the data is stored in row-order, which means that after the original seek (which is the slowest operation in a read -- sequential read is extremely fast), only a bit of data can be read (the column required to run the predicate for the row) before having to seek again. 

##### No Partial Tuples Constructed

Since after doing the AND of all the columns it is possible to skip all rows for which one of the predicate is false. In RS / early materialization, the evaluation of predicate is done in a pipelined fashion, which means that if 9 out of 10 predicates are true and the 10th is false, a 9-tuple is constructed and thrown away. A 9-bit mask is necessarily smaller than a 9-tuple.

##### Block Iteration

The last section of 5.2 covered block iteration and why it is faster. It is worth mentioning that CS can also take advantage of the fact that column data will either be all fixed width, or all variable width. This means that column that are fixed width can be processed much faster. In RS, if any of the column of an record is of variable width, the whole record become variable width and that does away with the possible optimizations.

##### Invisible Join

Their innovation if a form of late materialization that they call _invisible join_ with an added optimization that result in less _out of order_ accesses.

In late materialization, when the output n-tuple is being constructed, only one of the column will likely be in sorted order. Because of _locality of reference_, reading the columns out-of-order is relatively slow.
