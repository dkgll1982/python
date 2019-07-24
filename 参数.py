#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-06-22 16:55
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 参数
# @Software: PyCharm

# 定义一个函数
def girth(width , height):
    print("width: ", width)
    print("height: ", height)
    return 2 * (width + height)
# 传统调用函数的方式，根据位置传入参数
print(girth(3.5, 4.8))
# 根据关键字参数来传入参数
print(girth(width = 3.5, height = 4.8))
# 使用关键字参数时可交换位置
print(girth(height = 4.8, width = 3.5))
# 部分使用关键字参数，部分使用位置参数
print(girth(3.5, height = 4.8))

# 接下来在调用该函数时，既可使用传统的根据位置参数来调用（如上面程序中第 7 行代码所示），
# 也可根据关键字参数来调用（如上面程序中第 9 行代码所示），在使用关键字参数调用时可交换参数的位置（如上面程序中第 11 行代码所示〕，
# 还可混合使用位置参数和关键字参数（如上面程序中第 13 行代码所示）。

# 需要说明的是，如果希望在调用函数时混合使用关键字参数和位置参数，则关键字参数必须位于位置参数之后。换句话说，在关键字参数之后的只能是关键字参数。
# 位置参数必须放在关键字参数之前，下面代码错误
print(girth(width = 3.5, 4.8))

# 定义了支持参数收集的函数
def test(*books ,num) :
    print(books)
    # books被当成元组处理
    for b in books :
        print(b)
    print(num)
# 调用test()函数
test("C语言中文网", "Python教程", num = 20)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

def f3(a,b,c=0,*args,age=20,name='admin',**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'age =', age, 'name =', name,'kw =', kw)

f1(c=1, b=2, a=0, args=('a', 'b'))
f1(c=1, b=2, a=0)
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