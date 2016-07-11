#!/usr/bin/env python
# Obtain Web Page Info with Authentication
import getpass, sys, urllib2

class TerminalPassword(urllib2.HTTPPasswordMgr):
    def find_user_password(self, realm, auth_uri):
        ret_val = urllib2.HTTPPasswordMgr.find_user_password(
            self, realm, auth_uri)

        if ret_val[0] == None and ret_val[1] == None:
            # Did not find it in stored values; prompt user
            sys.stdout.write('Login required for %s at %s\n'
                             %(realm, auth_uri))
            sys.stdout.write('Username: ')
            username = sys.stdin.readline().rstrip()
            password = getpass.getpass().rstrip()

            return (username, password)
        else:
            return ret_val


req = urllib2.Request(sys.argv[1])
opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler(TerminalPassword()))
fd = opener.open(req)
info = fd.info()

print 'Retrieved', fd.geturl()

for k, v in info.items():
    print '%s: %s' %(k, v)
