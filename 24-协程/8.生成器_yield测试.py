def g1(x):
    yield range(x)
    #yield range(2*x)

def g2(x):
    #for x in range(x):
    #    yield x
    yield from range(x)  

g = g1(5)
print(type(g),g.__next__())  

g = g2(5)
print(g.__next__()) 

print('*'*40)

def g3(generator): 
    yield from generator

g = g1(5)
t = g3(g.__next__())

print(next(t)) 
print(next(t)) 
print(next(t)) 

print('-'*40)

#yield from 的简单实现
#从下面的代码可以看出，yield from 后面可以跟的可以是“生成器 、元组、 列表、range（）函数产生的序列等可迭代对象”
#简单地说，yield from  generator 。实际上就是返回另外一个生成器。而yield只是返回一个元素。
#从这个层面来说，有下面的等价关系：yield from iterable本质上等于 for item in iterable: yield item 。
def generator2():
    yield 'a'
    yield 'b'
    yield 'c'
    yield from ('d','e','f')
    yield from range(1024,10240,1024)
    yield from g2(10) #yield from iterable本质上等于 for item in iterable: yield item的缩写版
    yield from [11,22,33,44]
    yield from (12,23,34) 
 
for i in generator2():
    print(i,end=' , ') 
'''运行的结果为：
a , b , c , 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 11 , 22 , 33 , 44 , 12 , 23 , 34 , 0 , 1 , 2 ,
'''

print('\r\n','+'*40)

import time,random

def f():
    while True:
        r = yield 
        print(r)
 
f1 = f()
f2 = f()
f1.__next__()
f2.__next__()

for x in range(1,10):
    f1.send(x)
    f2.send(x*10)

