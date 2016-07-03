#!/usr/bin/env python
# Simple Server
import socket

host = '' # bind to all interfaces
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
# listen for clients, and let at most 1 connection wait to be processed
s.listen(1) 

print "Server is running on port %d; Ctrl-C to terminate." %port

while True:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile('rw', 0)
    clientfile.write('Welcome, ' + str(clientaddr) + '\n')
    clientfile.write('Please enter a string: ')
    line = clientfile.readline().strip()
    clientfile.write('You entered %d characters.\n' %len(line))
    clientfile.close()
    clientsock.close()


# > ./server.py
# Another terminal:
# > telnet localhost 51423
