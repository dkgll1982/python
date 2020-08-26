# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
# 如何分别从Spider、Middleware、Pipeline获取settings.py里的参数,参考如下：
# https://blog.csdn.net/weixin_40841752/article/details/82900326

from itemadapter import ItemAdapter
import pymysql

class MySQLPipeline:
    def __init__(self, settings):
        self.host = settings.get('MYSQL_HOST')
        self.database = settings.get('MYSQL_DATABASE')
        self.user = settings.get('MYSQL_USER')
        self.password = settings.get('MYSQL_PASSWORD')
        self.port = settings.get('MYSQL_PORT')

    #经常需要在pipeline或者中间件中获取settings的属性，可以通过scrapy.crawler.Crawler.settings属性
    @classmethod
    #cls参数就是Spider类本身，crawler是Crawler类对象
    def from_crawler(cls, crawler):
        # return cls(
        #     host=crawler.settings.get('MYSQL_HOST'),
        #     database=crawler.settings.get('MYSQL_DATABASE'),
        #     user=crawler.settings.get('MYSQL_USER'),
        #     password=crawler.settings.get('MYSQL_PASSWORD'),
        #     port=crawler.settings.get('MYSQL_PORT'),
        # )
        return cls(crawler.settings)

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host,
                                  self.user,
                                  self.password,
                                  self.database,
                                  charset='utf8',
                                  port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        data = dict(item)
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s)' % (item.table, keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item


from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['url'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item

    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name
