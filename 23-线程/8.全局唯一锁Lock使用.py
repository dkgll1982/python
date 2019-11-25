#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-20 23:18:13 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-20 23:18:13 
# @Software: vscode 

import threading,time

# 生成锁对象，全局唯一
lock = threading.Lock()
#锁有两种状态：locked(被某一线程拿到)和unlocked(可用状态)
#      操作锁的方式：acquire()和release()
#      如果状态是unlocked，可以调用acquire将状态改为locked#
#      如果状态是locked，acquire会被block直到另一个线程调用release释放锁
#      如果状态是unlocked，调用release会导致RuntimError异常
#      如果状态是locked，可以调用release将状态改为unlocked

# 获取锁。未获取到会阻塞程序，直到获取到锁才会往下执行
#lock.acquire()

# 释放锁，归回倘，其他人可以拿去用了
#lock.release()

# 注意：lock.acquire() 和 lock.release()必须成对出现。否则就有可能造成死锁。

def job1():
    global n
    for i in range(10):
        n+=1
        print('job1',n)

def job2():
    global n
    for i in range(10):
        n+=10
        print('job2',n)

n=0
t1=threading.Thread(target=job1)
t2=threading.Thread(target=job2)
t1.start()
t2.start()

#两个线程共用一个全局变量，又由于两线程是交替执行的，
# 当job1 执行三次 +1 操作时，job2就不管三七二十一 给n做了+10操作。
# 两个线程之间，执行完全没有规矩，没有约束。所以会看到输出当然也很乱。

#加了锁后，这个问题也就解决，来看看

time.sleep(1)
print('\r\n'+'*'*60)

def job1():
    global n, lock
    # 获取锁
    lock.acquire()
    for i in range(10):
        n += 1
        print('job1', n)
    time.sleep(1)
    print('等我把锁还给job2，job2就可以开始工作了...')
    time.sleep(2)
    lock.release() 

def job2():
    global n, lock
    # 获取锁
    lock.acquire()
    for i in range(10):
        n += 10
        print('job2', n)
    lock.release()

n = 0
# 生成锁对象
lock = threading.Lock()

t1 = threading.Thread(target=job1)
t2 = threading.Thread(target=job2)
t1.start()
t2.start()