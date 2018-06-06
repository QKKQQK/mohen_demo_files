# encoding: utf-8
from __future__ import division
import pymongo
import pprint
import random
from pymongo import MongoClient
from bson.objectid import ObjectId
import sys
import getopt
from datetime import datetime
from datetime import timedelta
import time


# 默认localhost 27017
client = MongoClient()
# 选择 test_tbl db
db = client['test_tbl']

# 辅助函数
def random_object_id():
    from_datetime = datetime.utcnow() + timedelta(days=random.randint(1, 10),hours=random.randint(1, 10),minutes=random.randint(0, 50),weeks=random.randint(1, 10))
    return ObjectId.from_datetime(generation_time=from_datetime)

def print_usage():
	print "Usage: test.py -n <number_of_inserts> -t <tbl_name>"

def random_data_list(func, n=100000):
	data_list = []
	for _ in xrange(n):
		data_list.append(func())
	return data_list

def add_random_data(func, n=100000):
	start = datetime.utcnow()
	start_sec = time.time()
	collection.insert_many(random_data_list(func, n=n))
	end = datetime.utcnow()
	end_sec = time.time()
	time_ms = (end_sec - start_sec) * 1000
	print "开始时间： " + str(start)
	print "结束时间： " + str(end)
	print "插入{num}条数据用时： {time}".format(num=n, time=(end - start))
	print "每条数据平均用时： {time_ms}毫秒".format(time_ms=(time_ms / n))

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

# tbl_report_raw 集合 测试函数
def tbl_report_raw_run_test():
    tbl_report_raw_extid_test()

def tbl_report_raw_extid_test():
	print "[测试搜索extid]"
	start = datetime.utcnow()
	results = collection.find({'extid' : ObjectId('5b7702090000000000000000')}).limit(100)
	end = datetime.utcnow()
	print "开始时间： " + str(start)
	print "结束时间： " + str(end)
	print "用时： {time}".format(time=(end - start))
	print "结果_id列表 (limit 100) : "
	print ([result['_id'] for result in results])
	print ""

# main
if __name__ == '__main__':
	global collection
	num = 10000
	func = None
	run_test = False
	insert_data = False
	if len(sys.argv) < 4:
		print_usage()
		sys.exit(1)
	try:
		opts, args = getopt.getopt(sys.argv[1:], "n:f:t")
	except getopt.GetoptError:
		print_usage()
		sys.exit(1)
	for opt, arg in opts:
		if opt == '-n':
			try:
				num = int(arg)
				if num <= 0:
					print "插入数据数量需要大于零"
					print_usage()
					sys.exit(2)
				insert_data = True
			except ValueError:
				print_usage()
				sys.exit(2)
		elif opt == '-f':
			if arg == 'raw':
				func = tbl_report_raw_random_data
				collection = db['tbl_report_raw_test']
			else:
				print_usage()
				sys.exit(1)
		elif opt == '-t':
			run_test = True
		else:
			print_usage()
			sys.exit(3)
	if insert_data:
		add_random_data(func, n=num)
	if run_test:
		tbl_report_raw_run_test()