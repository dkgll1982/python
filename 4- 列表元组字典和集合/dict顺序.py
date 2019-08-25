#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-23 23:10:08 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-23 23:10:08 
# @Software: vscode 

from collections import OrderedDict

dict ={}
for i in range(1,20,2):
    dict["key"+str(i)]="value"+str(i)
print(dict)

dict.setdefault("key2",234)

for k in sorted(dict.items(),key=lambda x:str(x[1]),reverse=True):
    print(k)

import collections  
d = collections.OrderedDict() 
d[3] = 'A'  
d[2] = 'B'  
d[1] = 'C'  
  
for k, v in d.items():  
   print (k, v  )    

r = OrderedDict([('红色','red'), ('绿色','green'), ('蓝色', 'blue')])
print(r)  