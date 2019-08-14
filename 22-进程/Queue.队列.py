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

q = queue.PriorityQueue(4)
q.put((1,'abcb'))
q.put((1,'abc1'))
q.put((1,'abc3'))
q.put((2,'abc4'))

print(q.get())
print(q.get())
print(q.get())
print(q.get())