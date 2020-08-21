# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 用法参考：https://www.cnblogs.com/zhaof/p/7196197.html?utm_source=itdadao&utm_medium=referral

import pymongo
from douban.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_connect

# 每个item piple组件是一个独立的pyhton类，必须实现以process_item(self,item,spider)方法
# 每个item pipeline组件都需要调用该方法
# 这个方法必须返回一个具有数据的dict,或者item对象，或者抛出DropItem异常，被丢弃的item将不会被之后的pipeline组件所处理
class DoubanPipeline:
    def __init__(self):
        super().__init__()
        #这里数据库的初始化连接也可以写在open_spider函数里
        host = mongo_host
        port = mongo_port
        self.dbname = mongo_db_name 
        self.sheetname = mongo_db_connect 
        client = pymongo.MongoClient(host = host,port = port)
        mydb = client[self.dbname]
        self.post = mydb[self.sheetname]
    
    #存数据    
    def process_item(self, item, spider):
        #item看着是dict，但是还不是python里面的dict，需要使用dict(item)转换一下，才能正常保存，不然报错，我这里改了就成功了：
        data = dict(item) 
        #写入mongodb的方法
        self.post.insert_one(data)
        return item
