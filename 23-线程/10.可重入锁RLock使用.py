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
# RLock定义：可重复锁，是线程相关的锁。同样是线程相关的还有threading.local。
# 重入锁实现可重入性原理或机制是：每一个锁关联一个线程持有者和计数器，当计数器为 0 时表示该锁没有被任何线程持有，
# 那么任何线程都可能获得该锁而调用相应的方法；当某一线程请求成功后，JVM会记下锁的持有线程，并且将计数器置为 1；
# 此时其它线程请求该锁，则必须等待；而该持有锁的线程如果再次请求这个锁，就可以再次拿到这个锁，同时计数器会递增；
# 当线程退出同步代码块时，计数器会递减，如果计数器为 0，则释放该锁。

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
