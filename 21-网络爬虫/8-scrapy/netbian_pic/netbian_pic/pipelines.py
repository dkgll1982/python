# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings #获取配置的方法

class NetbianPicPipeline:
    def process_item(self, item, spider):
        return item


class NetpicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url = item['link']
        yield scrapy.Request(image_url,meta = {"item" : item})       

    def item_completed(self, results, item, info):        
        # 如果results 的第一个参数值为true就返回第二个参数值得“path”值
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:     #如果其中没有图片，我们将丢弃项目                  
            raise DropItem('Image Downloaded Failed')   
        return item

    #定义下载图片存储的路径，我们需要处理一下，以此把图片存储到我们想存储的地方
    def file_path(self, request, response=None, info=None):
        item = request.meta.get("item")                 #获取传递的参数
        # settings = get_project_settings()               
        # images_store = settings.get("IMAGES_STORE")     #获取配置 
        image = item['title'].replace(' ','').replace('\r','').replace('\n','').replace('\t','') + '.jpg'
       
        # 返回图片路径
        return image