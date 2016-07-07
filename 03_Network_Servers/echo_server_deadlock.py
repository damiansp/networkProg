#!/usr/bin/env python
# Echo server
import socket, traceback

host = ''
port = 54321

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while True:
    try:
        client_sock, client_addr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    # Process connection
    try:
        print "Received connection from", client_sock.getpeername()
        while True:
            data = client_sock.recv(4096)
            if not len(data):
                break
            client_sock.sendall(data)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_ext()

    # Close connection
    try:
        client_sock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        
