#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-01 20:25:24 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-01 20:25:24 
# @Software: vscode 

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

class C1(A,B):
    pass

class C2(A,B):
    def bar(self):
        print('C2-bar')

class D(C1,C2):
    pass

if __name__ == '__main__':
    print(D.__mro__)
    d=D()
    d.foo()
    d.bar()


print('='*40)

class A1: pass
class A2: pass
class A3: pass
class B1(A1,A2): pass
class B2(A2): pass
class B3(A2,A3): pass
class C1(B1): pass
class C2(B1,B2): pass
class C3(B2,B3): pass
class D(C1, C2, C3): pass
 
print(isinstance(D(),C1) 
    and isinstance(D(),C2) 
    and isinstance(D(),C3) 
    and isinstance(D(),B1)
    and isinstance(D(),B2)
    and isinstance(D(),B3)
    and isinstance(D(),A1)
    and isinstance(D(),A2)
    and isinstance(D(),A3))

print("从D开始查找：")
for s in D.__mro__:
    print(s)

print("从C3开始查找：")
for s in C3.__mro__:
    print(s)

#参考链接：https://www.cnblogs.com/pyedu/p/10389307.html