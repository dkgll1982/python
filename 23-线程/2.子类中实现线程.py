#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-21 09:27:28 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-21 09:27:28 
# @Software: vscode 
import threading
import time

exit_flag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    #继承线程类，重写父类的run方法
    def run(self):
        print("Starting %s" %self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting %s" %self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exit_flag:
            import _thread
            _thread.exit()
        time.sleep(delay)
        print("%s:%s:counter-%s" %(threadName, time.ctime(time.time()),counter))
        counter -= 1
# 创建实例
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Exiting Main Thread")