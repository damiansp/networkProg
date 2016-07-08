#!/usr/bin/env python
# Basic getaddrinfo() list example
import sys, socket

# Obtain results from socket.SOCK_STREAM (TCP) only and put a list of them into
# the 'result' var
result = socket.getaddrinfo(sys.argv[1], None, 0, socket.SOCK_STREAM)
counter = 0

for item in result:
    # Print out the address tuple for ea item
    print '%-2d: %s' %(counter, item[4])
    counter += 1
