#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-07-29 23:04:51 
# @Last Modified by: guojun 
# @Last Modified time: 2019-07-29 23:04:51 
# @Software: vscode 

class Item:
    def __init__ (self, name, price):
        self.name = name
        self.price = price
    # 定义析构函数
    def __del__ (self):
        print('del删除对象')
# 创建一个Item对象，将之赋给im变量
im = Item('鼠标', 29.8)
x = im   # ①
# 打印im所引用的Item对象
del im
print('-'*40)