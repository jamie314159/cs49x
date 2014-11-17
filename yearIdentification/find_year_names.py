#!/usr/bin/python3

import re
AS = open('corpus/pre-identification/Amar-Suen_6/Amar-Suen-6_cdli.txt', 'r')
SH = open('corpus/pre-identification/Shulgi_42/Shulgi_42_cdli.txt', 'r')
years = open('yearsList.txt', 'w')
asyears = set([])
shyears = set([])


year = re.compile(r'^[0-9]+\. (mu[#| ].*)')
for line in SH:
	s = year.search(line) 
	if s:
		shyears.add(s.group(1))

for line in AS:
	s = year.search(line) 
	if s:
		asyears.add(s.group(1))

allyears = set([])
allyears.update(asyears)
allyears.update(shyears)

ay = list(allyears)
[years.write(l + '\n') for l in sorted(ay)]
