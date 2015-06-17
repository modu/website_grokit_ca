
import os
import sqlite3

DB_FILE = 'database.db'

def createTable(conn):
    """
    This creates the _truth table_, the table at the center of the star schema.
    """
    
    c = conn.cursor()
    
    # @@ have country in a foreign key
    c.execute("CREATE TABLE friends_list (name TEXT, country TEXT, age INT)") 
    conn.commit()
    
def createCountry(conn):
    """
    This is a _dimension table_, which means that it contain auxiliary for the truth table that is refered
    to by a foreign key.
    """
    
    c = conn.cursor()
    
    # @@ have country in a foreign key -- is this automatic?
    c.execute("CREATE TABLE countries (name TEXT, capital TEXT, population INT)") 
    conn.commit()    
    
def insertFriendToDB(conn, friendName, friendCountry, friendAge):
    
    cursor = conn.cursor()
    
    sql_cmd = "INSERT INTO friends_list VALUES ('%s', '%s', %i)" % (friendName, friendCountry, friendAge)
    print(sql_cmd)
    cursor.execute(sql_cmd)
    conn.commit()

def query(conn):
    cursor = conn.cursor()
    
    # SELECT *   -> ('Paul', 'CA', 25)
    # SELECT age -> (25,)
    sql_cmd = """SELECT name, age FROM friends_list WHERE age > 40;"""
    print(sql_cmd)
    ro = cursor.execute(sql_cmd)
    for r in ro:
        print(r)
    
def queryWithImplicitJoin(conn):
    cursor = conn.cursor()
    
    sql_cmd = """SELECT name, age FROM friends_list WHERE age > 40;"""
    print(sql_cmd)
    ro = cursor.execute(sql_cmd)
    for r in ro:
        print(r)
        
if __name__ == '__main__':

    if os.path.isfile(DB_FILE):
        os.remove(DB_FILE)
    conn = sqlite3.connect(DB_FILE)
    createTable(conn)
     
    insertFriendToDB(conn, 'Paul', 'CA', 25)
    insertFriendToDB(conn, 'Mary ', 'CA', 95)
    insertFriendToDB(conn, 'Jeanne ', 'US', 61)
    
    query(conn)
    
    conn.close()


