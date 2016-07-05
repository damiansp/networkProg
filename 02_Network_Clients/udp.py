#!/usr/bin/env python
# UDP example
import socket, sys

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # <- use Datagram protocol

try:
    port = int(textport)
except ValueError:
    # Try lookup instead
    port = socket.getserbyname(textport, 'udp')

s.connect((host, port))
print 'Enter data to transmit: '
data = sys.stdin.readline().strip()

s.sendall(data)
print 'Looking for replies; press Ctrl-C to stop.'

while True:
    buf = s.recv(2048)

    if not len(buf):
        break

    sys.stdout.write(buf)

# > ./udp.py localhost 51423
# > Type some text to submit
