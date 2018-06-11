from datetime import *
import time

print("UTC Now: ", datetime.utcnow())
print("UTC Now to Time: ", datetime.utcnow().time())
print("UTC Now to Timestamp: ", time.mktime(datetime.utcnow().timetuple()))
print("UTC from Timestamp: ", datetime.fromtimestamp(time.mktime(datetime.utcnow().timetuple())))

print("Now: ", datetime.now())
print("Now to Time: ", datetime.now().time())
print("Now to Timestamp: ", time.mktime(datetime.now().timetuple()))

print("Timestamp: ", time.time())
print("Timezone: ", time.timezone)
print("UTC Timestamp: ", time.time() + time.timezone)
print("UTC Datetime from Timestamp: ", datetime.utcfromtimestamp(time.time()))
print("Datetime from Timestamp: ", datetime.fromtimestamp(time.time()))
print("Datetime from UTC Timestamp: ", datetime.fromtimestamp(time.time() + time.timezone))