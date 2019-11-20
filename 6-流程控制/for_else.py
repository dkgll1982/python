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

        