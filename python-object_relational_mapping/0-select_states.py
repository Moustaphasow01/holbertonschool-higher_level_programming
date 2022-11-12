#!/usr/bin/python3
'''script that lists all states from the database '''
from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
