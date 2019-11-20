#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-18 10:39
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 12.生产者与消费者.py
# @Software: PyCharm
#参考链接：https://www.cnblogs.com/wongbingming/p/9035579.html

# Event 和 Condition 是threading模块原生提供的模块，原理简单，功能单一，
# 它能发送 True 和 False 的指令，所以只能适用于某些简单的场景中。

# 而Queue则是比较高级的模块，它可能发送任何类型的消息，包括字符串、字典等。
# 其内部实现其实也引用了Condition模块（譬如put和get函数的阻塞），
# 正是其对Condition进行了功能扩展，所以功能更加丰富，更能满足实际应用。

import threading,time,queue,random

#生产者
def product(id,q):
    while True:
        num = random.randint(0,10000)
        q.put(num);
        print("生产者%d生产了%d数据放入了队列"%(id,num))
        time.sleep(3)
    #任务完成
    q.task_done()

#消费者
def customer(id,q):
    while True:
        item = q.get()
        if item is None:
            break
        print("消费者%d消费了%d数据"%(id,item))
        time.sleep(2)
    #告知等待的队列(queue.join()这里在等待)任务的处理已完成。
    q.task_done() 

if __name__ =="__main__":
    #消息队列
    q = queue.Queue()

    #启动生产者
    for i in range(4):
        threading.Thread(target = product,args=(i,q)).start()
    #启动消费者
    for i in range(3):     
        threading.Thread(target = customer,args=(i,q)).start()
  