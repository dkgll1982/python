# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import ScrapyDeprecationWarning
import warnings
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline 
 
class ZolBizhi2Pipeline(ImagesPipeline): 
    def get_media_requests(self, item, info):
        image_url = item["image_urls"]
        for url in image_url: 
            # self.num + 1
            yield Request(url = url, meta={"image_title": item["image_title"]})
 
    def file_path(self, request, response=None, info=None):  
        image_title = request.meta['image_title']
        # 设置图片的路径
        image = image_title + '.jpg'
        # 返回图片路径
        return image 