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
import time
import os;

def run(int):
    print("子进程%d启动"%int)
    sleep(int);
    print("子进程%d结束"%int)

if __name__ == "__main__":
    print("主进程启动")
    start = time.time()
    #创建子进程
    #target说明执行的任务
    p1 = Process(target = run,args=(5,))
    p2 = Process(target = run,args=(3,))
    p3 = Process(target = run,args=(2,))

    #启动任务
    p1.start()
    p1.join()       #阻塞进程直到完成才往下执行
    p2.start()
    p2.join()
    p3.start() 
    p3.join()
    
    end = time.time()
    print("主进程结束,耗时：%s秒"%(end-start))