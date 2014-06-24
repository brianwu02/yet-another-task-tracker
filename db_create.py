#!usr/bin/env python
import psycopg2
import sys

HOST = '192.168.1.24'
DATABASE = 'testdb'
PORT = 5432
USER = 'test'
PASSWORD = 'password'


con = None
try:
    con = psycopg2.connect(
            host = HOST,
            port = PORT,
            database = DATABASE,
            user = USER,
            password = PASSWORD
            )

    cur = con.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    print ver 

    cur.execute("""
    CREATE TABLE Notes(
    id serial primary key,
    note TEXT,
    timestamp TIMESTAMP
    )""")

    con.commit()
    print cur.fetchone()
    

except psycopg2.DatabaseError, e:
    print('Error %s' % e)
    sys.exit(1)

finally:
    if con:
        con.close()
