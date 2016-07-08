#!/usr/bin/env python
# DNS query program
import sys, DNS, pydns_any, re

def get_reverse(query):
    '''
    Given the query, returns an appropriate reverse lookup string under 
    IN-ADDR.ARPA if query is an IP address; otherwise returns None.
    NOT IPv6-compatible.
    '''
    if re.search('^\d+\.\d+\.\d+\.\d+$', query): # check for IP address
        octets = query.split('.')
        octets.reverse()
        return '.'.join(octets) + '.IN-ADDR.ARPA'

    return None

def format_line(index, type_name, descr, data):
    ret_val = '%-2s %-5s' %(index, type_name)
    data = data.replace('\n', '\n         ')

    if descr != None and len(descr):
        ret_val += ' %-12s' %(descr + ':')

    return ret_val + ' ' + data

DNS.DiscoverNameServers()
queries = [(sys.argv[1], DNS.Type.ANY)]
done_queries = []
descriptions = { 'A': 'IP address',
                 'TXT': 'Data',
                 'PTR': 'Host name',
                 'CNAME': 'Alias for',
                 'NS': 'Name server' }

while len(queries):
    (query, qtype) = queries.pop(0)

    if query in done_queries:
        # Don't look up 2x
        continue

    done_queries.append(query)
    print '-' * 75
    print 'Results for %s (lookup type %s)' %(query, DNS.Type.typestr(qtype))
    print
    rev = get_reverse(query)

    if rev:
        print 'IP address given; doing reverse lookup using', rev
        query = rev

    answers = pydns_any.ns_lookup(query, qtype, verbose = 0)

    if not len(answers):
        print 'Not found.'

    count = 0

    for answer in answers:
        count += 1

        if answer['typename'] == 'MX':
            print format_line(
                count,
                answer['typename'],
                'Mail server',
                '%s, priority %d' %(answer['data'][1], answer['data'][0]))
            queries.append((answer['data'][1], DNS.Type.A))
        elif answer['typename'] == 'SOA':
            data = '\n' + '\n'.join([str(x) for x in answer['data']])
            print format_line(count, 'SOA', 'Start of authority', data)
        elif answer['typename'] in descriptions:
            print format_line(count,
                              answer['typename'],
                              descriptions[answer['typename']],
                              answer['data'])
        else:
            print format_line(
                count, answer['typename'], None, str(answer['data']))

        if answer['typename'] in ['CNAME', 'PTR']:
            queries.append((answer['data'], DNS.Type.ANY))
        if answer['typename'] == 'NS':
            queries.append((answer['data'], DNS.Type.A))
