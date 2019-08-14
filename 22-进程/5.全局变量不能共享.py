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
num = 100;

def run(str):
    print("子进程启动")
    global num
    num+=1
    sleep(1);
    print("子进程结束%d"%(num))

if __name__ == "__main__":
    print("主进程启动")
    #创建子进程
    #target说明执行的任务
    p = Process(target = run,args=("bad",))
    #启动任务
    p.start()
    #sleep(1);
    p.join()
    p2 = Process(target = run,args=("hight",))
    #启动任务
    p2.start()
    #sleep(1);
    p2.join()
    #run("bad")
    print("主进程结束%d"%(num))