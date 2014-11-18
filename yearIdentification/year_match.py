#!/usr/bin/python3
from pathlib import Path
import shutil

preID = Path('./corpus/pre-identification')
postID = Path('./corpus/post-identification')

tabletPaths = preID.glob('*/seperated/*')

tablets = [x for x in tabletPaths]

for t in tablets:
	with t.open() as currTablet:
		pass
		# print(currTablet)
		# Process tablet




AmarSuen6 = Path('./corpus/post-identification/Amar-Suen_6')
Shulgi42 = Path('./corpus/post-identification/Shulgi_42')
Ambiguous = Path('./corpus/post-identification/Ambiguous')
Unidentified = Path('./corpus/post-identification/Unidentified')

#shutil.copy(src, dst)