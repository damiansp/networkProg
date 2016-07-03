#!/usr/bin/env python
# Higher level Gopher client
import gopherlib, sys # gopherlib is deprecated :(

host = sys.argv[1]
file = sys.argv[2]

f = gopherlib.send_selector(file, host)
for line in f.readlines():
    sys.stdout.write(line)
