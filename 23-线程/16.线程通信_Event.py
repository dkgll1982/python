#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 22:59
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 11.线程通信.py
# @Software: PyCharm

from threading import Thread, Event
import time

event = Event()

def student(name):
    print("学生%s 正在听课" % name)
    # 学生听课在等待命令下课
    event.wait()
    # 参数可以设置超时时间 秒数，过了这个时间，即使没有收到信号，都可以活动
    #event.wait(2) 
    
    # 收到下课信号 学生去活动
    print("学生%s 课间活动" % name)

def teacher(name):
    print("老师%s 正在授课" % name)
    time.sleep(7)

    print()
    # 老师发送下课信号，学生也收到
    event.set()
    print("老师%s 通知下课" % name)

if __name__ == "__main__":
    stu1 = Thread(target=student, args=("小马",),)
    stu2 = Thread(target=student, args=("小红",),)
    stu3 = Thread(target=student, args=("小刚",),)

    t1 = Thread(target=teacher, args=("mike",),)

    stu1.start()
    stu2.start()
    stu3.start()
    t1.start()

'''

学生小马 正在听课
学生小红 正在听课
学生小刚 正在听课
老师mike 正在授课

学生小马 课间活动
学生小红 课间活动
学生小刚 课间活动
'''
