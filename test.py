# -*- coding:utf-8 -*-
import pymongo
import random
from pymongo import MongoClient
from bson.objectid import ObjectId
import sys
import getopt
from datetime import datetime, timedelta, tzinfo
import time as t
import pytz
import re


# 默认localhost 27017
client = MongoClient()
# 选择 test_tbl db
db = client['test_report']
# 时区
tz = pytz.timezone('Asia/Shanghai')

html_tags = ["a","abbr","acronym","address","applet","area","article","aside",
			 "audio","b","base","basefont","bdi","bdo","big","blockquote","body",
			 "br","button","canvas","caption","center","cite","code","col",
			 "colgroup","command","datalist","dd","del","details","dir","div",
			 "dfn","dialog","dl","dt","em","embed","fieldset","figcaption",
			 "figure","font","footer","form","frame","frameset","h6","head",
			 "header","hr","html","i","iframe","img","input","ins","isindex",
			 "kbd","keygen","label","legend","li","link","map","mark","menu",
			 "meta","meter","nav","noframes","noscript","object","ol","optgroup",
			 "option","output","p","param","pre","progress","q","rp","rt","ruby",
			 "s","samp","script","section","select","small","source","span",
			 "strike","strong","style","sub","details","sup","table","tbody",
			 "td","textarea","tfoot","th","thead","time","title","tr","track",
			 "tt","u","ul","var","video","wbr","xmp"]


# 从时间随机生成ObjectId
def random_object_id_from_datetime():
    from_datetime = datetime.utcnow() + timedelta(days=random.randint(1, 10),hours=random.randint(1, 10),minutes=random.randint(0, 50),weeks=random.randint(1, 10))
    return ObjectId.from_datetime(generation_time=from_datetime)

# 从范围随机生成ObjectId
def random_object_id_from_randint(n):
	to_hex = format(random.randint(0, n), 'x')
	to_hex = to_hex.zfill(24)
	return ObjectId(to_hex)

# 打印Usage
def print_usage():
	print("Usage: test.py -n <number_of_inserts> -t <tbl_name>")

# 生成随机数据list
def random_data_list(func, n=100000):
	data_list = []
	for _ in range(n):
		data_list.append(func())
	return data_list

# 把UTC时间改成UTC+8
def to_utc_8_datetime(year, month=1, day=1, hour=0, minute=0, second=0, microsecond=0):
	if not year:
		year = 1970
		hour = 9
	return datetime(year, month, day, hour, minute, second, microsecond) + \
			timedelta(hours=8)


# 生成随机数据
def add_random_data(func, n=100000):
	start = datetime.utcnow()
	start_sec = t.time()
	collection.insert_many(random_data_list(func, n=n))
	end = datetime.utcnow()
	end_sec = t.time()
	time_ms = (end_sec - start_sec) * 1000
	print("开始时间： " + str(start))
	print("结束时间： " + str(end))
	print("插入{num}条数据用时： {time}".format(num=n, time=(end - start)))
	print("每条数据平均用时： {time_ms}毫秒".format(time_ms=(time_ms / n)))

# tbl_report_raw 集合 随机数据生成
def tbl_report_raw_random_data():
	utc_timestamp = t.time() + t.timezone
	utc_datetime = datetime.fromtimestamp(utc_timestamp)
	exttype = random.randint(1, 600)
	rand_extlist = {}
	if random.randint(0, 9) > 4:
		rand_extlist = {'test_path' : [random_object_id_from_randint(10000) \
						for _ in range(random.randint(0,10))] }

	data = {
	  # 上传唯一id
	  # "_id" : random_object_id_from_datetime(),
	  # parent id
	  "pid" : random_object_id_from_datetime(),
	  # 事件名称
	  "name" : random.sample(html_tags, 1),
	  # 可用作删除
	  "flag" : random.randint(0, 1),
	  # 分类
	  "extid" : random_object_id_from_datetime(),
	  "exttype" : exttype,
	  "type" : exttype // 10,
	  # 拓展类别，如用户性别
	  "tag" : [random_object_id_from_randint(1000) for _ in range(random.randint(0,5))],
	  # 知识点树路径
	  "klist" : [random_object_id_from_randint(10000) for _ in range(random.randint(0,5))],
	  # 关系树路径
	  "rlist" : [random_object_id_from_randint(100) for _ in range(random.randint(0,7))],
	  # 拓展路径
	  "extlist" : rand_extlist,
	  # 届
	  "uyear" : random.randint(2013, 2018),
	  # 用户ID
	  "uid" : random_object_id_from_datetime(),
	  # 文件ID
	  "fid" : random_object_id_from_datetime(),
	  # 设备ID
	  "eid" : random_object_id_from_datetime(),
	  # 外部ID
	  "openid" : random_object_id_from_datetime(),
	  # 次数
	  "v1" : random.uniform(10, 90),
	  # 时长(秒)
	  "v2" : random.uniform(50, 500),
	  # 拓展数值
	  "v3" : { 'test_v3' : random.uniform(200, 222222)},
	  # 字符串数值
	  "cfg" : random.sample(html_tags, 1),
	  # UTC 日期时间
	  "utc_date" : utc_datetime,
	  "utc_ts" : utc_timestamp
	}
	return data

