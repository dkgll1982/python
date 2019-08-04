#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-03 21:22:14 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-03 21:22:14 
# @Software: vscode 

class Item:
    '定义代表商品的Item类'
    def __init__(self, price):
        self.price = price
    def __repr__(self):
        return 'Item[price=%g]' % self.price