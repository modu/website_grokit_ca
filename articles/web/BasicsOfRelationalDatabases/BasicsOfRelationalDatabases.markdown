# Short Introduction to Relational DataBase Management Systems (RDBMS).

## Interface and Architecture of Typical Row-Store Relational Database

Relational databases are structured in _tables_ that can refer to each other. A table is organized in _rows_ of information (also called a _record_). Each row has a set of _attributes_, which can be thought of as a property of a row. When grouped together, those attributes are referred to as a _column_ and typically have an associated name. The important thing to remember: **everything** is a value in a table.

	Table: friends_list

		(name)      (country)   (age)
		column_1    column_2    column_3
	Row_1   Paul        CA          25
	Row_2   Mary        CA          95
	[...] 
	Row_n   Jeanne      US          61

In the above example, a row of data of table ‘friends_list’ is (Paul, CA, 25). ‘95’ is the ‘age’ _attribute_ for Row_2 (name: Mary). Every table has a _primary key_, which uniquely identifies a row. In our example, the primary key could be the ‘name’ column (assuming that the names are unique in the whole database; in reality, primary keys are typically unique positive integers).

For historical reasons, RDBMS typically (physicalle) organize data by rows (because most early databases were dealing with online transaction processing (OLTP) type data). The physical data is stored on disk in a row-order: Paul, CA, 25; Mary, CA, 95; ... 61;. Next section will delve more in how the data is actually structured.

### How Tables Map to Data-Structures

Without any database administrator set constraint, the data is stored in an Index Allocation Map (IAM), which is basically a contigious array of data in no particular order alongside with an index ordered by id [Web_SQL_Datastructures, http://www.akadia.com/services/sqlsrv_data_structure.html]. This means that operations on columns stored in IAM must scan the entire table.

It is possible to create one (and only one!) clustered index per table, which structures data in a B-Tree whose keys are one of the column of the table (where that column has the property to have guaranteed unique entries).

It is possible to have indexes on more than one column, but requires the creation of a side-index (B-Tree again) containing tuples of (b-tree-id, actual-data-ref). Of course, this comes at the cost of more disk-data and more work to maintain consistency (everytime an entyr is update, so must its index).

For more information on the _data structure implementation_, I strongly suggest reading [Web_SQL_Datastructures, http://www.akadia.com/services/sqlsrv_data_structure.html].

### Relations Between Tables

Using simply one long table (a set of flat rows), it would be hard to represent arbitrary _composite_ data without duplication. For example, in the table of the previous section, what would happen if in addition to a county, we have query that require the population and gini coefficient for every person in the table?

It is possible to extend the table to contain columns ‘population’, ‘gini’ next to the ‘country’ column. This duplicates the information which wastes spaces and makes a simple update (CA’s population + 1 →  need to change all entries where ‘country’ = ‘CA’). A widely used relational model is the star schema [RDBMS_StarSchema, https://en.wikipedia.org/wiki/Star_schema], where the main table is called the _fact table_ and the anxiliary tables are called _dimensions tables_. Attributes in the fact tables that refer to records in a dimension table use a _foreign key_, which is really just a pointer to an entry in a different table.

	Table: countries 

		(name)      (population)
	Row_1   CA          35         
	Row_2   US          350        
	[...] 
	Row_n   DE          85       

### The SQL Language

SQL is a language that allows to run operation on a database. For example, here is a SQL statement that would return everyone living in CA:

SELECT column_name,
FROM table_name,
WHERE predicate

~~

SELECT age
FROM friends_table
WHERE age = 25;

@@ build those tables and queries.

@@ ‘problem’ when accessing data from dimension tables.

### Internals of a Query Processing

Tuple materialization.

## Column-Store Relational Database

@@@read more about that
[CStore, http://db.csail.mit.edu/projects/cstore/vldb.pdf]

The data is stored in disk in a column-fashion. The previous examples would have 3 columns: (names: Paul, Mary, Jeanne), (country: CA, CA, US), (ages: 25, 95, 61). The Record the data belongs to is identified by the index in the column at which the data is located [CStore_Paper, http://db.csail.mit.edu/projects/cstore/vldb.pdf].

# References

# Links

https://en.wikipedia.org/wiki/Relational_database
List of SQL commands: http://www.w3schools.com/sql/

# Code

dext.insertFile('sql_intro.py')

