#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-17 22:20:05 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-17 22:20:05 
# @Software: vscode 

import threading,time

sem = threading.Semaphore(5)

#如果在主机执行IO密集型任务的时候再执行这种类型的程序时，计算机就有很大可能会宕机。
#这时候就可以为这段程序添加一个计数器功能，来限制一个时间点内的线程数量。
def run():
    #with sem:
    #    for i in range(5):
    #        print("%s--%d"%(threading.currentThread().name,i))
    #        time.sleep(1);

    #等同于下边的用法        
    sem.acquire()    #计数器获得锁
    for i in range(5):
        print("%s--%d"%(threading.currentThread().name,i))
        time.sleep(1)
    sem.release()    #计数器释放锁

if __name__ == "__main__":
    for i in range(5):
        threading.Thread(target = run).start() 
