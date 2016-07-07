#!/usr/bin/env python
# Syslog example

# NOTE: TO get this to work, I had to copy syslog.so to this dir
# Logging goes to ...???
import syslog, sys, StringIO, traceback, os

def log_exception(include_traceback = 0):
    exc_type, exception, exc_traceback = sys.exc_info()
    exc_class = str(exception.__class__)
    message = str(exception)

    if not include_traceback:
        syslog.syslog(syslog.LOG_ERR, '%s: %s' %(exc_class, message))
    else:
        exc_fd = StringIO.StringIO()
        traceback.print_exception(
            exc_type, exception, exc_traceback, None, exc_fd)

        for line in exc_fd.getvalue().split('\n'):
            syslog.syslog(syslog.LOG_ERR, line)


def init_syslog():
    syslog.openlog('%s[%d]' %(os.path.basename(sys.argv[0]), os.getpid()),
                   0,
                   syslog.LOG_DAEMON)
    syslog.syslog('Started.')



init_syslog()

try:
    raise RuntimeError, 'Exception 1'
except:
    log_exception(0)

try:
    raise RuntimeError, 'Exception 2'
except:
    log_exception(1)

syslog.syslog('Terminating.')
    
