import json
from logger import logger
def json_parse(param):
	logger().info("In json_parse")
	return json2txt("jsontxt")
def json2txt(content):
	logger().info("In json2txt")
	return "1111","我有3个孩子"
def content2json(content):
	d=dict()
	for c in content:
		d[c[0]]=c[1]
	logger().info("In content2json")
	return d