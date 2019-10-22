#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-10-21 22:23:28 
# @Last Modified by: guojun 
# @Last Modified time: 2019-10-21 22:23:28 
# @Software: vscode 

class NotNegative():
    def __init__(self,name):
        self.name = name

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(self.name + ' must be >= 0')
        else:
            instance.__dict__[self.name] = value

class Product():
    quantity = NotNegative('quantity')
    price = NotNegative('price')

    def __init__(self,name,a,b):
        self.name = name
        self.quantity = a   #设置父类属性quantity=2，在描述符类set方法里判断属性值是否符合要求
        self.price = b

book = Product('mybook',2,5)