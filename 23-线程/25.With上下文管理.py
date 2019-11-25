#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-21 11:40:43 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-21 11:40:43 
# @Software: vscode 

 #当有两个相关的操作需要在一部分代码块前后分别执行的时候，可以使用with语法自动完成。
 # 同时，使用with语法可以在特定的地方分配和释放资源，因此，with语法也叫作"上下文管理器"。
 # 在threading模快中，所有带有acquire()方法和release()方法的对象都可以使用上下文管理器。主要用于代码块的收尾工作。
 #也就是说，下面的对象可以使用with语法：
 #Lock、RLock、Condition、Semaphore

import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

def threading_with(statement):
    with statement:
        logging.debug('%s acquired via with' % statement)

def threading_not_with(statement):
    statement.acquire()
    try:
        logging.debug('%s acquired directly' % statement)
    finally:
        statement.release()

if __name__ == '__main__':
    lock = threading.Lock()
    rlock = threading.RLock()
    condition = threading.Condition()
    mutex = threading.Semaphore(1)
    threading_synchronization_list = [lock, rlock, condition, mutex]

    for statement in threading_synchronization_list:
        t1 = threading.Thread(target=threading_with, args=(statement,))
        t2 = threading.Thread(target=threading_not_with, args=(statement,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()