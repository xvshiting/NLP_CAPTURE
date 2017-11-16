import tools 
from capture import capture
import json
def process(records):
	# print(param)
	records=json.loads(records)
	res=dict()
	for record in records:
		temp_dict=dict()
		key_ID,contents=tools.record_parse(record)
		# with open("./record.txt","a") as f:
		# 	f.write("\n\n\n"+key_ID+"\n\n")
		# 	f.write(contents+"\n")
		# print(contents)
		capture_content=capture().parse_re(contents)
		res[key_ID]=tools.content2dict(capture_content)
	return res