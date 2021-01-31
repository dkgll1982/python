# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class MeitubaPipeline:
    def process_item(self, item, spider):
        return item
 
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings #获取配置的方法
import os

# 自定义 创建下载及存储的特殊管道类
class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(url = item['image_urls'],meta = {"item" : item})       
        
    def item_completed(self, results, item, info):
        # 如果results 的第一个参数值为true就返回第二个参数值得“path”值
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:     #如果其中没有图片，我们将丢弃项目                  
            raise DropItem('Image Downloaded Failed')  
        return item             #默认情况下，item_completed()方法返回项目。

    #定义下载图片存储的路径，我们需要处理一下，以此把图片存储到我们想存储的地方
    def file_path(self, request, response=None, info=None):
        item = request.meta.get("item")                 #获取传递的参数
        settings = get_project_settings()               
        images_store = settings.get("IMAGES_STORE")     #获取配置
        #获取request的meta属性的name并拼接作为文件名称
        category = item['category']
        image = item['name'] + '.jpg'
              
        #获取IMAGES_STORE图片的默认地址并拼接
        file_path = os.path.join(images_store,category)
        #判断地址是否存在，不存在则创建
        if not os.path.exists(file_path):
            os.makedirs(file_path)
   
        #拼接文件夹地址与图片名存储的全部路径并返回！！！！原方法
        file_name = os.path.join(file_path,image)
        # 返回图片路径
        return file_name
