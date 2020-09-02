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
        #返回MySQLPipeline对象本身，cls()函数体参数对应的是MySQLPipeline对象本身的参数
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
        self.cursor.close()
        self.db.close()

    def process_item(self, item, spider):
        data = dict(item)
        
        data.pop('image_urls', '没有该键(key)')    #去掉该项 
        
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s)' % (item.table, keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item


from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings #获取配置的方法

# 自定义 创建下载及存储的特殊管道类
class ImagePipeline(ImagesPipeline):
    '''ImagePipeline根据image_urls中指定的url进行爬取，若不用默认字段则在这里重写
           可以通过get_media_requests为每个url生成一个Request
           get_media_requests函数返回示例如下：
           [(True,
               {’checksum’: ’2b00042f7481c7b056c4b410d28f33cf’,
               ’path’: ’full/7d97e98f8af710c7e7fe703abc8f639e0ee507c4.jpg’,
               ’url’: ’http://www.example.com/images/product1.jpg’}),
           (True,
               {’checksum’: ’b9628c4ab9b595f72f280b90c4fd093d’,
               ’path’: ’full/1ca5879492b8fd606df1964ea3c1e2f4520f076f.jpg’,
               ’url’: ’http://www.example.com/images/product2.jpg’}),
           (False,
               Failure(...))]
    ''' 
    # 接收item对象并将获取item对象中的url发送请求
    def get_media_requests(self, item, info):
        # 地址是列表的情况
        # for image_url in item['image_urls']:
        #     yield scrapy.Request(image_url)
        # 地址是字符串的情况
        yield Request(item['image_urls'])        
        
    # 当一个单独项目中的所有图片请求完成时（要么完成下载，要么因为某种原因下载失败）,
    # ImagesPipeline.item_completed() 方法将被调用。
    # 图片下载成功结束后，图片下载路径、url和校验和等信息会被填充到images字段中。
    # item_completed() 方法需要返回一个输出，其将被送到随后的项目管道阶段，
    # 因此你需要返回（或者丢弃）项目，如你在任意管道里所做的一样。    
    def item_completed(self, results, item, info):
        '''所有图片处理完毕后（不管下载成功或失败），会调用item_completed进行处理
           results是一个list 第一个为图片下载状态,
           get_media_requests在图片下载完毕后，处理结果会以二元组的方式返回给item_completed()函数的
           results，图片下载状态定义如下：
               (success, image_info_or_failure)  
               success表示图片是否下载成功；image_info_or_failure是一个字典
        '''
        # 图片下载路径、url和校验和等信息,下面是 results 参数的一个典型值:
        # success 是一个布尔值，当图片成功下载时为 True ，因为某个原因下载失败为``False``
        # url - 图片下载的url。这是从 get_media_requests() 方法返回请求的url。
        # path - 图片存储的路径（类似 IMAGES_STORE）
        # checksum - 图片内容的 MD5 hash
        # [
        #     (
        #         True, {
        #                 'url': 'https://p0.ssl.qhimgs1.com/t01a9e11720c9189b04.jpg', 
        #                 'path': 't01a9e11720c9189b04.jpg', 
        #                 'checksum': 'c47fd99ed4a98dbcf7f25cb3e1663657', 
        #                 'status': 'downloaded'
        #             }
        #      )
        # ]
        print('下载完成：',results)
        # 如果results 的第一个参数值为true就返回第二个参数值得“path”值
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:     #如果其中没有图片，我们将丢弃项目                  
            raise DropItem('Image Downloaded Failed')  
        return item             #默认情况下，item_completed()方法返回项目。

    #定义下载图片存储的路径，我们需要处理一下，以此把图片存储到我们想存储的地方
    def file_path(self, request, response=None, info=None):
        # 图片路径
        url = request.url
        # 通过分割图片路径获取图片名字
        file_name = url.split('/')[-1]
        # 返回图片路径
        return file_name
