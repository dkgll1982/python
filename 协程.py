#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-09 17:25
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 协程
# @Software: PyCharm

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()
c = consumer()
produce(c)