#!/usr/bin/env python
# Do a reverse DNS look up for an IP adress
import sys, socket

try:
    # Perform lookup
    result = socket.gethostbyaddr(sys.argv[1])

    # Display the host name
    print 'Primary host name:'
    print ' ' + result[0]

    # Display the list of available addresses also returned
    print '\nAddresses:'
    for item in result[2]:
        print ' ' + item
except socket.herror, e:
    print "Couldn't find name: ", e
