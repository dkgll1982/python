#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-09 14:00
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 序列化
# @Software: PyCharm

import pickle
#序列化保存到磁盘文件
f = open('C:\\Users\\dkgll\\Desktop\\python目录\\2.txt', 'wb')
d = dict(name='Bob', age=20, scoree=88)
pickle.dump(d, f)
f.close()

#反序列化读取文件
f = open('C:\\Users\\dkgll\\Desktop\\python目录\\2.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

#序列化为JSON
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)
print(d)

#反序列化JSON字符串
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)
print(json_str)

class Student(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex= sex

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'sex': std.sex
    }

s = Student("张三",20,"man");
print(json.dumps(s,default=lambda obj: obj.__dict__));
print(Student.__dict__)

