## Column-Store Relational Database

@@@read more about that

The data is stored in disk in a column-fashion. The previous examples would have 3 columns: (names: Paul, Mary, Jeanne), (country: CA, CA, US), (ages: 25, 95, 61). The Record the data belongs to is identified by the index in the column at which the data is located [CStore_Paper, http://db.csail.mit.edu/projects/cstore/vldb.pdf].
