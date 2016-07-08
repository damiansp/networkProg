#!/usr/bin/env python
# Performs a reverse lookup of IP address and sanity checks the results to
# detect fraudulent data
import sys, socket

def get_ip_address(host_name):
    '''
    Get a list of IP addresses from a given host name. 
    Standard (forward) DNS lookup.
    '''
    result = socket.getaddrinfo(host_name, None, 0, socket.SOCK_STREAM)
    return [x[4][0] for x in result]

def get_host_name(ip_addr):
    '''
    Get the host name for a given IP address.  Reverse lookup.
    '''
    return socket.gethostbyaddr(ip_addr)[0]

try:
    # First, do the reverse lookup and get the host name
    host_name = get_host_name(sys.argv[1]) # could raise socket.herror

    # Do forward lookup on result of reverse lookup
    ip_addrs = get_ip_address(host_name) # could raise socket.gaierror
except socket.herror, e:
    print 'No host names available for %s; may be normal.' %sys.argv[1]
    sys.exit(0)
except socket.gaierror, e:
    print('Got host name %s, but it could not be forward resolved: %s'
          %(host_name, str(e)))
    sys.exit(1)

# If the forward lookup did not yield the original IP addr anywhere, there is
# fraudulent info. Explain and exit.
if not sys.argv[1] in ip_addrs:
    print(
        'Got host name %s, but original IP %s did not appear on forward lookup'
        %(host_name, sys.argv[1]))
    sys.exit(1)

# Otherwise show validated host name
print 'Validated host name:', host_name
