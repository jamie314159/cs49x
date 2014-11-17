#!/usr/bin/python3

import re
AS = open('Amar-Suen_6/Amar-Suen-6_cdli.txt', 'r')
SH = open('Shulgi_42/Shulgi_42_cdli.txt', 'r')
years = open('yearsList.txt', 'w')
diff = open('diffList.txt', 'w')
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

diffyears = set([])
diffyears.update(asyears)
diffyears.intersection_update(shyears)

print(len(asyears))
print(len(shyears))
print(len(allyears))
print(len(diffyears))
ay = list(allyears)
dy = list(diffyears)
[years.write(l + '\n') for l in sorted(ay)]
[diff.write(l + '\n') for l in sorted(dy)]