#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-28 12:02
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 装饰器复习
# @Software: PyCharm
import functools
import time

def metric(fn):
    def warp(*args,**kwargs): 
        print('start:%s executed...'% (fn.__name__))  
        t1=time.time()
        time.sleep(3)
        fn(*args,**kwargs)
        t2=time.time()
        print('end:%s executed in %s ms' % (fn.__name__, t2-t1)) 
    return warp

@metric
def sum(*args):
    sum = 0
    for n in args:
        sum = sum + n
    print('sum:%d'%sum)

#逆向参数收集(在列表、元组前添加 *，在字典前添加 **。)
s = sum(*[x for x in range(11)])

print('='*40)

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def warpper(*args,**kwargs):
            t1 = time.time()
            print('%s——%s：begin call:%s'%(text,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t1)),func.__name__))
            func(*args,**kwargs)
            time.sleep(1)
            t2 = time.time()
            print('%s——%s：end call:%s,spend time:%ds'%(text,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t2)),func.__name__,t2-t1))
            return func
        warpper.__name__ = func.__name__
        return warpper
    return decorator

@log('日志输出')
@log('执行输出')
def hellword(text):
    print(text)

h = hellword("Hello Word!")

print(h.__name__)