#!/usr/bin/env python
# Basic HTML Title Retriever
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
            # Bad idea in most circumstances, but title is usually short so...
            self.title += data

    def handle_endtag(self, tag):
        if tag == 'title':
            self.reading_title = False

    def get_title(self):
        return self.title


fd = open(sys.argv[1])
tp = TitleParser()
tp.feed(fd.read())
print 'Title is:', tp.get_title()
