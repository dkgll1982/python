#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-11 17:42:09 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-11 17:42:09 
# @Software: vscode 

import threading,time

def run():
    print("子线程(%s)启动"%(threading.current_thread().name))

    #实现线程的功能
    time.sleep(2)
    print("打印")
    time.sleep(2)

    print("子线程(%s)结束"%(threading.current_thread().name))

if __name__ == "__main__":
    #任何进程默认就会启动一个线程，成为主线程，主线程就可以启动新的子线程
    #current_thread(): 返回当前线程的实例
    print("主线程(%s)启动"%(threading.current_thread().name))

    #创建子线程
    t = threading.Thread(target=run,name="rootThread")
    t.start()

    #等待线程结束
    t.join()

    print("主线程(%s)结束"%(threading.current_thread().name))