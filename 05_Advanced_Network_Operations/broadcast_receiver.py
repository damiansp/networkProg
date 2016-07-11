#!/usr/bin/env python
# UDP Broadcast Server (LAN use only)
import socket, traceback

host = ''
port = 54321
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

while True:
    try:
        message, address = s.recvfrom(8192)
        print 'Received data from', address

        # Acknowledge
        s.sendto('I am here.', address)
    except(KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
