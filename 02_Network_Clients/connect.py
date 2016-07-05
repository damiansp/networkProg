#!/usr/bin/env python
# Basic connection example
import socket

print "Creating socket...",
s = socket.socket(socket.AF_INET, # communication type (= IPv4, internet std)
                  socket.SOCK_STREAM) # for TCP connection
print "... done."

print "Connecting to remote host...",
s.connect(('www.google.com', 80)) # hostname, remote port
print "...done."



