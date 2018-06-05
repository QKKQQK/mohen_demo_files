# encoding: utf-8

import pymongo
import pprint
import random
from pymongo import MongoClient
from bson.objectid import ObjectId
import bson.json_util
from datetime import datetime

# 默认localhost 27017
client = MongoClient()
# 选择 test_tbl db
db = client['test_tbl']
# 选择 tbl_report_raw_test 集合
collection = db['tbl_report_raw_test']

# 测试连接
pprint.pprint(collection.find_one())

def insert():
	post = {
	  "name" : "手写风格",
	  "flag" : random.randint(0, 1),
	  "extid" : ObjectId("000000000000000000000000"),
	  "exttype" : random.randint(1, 600),
	  "type" : random.randint(1, 6) * 10,
	  "tag" : [],
	  "klist" : [ObjectId("5a0ab7dad5cb310b9830ef27"), ObjectId("5a0ab7dad5cb310b9830ef27")],
	  "rlist" : [],
	  "extlist" : [],
	  "uid" : ObjectId("5a0ab7dad5cb310b9830ef27"),
	  "uyear" : random.randint(2000, 2018),
	  "date" : datetime.utcnow(),
	  "pid" : ObjectId("5a0ab7dad5cb310b9830ef27"),
	  "eid" : ObjectId("5a0ab7dad5cb310b9830ef27"),
	  "v1" : random.uniform(10, 90),
	  "v2" : random.uniform(50, 500),
	  "v3" : random.uniform(200, 222222),
	  "cfg" : "测试测试测试测试",
	  "outid" : ObjectId("5a0ab7dad5cb310b9830ef27"),
	  "_tick" : datetime.utcnow()
	}
	collection.insert_one(post)



for _ in xrange(10000):
	insert()