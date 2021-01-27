# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class PwrzPipeline:
    def __init__(self,host,port,user,password,database):
        super().__init__()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database 
     
    @classmethod 
    def from_crawler(cls, crawler): 
        return cls(
            host = crawler.settings.get('MYSQL_HOST'),
            port = crawler.settings.getint('MYSQL_PORT'),          #注意数据类型，此处端口是数值类型
            user = crawler.settings.get('MYSQL_USER'),
            password = crawler.settings.get('MYSQL_PASSWORD'),
            database = crawler.settings.get('MYSQL_DBNMAE'),
        )
    
    def open_spider(self,spider):
        self.conn = pymysql.connect(user = self.user,
                                    host = self.host,
                                    port = self.port,
                                    password = self.password,
                                    db = self.database) 
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.conn.cursor()
        
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
        
    def process_item(self, item, spider):                
        # SQL 插入语句
        sql = """INSERT INTO pwrz(`title`,`author`,`vnum`,`cnum`,`time`,`content`)
                 VALUES ('%s', '%s',  %s,  %s, '%s',  '%s')
            """%(item["title"],item["author"],item["vnum"],item["cnum"],item["time"],item["content"])
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            print('插入错误！')
            self.conn.rollback()
        return item
    
