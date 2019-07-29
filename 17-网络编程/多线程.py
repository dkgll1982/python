#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-10 10:01
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 多线程
# @Software: PyCharm

import time
import threading

def job1():
    global n#, lock
    # 获取锁
    #lock.acquire()
    for i in range(10):
        n += 1
        print('job1', n)
    print("等待锁资源释放......")
    time.sleep(3)
    #lock.release()


def job2():
    global n#, lock
    # 获取锁
    #lock.acquire()
    for i in range(10):
        n += 10
        print('job2', n)
    #lock.release()

n = 0
# 生成锁对象
#lock = threading.Lock()

t1 = threading.Thread(target=job1)
t2 = threading.Thread(target=job2)
t1.start()
t2.start()