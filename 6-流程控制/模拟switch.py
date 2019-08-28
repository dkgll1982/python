#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-28 10:17:09 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-28 10:17:09 
# @Software: vscode 


#Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
#语法
#get()方法语法：
#dict.get(key, default=None)

dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print(dict.get('Nam2e','dfgd')) 

#通过字典实现
def foo1(var):
    return {
            'a': 1,
            'b': 2,
            'c': 3,
    }.get(var,'error')    #'error'为默认返回值，可自设置
    
print(foo1('a'))

#通过匿名函数实现

def foo2(var,x):
    return {
            'a': lambda x: x+1,
            'b': lambda x: x+2,
            'c': lambda x: x+3, 
    }[var](x)

print(foo2('a',1))
