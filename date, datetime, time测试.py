from datetime import *
import time

print("UTC Now: ", datetime.utcnow())
print("UTC Now to Time: ", datetime.utcnow().time())
print("UTC Now to Timestamp: ", time.mktime(datetime.utcnow().timetuple()))
print("UTC from Timestamp: ", datetime.fromtimestamp(time.mktime(datetime.utcnow().timetuple())))

print("Now: ", datetime.now())
print("Now to Time: ", datetime.now().time())
print("Now to Timestamp: ", time.mktime(datetime.now().timetuple()))

# 当地时间Timestamp
print("Timestamp: ", time.time())
print("Timezone: ", time.timezone)
# UTC时间 Timestamp
print("UTC Timestamp: ", time.time() + time.timezone)
print("UTC Datetime from Timestamp: ", datetime.utcfromtimestamp(time.time()))
print("Datetime from Timestamp: ", datetime.fromtimestamp(time.time()))
# utcfromtimestamp 会根据本机时区增减时差
print("Datetime from UTC Timestamp: ", datetime.utcfromtimestamp(time.time()))