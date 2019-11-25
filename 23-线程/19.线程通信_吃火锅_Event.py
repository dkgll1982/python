#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: 航天神舟智慧系统技术有限公司
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2019-11-22 20:17:50
# @Last Modified by: guojun
# @Last Modified time: 2019-11-22 20:17:50
# @Software: vscode
# 参考链接：https://www.cnblogs.com/yoyoketang/p/8341972.html

# 小伙伴a,b,c围着吃火锅，当菜上齐了，请客的主人说：开吃！，于是小伙伴一起动筷子，这种场景如何实现
# 场景：小伙伴a和b准备就绪，当收到通知event.set()的时候，会执行a和b线程

import threading
import time

event = threading.Event() 

def chihuoguo(name):
    # 等待事件，进入等待阻塞状态
    print('%s 已经启动' % threading.currentThread().getName())
    print('小伙伴 %s 已经进入就餐状态！' % name)
    time.sleep(1)
    event.wait()
    # 收到事件后进入运行状态
    print('%s 收到通知了.' % threading.currentThread().getName())
    print('小伙伴 %s 开始吃咯！' % name) 

# 设置线程组
threads = []

# 创建新线程
thread1 = threading.Thread(target=chihuoguo, args=("a", ))
thread2 = threading.Thread(target=chihuoguo, args=("b", ))

# 添加到线程组
threads.append(thread1)
threads.append(thread2)

# 开启线程
for thread in threads:
    thread.start()

time.sleep(0.1)
# 发送事件通知
print('主线程通知小伙伴开吃咯！')
event.set()
