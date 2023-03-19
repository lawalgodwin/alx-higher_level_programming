#!/usr/bin/python3

"""A script that lists all cities from the database hbtn_0e_4_usa
   You can only use execute once
"""

import MySQLdb

from sys import argv

if __name__ == '__main__':
    """List all cities"""
    # connect to db and get db cursor
    user = argv[1]
    password = argv[2]
    database = argv[3]

    DB = MySQLdb.connect(user=user, passwd=password, db=database)
    db_cursor = DB.cursor()
    # execute query and get result using the cursor
    stmt = """SELECT c.id, c.name, s.name
              FROM cities AS c
              JOIN states AS s
              ON c.state_id = s.id
        """
    db_cursor.execute(stmt)
    row_selected = db_cursor.fetchall()
    for row in row_selected:
        print(row)
