#!/usr/bin/env python
# Expanded pydns library example
import sys, DNS

def hier_query(qstring, qtype):
    '''
    Given a query type, qtype, returns answers of that type for lookup qstring.
    If no answers found, removes teh most specific component (before leftmost
    period) and retries.  If topmost query fails, return None.
    '''
    req_obj = DNS.Request()

    try:
        answer_obj = req_obj.req(name = qstring, qtype = qtype)
        answers = [x['data'] for x in answer_obj.answers if x['type'] == qtype]
    except DNS.Base.DNSError:
        answers = [] # fake an empty return

    if len(answers):
        return answers
    else:
        remainder = qstring.split('.', 1)

        if len(remainder) == 1:
            return None
        else:
            return hier_query(remainder[1], qtype)

def find_nameservers(host_name):
    '''
    Attempts to determine the authoritative nameservers for a given host name.
    Reutrns None on failure.
    '''
    return hier_query(host_name, DNS.Type.NS)

def get_records_from_nameserver(qstring, qtype, ns_list):
    ''' 
    Given a list of nameservers in ns_list, executes the query requested by
    qstring and qtype on each in order, returning data from the first server
    returnin at least 1 answer.  If no server returned answers, returns [].
    '''
    for ns in ns_list:
        req_obj = DNS.Request(server = ns)

        try:
            answers = req_obj.req(name = qstring, qtype = qtype).answers
            if len(answers):
                return answers
        except DNS.Base.DNSError:
            pass

    return []

def ns_lookup(qstring, qtype, verbose = 1):
    ns_list = find_nameservers(qstring)
    if ns_list == None:
        raise RunTimeError, "Could not find nameserver to use."
    if verbose:
        print "Using nameservers:", ", ".join(ns_list)

    return get_records_from_nameserver(qstring, qtype, ns_list)



if __name__ == '__main__':
    query = sys.argv[1]
    DNS.DiscoverNameServers()

    answers = ns_lookup(query, DNS.Type.ANY)

    if not len(answers):
        print 'Not found.'

    for item in answers:
        print '%-5s %s' %(item['typename'], item['data'])
    
