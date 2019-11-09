#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-03 12:46:25 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-03 12:46:25 
# @Software: vscode  

# 如果 a 有 __add__ 方法， 而且返回值不是 NotImplemented， 调用a.__add__(b)， 然后返回结果。
# 如果 a 没有 __add__ 方法， 或者调用 __add__ 方法返回NotImplemented， 检查 b 有没有 __radd__ 方法， 
# 如果有， 而且没有返回 NotImplemented， 调用 b.__radd__(a)， 然后返回结果。
# 如果 b 没有 __radd__ 方法， 或者调用 __radd__ 方法返回NotImplemented， 抛出 TypeError， 
# 并在错误消息中指明操作数类型不支持。
# ————————————————
# 版权声明：本文为CSDN博主「很长很长的名字」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/u011019726/article/details/77834602

class A:
    def __init__(self, value): 
        self.value = value 
    def __add__(self, other): 
       return self.value + other.value+1
    def __radd__(self, other): 
       return self.value + other.value+2
    def __str__(self):
        return 'SUM=%s'%self.value

class B:
    def __init__(self, value): 
        self.value = value 
    #def __add__(self, other): 
    #    return self.value + other.value+3
    #def __radd__(self, other): 
    #    return self.value + other.value+4   
    def __str__(self):
        return 'SUM=%s'%self.value   
		
a = A(1)
b = B(2)

print(a+b)
print(b+a)

