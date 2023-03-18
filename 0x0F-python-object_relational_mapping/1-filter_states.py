#!/usr/bin/python3

"""A script that filters all states starting with 'N'"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Filter only states begining with N"""
    # connect to db and get cursor
    user = argv[1]
    password = argv[2]
    database = argv[3]
    db = MySQLdb.connect(user=user, passwd=password, db=database)
    db_cursor = db.cursor()

    query = '''SELECT * FROM states
               WHERE name LIKE "N%"
            '''
    db_cursor.execute(query)

    rows = db_cursor.fetchall()

    for row in rows:
        print(row)
