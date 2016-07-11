#!/usr/bin/env python
# Obtain web page info
import sys, urllib2

req = urllib2.Request(sys.argv[1])
fd = urllib2.urlopen(req)
info = fd.info()

print 'Retrieved', fd.geturl()

for key, value in info.items():
    print '%s = %s' %(key, value)
