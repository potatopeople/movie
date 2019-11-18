import time
import datetime

time_tup = time.localtime(time.time())
date1 = time.strftime('%Y-%m-%d %H:%M:%S', time_tup)
date2 = '2019-11-07 16:16:00'
d1 = datetime.datetime.strptime(date1,"%Y-%m-%d %H:%M:%S")
d2 = datetime.datetime.strptime(date2,"%Y-%m-%d %H:%M:%S")
print(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
d = d1 - d2
if d.seconds >= 960:
    print('过期')
else:
    print('ok')
print('相差的秒数：{}'.format(d.seconds))
