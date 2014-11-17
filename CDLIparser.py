
# coding: utf-8

## CDLI Data Parser

#### C-ATF Reference: http://oracc.museum.upenn.edu/doc/help/editinginatf/cdliatf/

#### Read in data from file



import re
cdli = open('CDLI_Data/cdli.txt', 'r')
data = []
item = {}
text = []
for line in cdli:
    if line not in ['\n', " \n"]:
        text.append(line.strip('\n'))
    else:
        if text != []:
            item['raw'] = text
            data.append(item)
            text = []
            item = {}


#### Identify Meta-Data



for item in data:
    for line in item['raw']:
        if line[0].isalpha():
            l = re.search('([^:]*):(.*)', line)
            item[l.group(1)] = l.group(2)




meta = re.compile('(.*): ?(.*)')
remove = []
for item in data:
    for line in item['raw']:
        m = meta.search(line)
        if m != None:
            item[m.group(1)] = m.group(2)




def level(line):
    if line in ['@tablet', '@envelope']:
        return(0)
    else:
        if line[0] == '@':
            return(1)
        else:
            return(2)

for item in data:
    item['text'] = {}
    curr = item['text']
    currlevel = 0
    for line in item['raw']:
        if level(line) == 0:
            if currlevel == 0:
                curr[line.strip('@')] = {}
                prev = curr
                curr = curr[line.strip('@')]
            else:
                curr = item['text']
                curr[line.strip('@')] = {}
                prev = curr
                curr = curr[line.strip('@')]
            currlevel = 0
        elif level(line) == 1:
            if currlevel == 0:
                curr[line.strip('@')] = []
                prev = curr
                curr = curr[line.strip('@')]
            elif currlevel == 1:
                curr = prev
                curr[line.strip('@')] = []
                prev = curr
                curr = curr[line.strip('@')]
            currlevel = 1
        elif level(line) == 2:
            if currlevel == 1:
                curr.append(line)




print(data[0])




import json
print(json.dumps(data[0], sort_keys=True, indent=4, separators=(',', ': ')))




t = "1'. mu szu-{d}suen lugal"
l2 = re.compile('([0-9]+.*\. )(.*)')
l2.search(t).group(1)

