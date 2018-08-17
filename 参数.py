#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-06-22 16:55
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 参数
# @Software: PyCharm


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

def f3(a,b,c=0,*args,age=20,name='admin',**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'age =', age, 'name =', name,'kw =', kw)

f1(1, 2)
#a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)
#a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99)
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, 99,d=3, ext=None)
#a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
f3(1,2,3,1,2,3,4,5,age=32,name='郭君',sex="女性")


def add_end(L=["1"]):
    L.append('END')
    return L

d = add_end([])
add_end()
add_end()
print(d);
print(d);

print("******************8")


def foo(x,y=1,**kwargs):
    print(x)
    print(y)
    print(kwargs)
foo(1,a=2,b=3,c=4)


#带有不定参数的装饰器
import time

def deco(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper


@deco
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))

@deco
def func2(a,b,c):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b+c))


if __name__ == '__main__':
    f = func
    func2(3,4,5)
    f(3,4)
    #func()