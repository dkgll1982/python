#!/usr/bin/python3
 
import pymongo
 
#查找 name 字段为 "RUNOOB" 的数据： 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["douban"]
mycol = mydb["sites"]
 
myquery = { "name": "RUNOOB" }
 
mydoc = mycol.find(myquery).limit(2)
 
for x in mydoc:
  print(x)