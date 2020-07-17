#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-07-13 14:04:51 
# @Remark: 人生苦短，我用python！
# 参考链接：https://blog.csdn.net/mouday/article/details/90107654

from tinydb import TinyDB,Query,where
import sys
import os 

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

db = TinyDB(realpath('db3.json'))

student = db.table("student")

#删一条，或者说删符合条件的
a = student.remove(Query().name == 'mary')
print(student.all())

#清空所有数据
student.truncate()
print(student.all())

# 插入数据
student.insert({"name": "Tom", "age": 23})

# 插入多条
student.insert_multiple([
    {"name": "Jack", "age": 24},
    {"name": "mary", "age": 25},
    {"name": "marya", "age": 45},
    {"name": {"first_name":"张",":'last_name":"三"}, "age": 25},
    {"name": {"first_name":"王",":'last_name":"八"}, "age": 25}
])

# 查询所有
print(student.all())
# [
#   {'name': 'Tom', 'age': 23},
#   {'name': 'Jack', 'age': 24},
#   {'name': 'mary', 'age': 25}
# ]

# 查询部分
query = Query()
result = student.search(query.name == 'Tom')
print(result)
# [{'name': 'Tom', 'age': 23}]

#嵌套查询
result = student.search(query.name.first_name == '王')
print('-----------',result)

result = student.search(query.age > 24)
print(result)
# [{'name': 'mary', 'age': 25}]

# 逻辑查询
print(student.search(~(query.name == 'Jack')))  # Negate
print(student.search((query.name == 'Jack') & (query.age <= 30)))  # And
print(student.search((query.name == 'Jack') | (query.name == 'mary')))  # Or

# 更新
student.update({'age': 26,"job":'engineer'}, query.name == "Tom")
print(student.search(query.name=="Tom"))
# [{'name': 'Tom', 'age': 26}]

#看一个表当中的key 是否存在 
#db.search(where('name')=='John')
print('==============>',student.contains(where('name')=='Tom'))
# 删除
print(student.all())
student.remove(query.age < 25)
print(student.all())
# [{'name': 'Tom', 'age': 26}, {'name': 'mary', 'age': 25}]

# 关闭
db.close()

