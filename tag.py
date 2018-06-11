# -*- coding:utf-8 -*-
import re

with open("tag.txt", 'r') as f:
	content = f.read()
	#print(content)
	result = re.sub('(>.*[\r\n]*.*<)', '","', content)
	print(result)
