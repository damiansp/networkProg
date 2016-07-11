#!/usr/bin/env python
# Broadcast sender (LAN only)
import socket, sys

dest = ('<broadcast>', 54321)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto('Hello', dest)
print 'Looking for replies; ^C to stop'

while True:
    (buf, addr) = s.recvfrom(2048)

    if not len(buf):
        break

    print 'Received from %s: %s' %(addr, buf)
