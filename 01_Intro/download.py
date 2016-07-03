#!/usr/bin/env python
# Download example
import urllib, sys

f = urllib.urlopen(sys.argv[1])

while True:
    buf = f.read(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)

# > ./download.py gopher://quux.org/

# > ./download.py http://http.us.debian.org/debian/ls-lR.gz | gunzip | more
