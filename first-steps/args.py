#! /usr/bin/env python

import sys

if len(sys.argv) >= 2:
	print("You supplied more than 2 arguments")
elif len(sys.argv) != 1:
	print("You supplied no arguments")
else: 
	print("You supplied 1 argument")
