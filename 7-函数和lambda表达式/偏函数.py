#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-13 15:44
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 偏函数
# @Software: PyCharm

from datetime import datetime, timedelta


def GetNextDay(baseday, n): 
    return str((datetime.strptime(str(baseday), '%Y-%m-%d')+timedelta(days=n)).date())


selected_day = '2013-07-31'
n = GetNextDay('2013-07-31', 2)
print(n)

import functools
nday = functools.partial(GetNextDay, selected_day, 3)
nday2 = functools.partial(GetNextDay, selected_day)
print(nday())
print(nday2(1))
print(nday2(2))
print(nday2(6))
print(nday2(13))
print(nday2(29))
print('----------------')