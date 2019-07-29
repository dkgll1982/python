#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-15 16:54
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 多继承拓扑排序
# @Software: PyCharm
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class A(object):
    def foo(self):
        print('A foo')
    def bar(self):
        print('A bar')

class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')

class C1(A):
    pass

class C2(B):
    def bar(self):
        print('C2-bar')

#排在前面的父类中的方法会“遮蔽”排在后面的父类中的同名方法
class D(C1,C2):
    pass

if __name__ == '__main__':
    print(D.__mro__)
    d=D()
    d.foo() # A 
    d.bar() # A

# 遵循C3算法：D——>C1——>A——>C2——>B——>OBJECT

class A(object):
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
         print("B")

class C(object):
    def __init__(self):
        print("C")

class D(B,C):
    def __init__(self):
        print("D")
print(D.__mro__)
D();  #D B a c