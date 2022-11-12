#!/usr/bin/python3
'''script that lists all states from the database hbtn_0e_0_usa'''

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    # User credentials
    user_name = argv[1]
    user_pass = argv[2]
    db_name = argv[3]
    host_name = 'localhost'
    host_port = 3306

    # Connect to MySQL DB and create the cursor
    db = MySQLdb.connect(host_name,
                         user_name,
                         user_pass,
                         db_name,
                         port=host_port)
    cursor = db.cursor()

    # Make and tun query
    sql = """SELECT * FROM states
            ORDER BY id"""
    cursor.execute(sql)
    result = cursor.fetchall()

    # print each elements in result
    for each in result:
        print(each)
    # disconnect from server
    cursor.close()
    db.close()
