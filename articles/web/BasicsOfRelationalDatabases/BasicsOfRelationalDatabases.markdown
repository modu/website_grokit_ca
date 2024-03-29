# Short Introduction to Relational DataBase Management Systems (RDBMS).

## Interface and Architecture of Typical Row-Store Relational Database

Relational databases are structured in _tables_ that can refer to each other. A table is organized in _rows_ of information (also called a _record_). Each row has a set of _attributes_, which can be thought of as a property of a row. When grouped together, those attributes are referred to as a _column_ and typically have an associated name.

    Table: friends_list

            (name)      (country)   (age)
            column_1    column_2    column_3
    Row_1   Paul        CA          25
    Row_2   Mary        CA          95
    [...] 
    Row_n   Jeanne      US          61

In the above example, a row of data of table ‘friends_list’ is (Paul, CA, 25). ‘95’ is the ‘age’ _attribute_ for Row_2 (name: Mary). Every table has a _primary key_, which uniquely identifies a row. In our example, the primary key could be the ‘name’ column (assuming that the names are unique in the whole database; in reality, primary keys are typically unique positive integers).

For historical reasons, RDBMS typically (physically) organize data by rows (because most early databases were dealing with online transaction processing (OLTP) type data). The physical _data_ is _stored_ on disk in a _row-order_: Paul, CA, 25; Mary, CA, 95; ... 61;. Next section will delve more in how the data is actually structured.

## Relations Between Tables

Using simply one long table (a set of flat rows), it would be hard to represent arbitrary _composite_ data without duplication. For example, in the table of the previous section, what would happen if in addition to a county, we have query that require the population and capital (of the country they live in) for every person in the table?

It is possible to extend the table to contain columns ‘population’, ‘capital’ next to the ‘country’ column. This duplicates the information which wastes spaces and makes a simple update (CA’s population + 1 ?  need to change all entries where ‘country’ = ‘CA’). A widely used relational model is the _star schema_ [RDBMS_StarSchema, https://en.wikipedia.org/wiki/Star_schema], where the main table is called the _fact table_ and the ancilliary tables are called _dimensions tables_. Attributes in the fact tables that refer to records in a dimension table use a _foreign key_, which is really just a pointer to an entry in a different table.

    Table: countries 

            (name)      (population)   (capital)
    Row_1   CA          35.16          Ottawa 
    Row_2   US          318.9          Washington

## How Tables Map to Data-Structures

Without any database administrator set constraint, the data is stored in an _Index Allocation Map_ (IAM), which is basically a contiguous array of data in no particular order alongside with an index ordered by id [Web_SQL_Datastructures, http://www.akadia.com/services/sqlsrv_data_structure.html]. This means that operations on columns stored in IAM must scan the entire table.

It is possible to create one (and only one!) _clustered index_ per table, which structures data in a _B-Tree_ whose keys are one of the column of the table (where that column has the property to have guaranteed unique entries).

It is possible to have _indexes_ on more than one column, but requires the creation of a side-index (data structure: B-Tree again) containing tuples of (b-tree-id, actual-data-ref). Of course, this comes at the cost of more disk-data and more work to maintain consistency (every time an entry is updated, so must its index).

## The SQL Language

SQL is a language that allows to run operation on a database. This section has a few examples of the language, please refer to the appendix for a python script that allows you to play with a SQL database. We will cover only simple queries to read data, but the fundamental remains the same to read data.

At the base, A SQL query consists of:

    SELECT <column_1, column_2, ..., column_n>
    FROM   <table_1, table_2, ..., table_n>
    WHERE  <predicate_1>
    AND    <predicate_2>
    [...]
    AND    <predicate_n>

For example:

    SELECT name, age 
    FROM   friend 
    WHERE  age > 40
    
...outputs:

    ('Mary', 95)
    ('Jeanne', 61)

### How Operations are Executed

The SELECT clause defines which _elements_ need to form the output. The elements can be from the fact table or any of the dimension table. The FROM clause defines the source tables. The WHERE is just a set of predicate. The predicates run one-by-one, if any data is missing to run the predicate, it is fetched from the dimension table. If all predicates match then the elements from the SELECT will be part of the output (the current _row_ is part of the output).

### Think of Cross Products

One of the principal insight to get is that when selecting from more than one table, the SQL engine will basically do a cross product of the two tables (another way to think of it is a double nested loop):

SQL:

    SELECT friend.name, friend.age 
    FROM   friend, country 
    
Output:

    ('Paul', 25)
    ('Paul', 25)
    ('Mary', 95)
    ('Mary', 95)
    ('Jeanne', 61)
    ('Jeanne', 61)

This can seem counter-intuitive. But looking at what we ask the engine, it makes perfect sense. The SELECT statement asks to form a 2-tuple of (name, age) from two tables. It does not matter that we actually do not ask for any of the data from the 'country' table in the SELECT clause. The FROM clause has two tables, therefore the cross product of the two tables (for every row of country, for every row of friend) is generated. Since there is not WHERE clause (no predicate), all outputs are positive and form the output.

### Implicit Join

This is important to understand since, for example, in this more sensible query:

    SELECT friend.name, friend.age, country.capital, country.population
    FROM   friend, country 
    WHERE  friend.country = country.name
    AND    friend.age > 40

The output looks very reasonable:    

    ('Mary', 95, 'Ottawa', 35.16)
    ('Jeanne', 61, 'Washington', 318.9)

The main insight here is the odd-looking line _WHERE  friend.country = country.name_. This is what links (_joins_) two tables together: an entity in table 'friend' _relates_ to an entity in table 'country' if the predicate is true. This is called an _implicit join_.

#### Predicates Order and Selectivity

It is easy to forget that the SQL engine may potentially have to go over all 6 combinations of the cross product of 'friends X country'. Fortunately for us, SQL typically will execute the predicate in order of _selectivity_, so the total number of operations is much smaller than the cross product of all table referenced. However, degenerate queries where all predicates return true most of the time can quickly bring a SQL engine to its knees for large enough table.

## Transactions

SQL supports transaction on generic statements. An example from [MySQL](https://dev.mysql.com/doc/refman/5.0/en/commit.html):

    START TRANSACTION;
    SELECT @A:=SUM(salary) FROM table1 WHERE type=1;
    UPDATE table2 SET summary=@A WHERE type=1;
    COMMIT;

At the cost of efficiency (think about what it means for locking data), this is a principal advantage over Key-Value Pair datastores where transaction support is fundamentally more limited (because information is sharded across different machines).

# Appendix: Example SQL Code

dext.insertCode('sql_intro.py')

