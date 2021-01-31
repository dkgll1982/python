#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-11 17:38:32 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-11 17:38:32 
# @Software: vscode 

import queue
from multiprocessing import Process,Queue

'''------------------------------优先级队列-----------------------------'''
#特点：数字越小，优先级越高
#优先级队列中的任务顺序跟放入时的顺序是无关的，而是按照任务的大小来排序，最小值先被取出。那任务比较大小的规则是怎么样的呢。
#如果是内置类型，比如数值或者字符串，则按照自然顺序来比较排序。
#如果是列表或者元祖，则先比较第一个元素，然后比较第二个，以此类推，直到比较出结果
#如果是自定义类型，需要实现 __lt__ 比较函数
q = queue.PriorityQueue(4)
#q = Queue(4)
q.put((1,'abcd'))
q.put((1,'abc1'))
q.put((1,'abc3'))
q.put((2,'abc4'))

print(q.get())
print(q.get())
print(q.get())
print(q.get())

print('*'*40)

class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', self.description) 
 
    def __lt__(self, other):
        # 2021/01/30:此处定义：先比较priority，如果当前实例小于另一个实例，返回true，
        # 再比较description，如果当前实例大于另一个实例，返回true
        return self.priority < other.priority if self.priority != other.priority else self.description > other.description 
 
q2 = queue.PriorityQueue()
 
q2.put(Job(5, 'Mid-level job'))
q2.put(Job(20, 'Low-level job'))
q2.put(Job(13, 'Dow-level job'))
q2.put(Job(20, 'Low-Devel job'))
q2.put(Job(13, 'Important job')) #数字越小，优先级越高
 
while not q2.empty():
    next_job = q2.get() #可根据优先级取序列
    print('Processing job', next_job.priority,',',next_job.description)
 