#!/usr/bin/env python
# High level Gopher client with urllib
import urllib, sys

host = sys.argv[1]
file = sys.argv[2]

f = urllib.urlopen('gopher://%s%s' %(host, file))
for line in f.readlines():
    sys.stdout.write(line)
