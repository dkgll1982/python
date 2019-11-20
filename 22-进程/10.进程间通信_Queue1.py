#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-11 16:40:47 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-11 16:40:47 
# @Software: vscode 

#进程间通信
#进程彼此之间互相隔离，要实现进程间通信（IPC），multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的。

from multiprocessing import Process,Queue
import os,time

def write(q):
    print("启动写子进程%s" %(os.getpid()))
    for chr in ["A","B","C","D"]:
        q.put(chr);
        time.sleep(0.1)   
    print("结束写子进程%s"%(os.getpid()))

def read(q):
    print("启动读子进程%s"%(os.getpid()))
    while True:
        value = q.get(True)
        time.sleep(1) 
        print("value = " + value)
    print("结束读子进程%s" %(os.getpid()))

if __name__ == "__main__":
    #父进程创建队列，并传递给子进程
    q = Queue()
    pw = Process(target = write,args=(q,))
    pr = Process(target = read,args=(q,))

    pw.start();
    pr.start()

    #join()方法可以在当前位置阻塞主进程，带执行join()的进程结束后再继续执行主进程的代码逻辑。
    pw.join()
    time.sleep(5) 
    #pr进程里是个死循环，无法等待其结束，只能强行结束
    pr.terminate()

    print("父进程结束")
    #利用多线程时，一般都先让子线程调用start() ，然后再去调用join()，让主进程等待子进程结束才继续走后续的逻辑。
