#!/usr/bin/env python
# Basic getaddrinfo() not quite right list example
# Takes a hostname on the command line and prints all resulting matches
# Broken: a given name may occur mult times
import sys, socket

# Put the list of results into the "result" var
result = socket.getaddrinfo(sys.argv[1], None)

counter = 0
for item in result:
    # Print out the address tuple for ea item
    print '%-2d: %s' %(counter, item[4])
    counter += 1
