#!/usr/bin/python3

import re, sys
doc = open(sys.argv[1], 'r')

curr = []
for line in doc:
	if line not in ['\n', " \n"]:
		curr.append(line)
		if line[0] == '&':
			tabletID = line[1:8]
	else:
		if curr != []:
			out = open('seperated/'+tabletID, 'w')
			[out.write(l) for l in curr]
			tabletID = ''
			curr = []