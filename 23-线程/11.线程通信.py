#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 22:59
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 11.线程通信.py
# @Software: PyCharm

import threading,time

def func():
    #事件对象
    event = threading.Event()
    def run():
        for i in range(5):
            #阻塞，等待事件的触发
            event.wait()
            event.clear()
            print("sunck is a good man!!%d"%i)
    t = threading.Thread(target = run).start()
    return event

e = func()

#触发事件
for i in range(5):
    time.sleep(2)
    e.set()



