#!/usr/bin/env python
# Obtain a web page (note: works with HTTP and FTP)
import sys, urllib2

req = urllib2.Request(sys.argv[1])
fd = urllib2.urlopen(req)

while True:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data)
