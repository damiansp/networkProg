#!/usr/bin/env python
# Basic example of getaddrinfo()
import socket, sys

result = socket.getaddrinfo(sys.argv[1], None)
print result[0][4]
