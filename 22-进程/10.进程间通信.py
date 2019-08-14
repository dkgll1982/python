#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-11 16:40:47 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-11 16:40:47 
# @Software: vscode 

from multiprocessing import Process,Queue
import os,time

def write(q):
    print("启动写子进程%s" %(os.getpid()))
    for chr in ["A","B","C","D"]:
        q.put(chr);
        time.sleep(1)   
    print("结束写子进程%s"%(os.getpid()))

def read(q):
    print("启动读子进程%s"%(os.getpid()))
    while True:
        value = q.get(True)
        print("value = " + value)
    print("结束读子进程%s" %(os.getpid()))

if __name__ == "__main__":
    #父进程创建队列，并传递给子进程
    q = Queue()
    pw = Process(target = write,args=(q,))
    pr = Process(target = read,args=(q,))

    pw.start();
    pr.start()

    #
    pw.join()
    #pr进程里是个死循环，无法等待其结束，只能强行结束
    pr.terminate()

    print("父进程结束")

