# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class QiushibaikePipeline:        
    def process_item(self, item, spider):
        self.fp = None  # 定义一个文件描述符属性
        
    # 下列都是在重写父类的方法：
    # 开始爬虫时，执行一次
    def open_spider(self, spider):
        print('爬虫开始')
        self.fp = open('./data.txt', 'w',encoding='utf-8')
        
    # 专门处理item对象
    # 因为该方法会被执行调用多次，所以文件的开启和关闭操作写在了另外两个只会各自执行一次的方法中。
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        contents = '{}:{}\n\n'.format(author,content)
        self.fp.write(contents)
        return item  # 传递到下一个被执行的管道类

    def close_spider(self, spider):
        print('爬虫结束')
        self.fp.close()

#管道文件中的一个管道类对应的是讲数据存储到一种平台
#爬虫文件提交的item只会给管道文件中第一个被执行的管道类接受
#process_item的return item表示item传递到下一个被执行的管道类
#将数据存储到数据库
class mysqlPipeline(object):
    def __init__(self, settings):
        self.conn = None  # 定义一个文件描述符属性
        self.cursor = None
        self.num = 0
        
        self.host = settings.get('MYSQL_HOST')
        self.database = settings.get('MYSQL_DATABASE')
        self.user = settings.get('MYSQL_USER')
        self.password = settings.get('MYSQL_PASSWORD')
        self.port = settings.get('MYSQL_PORT') 
        
    #经常需要在pipeline或者中间件中获取settings的属性，可以通过scrapy.crawler.Crawler.settings属性
    @classmethod
    #cls参数就是Spider类本身，crawler是Crawler类对象
    def from_crawler(cls, crawler): 
        return cls(crawler.settings)
    
    # 下列都是在重写父类的方法：
    # 开始爬虫时，执行一次
    def open_spider(self, spider):
        self.conn = pymysql.Connect(host=self.host ,port=self.port,user=self.user,password=self.password,db=self.database,charset='utf8')
        print('爬虫数据库开始')

    # 专门处理item对象
    # 因为该方法会被执行调用多次，所以文件的开启和关闭操作写在了另外两个只会各自执行一次的方法中。
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into qiubai values(%s,%s)' ,(author,content))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        print('爬虫数据库结束')
        self.cursor.close()
        self.conn.close()