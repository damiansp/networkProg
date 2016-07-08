#!/usr/bin/env python
# Get host info
import sys, socket

def get_ip_address(host_name):
    '''
    Given a host name, do forward DNS lookup.
    Return IP addreess for host.
    '''
    result = socket.getaddrinfo(host_name, None, 0, socket.SOCK_STREAM)
    return [x[4][0] for x in result]

# Calling gethostname() returns the name of the loval machine
host_name = socket.gethostname()
print 'Host name:', host_name

# Tyr to get the fully qualified name
print 'Fully-qualified name:', socket.getfqdn(host_name)

try:
    print 'IP addresses:', ', '.join(get_ip_address(host_name))
except socket.gaierror, e:
    print "Couldn't get IP addresses:", e
