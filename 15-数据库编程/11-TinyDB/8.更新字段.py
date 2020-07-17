from tinydb import TinyDB
from tinydb import Query
import sys
import os 

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

db = TinyDB(realpath('data.json'))
db.truncate()   #先清空数据
db.insert_multiple([
    {'name':'a'},
    {'name':'b'},
    {'name':'c'},
    {'name':'d'},
    {'name':'e'},
    {'name':'f'},
    {'name':'g'},
    {'name':'h'},
])
print(db.all())  # 
db.update({'age':10})
print(db.all())  
# 每个字段里面都增加了同样的新键值对
# [{'name': 'a', 'age': 10},{'name': 'b', 'age': 10}, {'name': 'c', 'age': 10},{'name': 'd', 'age': 10},{'name': 'e', 'age': 10},{'name': 'f', 'age': 10}]

from tinydb.operations import delete
from tinydb.operations import increment,decrement
from tinydb.operations import add, subtract,set,mult

User = Query()
db.update(delete('age'),User.name == 'a')       # {'name': 'a'}  -->直接删除了'age':10
db.update(increment('age'), User.name == 'b')   # {'name': 'b', 'age': 11}  -->10+1
db.update(decrement('age'), User.name == 'c')   # {'name': 'c', 'age': 9}  -->10-1  
db.update(add('age',5), User.name == 'd')       # {'name': 'd', 'age': 15}  -->10+5
db.update(subtract('age',5), User.name == 'e')  # {'name': 'e', 'age': 5} -->10-5
db.update(set('age',100), User.name == 'f')     # {'name': 'f', 'age': 100}  -->100
db.update(mult('age',5), User.name == 'g')      # {'name': 'd', 'age': 15}  -->10+5
    
#自定义方法，可以按照下面的格式要求写自己的逻辑：
def divisor(field, n):
    """
    # 2020-07-17 dkgll add
    """
    def transform(doc):
        doc[field] /= n

    return transform

db.update(divisor('age',5), User.name == 'h')      # {'name': 'd', 'age': 15}  -->10+5

for filed in db.all():
    print(filed)
    
db.update({'name':'a','logger-in': True}, User.name == 'a')
db.update({'name':'b','age': 200},User.name == 'b')

print('*'*40)

for filed in db.all():
    print(filed)
    
print('+'*40)

a = len(db)
b = db.get(User.name == 'a')
c = db.contains(User.name == 'a')
d = db.count(User.name == 'a')
print(a) #11
print(b) # {'name': 'a', 'logger-in': True}
print(c) #True
print(d) # 1