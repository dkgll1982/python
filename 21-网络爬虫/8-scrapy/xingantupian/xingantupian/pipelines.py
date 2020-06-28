# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

class xingantupianPipeline(object):
    def process_item(self, item, spider):
        return item

class QiushiImagePipeline(ImagesPipeline): 
    # 下载图片时加入referer请求头
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            headers = {'referer':item['referer']}
            yield Request(image_url, meta={'item': item}, headers=headers)
            # 这里把item传过去，因为后面需要用item里面的书名和章节作为文件名

    # 获取图片的下载结果, 控制台查看
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    # 修改文件的命名和路径
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_guid = request.url.split('/')[-1]
        filename = './{}/{}'.format(item['title'], image_guid)
        return filename
 