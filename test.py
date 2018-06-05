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

# 辅助函数
def random_object_id():
    from_datetime = datetime.utcnow() + timedelta(days=random.randint(1, 10),hours=random.randint(1, 10),minutes=random.randint(0, 50),weeks=random.randint(1, 10))
    return ObjectId.from_datetime(generation_time=from_datetime)

# tbl_report_raw 集合 辅助函数
def tbl_report_raw_random_data():
	data = {
	  "name" : "手写风格",
	  "flag" : random.randint(0, 1),
	  "extid" : random_object_id(),
	  "exttype" : random.randint(1, 600),
	  "type" : random.randint(1, 6) * 10,
	  "tag" : [],
	  "klist" : [random_object_id() for _ in xrange(random.randint(0,3))],
	  "rlist" : [random_object_id() for _ in xrange(random.randint(0,3))],
	  "extlist" : [random_object_id() for _ in xrange(random.randint(0,3))],
	  "uid" : random_object_id(),
	  "uyear" : random.randint(2000, 2018),
	  "date" : datetime.utcnow(),
	  "pid" : random_object_id(),
	  "eid" : random_object_id(),
	  "v1" : random.uniform(10, 90),
	  "v2" : random.uniform(50, 500),
	  "v3" : random.uniform(200, 222222),
	  "cfg" : "测试测试测试测试",
	  "outid" : random_object_id(),
	  "_tick" : datetime.utcnow()
	}
	return data

def tbl_report_raw_random_data_list(n=100000):
	data_list = []
	for _ in xrange(n):
		data_list.append(tbl_report_raw_random_data())
	return data_list

def tbl_report_raw_add_random_data(n=100000):
	start = datetime.utcnow()
	print "开始时间： " + str(start)
	collection.insert(tbl_report_raw_random_data_list(n))
	end = datetime.utcnow()
	print "结束时间： " + str(end)
	print "用时： " + str(end - start)

# 插入10万条数据 ~1min
# 插入50万条数据 ~5min
tbl_report_raw_add_random_data(n=100000)