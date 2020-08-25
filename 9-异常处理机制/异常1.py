# -*- coding: utf-8 -*-
# @Time    : 2018/05/23
# @Author  : suixin
# @Email   : 350606539@QQ.com
# @File    : 异常.py

import sys

raise Exception("错误的信息，下面不在执行")
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a / b
    print("您输入的两个数相除的结果是：", c )
except IndexError:
    print("索引错误：运行程序时输入的参数个数不够")
except ValueError:
    print("数值错误：程序只能接收整数参数")
except ArithmeticError:
    print("算术错误")
except Exception:
    print("未知异常")

print('-'*40)

try:
     s = None
     if s is None:
         print("s 是空对象")
         raise NameError     #如果引发NameError异常，后面的代码将不能执行
     print(len(s))  #这句不会执行，但是后面的except还是会走到
except TypeError:
     print("空对象没有长度")
 
s = None
if s is None:
    raise NameError 
print('is here?') #如果不使用try......except这种形式，那么直接抛出异常，不会执行到这里


import traceback

a=12
b=20
e="*"

a = input("请输入任何内容：");
try:
    print('try...')
    r = 10 / int(a)
    print('result:', r)
except ValueError as a:
    print('ValueError:', a)
except ZeroDivisionError as a:
    print('ZeroDivisionError:', a)
finally:
    print('finally...')
print('END')

print('-'*40)
