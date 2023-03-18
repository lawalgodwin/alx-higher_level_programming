#!/usr/bin/python3

""" Select states from database """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """Connect to the DB and get all the states"""
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    db_cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id;"
    db_cursor.execute(query)
    states = db_cursor.fetchall()
    for s in states:
        print(f"{s}")
