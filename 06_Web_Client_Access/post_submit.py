#!/usr/bin/env python
# Submit POST data
import sys, urllib, urllib2

zipcode = sys.argv[1]
url = 'http://www.wunderground.com/cgi-bin/findweather/getForecast'
data = urllib.urlencode([('query', zipcode)])
req = urllib2.Request(url)
fd = urllib2.urlopen(req, data)

while True:
    data = fd.read(1024)
    if not len(data):
        break

    sys.stdout.write(data)
