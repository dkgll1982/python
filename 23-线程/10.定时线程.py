#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 22:39
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 10.定时线程.py
# @Software: PyCharm

import  threading,time

def run():
    print("线程执行")

#延迟5秒执行
t = threading.Timer(5,run)

t.start()

t.join()

print("父线程结束")