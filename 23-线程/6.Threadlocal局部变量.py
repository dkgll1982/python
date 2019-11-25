#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-19 14:53:00 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-19 14:53:00 
# @Software: vscode 

#参考链接：https://www.liaoxuefeng.com/wiki/897692888725344/923057354442720

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    print('Hello, %s (in %s)' % (local_school.student, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()