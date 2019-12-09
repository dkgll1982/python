#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: 航天神舟智慧系统技术有限公司
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2019-11-19 11:06:08
# @Last Modified by: guojun
# @Last Modified time: 2019-11-19 11:06:08
# @Software: vscode
from multiprocessing import Queue,Process
import os
import time
import threading 

def writequeue(q):
    for i in range(31):
        q.put(i)
        print('write to %s,queue is full?%s' % (i,q.full()))    #full()检测队列是否已经满了,True: 满
 
def readqueue(q):
    while True:
        time.sleep(0.5)
        #队列的特点是:先进先出 所以get拿的顺序也是,先进先出 first in first out
        print("read to %s,queue is empty?%s" % (q.get(),q.empty()))   #empty()检测队列是否为空,True:空
        if(q.empty()):
            break

if __name__ == "__main__":
    q = Queue(4)
    
    print("main process start...")

    qw = Process(target=writequeue,args=(q,))
    qr = Process(target=readqueue,args=(q,))

    qw.start()
    qr.start()

    qw.join()

    #time.sleep(5)
    #qr.terminate()  #qr进程里是个死循环，无法等待其结束，只能强行结束

    #第27行检测队列已经为空，跳出循环，此处就可以通过join()方法结束子线程
    qr.join()

    print('main process stop...')