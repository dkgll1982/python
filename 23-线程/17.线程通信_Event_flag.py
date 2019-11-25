#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 22:59
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 11.线程通信.py
# @Software: PyCharm

#条件同步和条件变量（condition）同步差不多意思，只是少了锁功能，因为条件同步设计于不访问共享资源的条件环境。

#event围绕一个标志位在搞。
#event=threading.Event()：条件环境对象，初始值 为False；
#event.isSet()：返回event的状态值；
#event.wait()：如果 event.isSet()==False将阻塞线程；
#event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
#event.clear()：恢复event的状态值为False。

import threading
import time

event = threading.Event()

print('1:%s'%event.is_set())

event.wait(1)
print('2:%s'%event.is_set())

event.set()
print('3:%s'%event.is_set())

event.clear()
print('4:%s'%event.is_set()) 

