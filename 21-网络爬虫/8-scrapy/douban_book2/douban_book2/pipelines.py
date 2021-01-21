# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json 
import pymysql as db

class DoubanBook2Pipeline:  
    """ 将抓取到的数据存入json文件中 """
    def __init__(self):
        self.file = open("./items.json", "w",encoding='utf-8')  
       
    def process_item(self, item, spider): 
        for k in item:
            print(item[k])             
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self,spider):
        self.file.close()
        
class MySQLPipeline(object):
    def __init__(self):
        self.con=db.connect(user="root",passwd="123456",host="localhost",db="cig",charset="utf8")
        self.cur=self.con.cursor()
        self.cur.execute('drop table douban_booke')
        self.cur.execute("create table douban_booke(id int primary key auto_increment,tags varchar(50), name varchar(255) NOT NULL, author varchar(255) NULL, press varchar(100) NULL, date varchar(30) NULL, page varchar(50) NULL, price varchar(30) NULL, score varchar(30) NULL, ISBN varchar(30) NULL, author_profile varchar(1500) NULL, content_description varchar(3000) NULL, link varchar(255) NULL )default charset=utf8;")
    
    def process_item(self, item, spider):
        self.cur.execute("insert into douban_booke(tags, name, author, press, date, page, price, score, ISBN, author_profile,content_description, link) values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(item["tags"], item["name"], item["author"], item["press"], item["date"],item["page"], item["price"], item["score"], item["ISBN"],item["author_profile"], item["content_description"], item["link"]))
        self.con.commit()
        return item
    
    def close_spider(self,spider):
        self.cur.close()
        self.con.close()