#!/usr/bin/env python
# UDP example without using connect
import socket, sys, struct, time

hostname = 'time.nist.gov'
port = 37
host = socket.gethostbyname(hostname)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # <- use Datagram protocol
s.sendto('', (host, port))

print "Looking for replies; Ctrl-C to stop."
buf = s.recvfrom(2048)[0]
if len(buf) != 4:
    print 'Wrong sized reply %d: %s' %(len(buf), buf)
    sys.exit(1)

secs = struct.unpack('!I', buf)[0]
secs -= 2208988800
print time.ctime(int(secs))
