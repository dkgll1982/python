#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-06-08 11:44
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : time.py
# @Software: PyCharm

from datetime import datetime
import time

i = datetime.now()
cday = i.strftime('%Y-%m-%d %H:%M:%S')
print(cday)
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second) 

c_time = int(round(time.time() * 1000))
time_stamp = 1590404476332
time_array = time.localtime(float(time_stamp/1000))
other_way_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
diff = float((time_stamp-c_time)/1000)
print("当前时间：{}，过期时间为：{}，还剩{}".format(cday,other_way_time,diff))
import datetime
 
# 范围时间
d_time = datetime.datetime.strptime(str(datetime.datetime.now().date())+'9:30', '%Y-%m-%d%H:%M')
d_time1 =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'21:03', '%Y-%m-%d%H:%M')
 
# 当前时间
n_time = datetime.datetime.now()
 
print(d_time,d_time1,n_time) 
# 判断当前时间是否在范围时间内
if n_time < d_time or n_time > d_time1:
    print('当前时间不在时间范围内') 
else:
    print('当前时间在时间范围内')