# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
# ImagesPipeline 为系统中下载图片的管道
from scrapy.pipelines.images import ImagesPipeline

class MeishiPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url = item['src'][0],meta = {'item':item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        # 设置图片的路径
        image = item['title']+'.jpg'
        # 返回图片路径
        return image