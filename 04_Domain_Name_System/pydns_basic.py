#!/usr/bin/env python
# Basic pydns library example
import sys, DNS

query = sys.argv[1]
DNS.DiscoverNameServers()

req_obj = DNS.Request()
answer_obj = req_obj.req(name = query, qtype = DNS.Type.ANY)

if not len(answer_obj.answers):
    print 'Not found'

for item in answer_obj.answers:
    print '%-5s %s' %(item['typename'], item['data'])
