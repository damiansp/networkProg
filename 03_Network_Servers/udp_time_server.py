#!/usr/bin/env python
# UDP Yesterday's time server
import socket, traceback, time, struct

host = ''
port = 54321

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

while True:
    try:
        message, address = s.recvfrom(8192)
        secs = int(time.time()) # = seconds since 01 Jan 1970
        secs -= (60 * 60 * 24)  # 24 hours ago
        secs += 2208988800      # convert to secs since 01 Jan 1900
        reply = struct.pack('!I', secs)
        s.sendto(reply, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
