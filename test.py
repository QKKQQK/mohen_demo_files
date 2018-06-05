# encoding: utf-8

import pymongo
import pprint
import random
from pymongo import MongoClient
from bson.objectid import ObjectId
import bson.json_util
from datetime import datetime
from datetime import timedelta

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
	  "extid" : object_id_from_datetime(),
	  "exttype" : random.randint(1, 600),
	  "type" : random.randint(1, 6) * 10,
	  "tag" : [],
	  "klist" : [object_id_from_datetime() for _ in xrange(random.randint(0,3))],
	  "rlist" : [object_id_from_datetime() for _ in xrange(random.randint(0,3))],
	  "extlist" : [object_id_from_datetime() for _ in xrange(random.randint(0,3))],
	  "uid" : object_id_from_datetime(),
	  "uyear" : random.randint(2000, 2018),
	  "date" : datetime.utcnow(),
	  "pid" : object_id_from_datetime(),
	  "eid" : object_id_from_datetime(),
	  "v1" : random.uniform(10, 90),
	  "v2" : random.uniform(50, 500),
	  "v3" : random.uniform(200, 222222),
	  "cfg" : "测试测试测试测试",
	  "outid" : object_id_from_datetime(),
	  "_tick" : datetime.utcnow()
	}
	collection.insert_one(post)

def object_id_from_datetime():
    from_datetime = datetime.utcnow() + timedelta(days=random.randint(1, 10),hours=random.randint(1, 10),minutes=random.randint(0, 50),weeks=random.randint(1, 10))
    return ObjectId.from_datetime(generation_time=from_datetime)

for _ in xrange(3000000):
	insert()