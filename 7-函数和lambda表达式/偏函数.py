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

# 偏函数和使用默认参数的区别？
# 默认参数，只能代表一种情况，比如说int，默认参数base是10，这样只有在转换为10进制整数时，
# 不需要输入base参数了，因为有默认，但是如果想转为2、8、16进制了，那每次调用时都要输出参数了，
# 现在有了偏函数这个功能，你可以根据int函数，只要有需要，你可以创建任意多的偏函数，
# 例如int2、int8、int16，这样用户在调用的时候就会方便很多了
import functools
nday = functools.partial(GetNextDay, selected_day, 3)
nday2 = functools.partial(GetNextDay, selected_day)
print(nday())
print(nday2(1))
print(nday2(2))
print(nday2(6))
print(nday2(13))
print(nday2(29))
print('-'*40)