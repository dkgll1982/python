#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-07-25 14:20:27 
# @Last Modified by: guojun 
# @Last Modified time: 2019-07-25 14:20:27 
# @Software: vscode 

def get_math_func(type) :
    result=1
    # 该函数返回的是Lambda表达式
    if type == 'area':
        return lambda a,b: a * b  # ①
    elif type == 'square':
        return lambda n: n * n  # ①
    elif type == 'cube':
        return lambda n: n * n * n  # ②
    else:
        return lambda n: (1 + n) * n / 2 # ③
# 调用get_math_func()，程序返回一个嵌套函数
math_func = get_math_func("area")
print(math_func(4,5)) # 输出20
math_func = get_math_func("cube")
print(math_func(5)) # 输出125
math_func = get_math_func("square")
print(math_func(5)) # 输出25
math_func = get_math_func("other")
print(math_func(5)) # 输出15.0
print('-'*40);
x = lambda x,y:x*y
print(x(2,4))

print('-'*40)
x = map(lambda x,y: x*y ,[3,4],[3,4])
print([e for e in x])
# 传入计算平方的lambda表达式作为参数
x = map(lambda x: x*x , range(8))
print([e for e in x]) # [0, 1, 4, 9, 16, 25, 36, 49]
# 传入计算平方的lambda表达式作为参数
y = map(lambda x: x*x if x % 2 == 0 else 0, range(8))
print([e for e in y]) # [0, 0, 4, 0, 16, 0, 36, 0]