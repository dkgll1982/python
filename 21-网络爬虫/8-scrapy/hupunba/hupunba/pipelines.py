# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 参考链接：https://blog.csdn.net/qq_41532599/article/details/80367457
# Item Pipeline用法：https://www.cnblogs.com/zhaof/p/7196197.html?utm_source=itdadao&utm_medium=referral
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql 

#2020/12/29：通过调试大致摸清完整的执行流程：
#1：首次运行scrapy crawl xxxxx，进入from_crawler实例化对象，作为参数传给pipeline类本身
#2：执行init构造方法进行初始化，如果from_crawler返回有参数，此处也需要带上参数
#3：执行open_spider方法
#4：进入spider，执行parse方法（）
#5：只要有yield item。就将item放入管道pipeline，执行process_item方法
#6：执行完成process_item方法，再次返回spider，往下执行，直到再次yield item，循环到5.依次类推
#7：当yield item结束，spider再无内容，执行close_spider方法，执行结束

class HupunbaPipeline: 
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
   
    # (可选)此方法如果实现了,那么Pipeline对象从这里调用,必须返回一个cls(参数)对象   
    # 注意：在spider中from_crawler方法调用是在spider类实例化以后，
    # 而在中间件，管道及拓展中，from_crawler方法调用是在相应的类实例化以前，在使用上要做区分。    
    @classmethod
    def from_crawler(cls, crawler):
        #此处返回的是类，即HupunbaPipeline本身，cls的参数即HupunbaPipeline的参数
        return cls(
            host = crawler.settings.get('MYSQL_HOST'),
            port = crawler.settings.getint('MYSQL_PORT'),          #注意数据类型，此处端口是数值类型
            user = crawler.settings.get('MYSQL_USER'),
            password = crawler.settings.get('MYSQL_PASSWORD'),
            database = crawler.settings.get('MYSQL_DBNMAE'),
        )
        
    # (可选)数据库的连接初始化工作可以放在该函数里。也可以放到__init__()方法里
    # 蜘蛛打开的时候执行的
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
        
    # (可选)蜘蛛关闭的时候执行的    
    def close_spider(self,spider):
        print('爬取结束，断开数据库连接')
        # 这个会在结束时开始时第一次进入pipelines.py进入，之后不再进入
        self.conn.close()

    # (必须实现的方法)每个item piple组件是一个独立的pyhton类，必须实现以process_item(self, item, spider)方法
    # 每个item pipeline组件都需要调用该方法，这个方法必须返回一个具有数据的dict, 或者item对象，
    # 或者抛出DropItem异常，被丢弃的item将不会被之后的pipeline组件所处理   
    def process_item(self, item, spider): 
        '''
            spider就是爬取数据的蜘蛛，item就是爬取到的数据，
            执行完数据库插入之后，需要执行返回，也就是需要：return item。
            以上方法是必须要实现的方法
            无论你是插入mysql、mongodb还是其他数据库，都必须实现这么一个方法
        '''
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
        except pymysql.Error :
            print("插入错误")
 
        return item