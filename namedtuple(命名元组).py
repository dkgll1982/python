#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2018-08-19 09:46:47 
# @Last Modified by: guojun 
# @Last Modified time: 2018-08-19 09:46:47 
# @Software: vscode 

from collections import namedtuple
 
# collections.namedtuple(typename, field_names, verbose=False, rename=False) 
# 返回一个具名元组子类 typename，其中参数的意义如下：

# typename：元组名称
# field_names: 元组中元素的名称
# rename: 如果元素名称中含有 python 的关键字，则必须设置为 rename=True
# verbose: 默认就好

# 两种方法来给 namedtuple 定义方法名
#User = collections.namedtuple('User', ['name', 'age', 'id'])
User = namedtuple('User', 'name age id')
user = User('tester', '22', '464643123')

print(user) 

Friend=namedtuple("Friend",['name','age','email'])
 
f1=Friend('xiaowang',33,'xiaowang@163.com')
print(f1)
print(f1.age)
print(f1.email)
f2=Friend(name='xiaozhang',email='xiaozhang@sina.com',age=30)
print(f2)
 
name,age,email=f2
print(name,age,email)