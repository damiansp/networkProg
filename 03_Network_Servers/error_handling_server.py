#!/usr/bin/env python
# Server with error handling
import socket, traceback

host = ''
port = 54321

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while True:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    # Process connection
    try:
        print "Received connection from", clientsock.getpeername()
        # ...Process here...
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

    # Close connection
    try:
        clientsock.close()
        # ...close file objects here too....
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
