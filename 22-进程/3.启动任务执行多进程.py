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
import os;

def run(str):
    while True:
        print("sunck is a %s man:%s，parent pid is %s"%(str,os.getpid(),os.getppid()));
        sleep(1.2);

if __name__ == "__main__":
    print("主进程启动:%s"%(os.getpid()))
    #创建子进程
    #target说明执行的任务
    p = Process(target = run,args=("bad",))
    #启动任务
    p.start()
    while True:
        sleep(1)
        print("sunck is a good man")