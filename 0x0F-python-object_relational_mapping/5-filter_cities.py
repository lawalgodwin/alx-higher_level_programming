#!/usr/bin/python3

"""A a script that takes in the name of
   a state as an argument and lists all cities
   of that state, using the database hbtn_0e_4_usa

   You can use execute only once
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Get the cities in a given state"""
    # connect to DB and get cursor
    _, user, password, database, state = argv
    DB = MySQLdb.connect(user=user, passwd=password, db=database)
    db_cursor = DB.cursor()
    # execute query and get result

    stmt = """SELECT c.name
                FROM cities AS c
                JOIN states AS s
                ON c.state_id = s.id
                WHERE s.name LIKE BINARY %s"""
    db_cursor.execute(stmt, [state])
    cities = db_cursor.fetchall()
    result = ", ".join(list(map(lambda x: x[0], cities)))
    print(result)
