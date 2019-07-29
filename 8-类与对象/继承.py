#!/usr/bin/python

class Vector:
    def __init__(self, a, b):
        print("初始化方法")
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector2 (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a+13, self.b + other.b)

def pri(self):
    print("我是外部绑定的方法")

def priv(self):
    print("实例绑定方法")

from types import MethodType
Vector.pri=pri;

v1 = Vector(2, 10)
v2 = Vector(5, -2)
v3= Vector(5, -2)

v2.priv=MethodType(priv,v2);

print(v1 + v2 + v3)

if hasattr(v3,'__str__')=="False":
    print(getattr(v3,'sdfdsfsd'))

v2.pri()
v2.priv()