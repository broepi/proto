#!/usr/bin/python2

import os
import os.path
import sys

execfile (os.path.dirname (os.path.realpath (__file__))+"/proto.py")

# check arguments
if len(sys.argv) != 2:
	print "usage: script <projectname>"
	sys.exit (-1)

projectName = sys.argv[1]

fs = open ("Project", "w")
fs.write ("""
projectName = \""""+projectName+"""\"
# libs = [ "libname" ]
# extraGppOpts = \"--some-g++-option\"
# extraLinkerOpts = \"--some-ld-option\"
""")
fs.close ()

