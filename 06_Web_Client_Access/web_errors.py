#!/usr/bin/env python
# Obtain web page with full error handling
import socket, sys, urllib2

req = urllib2.Request(sys.argv[1])

try:
    fd = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print 'Error retrieving data:', e
    print 'Server error document follows:\n'
    print e.read()
    sys.exit(1)
except urllib2.URLError, e:
    print 'Error retrieving data:' e
    sys.exit(2)

print 'Retrieved', fd.geturl()

bytes_read = 0

while True:
    try:
        data = fd.read(1024)
    except socket.error, e:
        print 'Error reading data:', e
        sys.exit(3)

    if not len(data):
        break

    bytes_read += len(data)
    sys.stdout.write(data)

if (fd.info().has_key('Content-Length') and
    long(fd.info()['Content-Length']) != long(bytes_read)):
    print('Expected document of size %d, but only read %d bytes'
          %(long(fd.info()['Content-Length']), bytes_read))
    sys.exit(4)
