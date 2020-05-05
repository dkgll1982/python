#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["douban"]
mycol = mydb["sites"]
  
# 查询 sites 文档中的第一条数据：
x = mycol.find_one()
 
print(x)

# find() 方法可以查询集合中的所有数据，类似 SQL 中的 SELECT * 操作。
x = mycol.find()
for x in mycol.find():
  print(x)

# 查询指定字段的数据
# 我们可以使用 find() 方法来查询指定字段的数据，将要返回的字段对应值设置为 1。
# 如：db.movie.find({},{ "_id": 0}).pretty()
for x in mycol.find({},{ "_id": 0, "name": 1, "alexa": 1 }).sort("alexa"):
  print(x)