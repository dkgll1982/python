#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-07-13 11:10:50 
# @Remark: 人生苦短，我用python！

from tinydb import TinyDB, Query
import sys
import os 

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

db = TinyDB(realpath('db2.json'))
table = db.table('name')
table.insert({'value': True})
db.insert({'name': 'John', 'age': 22})
print(table.all())