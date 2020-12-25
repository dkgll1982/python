#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 19:02:40 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 19:02:40 
# @Software: vscode

from multiprocessing import Process
from time import sleep 
import os
num = 100

def run(str):
    print("子进程启动,参数：%s"%str)
    global num
    num+=1
    sleep(1)
    print("子进程结束%d"%(num))

if __name__ == "__main__":
    print("主进程启动")
    p = Process(target = run,args=("bad",))
    #守护进程：一定具有daemon属性标志，（thread.setDaemon(True)）就表示这个线程“不重要”。
    #总结：
    # 1.主进程退出，不管子进程是否执行完，子进程都会退出；
    # 2.非守护进程运行完，主进程才算真正的运行完。
    # 3.如果是多进程的话，那么主进程先运行，再运行子进程；如果是多线程的话，那么按照代码的输出顺序输出。
    # 4.如果在守护进程中子进程加了join()（起到阻塞作用），那么主进程会等子进程都运行完。
    p.daemon=True
    p.start()
    #p.join()   
    p2 = Process(target = run,args=("hight",))
    p2.start()
    #p2.join()  
    #如果不用join，守护进程会在主进程代码执行结束后就终止
    print("主进程结束%d"%(num))