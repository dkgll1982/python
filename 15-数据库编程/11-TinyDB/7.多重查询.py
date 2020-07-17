from tinydb import TinyDB,Query,where
import sys
import os 
import re

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

db = TinyDB(realpath('db3.json'))
student = db.table("student")

# 多重查询，用两个Query()实例去嵌套查询
G = Query()
P = Query() 

#db相当于 db.table('_default')，我们现在要查询的是db.table('student')
student.insert({
        'name': 'user',
        'permissions': [{'type': 'read'}]})
student.insert({
        'name': 'sudo',
        'permissions': [{'type': 'read'}, {'type': 'sudo'}]})
student.insert({
        'name': 'admin',
        'permissions': [{'type': 'read'}, {'type': 'write'}, {'type': 'sudo'}]})

# 任意符合P.type == 'read'条件的都返回
s = student.search(G.permissions.any(P.type == 'read'))
print(s) 
#[{'name': 'user', 'permissions': [{'type': 'read'}]}, 　　　　　　
# {'name': 'sudo', 'permissions': [{'type': 'read'}, {'type': 'sudo'}]}, 　　　　
# {'name': 'admin', 'permissions': [{'type': 'read'}, {'type': 'write'}, {'type': 'sudo'}]}
#]
# 完全符合P.type == 'read'条件的才返回，方法名字如果换成 only可能更好理解
t = student.search(G.permissions.all(P.type == 'read'))
print(t) 
# [{'name': 'user', 'permissions': [{'type': 'read'}]}]

#还是使用 any(...) 和 all(...) 方法。总结哈：
# any([...]) 是任意匹配，只要列表里面有一项能匹配到，就会返回。
# all([...]) 是全部匹配，只有列表里面全部都能匹配到，才会返回。