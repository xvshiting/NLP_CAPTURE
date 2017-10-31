import json

import urllib.parse
import urllib.request

url = "http://localhost:8899/"

param = {'k': 'v'}
req_dict = {'param': param}
req_json = json.dumps(req_dict)
req_post = req_json.encode('utf-8')
print(req_post)

headers = {'Content-Type': 'application/json'}
req = urllib.request.Request(url=url, headers=headers, data=req_post)
res = urllib.request.urlopen(req)
res = res.read().decode('utf-8')
print(res)