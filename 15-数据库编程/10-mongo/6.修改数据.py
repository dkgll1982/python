import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["douban"]
mycol = mydb["sites"]
 
myquery = { "name": { "$regex": "^F" } }
newvalues = { "$set": { "alexa": "123" } }

#我们可以在 MongoDB 中使用 update_one() 方法修改文档中的记录。该方法第一个参数为查询的条件，第二个参数为要修改的字段。 
#如果要修改所有匹配到的记录，可以使用 update_many()。
x = mycol.update_many(myquery, newvalues)
 
print(x.modified_count, "文档已修改")