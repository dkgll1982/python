#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: 航天神舟智慧系统技术有限公司
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2019-08-11 18:14:10
# @Last Modified by: guojun
# @Last Modified time: 2019-08-11 18:14:10
# @Software: vscode

'''
    多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在每个进程中，互不影响，而多线程中，所有变量都由所有线程共享。
    所以，任何一个变量都可以被任意一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时修改一个变量，容易把数据改乱了。
'''

import threading
num = 10

#锁对象
lock = threading.Lock()


def run(n):
    global num
    for i in range(1000000):
        # with(lock):           #with Lock的作用相当于自动获取和释放锁(资源)
        #     num = num + n     #锁定期间，其他线程不可以干活
        #     num = num - n

        #两个线程会最开始抢这个锁，拿到锁就会处于关锁，执行后面的程序，其他线程执行处于监听状态，等待这个线程开锁，再抢锁    
        lock.acquire()
        num = num + n
        num = num - n
        lock.release()

if __name__ == "__main__":
    t1 = threading.Thread(target=run, args=(6,))
    t2 = threading.Thread(target=run, args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("num=", num)
