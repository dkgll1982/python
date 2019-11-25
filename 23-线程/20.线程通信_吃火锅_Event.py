#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: 航天神舟智慧系统技术有限公司
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2019-11-22 20:21:42
# @Last Modified by: guojun
# @Last Modified time: 2019-11-22 20:21:42
# @Software: vscode
# 参考链接：https://www.cnblogs.com/yoyoketang/p/8341972.html

# 小伙伴a,b,c围着吃火锅，当菜上齐了，请客的主人说：开吃！，于是小伙伴一起动筷子，这种场景如何实现
# 场景：当小伙伴a,b,c集结完毕后，请客的人发话：开吃咯！

import threading
import time

event = threading.Event()

def chiHuoGuo(name):
    # 等待事件，进入等待阻塞状态
    print('%s已经启动' % threading.currentThread().getName())
    print('小伙伴%s已经进入就餐状态!' % name)
    time.sleep(1)
    event.wait()  #阻塞在這裡，等待flag為True才往下執行

    # 收到事件后进入运行状态
    print('%s收到通知了.' % threading.currentThread().getName())
    print('%s小伙伴%s开始吃咯！' % (time.time(), name))

class myThread (threading.Thread):  # 继承父类threading.Thread
    def __init__(self, name):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.people = name

    def run(self):                  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''重写run方法'''
        chiHuoGuo(self.people)      # 执行任务
        print(("qq交流群:226296743"))
        print(("结束线程:%s" % threading.currentThread().getName()))

# 设置线程组
threads = []

# 创建新线程
thread1 = myThread("a")
thread2 = myThread("b")
thread3 = myThread("c")

# 添加到线程组
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

# 开启线程
for thread in threads:
    thread.start()

time.sleep(0.1)

# 发送事件通知
print('集合完毕,人员到齐了,开吃咯！')
event.set()
