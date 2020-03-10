#!/usr/bin/env python
import sys
import csv
import json
import pickle
from collections import defaultdict
reload(sys)
sys.setdefaultencoding("utf-8")
d = defaultdict(list)
key_value_list = []
for line in sys.stdin:
	line = line.strip()
	#line = line.encode("raw-unicode-escape")
	index_key = line.split("::")
	index_keys = index_key[2].split("|")
	for i in index_keys:
		if(i == ''):
			key_value = ("none",index_key[1])
		else:
			key_value = (i.lower(),index_key[1])
		key_value_list.append(key_value)
		#print(key_value)
for k,v in key_value_list:
	d[k].append(v)
with open("data_file.pickle", "wb") as write_file:
	pickle.dump(d, write_file)
