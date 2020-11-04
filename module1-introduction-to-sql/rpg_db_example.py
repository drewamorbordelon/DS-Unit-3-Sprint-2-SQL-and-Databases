import sqlite3
from query import *


#  conn = sqlite3.connect("rpg_db.sqlite3")
def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)



def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


#  Define a query
GET_CHARACTERS = """
    SELECT * 
    FROM charactercreator_character;
"""



if __name__ == "__main__":
    # connect to DB
    conn = connect_to_db()
    # Create cursor
    curs = conn.cursor()
    results = execute_query(curs, GET_CHARACTERS)
    print(results[0])



