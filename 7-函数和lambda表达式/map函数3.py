#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-07-29 16:02:21 
# @Last Modified by: guojun 
# @Last Modified time: 2019-07-29 16:02:21 
# @Software: vscode 
 
print(list(map(lambda x,y,z:'%d*%d*%d=%s'%(x,y,z,x*y*z),[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7])))

#若是传入的多个可迭代对象长度不相同，则按最短的长度进行处理(这是针对python3的)。具体用法如下： 
ls1=[1,2,3,4,5]
ls2=[2,3,4,5]
print(list(map(lambda x,y:x+y,ls1,ls2)))
#['Aa', 'Bb']
from functools import reduce
print(reduce(lambda x,y:x+y,[1,2,3,4,5]))