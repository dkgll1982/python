from tinydb import TinyDB,Query,where
import sys
import os 
import re

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

db = TinyDB(realpath('db3.json'))
student = db.table("student")
User = Query()

# 查询所有
print(student.all())
#自定义查询 test(...) 
# 不带参数
test_func = lambda s:s == 'Tom'
o = student.search(User.name.test(test_func))
print(o)    # [{'name': 'John', 'age': 22}]
# 带参数
def test_func1(val, m, n):
    return m <= val <= n
p = student.search(User.age.test(test_func1,2,40))
print(p)    #[{'name': 'John', 'age': 22}, {'name': 'sheet', 'age': 23}]

print('-'*40)

#字段里面包含列表时 any(...)  all(...) 
student.insert({'name': 'user1', 'groups': ['user']})
student.insert({'name': 'user2', 'groups': ['admin', 'user']})
student.insert({'name': 'user3', 'groups': ['sudo', 'user']})

# any():只要'groups'对应的值中在['admin','sudo']里面出现，都会返回
q = student.search(User.groups.any(['admin','sudo']))
# all():完全符合查询条件['admin','user']的，才会被返回
r = student.search(User.groups.all(['admin','user']))
print(q)    # [{'name': 'user2', 'groups': ['admin', 'user']}, {'name': 'user3', 'groups': ['sudo', 'user']}]
print(r)    # [{'name': 'user2', 'groups': ['admin', 'user']}]