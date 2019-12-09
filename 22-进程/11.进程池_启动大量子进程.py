#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 19:02:40 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 19:02:40 
# @Software: vscode

from multiprocessing import Pool
import os,time,random 
import os;
num = 100;

def run(name):
    print("子进程%d启动--%s,父进程id:%s" %(name,os.getpid(),os.getppid())) 
    start =time.time();
    time.sleep(random.choice([2,3,4]))
    end = time.time();
    print("子进程%d结束--%s--耗时%0.2f" %(name,os.getpid(),end-start))

if __name__ == "__main__": 
    print("主进程启动,pid:%s,ppid:%s"%(os.getpid(),os.getppid()))
    #创建多个进程
    #进程池
    #表示可以同时执行的进程数量，默认大小是CPU核心数 
    pp = Pool(3)
    for i in range(4): 
        #创建进程，放入进程池统一管理
        pp.apply_async(run,args=(i,))
    #调用join之前必须先close,调用close之后不能再添加新的进程
    time.sleep(10)
    pp.close()
    #进程池对象调用join，会等待进程池所有的子进程结束之后再去执行父进程
    pp.join()
    #run("bad")
    print("主进程结束,pid:%s,ppid:%s"%(os.getpid(),os.getppid()))