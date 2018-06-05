import pymongo
from pymongo import MongoClient

# 默认localhost 27017
client = MongoClient()

# 选择 test_tbl db
db = client['test_tbl']

# 选择 tbl_report_raw_test 集合
collection = db['tbl_report_raw_test']