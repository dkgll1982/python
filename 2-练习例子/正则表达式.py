#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-17 15:27
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 正则表达式
# @Software: PyCharm

import re
if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
    print("-  ok")
if re.match(r'^\d{3}\d{3,8}$', '01012345'):
    print("ok")