import tools 
from capture import capture
def process(param):
	print(param)
	key_ID,contents=tools.json_parse(param)
	capture_content=capture().parse_re(contents)
	return tools.content2json(capture_content)