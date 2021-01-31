# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import scrapy
import uuid
from scrapy.pipelines.images import ImagesPipeline

class DoubanBookPipeline:
    def __init__(self,settings): 
        self.dbconf = settings.get('DB_CONF')       #获取数据库连接配置参数
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)
    
    def open_spider(self,spider):
        self.conn = pymysql.connect(**self.dbconf)   #将字典解析成可变参数
        self.cursor = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

    def process_item(self,item,spider):
        sql = "insert into books(id,name,author,price,edition_time,publisher,ratings) values (%s,%s,%s,%s,%s,%s,%s) " 
        self.cursor.execute(sql,
                            (str(uuid.uuid1()),
                             item['name'],
                             item['author'],
                             item['price'],
                             item['edition_time'],
                             item['publisher'],
                             item['ratings'])
                            )     
        self.conn.commit()
        return item
    
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
