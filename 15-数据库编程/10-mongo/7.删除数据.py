#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["douban"]
mycol = mydb["sites"]
 
myquery = { "name": "Taobao" }
 
#我们可以使用 delete_one() 方法来删除一个文档，该方法第一个参数为查询对象，指定要删除哪些数据。 
mycol.delete_one(myquery)
 
# 删除后输出
for x in mycol.find():
  print(x)

#我们可以使用 delete_many() 方法来删除多个文档，该方法第一个参数为查询对象，指定要删除哪些数据。
x = mycol.delete_many(myquery)
 
print(x.deleted_count, "个文档已删除")

#delete_many() 方法如果传入的是一个空的查询对象，则会删除集合中的所有文档：
x = mycol.delete_many({})
 
print(x.deleted_count, "个文档已删除")