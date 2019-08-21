#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-18 16:46
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 13.线程调度.py
# @Software: PyCharm

import threading,time

#线层条件变量
cond = threading.Condition()
def run1():
    with cond:
        for i in range(0,10,2):
            print(threading.current_thread().name,i)
            #time.sleep(1)
            cond.wait()
            cond.notify()
def run2():
    with cond:
        for i in range(1,10,2):
            print(threading.current_thread().name,i)
            #time.sleep(1)
            cond.notify()
            cond.wait()

threading.Thread(target= run1).start()
threading.Thread(target= run2).start()