# tbl_report_raw_separate_date 集合 随机数据生成
def tbl_report_raw_separate_date_random_data():
	data = {
	  "name" : "手写风格",
	  "flag" : random.randint(0, 1),
	  "extid" : random_object_id_from_datetime(),
	  "exttype" : random.randint(1, 600),
	  "type" : random.randint(1, 6) * 10,
	  "tag" : [],
	  "klist" : [random_object_id_from_randint(10000) for _ in range(random.randint(0,5))],
	  "rlist" : [random_object_id_from_randint(100) for _ in range(random.randint(0,7))],
	  "extlist" : [random_object_id_from_randint(10000) for _ in range(random.randint(0,10))],
	  "uid" : random_object_id_from_datetime(),
	  "uyear" : random.randint(2000, 2018),
	  "date_y" : random.randint(2010, 2018),
	  "date_m" : random.randint(1, 12),
	  "date_d" : random.randint(1, 28),
	  "time_h" : random.randint(0, 23),
	  "time_m" : random.randint(0, 59),
	  "time_s" : random.randint(0, 59),
	  "pid" : random_object_id_from_datetime(),
	  "eid" : random_object_id_from_datetime(),
	  "v1" : random.uniform(10, 90),
	  "v2" : random.uniform(50, 500),
	  "v3" : random.uniform(200, 222222),
	  "cfg" : "测试测试测试测试",
	  "outid" : random_object_id_from_datetime(),
	  "_tick" : t.time()
	}
	return data

def run_test_suite(func):
	func()

# tbl_report_raw 集合 测试函数
def tbl_report_raw_run_test():
	print("###单个条件匹配###")
	# TODO 测试name
	# TODO 测试flag
	general_test_count({'extid' : ObjectId('5b7702090000000000000000')})
	general_test_count({'exttype' : 355})
	general_test_count({'type' : 50})
	# TODO 测试tag
	general_test_count({'klist' : {'$in': [ObjectId('5b25389d0000000000000000')]}})
	general_test_count({'rlist' : {'$in': [ObjectId("5b6215650000000000000000")]}})
	general_test_count({'extlist.test_path' : {'$exists' : True, '$in' : [ObjectId('000000000000000000001186')]}})
	general_test_count({'uid' : ObjectId("5b3d42210000000000000000")})
	general_test_count({'uyear' : {'$gt' : 2016}})
	# TODO 测试date
	general_test_count({'pid' : ObjectId("5b2296760000000000000000")})
	general_test_count({'eid' : ObjectId("5b479e3a0000000000000000")})
	general_test_count({'v1' : {'$gt' : 55, '$lt' : 60}})
	general_test_count({'v2' : {'$gt' : 150, '$lt' : 300}})
	general_test_count({'v3' : {'$gt' : 200, '$lt' : 100000}})
	#general_test_count({'outid' : ObjectId("5b574baa0000000000000000")})
	# TODO 测试_tick
	print("###多个条件混合匹配###")
	general_test_count({'uyear' : {'$gt' : 2017}, 'v1' : {'$gt' : 89.9}})
	general_test_count({'uyear' : {'$gt' : 2015}, 'v1' : {'$gt' : 10}, 
						'klist' : {'$in': [ObjectId('5b25389d0000000000000000')]}})
	general_test_count({'uyear' : {'$gt' : 2015}, 'exttype' : 400, 
						'klist' : {'$in': [ObjectId("5a0ab7dad5cb310b9830ef27")]}})
	general_test_print({'date' : {'$lt' : datetime.now(tz)}})
	general_test_count({'uyear' : {'$gt' : 2016}, 'exttype' : {'$gt' : 400}, 
						'extlist.test_path' : {'$exists' : True, '$in' : [ObjectId('000000000000000000001186')]}})

