from datetime import datetime

f = open('access.log.1')

for line in f:
    line = line.strip()
    l = line.split(' ')
    liners =  float(l[0])
    print datetime.fromtimestamp(liners)
f.close()

