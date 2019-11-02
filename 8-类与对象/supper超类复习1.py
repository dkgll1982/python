#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-02 17:26:52 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-02 17:26:52 
# @Software: vscode 
# 参考链接：http://jianshu.com/p/8ddb595628d1
# 参考链接：https://www.jianshu.com/p/e7d27949b71b
 
print('****以下为单继承：','*'*40) 
class A:
    def __init__(self):
        print('A',end= ' ')
 
class B:
    def __init__(self):
        print('B',end= ' ')
 
class C(B):
    def __init__(self):
        #在单继承时，super().__init__()与(父类)Base.__init__()是一样的。super()避免了基类的显式调用。代码如下：
        B.__init__(self)
        super(C, self).__init__()
        # python3写法简化：super().__init()  
        # 在类定义中以super()方式调用，是一种省略写法，由解释器填充必要参数。填充的第一个参数是当前类，第二个参数是self：
        super().__init__()
        print('C',end= ' ')
 
#C()

print('\r\n****以下为多继承(super)：','*'*40) 

class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")

class A(Base):
    def __init__(self):
        print("enter A")
        super(A, self).__init__()
        print("leave A")

class B(Base):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()
        print("leave B")

class D(Base):
    def __init__(self):
        print("enter D")
        Base().__init__()
        print("leave D")

class C(A, B, D):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")

C()

# 测试结果
# enter C
# enter A
# enter B
# enter Base
# leave Base
# leave B
# leave A
# leave C

print('\r\n****以下为多继承(不采用super)：','*'*40) 

class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")

class A(Base):
    def __init__(self):
        print("enter A")
        Base().__init__()
        print("leave A")

class B(Base):
    def __init__(self):
        print("enter B")
        Base().__init__()
        print("leave B")

class C(A, B):
    def __init__(self):
        print("enter C")
        A().__init__()
        B().__init__()
        print("leave C")

#C()
 