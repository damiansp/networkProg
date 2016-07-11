#!/usr/bin/env python
# HTML Title Retriever with Entity and Character Reference Support
from htmlentitydefs import entitydefs as ed
from HTMLParser import HTMLParser
import sys

class TitleParser(HTMLParser):
    def __init__(self):
        self.title = ''
        self.reading_title = False
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.reading_title = True

    def handle_data(self, data):
        if self.reading_title:
            self.title += data

    def handle_endtag(self, tag):
        if tag == 'title':
            self.reading_title = False

    # Handle HTML entities (e.g., &amp;)
    def handle_entityref(self, name):
        if ed.has_key(name):
            self.handle_data(ed[name])
        else:
            self.handle_data('&' + name + ';')

    def gettitle(self):
        return self.title

    def handle_charref(self, name):
        # Validate name
        try:
            char_num = int(name)
        except ValueError:
            return

        if char_num < 1 or char_num > 255:
            return

        self.handle_data(chr(char_num))


fd = open(sys.argv[1])
tp = TitleParser()
tp.feed(fd.read())
print 'Title:', tp.gettitle()
