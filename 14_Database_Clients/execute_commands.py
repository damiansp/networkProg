#!/usr/bin/env python
# Execute DB commands python
import psycopg

def get_dsn(db = None, user = None, passwd = None, host = None):
    if user == None:
        import os, pwd

        # Default to user login
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
print '...connection successful.'

cur = dbh.cursor()
cur.execute(
    '''
    CREATE TABLE ch14(
        mynum integer UNIQUE,
        mystring varchar(30))
    ''')

cur.execute('INSERT INTO ch14 VALUES (5, "Five")')
cur.execute('INSERT INTO ch14 VALUES (0)')
dbh.commit()
dbh.close()
