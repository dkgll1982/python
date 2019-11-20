#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 22:59
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 11.线程通信.py
# @Software: PyCharm
import threading
import time

event = threading.Event()

# 两个线程，一个线程每隔一秒输出一个数，另一个线程每隔五秒控制一次开关变化（开变关，关变开）
def MainThread():
    i = 0
    while(True):
        event.wait()
        print(i)
        i += 1
        time.sleep(1)

def ControlThread():
    while(True):
        print('start')
        event.set()
        time.sleep(5)
        print('stop')
        event.clear()
        time.sleep(5)

if __name__ == '__main__':
    t1 = threading.Thread(target=MainThread)
    t2 = threading.Thread(target=ControlThread)
    t1.start()
    t2.start()

#第一步：event.wait()，阻塞
#第二步：print('start')，输出:start
#第三步：event.set()
#第四步：print(i)，输出:0
#第五步：print(i)，输出:1
#第六步：print(i)，输出:2
#第七步：print(i)，输出:3
#第八步：print(i)，输出:4
#第九步：print('stop')，输出:stop
#第十步：event.clear(),此时的wait()方法将阻塞
#第十一步：time.sleep(5)之后循环重新回到print('start')
#         重复第二步到第十步，依次为start 5 6 7 8 9 stop start 10 11 12 13 14 ...
  
