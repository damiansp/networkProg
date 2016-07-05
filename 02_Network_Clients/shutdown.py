#!/usr/bin/env python
# Handling common socket errors (2)
import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e: # general i/o communication problems
    print "Strange error creating socket: %s" %e
    sys.exit(1)

#Try parsing it as a numeric port number
try:
    port = int(textport)
except ValueError:
    # That didn't work--prob a protocol name: look up:
    try:
        port = socket.getservbyname(textport, 'tcp')
    except socket.error, e:
        print "Couldn't find your port: %s" %e
        sys.exit(1)

try:
    s.connect((host, port))
except socket.gaierror, e: # error looking up address info
    print 'Address-related error connecting to server: %s' %e
    sys.exit(1)
except socket.error, e:
    print 'Connection error: %s' %e
    sys.exit(1)

print "Sleeping..."
time.sleep(10)
print "Continuing."

try:
    s.sendall('GET %s HTTP/1.0\r\n\r\n' %filename)
except socket.error, e:
    print 'Error sending data: %s' %e
    sys.exit(1)

try:
    s.shutdown(1)
except socket.error, e:
    print 'Error sending data (detected by shutdown): %s' %e
    sys.exit(1)
    
while True:
    try:
        buf = s.recv(2048)
    except socket.error, e:
        print 'Error receiving data: %s' %e
        sys.exit(1)

    if not len(buf):
        break

    sys.stdout.write(buf)


# > ./shutdown.py localhost 8765 /test-ignore.html
