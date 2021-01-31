# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class ChinazImgPipeline:
    def process_item(self, item, spider):
        return item

# ImagesPipeline用于文件下载管道类，下载过程支持异步和多线程
class ImgPipeLine(ImagesPipeline):
    # 对item中的图片进行请求操作
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'])
        
    # 定制图片的名称
    def file_path(self, request, response=None, info=None):
        imgName = request.url.split('/')[-1]
        return imgName
    #
    def item_completed(self, results, item, info):
        return item  # 传递到下一个即将被执行的管道类