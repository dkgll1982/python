#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: 航天神舟智慧系统技术有限公司
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2019-11-22 21:35:41
# @Last Modified by: guojun
# @Last Modified time: 2019-11-22 21:35:41
# @Software: vscode
# 参考链接：https://www.cnblogs.com/mylu/p/11253143.html

from threading import Event, current_thread, Thread
import time
event = Event() 

def check():
    print('%s  ....' % current_thread().name)
    time.sleep(5)
    event.set() 

def connect():
    count = 1
    while not event.is_set():  # event是否被set过，是返回True,否返回False
        if count == 5:         # 修改数字，看看不同的结果
            print('%s 尝试的次数过多，请稍后重试' % (current_thread().name))
            return
        print('%s 尝试第%s次连接...' % (current_thread().name, count))
        
        # connect线程执行到event.wait(1)时开始等待1秒，count计数+1，如果到check线程执行event.set()前已经4秒，
        # 则终止线程connect，否则event.is_set() is True ,立即继续线程connect
        event.wait(1)     
        count += 1
        print('count=%s'%count)
    print('%s 开始连接...' % current_thread().name)

if __name__ == '__main__':
    t1 = Thread(target=connect,name='Host-192.168.1.110')
    t2 = Thread(target=connect,name='Host-192.168.1.111')
    t3 = Thread(target=connect,name='Host-192.168.1.112')

    c1 = Thread(target=check,name='Service-10.0.0.1')
    
    t1.start()
    t2.start()
    t3.start()
    c1.start()

    t1.join()
    t2.join()
    t3.join()
    c1.join()

    print('所有连接已终止....')
