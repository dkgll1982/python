# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from douban.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_connect

class DoubanPipeline:
    def __init__(self):
        super().__init__()
        host = mongo_host
        port = mongo_port
        self.dbname = mongo_db_name 
        self.sheetname = mongo_db_connect 
        client = pymongo.MongoClient(host = host,port = port)
        mydb = client[self.dbname]
        self.post = mydb[self.sheetname]
    
    #存数据    
    def process_item(self, item, spider):
        data = dict(item) 
        self.post.insert_one(data)
        return item
