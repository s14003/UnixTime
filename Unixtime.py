from datetime import datetime

f = open('access.log.1')
test = f.read().strip()
lines2 = test.split('\n')
f.close()

i = 0
size = len(lines2) - 1

while i < size:
    line = lines2[i]
    date = line[14:]
    date2 = float(line[0:13])
    datetime = datetime.fromtimestamp(date2)

    print str(datetime) + date2
    i += 1
