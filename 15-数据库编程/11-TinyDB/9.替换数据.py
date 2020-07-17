from tinydb import TinyDB
from tinydb import Query
import sys
import os 

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

db = TinyDB(realpath('test_write.json'))
db.truncate()           #先清空数据

db.insert_multiple({'name':'a','age':i} for i in range(5))

User = Query()
docs = db.search(User.name == 'a')
db.write_back(docs)     # 将新的字段写入到json文件。
print(db.all())