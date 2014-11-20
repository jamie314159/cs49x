#!/usr/bin/python3
from pathlib import Path
import shutil
import re
import os


def sort(a,b,c):
	as6 = []
	sh42 = []
	amb = []
	as6txt = open(a, 'r')
	sh42txt = open(b, 'r')
	ambtxt = open(c, 'r')
	rootdir = './corpus/pre-identification'
	dstpathas6 = './corpus/post-identification/Amar-Suen_6'
	dstpathsh42 = './corpus/post-identification/Shulgi_42'
	dstpathamb = './corpus/post-identification/Ambiguous'
	dstpathunid = './corpus/post-identification/Unidentified'

	for line in as6txt:
		if line not in ['\n',"\n"]:
			as6.append(line.strip('\n'))

	for line in sh42txt:
		if line not in ['\n',"\n"]:
			sh42.append(line.strip('\n'))
	
	for line in ambtxt:
		if line not in ['\n',"\n"]:
			amb.append(line.strip('\n'))


	for subdir, dirs, files in os.walk(rootdir):
		for infile in files:
			matched = False
			currtxt = open(os.path.join(subdir, infile), 'r')
			for nline in currtxt:
				nline = nline.rstrip('\n').rstrip()[3:]
				if nline in as6:
					shutil.copyfile(os.path.join(subdir, infile),dstpathas6 + '/' + infile)
					matched = True
					break
				elif nline in sh42:
					shutil.copyfile(os.path.join(subdir, infile),dstpathsh42 + '/' + infile)
					matched = True
					break
				elif nline in amb:
					shutil.copyfile(os.path.join(subdir, infile),dstpathamb + '/' + infile)
					matched = True
					break
			if matched == False:
				shutil.copyfile(os.path.join(subdir, infile),dstpathunid + '/' + infile)



sort('AmarSuen6Years.txt', 'Shulgi42Years.txt', 'AbrrevYears.txt')