#!/usr/bin/env python
# Basic server
import socket

host = '' # bind to all interfaces
port = 51432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSESDDR, 1)
s.bind((host, port))

print 'Waiting for connections...'
s.listen(1) # number allowed to queue

while True:
    clientsock, clientaddr = s.accept()
    print "Received connection from", clientsock.getpeername()
    clientsock.close()
