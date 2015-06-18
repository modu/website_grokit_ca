
import os
import sqlite3

DB_FILE = 'database.db'

def createFriendsTable(conn):
    """
    This creates the _truth table_, the table at the center of the star schema.
    """
    
    c = conn.cursor()
    
    c.execute("CREATE TABLE friend (name TEXT, country TEXT, age INT)") 
    conn.commit()
    
def createCountryTable(conn):
    """
    This is a _dimension table_, which means that it contain auxiliary for the truth table that is refered
    to by a foreign key.
    """
    
    c = conn.cursor()
    
    c.execute("CREATE TABLE country (name TEXT, capital TEXT, population FLOAT)") 
    conn.commit()    
    
def insertFriendToDB(conn, friendName, friendCountry, friendAge):
    
    cursor = conn.cursor()
    
    sql_cmd = "INSERT INTO friend VALUES ('%s', '%s', %i)" % (friendName, friendCountry, friendAge)
    cursor.execute(sql_cmd)
    conn.commit()

def insertCountriesToDB(conn, name, capital, population):
    
    cursor = conn.cursor()
    
    sql_cmd = "INSERT INTO country VALUES ('%s', '%s', %f)" % (name, capital, population)
    cursor.execute(sql_cmd)
    conn.commit()

def query(conn):
    cursor = conn.cursor()
    
    # SELECT *   -> ('Paul', 'CA', 25)
    # SELECT age -> (25,)
    sql_cmd = """
    SELECT name, age 
    FROM friend 
    WHERE age > 40
    """

    print(sql_cmd)
    ro = cursor.execute(sql_cmd)
    for r in ro:
        print(r)
    
def queryCrossProduct(conn):
    cursor = conn.cursor()
    
    sql_cmd = """
    SELECT friend.name, friend.age 
    FROM friend, country 
    """ 

    print(sql_cmd)
    ro = cursor.execute(sql_cmd)
    for r in ro:
        print(r)

def queryWithImplicitJoin(conn):
    cursor = conn.cursor()
    
    sql_cmd = """
    SELECT friend.name, friend.age, country.capital, country.population
    FROM friend, country 
    WHERE friend.country = country.name
    AND   friend.age > 40
    """ 

    print(sql_cmd)
    ro = cursor.execute(sql_cmd)
    for r in ro:
        print(r)
        
if __name__ == '__main__':

    if os.path.isfile(DB_FILE):
        os.remove(DB_FILE)

    conn = sqlite3.connect(DB_FILE)
    createFriendsTable(conn)
    createCountryTable(conn)
     
    insertFriendToDB(conn, 'Paul', 'CA', 25)
    insertFriendToDB(conn, 'Mary', 'CA', 95)
    insertFriendToDB(conn, 'Jeanne', 'US', 61)

    insertCountriesToDB(conn, 'CA', 'Ottawa', 35.16)
    insertCountriesToDB(conn, 'US', 'Washington', 318.9)
    
    query(conn)
    queryCrossProduct(conn)
    queryWithImplicitJoin(conn)
    
    conn.close()


