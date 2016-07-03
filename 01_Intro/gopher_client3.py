#!/usr/bin/env python
# Simple Gopher Client with basic error handling
import socket, sys

port = 70 # port used by Gopher
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

fd = s.makefile('rw', 0) # mode = 'rw', buffering style 0 = disabled
fd.write(filename + '\r\n')

for line in fd.readlines():
    sys.stdout.write(line)



# To run
# > ./gopher_client3.py url.com /
    
