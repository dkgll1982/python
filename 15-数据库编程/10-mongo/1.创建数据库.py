#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
 
dblist = myclient.list_database_names()
# 注意: 在 MongoDB 中，数据库只有在内容插入后才会创建! 
# 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。
print(dblist)

#判断数据库是否已存在
#我们可以读取 MongoDB 中的所有数据库，并判断指定的数据库是否存在： 
if "douban" in dblist:
  print("数据库已存在！")