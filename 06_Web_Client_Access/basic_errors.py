#!/usr/bin/env python
# Obtain web page info with simple error handling
import sys, urllib2

req = urllib2.Request(sys.argv[1])

try:
    fd = urllib2.urlopen(req)
except urllib2.URLError, e:
    print 'Error retrieving data:', e
    sys.exit(1)

print 'Retrieved', fd.geturl()

info = fd.info()

for k, v in info.items():
    print '%s: %s' %(k, v)
