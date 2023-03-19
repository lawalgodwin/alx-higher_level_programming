#!/usr/bin/python3

"""A script that takes in an argument and
   displays all values in the states table
   of hbtn_0e_0_usa where name matches the argument.

   Script should be safe from SQL injection
"""

import MySQLdb

from sys import argv

if __name__ == '__main__':
    """List states matching the argument"""
    # connect to DB and get cursur
    user = argv[1]
    password = argv[2]
    database = argv[3]
    DB = MySQLdb.connect(user=user, passwd=password, db=database)

    db_cursor = DB.cursor()
    # query the DB usng the cursor
    stmt = 'SELECT * FROM states WHERE name LIKE BINARY %(name)s'
    db_cursor.execute(stmt, {'name': argv[4]})

    rows_fetched = db_cursor.fetchall()
    for row in rows_fetched:
        print(row)
