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
    多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在每个进程中，互不影响，而多线程中，所有变脸都有所有线程共享。
    所以，任何一个变量都可以被任意一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时修改一个变量，容易把数据改乱了。
'''

import threading
num = 10

#锁对象
lock = threading.Lock()

def run(n):
    global num 
    for i in range(1000000):
        #锁，确保了代码这段代码只能由一个线程从头到尾的完整执行，设置到全局变量才考虑加锁
        #阻止了多线程的并发执行，包含锁的某段代码实际上只能以单线程模式执行，所以效率大大滴降低了
        #由于可以存在于多个锁，不同线程持有不同的锁，并试图获取其他的锁，可能造成死锁。导致多个线程挂起。这样靠操作系统强制终止。
        '''
        lock.acquire()
        try:
            num = num + n
            num = num - n
        finally:
            #修改完一定要释放锁
            lock.release()
        '''
        #与上面代码相同，with lock可以自动上锁和解锁
        with(lock):
            num = num + n
            num = num - n
            
if __name__ =="__main__":
    t1 =threading.Thread(target=run,args=(6,))
    t2 =threading.Thread(target=run,args=(9,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print("num=",num)