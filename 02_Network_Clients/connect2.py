#!/usr/bin/env python
# Connection example with query to find port number
import socket

print "Creating socket...",
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "...done."

print "Looking up port number...",
port = socket.getservbyname('http', 'tcp') # queries a list at /etc/services
print "...done."

print "Connecting to remote host on port %d..." %port,
s.connect(('www.google.com', port))
print "...done."
