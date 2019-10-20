#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2018-08-17 11:13:55 
# @Last Modified by: guojun 
# @Last Modified time: 2018-08-17 11:13:55 
# @Software: vscode 

import sys
import time;  # 引入time模块

a = 21
b = 10
c = 0
 
c = a + b
print ("1 - c 的值为：", c)
 
c = a - b
print ("2 - c 的值为：", c)
 
c = a * b
print ("3 - c 的值为：", c)
 
c = a / b
print ("4 - c 的值为：", c)
 
c = a % b
print ("5 - c 的值为：", c)
 
# 修改变量 a 、b 、c
a = 2
b = 3
c = a*b 
print ("6 - c 的值为：", c)
 
a = 25
b = 5
c = a//b 
print ("7 - c 的值为：", c)

print('1--',a and b);
print('2--',a or b);
print('3--',not(a and b));
print('4--',c is b);


a = 20
b = 20
 
if ( a is b ):
   nb=123;
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
 
if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")
 
# 修改变量 b 的值
b = 30
if ( a is b ):
   nb=1233;
   print ("3 - a 和 b 有相同的标识")
else:
   nb=123333333;
   print ("3 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")

str1 = "this is string example from runoob....wow!!!"

print ("str.capitalize() : ", str1.capitalize())

str1 = "[www.runoob.com]"

print ("str.center(40, '*') : ", str1.center(40, '*').upper())

dict={"name":"张三丰","age":12,"sex":"男"};
print(dict['name']);

list = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])

print(list)

for i, val in enumerate(list):
    print("序号：%s   值：%s" % (i + 1, val), end='  ***  ')

list=['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ'];

for x in list:
    print(x)

print ('')
print ('*****************************************')   # 输出迭代器的下一个元素
print ('')

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素
print (next(it))

# 计算面积函数
def area(width, height):
    print("Welc22222222222222ome", height)
    return width * height
 
def print_welcome(name):
    print("Welcome", name)
    print("Welcome2", name)

print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(height=2,width=121)) 

print ('')
print ('*****************************************')   # 输出迭代器的下一个元素
print ('')

def printinfo( arg1, *vartuple ):
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))

print(nb);

num = 1
def fun1(): 
    global num 
    print(num) 
    num = 123
    print(num)
fun1()

func2=lambda x:print("调用的参数值是："+str(x)); 

func2(123);

fun4=func2(123222);

fun4;