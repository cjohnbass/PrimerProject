#! /usr/bin/python

import os

print "Content-type: text/html\n\n"

if os.environ['REQUEST_METHOD'] == 'GET':
    if os.environ['QUERY_STRING']:
        f = open('./query.html', 'r')
        print f.read()
        f.close()
    else:	
	f = open('./index.html', 'r')
	print f.read()
	f.close()
