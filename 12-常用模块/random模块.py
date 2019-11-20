#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 10:14:37 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 10:14:37 
# @Software: vscode 
# 参考链接：https://www.cnblogs.com/Grace-gao/p/10956226.html

import random
#生成范围为0.0≤x<1.0 的伪随机浮点数
print (random.random())
#生成范围为2.5≤x<10.0 的伪随机浮点数
print(random.uniform(20, 10))
print (random.uniform(2.5, 10.0))
#生成呈指数分布的伪随机浮点数
print (random.expovariate(1/5))
#生成从0 到9 的伪随机整数
print(random.randint(10,100))
print(random.randrange(10))
#生成从0 到100 的随机偶数
print (random.randrange(0, 101 , 3))
#随机抽取一个元素
print (random.choice(['Python','Swift','Kotlin']))
print (random.choice(('Python','Swift','Kotlin')))
book_list = ['Python','Swift','Kotlin']
#对列表元素进行随机排列
random.shuffle (book_list)
print (book_list)
random.shuffle (book_list)
print (book_list)
#随机抽取4 个独立的元素
print (random.sample([10, 20 , 30 , 40 , 50], k=4))

# choices(population, weights=None, *, cum_weights=None, k=1)：从population中进行K次随机选取，每次选取一个元素（注意会出现同一个元素多次被选中的情况），
# weights是相对权重值，population中有几个元素就要有相对应的weights值，cum_weights是累加权重值，例如，相对权重〔10, 5, 30，5〕相当于累积权重〔10, 15, 45，50〕。
# 在内部，在进行选择之前，相对权重被转换为累积权重，因此提供累积权重节省了工作。返回一个列表。
 
#指定随机抽取6 个元素，各元素被抽取的权重（概率）不同
print(random.choices(['Python','Swift','Kotlin'], [5, 5, 1], k=6))  

seq = ['red1','yellow2','blue3', 'green4' ]
random.shuffle(seq)           #列表重新排序
print(seq)
import time
print(time.localtime()) 