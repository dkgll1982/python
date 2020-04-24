#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-21 14:31:46 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-21 14:31:46 
# @Software: vscode 
#参考链接：https://www.cnblogs.com/wongbingming/p/9035579.html

# maxsize默认为0，不受限
# 一旦>0，而消息数又达到限制，q.put()也将阻塞
#q = Queue(maxsize=0)

# 阻塞程序，等待队列消息。
#q.get()

# 获取消息，设置超时时间
#q.get(timeout=5.0)

# 发送消息
#q.put()

# 等待所有的消息都被消费完
#q.join()

# 以下三个方法，知道就好，代码中不要使用

# 查询当前队列的消息个数
#q.qsize()

# 队列消息是否都被消费完，True/False
#q.empty()

# 检测队列里消息是否已满
#q.full()

from queue import Queue
from threading import Thread
import time

class Student(Thread):
    def __init__(self, name, queue):
        super().__init__()
        self.name = name
        self.queue = queue

    #线程类：重写run方法
    def run(self):
        while True:
            # 阻塞程序，时刻监听老师，接收消息
            msg = self.queue.get() 
            # 一旦发现点到自己名字，就赶紧答到
            if msg == self.name:
                print("{}：到！".format(self.name))
                #直接退出
                break

class Teacher:
    def __init__(self, queue):
        self.queue=queue

    def call(self, student_name):
        print("老师：{}来了没？".format(student_name))
        # 发送消息，要点谁的名
        self.queue.put(student_name)


queue = Queue()
teacher = Teacher(queue=queue)
s1 = Student(name="小明", queue=queue)
s2 = Student(name="小亮", queue=queue)
s1.start()      #启动线程类
s2.start()

print('开始点名~')
teacher.call('小明')
time.sleep(1)
teacher.call('小亮')

s1.join()
s2.join()