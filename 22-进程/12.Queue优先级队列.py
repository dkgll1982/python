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
q = queue.PriorityQueue(4)
#q = Queue(4)
q.put((1,'abcb'))
q.put((1,'abc1'))
q.put((1,'abc3'))
q.put((2,'abc4'))

print(q.get())
print(q.get())
print(q.get())
print(q.get())