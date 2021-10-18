

#Load the string with strptime() and get the time() component:

from datetime import datetime
s = "1900-01-01 00:05:00"
dt = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
dt.time().isoformat()
# >>>'00:05:00'

#Here we are dumping the time with isoformat() in ISO 8601 format, 
#but you can also dump the datetime.time back to string with strftime():

dt.time().strftime("%H:%M:%S")
#>>>'00:05:00'

