#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-02 10:52:03 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-02 10:52:03 
# @Software: vscode     
#原文链接：https://blog.csdn.net/y6622576/article/details/78993960

class Chain(object):
    def __init__(self, attr=''):
       self.__attr = attr

    def __getattr__(self, attr):
       return Chain('%s/%s' % (self.__attr, attr))

    # 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
    # 能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
    # 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
    def __call__(self, attr):
       return Chain('%s/%s' % (self.__attr, attr))

    def __str__(self):
       return self.__attr
    
    def users(self,attr):
        return Chain('%s/%s' % (self.__attr, attr))

    __repr__ = __str__ 

#链式调用：Chain().status.users('michael').repos分解如下 
t =  Chain()
t1 = t.status               #查找urls的属性users，没找到定义的属性，那就调用__getattr__方法
t2 = t1.users
t3 = t2('micheal')          #实例方法调用__call__方法，此处还可以进行参数传递
print("%s, %s, %s"%(t1,t2,t3)) #/status/users/micheal/repos
#t4 = t3.repos

#print("%s, %s, %s, %s"%(t1,t2,t3,t4)) #/status/users/micheal/repos