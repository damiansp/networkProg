#!/usr/bin/env python
# Network Byte Order
import struct, sys

def htons(num):
    ''' Convert host byte order to network byte order, short (16-bit int)'''
    return struct.pack('!H', num) # H: 16 bit; !: use network byte order

def htonl(num):
    ''' Convert host byte order to network byte order, long (32-bit int)'''
    return struct.pack('!I', num) # I: 32-bit

def ntohs(data):
    ''' Convert network byte order to host, short (16-bit int)'''
    return struct.unpack('!H', data)[0]

def ntohl(data):
    ''' Convert  network byte order to host, long (32-bit int)'''
    return struct.unpack('!I', data)[0]

def send_string(data):
    return htonl(len(data)) + data

print 'Enter a string:'
str = sys.stdin.readline().rstrip()

print repr(send_string(str))
