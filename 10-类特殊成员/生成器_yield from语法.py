#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-17 17:04
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : yield from语法
# @Software: PyCharm

# Python 主要提供了以下两种方式来创建生成器：
# 使用 for 循环的生成器推导式。
# 调用带 yield 语句的生成器函数。

f = ((x,y) for x in range(5) for y in range(5))
print(f)
for item in f:
    print(item,end = ' ')
print('')

f1 = ({x:y} for x in range(5) for y in range(5))
print(f1)
for key in f1:
    print(key,end = ' ')
print('')

def g1(x):
    yield range(x) 

def g2(x):
    yield from range(x) 

it1 = g1(5)
it2 = g2(5)

print(type(it1))
print(type(it2))

print(type([x for x in it1]))
# out [range(0, 5)]
print(type([x for x in it2]))
# out [0, 1, 2, 3, 4]

def test(val, step):
    print("--------函数开始执行------")
    cur = 0
    # 遍历0～val
    for i in range(val):
        # cur添加i*step
        cur += i * step
        #print(cur,end =' ');
        yield cur
t= test(12,1)

print('-'*40)

#调用包含 yield 语句的函数并不会立即执行，它只是返回一个生成器
print(type(t))                  # <class 'generator'>
print(next(t),end = ' ')
print(next(t),end = ' ')
print(next(t),end = ' ') 
print(t.__next__(),end = ' ')
print(t.__next__(),end = ' ')
print(t.__next__(),end = ' ')

print('-'*40)

#将生成器转换成列表
print (list (t))
#再次创建生成器 
t= test(12,1)
#将生成器转换成元组
print(tuple(t))

print('-'*40)

def square_gen(val):
    i = 0
    out_val = None
    while True:
        # 使用yield语句生成值，使用out_val接收send()方法发送的参数值
        out_val = (yield out_val ** 2) if out_val is not None else (yield i ** 2)
        # 如果程序使用send()方法获取下一个值，out_val会获取send()方法的参数
        if out_val is not None : print("====%d" % out_val)
        i += 1

sg = square_gen(5)
# 第一次调用send()方法获取值，只能传入None作为参数
print(sg.send(None))  # 0
print(next(sg))  # 1
print('-'*40)
# 调用send()方法获取生成器的下一个值，参数9会被发送给生成器
print(sg.send(9))  # 81
# 再次调用next()函数获取生成器的下一个值
print(next(sg))  # 9

print('-'*40)

def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b      # 使用 yield
        # print b 
        a, b = b, a + b 
        n = n + 1
        print('b,a,n %d, %d, %d'%(b,a,n))
 
#第一次：遇到yield直接返回1
#第二次：先执行 b=0+1=1，a=1，n=0+1=1，然后返回1
#第三次：先执行 b=1+1=2，a=1，n=1+1=2，然后返回2
#第四次：先执行 b=1+2=3，a=2，n=2+1=3，然后返回3
#第五次：先执行 b=2+3=5，a=3，n=3+1=4，然后返回5
#第六次：先执行 b=5+3=8，a=5，n=4+1=5，然后 while n < max，即 5<5 不成立，执行完毕退出！

f = fab(5);
print(f.__next__());
print(f.__next__());
print(f.__next__());
print(f.__next__());
print(f.__next__());
#for n in fab(5): 
#    print(n)

print('-'*40);

# def fab(max):
#     #for x in range(max):
#     #    n = yield x
#     n= yield from max
#     print('n:',n);

# f = fab('1234567');
# print(type(f))
# print(f.send(None))
# # next()跟send()不同的地方是，next()只能以None作为参数传递，而send()可以传递yield的值。
# print(f.__next__()) 
# print(f.__next__())
# print(f.__next__())
# print(f.__next__()) 

#for x in range(5,0,-1):
#     print("x:",x);
def g(x):
    yield from range(x,0,-1)
    yield from range(x)
l = list(g(5));
print(l)

print('-'*40)

def accumulate():
    tally = 0
    while 1:
        next = yield
        if next is None:
            return tally
        tally += next

def gater_tallies(tallies):
    while 1:
        tally = yield from accumulate()
        tallies.append(tally)

tallies = []
acc = gater_tallies(tallies)
print(acc.__next__());
for i in range(4):
    acc.send(4)

acc.send(None)
for i in range(5):
    acc.send(i)

acc.send(None)
print(tallies)