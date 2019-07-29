#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-07-25 14:03:37 
# @Last Modified by: guojun 
# @Last Modified time: 2019-07-25 14:03:37 
# @Software: vscode 


# 定义函数类型的形参，其中fn是一个函数
def map(data, fn) :   
    result = []
    # 遍历data列表中每个元素，并用fn函数对每个元素进行计算
    # 然后将计算结果作为新数组的元素
    for e in data :
        result.append(fn(e))
    return result
# 定义一个计算平方的函数
def square(n) :
    return n * n
# 定义一个计算立方的函数
def cube(n) :
    return n * n * n
# 定义一个计算阶乘的函数
def factorial(n) :
    result = 1
    for index in range(2, n + 1) :
        result *= index
    return result
data = [3 , 4 , 9 , 5, 8]
print("原数据: ", data)
# 下面程序代码3次调用map()函数，每次调用时传入不同的函数
print("计算数组元素的平方")
print(map(data , square))
print("计算数组元素的立方")
print(map(data , cube))
print("计算数组元素的阶乘")
print(map(data , factorial))
print('------------------------------------------------')
#函数内部返回函数
def get_math_func(type) :
    # 定义一个计算面的局部函数
    def area(a,b):
        return a*b
    # 定义一个计算平方的局部函数
    def square(n) :  # ①
        return n * n
    # 定义一个计算立方的局部函数
    def cube(n) :  # ②
        return n * n * n
    # 定义一个计算阶乘的局部函数
    def factorial(n) :   # ③
        result = 1
        for index in range(2 , n + 1):
            result *= index
        return result
    # 返回局部函数
    if type == "area" :
        return area
    elif type == "square" :
        return square
    elif type == "cube" :
        return cube
    else:
        return factorial

# 调用get_math_func()，程序返回一个嵌套函数
math_func = get_math_func("area") # 得到square函数
print(math_func(4,5)) # 输出20
math_func = get_math_func("cube") # 得到cube函数
print(type(math_func))
print(math_func(5)) # 输出125
math_func = get_math_func("square") # 得到square函数
print(math_func(5)) # 输出25
math_func = get_math_func("other") # 得到factorial函数
print(math_func(5)) # 输出120
