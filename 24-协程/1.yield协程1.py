#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-09 17:25
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 协程
# @Software: PyCharm
#! -*- coding: utf-8 -*-
#inspect模块用于收集python对象的信息，可以获取类或函数的参数的信息，源码，解析堆栈，对对象进行类型检查等等
import inspect

# 协程使用生成器函数定义：定义体中有yield关键字。
def simple_coroutine():
    print('-> coroutine started')
    # yield 在表达式中使用；如果协程只需要从客户那里接收数据，yield关键字右边不需要加表达式（yield默认返回None）
    x = yield
    print('-> coroutine received:', x)


my_coro = simple_coroutine()
my_coro # 和创建生成器的方式一样，调用函数得到生成器对象。
# 协程处于 GEN_CREATED (等待开始状态)
print('1:'+inspect.getgeneratorstate(my_coro))

my_coro.send(None)
# 首先要调用next()函数，因为生成器还没有启动，没有在yield语句处暂停，所以开始无法发送数据
# 发送 None 可以达到相同的效果 my_coro.send(None)
#next(my_coro)
# 此时协程处于 GEN_SUSPENDED (在yield表达式处暂停)
print('2:'+inspect.getgeneratorstate(my_coro))

# 调用这个方法后，协程定义体中的yield表达式会计算出42；现在协程会恢复，一直运行到下一个yield表达式，或者终止。
#my_coro.send(42)
print('3:'+inspect.getgeneratorstate(my_coro))

my_coro.close();
print('4:'+inspect.getgeneratorstate(my_coro))

# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
# c = consumer()
# produce(c)