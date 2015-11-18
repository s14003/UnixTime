from datetime import datetime

f = open('access.log.1')
lines2 = f.read().split('\n')
f.close()

line = lines2[0]
date = line[0:13]
date2 = line[14:]
print date + date2
