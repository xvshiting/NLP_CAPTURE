import os
import json
files=os.listdir("."+os.sep+"result")
contents=[]
for f in files:
	if not f.endswith('txt'):
		continue
	with open("."+os.sep+"result"+os.sep+f,'r')as f_r:
		contents=contents+json.load(f_r)
with open("./all_result.txt",'w')as f:
	json.dump(contents,f)