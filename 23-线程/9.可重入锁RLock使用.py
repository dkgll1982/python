#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: 航天神舟智慧系统技术有限公司
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2019-11-20 22:55:27
# @Last Modified by: guojun
# @Last Modified time: 2019-11-20 22:55:27
# @Software: vscode

import threading

# 每个thread都运行f()，f()获取锁后，运行g()，但g()中也需要获取同一个锁。如果用Lock，这里多次获取锁，就发生了死锁。 
# 但我们代码中使用了RLock。在同一线程内，对RLock进行多次acquire()操作，程序不会堵塞
Rlock = threading.RLock() 

def f():
    with Rlock:
        g()
        h() 

def g():
    with Rlock:
        h()
        do_something1() 

def h():
    with Rlock:
        do_something2() 
 
def do_something1():
    print('do_something1') 

def do_something2():
    print('do_something2') 

try:
    threading.Thread(target=f).start()
    threading.Thread(target=f).start()
    threading.Thread(target=f).start()
except Exception as e:
    print("Error: unable to start thread")
