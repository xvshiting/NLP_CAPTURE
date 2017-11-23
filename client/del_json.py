import json
# import urllib.parse
import urllib2
import os
import sys

url = "http://localhost:8899/DelJson/"



# param = {'k': 'v'}
# req_dict = {'param': param}
# req_json=[]
# files=os.listdir("./result")
# # print(files)
# for file in files:
# 	if not file.endswith("txt")or file.startswith('.'):
# 		continue
# 	file_path="./result"+os.sep+file
# 	with open(file_path,'r')as f:
# 		req_json=json.load(f)
# 	req_json=json.dumps(req_json)
# 	req_post = req_json.encode('utf-8')
# 	headers = {'Content-Type': 'application/json'}
# 	req = urllib2.Request(url=url, headers=headers, data=req_post)
# 	res = urllib2.urlopen(req)
# 	res = res.read().decode('utf-8')
# 	print(res)

def delJson(name):
	# print(name)
	# print(content)
	my_url=url+name
	req_json=json.dumps(content)
	req_post=req_json.encode('utf_8')
	headers = {'Content-Type': 'application/json'}
	req=urllib2.Request(url=my_url, headers=headers, data=req_post)
	res = urllib2.urlopen(req)
	res = res.read().decode('utf-8')
	print(res)

if __name__ == '__main__':
	file_path=sys.argv[1]
	delJson(file_path)
