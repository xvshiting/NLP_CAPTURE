import json

import urllib.parse
import urllib.request
import os

url = "http://localhost:8899/"

param = {'k': 'v'}
req_dict = {'param': param}
req_json=[]
files=os.listdir("./result")
# print(files)
for file in files:
	if not file.endswith("txt"):
		continue
	file_path="./result"+os.sep+file
	with open(file_path,'r')as f:
		req_json=json.load(f)
	req_json=json.dumps(req_json)
	req_post = req_json.encode('utf-8')
	headers = {'Content-Type': 'application/json'}
	req = urllib.request.Request(url=url, headers=headers, data=req_post)
	res = urllib.request.urlopen(req)
	res = res.read().decode('utf-8')
	print(res)