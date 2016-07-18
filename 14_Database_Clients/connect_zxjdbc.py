#!/usr/bin/env python
# Basic connection through zxJDBC to PostgreSQL
# requires jython interpreter (www.jython.org)
from com.ziclix.python.sql import zxJDBC
import os

dbh = zxJDBC.connect('jdbc:postgresql://localhost/foo',
                     'damiansp',
                     None,
                     'org.postgresql.Driver')
print 'Connection successful.'
dbh.close()
