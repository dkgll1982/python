from tinydb import TinyDB,Query,where  # 要先导入where
import sys
import os 

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

db = TinyDB(realpath('db.json'))
d = db.search(where('name')=='John')
e = db.search(Query()['name']=='John')
print(d) # [{'name': 'John', 'age': 22}]
print(e) # [{'name': 'John', 'age': 22}]