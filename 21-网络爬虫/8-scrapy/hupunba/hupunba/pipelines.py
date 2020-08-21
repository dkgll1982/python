# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 参考链接：https://blog.csdn.net/qq_41532599/article/details/80367457

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql 

class HupunbaPipeline: 
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
      
    # 注意：在spider中from_crawler方法调用是在spider类实例化以后，
    # 而在中间件，管道及拓展中，from_crawler方法调用是在相应的类实例化以前，在使用上要做区分。    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host = crawler.settings.get('MYSQL_HOST'),
            port = crawler.settings.getint('MYSQL_PORT'),          #注意数据类型，此处端口是数值类型
            user = crawler.settings.get('MYSQL_USER'),
            password = crawler.settings.get('MYSQL_PASSWORD'),
            database = crawler.settings.get('MYSQL_DBNMAE'),
        )
        
    # 数据库的连接初始化工作可以放在该函数里。也可以放到__init__()方法里
    def open_spider(self,spider):
        print("准备创建一个数据库")
        # 这个会在项目开始时第一次进入pipelines.py进入，之后不再进入
        # 建立mysql 的连接：
        self.conn = pymysql.connect(host = self.host,
                                    port = self.port,
                                    user = self.user,
                                    password = self.password,
                                    db = self.database,
                                    charset = 'utf8')
        self.cursor = self.conn.cursor()
        self.conn.commit()
        
    def close_spider(self,spider):
        print('爬取结束，断开数据库连接')
        # 这个会在结束时开始时第一次进入pipelines.py进入，之后不再进入
        self.conn.close()        
        
    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                "insert into player_info( playerimg,playerteam,playername,playernumber,playerjob,playertall,playerweight,playerbirthday,playercont,playersal) "
                "values(%s ,%s, %s, %s ,%s ,%s, %s, %s, %s,%s)",
                (
                 item["playerimg"],
                 item['playerteam'],
                 item['playername'],
                 item['playernumber'],
                 item['playerjob'],
                 item['playertall'],
                 item['playerweight'],
                 item['playerbirthday'],
                 item['playercont'],
                 item['playersal'])
                )
            self.conn.commit()
        except pymysql .Error :
            print("插入错误")
 
        return item
    