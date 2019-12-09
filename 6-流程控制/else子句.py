#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-09 10:37:09 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-09 10:37:09 
# @Software: vscode 
a_list = [330, 1.4, 50, 'fkit', -3.5]
for ele in a_list:
    if isinstance(ele,float) or isinstance(ele,int):
        print('元素: ', ele) 
        break
else:
    # 访问循环计数器的值，依然等于最后一个元素的值
    print('else块: ', ele)

print('*'*40)    

#参考链接：https://www.php.cn/python-tutorials-408164.html
for n in range(2, 10): 
    for x in range(2, n): 
        if n % x == 0: 
            print( n, 'equals', x, '*', n/x) 
            break 
    else: 
        # loop fell through without finding a factor 
        print(n, 'is a prime number')

print('='*40)    

#while...else 语法

#while 判断条件:
#    语句1....
#else:
#    语句2....
#for...else 语法

#for 遍历对象:
#    语句1....
#else:
#    语句2....
#这种奇怪的语法是说：

#当 while/for 循环正常执行完的情况下，执行 else 输出；

#如果当 while/for 循环中执行了跳出循环的语句，比如 break，将不执行 else 代码块的内容； 

def suger():
    value = True
    if value is True:
        print('value is True')
    else:
        print('value is False')

    for idx in range(1, 5):
        print('idx  {0}'.format(idx))
    else:
        print('exit for loop')

    num = 30
    while num > 20:
        num = num - 1

    else:
        print('exit while loop')

    try:
        with open("data.txt") as file:
            data = file.readlines()
    except Exception:
        print('open failed')
    else:
        print('open succeed')


suger() 