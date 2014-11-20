import re
import shutil
import os

def sort(a,b,c):
	as6 = []
	sh64 = []
	unid = []
	as6txt = open(a, 'r')
	sh64txt = open(b, 'r')
	unidtxt = open(c, 'r')
	rootdir = #-pathtorootdir
	for line in as6txt:
		if line not in ['\n',"\n"]:
			as6.append(line.strip('\n'))

	for shline in sh64txt
		if shline not in ['\n',"\n"]:
			sh64.append(line.strip('\n'))
	
	for uniline in unidtxt
		if uniline not in ['\n',"\n"]:
			unid.append(line.strip('\n'))

	for subdir, dirs, files in os.walk(rootdir):
		for infile in files:
			currtxt = open(infile.txt, 'r')
			for nline in currtxt:
				if nline in as6:
					copyfile(os.path.jooin(subdir, infile),-dstpathas6/infile)
					break
				elif nline in sh64
					copyfile(os.path.jooin(subdir, infile),-dstpathsh64/infile)
					break
				elif nline in unid
					copyfile(os.path.jooin(subdir, infile),-dstpathunid/infile)
					break
				else:
					None

