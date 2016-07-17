#!/usr/bin/env python
# Basic connection to PostgreSQL with pyscopg
import psycopg

def get_dsn(db = None, user = None, passwd = None, host = None):
    if user == None:
        # Default user to the one they're logged in as
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
print 'Connecting to %s' %dsn
dbh = psycopg.connect(dsn)
print 'Connection successful.'
dbh.close()
