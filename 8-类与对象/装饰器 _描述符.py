#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-10-20 21:14:53 
# @Last Modified by: guojun 
# @Last Modified time: 2019-10-20 21:14:53 
# @Software: vscode 
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-13 10:30
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 装饰器
# @Software: PyCharm
 

#描述符类基于以下 3 个特殊方法，换句话说，这 3 个方法组成了描述符协议：
#__set__(self, obj, type=None)：在设置属性时将调用这一方法（本节后续用 setter 表示）；
#__get__(self, obj, value)：在读取属性时将调用这一方法（本节后续用 getter 表示）；
#__delete__(self, obj)：对属性调用 del 时将调用这一方法。
#其中，实现了 setter 和 getter 方法的描述符类被称为数据描述符；反之，如果只实现了 getter 方法，则称为非数据描述符。

#描述符类
class revealAccess:
    def __init__(self, initval = None, name = 'var'):
        self.val = initval  #10
        self.name = name    #'var "x"'

    def __get__(self, obj, objtype):
        print("Retrieving",self.name)
        return self.val

    def __set__(self, obj, val):
        print("updating",self.name)
        self.val = val

class myClass:
    x = revealAccess(10,'var "x"')
    y = 5

m = myClass()
print(m.x)

print('-'*40)

m.x = 20

print(m.x)
print(m.y)

print('-'*40)

print(myClass.__dict__)
print('-'*40)
m.y = 1
print(m.__dict__)