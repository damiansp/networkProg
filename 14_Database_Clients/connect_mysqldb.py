#!/usr/bin/env python
# Basic MySQL connections
import MySQLdb

print 'Connecting...'
dbh = MySQLdb.connect(db = 'foo')
print 'Connection successful.'
dbh.close()
