# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os 
from scrapy.pipelines.images import ImagesPipeline
from carhome import settings

# class CarhomePipeline:
#     def process_item(self, item, spider):
#         return item
    
class BMWImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 这个方法是在发送下载请求之前调用，其实这个方法本身就是去发送下载请求的
        request_objs = super(BMWImagesPipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        # 这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
        path = super(BMWImagesPipeline, self).file_path(request, response, info)
        boxTitle = request.item.get('boxTitle')
        imagesStore = settings.IMAGES_STORE
        boxTitlePath = os.path.join(imagesStore, boxTitle)
        if not os.path.exists(boxTitlePath):
            os.mkdir(boxTitlePath)
        imageName = path.replace("full/", "")
        imagePath = os.path.join(boxTitlePath, imageName)
        return imagePath