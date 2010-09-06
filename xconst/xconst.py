#!/usr/bin/env python
#------------------------------------------------------------------------------

import sys
import getopt

#------------------------------------------------------------------------------

class App :
	name = "xconst"
	version = "0.0.1"
	author = ["Yasuhiro Kanda"]

#------------------------------------------------------------------------------

def main () :
	try :
		optlist, args = getopt . getopt (sys . argv[1:], "hvi:", longopts=["help", "version", "input="])

	except getopt . GetoptError :
		sys . exit (1)

	for opt, arg in optlist :
		if opt in ("-h", "--help") :
			print "help!!"

		if opt in ("-v", "--version") :
			print "xconst, version " + App . version

		if opt in ("-i", "--input") :
			print arg
			sys . exit (0)

	# for arg in sys . argv :
	#	print arg

#------------------------------------------------------------------------------

if __name__ == '__main__' :
	main ()
