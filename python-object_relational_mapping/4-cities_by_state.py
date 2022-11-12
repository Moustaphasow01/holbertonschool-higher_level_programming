#!/usr/bin/python3

"""
== Safe version / prevents SQL Injection ==
Script to list all states
from database hbtn_0e_0usa
where name of states matches an argument of command line
"""

import MySQLdb
import sys

if "__main__" == __name__:
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="root",
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC"
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
