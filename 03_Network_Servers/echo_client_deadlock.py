#!/usr/bin/env python
# Echo client with deadlock
import socket, sys

port = 54321
host = 'localhost'
data = 'x' * 10485760 # 10MB of data

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

bytes_written = 0
while bytes_written < len(data):
    start_pos = bytes_written
    end_pos = min(bytes_written + 1024, len(data))
    bytes_written += s.send(data[start_pos:end_pos])
    sys.stdout.write('Wrote %d bytes\r' %bytes_written)
    sys.stdout.flush()

s.shutdown(1)

print 'All data sent.'
while True:
    buf = s.recv(1024)
    if not len(buf):
        break
    sys.stdout.write(buf)
