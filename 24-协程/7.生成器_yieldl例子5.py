#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2018-08-17 17:16:24 
# @Last Modified by: guojun 
# @Last Modified time: 2018-08-17 17:16:24 
# @Software: vscode  

def a():
    print ("do a() will not print out")
    yield 5
    
a()

print ("===============test a()")

def b():
    print ("list generator will in def , print here...")
    yield 5

g_obj = b()

print ("===============g_obj test b: %s" % g_obj)
print ("just generator obj, not in b def")
print ("list_g: %s" % list(g_obj))

def c():
    print ("next() will here... test generator next(), next attrbute not in python3, python2.6 is exist")
    yield 5
    print ("test generator next2")

g_obj = c()
print ("===============g_obj test c: %s" % g_obj)
#g_obj.next()
#print ("dir g_obj: %s " % dir(g_obj))

def d():
    global m
    global n
    print ("send() will here... test generator send()")
    m = yield 5
    print ("send input is m : %s" % m)
    n = yield 6
    print ("test generator send2")

g_obj = d()
print ("===============g_obj test d: %s" % g_obj)

s_return1 = g_obj.send(None)
s_return2 = g_obj.send("send twice")
print ("the next send input will be the result of last yield, just like m is : %s, s_return1 is : %s, s_return2 is : %s" % (m, s_return1, s_return2))
#print ("not next send so n is undefind, n is : %s" % n)