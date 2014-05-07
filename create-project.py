#!/usr/bin/python2

from proto import *

# check arguments
if len(sys.argv) != 2:
	print "usage: script <projectname>"
	sys.exit (-1)

projectName = sys.argv[1]

fs = open ("Project", "w")
fs.write ("""
projectName = \""""+projectName+"""\"
libs = []
""")
fs.close ()

