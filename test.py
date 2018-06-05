# encoding: utf-8

import pymongo
import pprint
from pymongo import MongoClient


# 默认localhost 27017
client = MongoClient()
# 选择 test_tbl db
db = client['test_tbl']
# 选择 tbl_report_raw_test 集合
collection = db['tbl_report_raw_test']

# 测试连接
pprint.pprint(collection.find_one())