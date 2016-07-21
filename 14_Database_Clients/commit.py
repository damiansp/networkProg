#!/usr/bin/env python
# Commit example
import psycopg

def get_dsn(db = None, user = None, passwd = None, host = None):
    if user == None:
        # Default to login
        import os, pwd
        user = pwd.getpwuid(os.getuid())[0]

    if db == None:
        # Default to username
        db = user

    dsn = 'dbname=%s user=%s' %(db, user)

    if passwd != None:
        dsn += ' password=' + passwd

    if host != None:
        dsn += ' host=' + host

    return dsn


dsn = get_dsn()
print 'Connecting to %s...' %dsn
dbh = psycopg.connect(dsn)
print '...connection succesful.'

cur = dbh.cursor()
cur.execute('DELETE FROM ch14')  # Still visible until commit() even if...
cur.execute('INSERT INTO ch14 VALUES (0)') # ...this step takes a long time

dbh.commit()
dbh.close()
