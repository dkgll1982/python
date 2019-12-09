#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-03 17:33
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : YIELD
# @Software: PyCharm
def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return

r = read_file(r"backup\\note.txt");
r.__next__();
print(r.send(1000));

def f():
    print('start')
    a = yield 1
    print(a)
    print('middle....')
    b = yield 2  # 2这个值只是迭代值，调用next时候返回的值
    print(b)  # 传入的参数是给当前yield的，也就是yield 2，因为当前函数走到了yield 2，所以传入的参数没有给yield 1
    print('next')
    c = yield 3
    print(c)

a = f()
print('-'*40)
next(a)
print('-'*40)
next(a)
print('-'*40)
a.send('msg')
print('-'*40)


def h():
    print('Wen Chuan')
    m = yield 5  # Fighting!
    print(m)
    d = yield 12
    print('We are together!')
c = h()
print('1:',c.__next__())  #相当于c.send(None)
print('2:',c.send('Fighting!'))  #(yield 5)表达式被赋予了'Fighting!'

print('-'*40)
def func():
     n = 0
     while 1:
        n = yield n
        print('good',n)

f = func()
print(f.__next__())
print(f.__next__())
print(f.__next__())

def test():
    s = 0;
    for i in range(10):
        s = yield i*s
        print('i:',i)
        print('s:',s)
        print('i * s',i*s)

t = test();
t.send(None)
x = t.send(2)
print('-'*40)

x = t.send(3)
print(x)

print('-'*40)

def fun():
    for i in range(20):
        yield i
        print('good',i)

a = fun()
a.__next__()
a.__next__()
a.__next__()


class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()
print('-'*40)

def func():
    n = 0;
    i=1;
    while i<10:
        i+=1;
        n = yield n

f = func()
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.send(2))
print(f.send(1))

print('-'*40)


def fun():
    r= 0
    for i in range(20):
        x = yield r

a=fun()
print(a.__next__())
print(a.send(2))
print(a.send(1))
print(a.__next__())
print(a.__next__())

print('-'*40)

def xunhuan(i):
    l=0;
    while l<i:
        yield l*l;
        l=l+1

m = xunhuan(20);
print(m.__next__())

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1

f = xunhuan(5)
print(type(f))
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())