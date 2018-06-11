from datetime import *
import time

print("UTC Now: ", datetime.utcnow())
print("UTC Now to Time: ", datetime.utcnow().time())
print("Now: ", datetime.now())
print("Now to Time: ", datetime.now().time())
print("Timestamp: ", time.time())
print("UTC Datetime from Timestamp: ", datetime.fromtimestamp(time.time()))
print("Datetime from Timestamp: ", datetime.fromtimestamp(time.time()))