def tbl_report_raw_separate_date_run_test():
	print("###单个条件匹配###")
	# TODO 测试name
	# TODO 测试flag
	general_test_count({'extid' : ObjectId('5b7702090000000000000000')})
	general_test_count({'exttype' : 355})
	general_test_count({'type' : 50})
	# TODO 测试tag
	general_test_count({'klist' : {'$in': [ObjectId('5b25389d0000000000000000')]}})
	general_test_count({'rlist' : {'$in': [ObjectId("5b6215650000000000000000")]}})
	# TODO 测试extlist
	general_test_count({'uid' : ObjectId("5b3d42210000000000000000")})
	general_test_count({'uyear' : {'$gt' : 2016}})
	# TODO 测试date
	general_test_count({'pid' : ObjectId("5b2296760000000000000000")})
	general_test_count({'eid' : ObjectId("5b479e3a0000000000000000")})
	general_test_count({'v1' : {'$gt' : 55, '$lt' : 60}})
	general_test_count({'v2' : {'$gt' : 150, '$lt' : 200}})
	general_test_count({'v3' : {'$gt' : 200, '$lt' : 1000}})
	general_test_count({'outid' : ObjectId("5b574baa0000000000000000")})
	# TODO 测试_tick
	print("###多个条件混合匹配###")
	# 选择exttype, klist知识点元素，特定日期，特定时间
	general_test_count({'exttype' : 400, 
						'type' : 30,
						'date_y' : 2016, 'date_m' : 6})
	general_test_count({'klist' : {'$in': [random_object_id_from_randint(10000) for _ in range(30)]},
						'date_y' : 2015, 'date_m' : 6,
						'time_h' : {'$gt' : 12}})
	general_test_count({'klist' : {'$in': [random_object_id_from_randint(10000) for _ in range(30)]},
						'date_y' : 2015, 'date_m' : 6})
	# 选择exttype, klist知识点元素，日期范围
	stamp = t.mktime(datetime(2015,9,10,hour=12,minute=30,second=30))
	print(stamp)
	general_test_count({'klist' : {'$in': [random_object_id_from_randint(10000) for _ in range(30)]},
						'_tick' : {'$gt' : stamp}})


# 通用测试函数 计数
def general_test_count(query):
	fields = query.keys()
	print("[测试搜索{fields}]".format(fields=fields))
	print("查询条件： " + str(query))
	start = start_sec = t.time()
	results = collection.find(query).count()
	end = end_sec = t.time()
	time_ms = (end_sec - start_sec) * 1000
	print("用时： {time_ms}毫秒".format(time_ms=time_ms))
	print("结果个数: " + str(results))
	print("")
	return int(results)

# 通用测试函数 打印
def general_test_print(query, limit=1000000):
	fields = query.keys()
	print("[测试搜索{fields}]".format(fields=fields))
	print("查询条件： " + str(query))
	print("限制个数: " + str(limit))
	start = start_sec = t.time()
	results = collection.find(query).limit(limit)
	end = end_sec = t.time()
	time_ms = (end_sec - start_sec) * 1000
	print("用时： {time_ms}毫秒".format(time_ms=time_ms))
	print("结果个数： " + str(results.count()))
	for result in results:
		print("_id: " + str(result['_id']) , \
		({field : result[re.sub('\.+.*', '', field)] for field in fields}))
	print("")

# 通用函数 批量删除
def general_delete(query):
	count = general_test_count(query)
	if count:
		print("即将删除{count}条数据, [Y/N]?".format(count=count))
		sys.stdout.flush()
		option = input()
		if option != 'Y':
			print("放弃删除")
		else:
			start = start_sec = t.time()
			collection.delete_many(query)
			end = end_sec = t.time()
			time_ms = (end_sec - start_sec) * 1000
			print("用时： {time_ms}毫秒".format(time_ms=time_ms))
			print("删除个数： ", count)
			print("删除每条数据平均用时： {time_ms}毫秒".format(time_ms=(time_ms / count)))
	else:
		print("无数据可供删除")

# main
if __name__ == '__main__':
	global collection
	num = 10000
	func = None
	test_func = None
	run_test = False
	insert_data = False
	delete_data = False
	if len(sys.argv) < 4:
		print_usage()
		sys.exit(1)
	try:
		opts, args = getopt.getopt(sys.argv[1:], "n:f:td")
	except getopt.GetoptError:
		print_usage()
		sys.exit(1)
	for opt, arg in opts:
		if opt == '-n':
			try:
				num = int(arg)
				if num <= 0:
					print("插入数据数量需要大于零")
					print_usage()
					sys.exit(2)
				insert_data = True
			except ValueError:
				print_usage()
				sys.exit(2)
		elif opt == '-f':
			if arg == 'raw':
				func = tbl_report_raw_random_data
				test_func = tbl_report_raw_run_test
				collection = db['tbl_report_raw3']
			elif arg == 'raw_s':
				func = tbl_report_raw_separate_date_random_data
				test_func = tbl_report_raw_separate_date_run_test
				collection = db['tbl_report_raw_separate_date']
			else:
				print_usage()
				sys.exit(1)
		elif opt == '-t':
			run_test = True
		elif opt == '-d':
			delete_data = True
		else:
			print_usage()
			sys.exit(3)
	if insert_data:
		add_random_data(func, n=num)
	if run_test:
		run_test_suite(test_func)
	if delete_data:
		general_delete({'exttype' : {'$gte' : 0}})