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
    #使用with来使用线程条件变量
    with cond:
        for i in range(0,10,2):
            print(threading.current_thread().name,i)
            #time.sleep(1)
            #执行完成后等待信号（这里等待的是run2函数执行完打印步数和线程名称后的释放信号）
            cond.wait()
            #释放信号（这里是释放run2函数执行完打印步数和线程名称之后释放run2的信号）
            cond.notify()
def run2():
    with cond:
        for i in range(1,10,2):
            print(threading.current_thread().name,i)
            #time.sleep(1)
            #释放信号（这里释放的是run1打印完步数 0 的时候等待的信息）
            cond.notify()
            #等待信号（这里是run2执行完打印线程名称和步数后进入等待状态）
            cond.wait()

threading.Thread(target= run1).start()
threading.Thread(target= run2).start()
