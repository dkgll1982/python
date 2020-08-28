# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.images import ImagesPipeline
import scrapy

#继承ImagesPipeline，重写get_media_requests()和file_path()方法
class PostbarPipeline(ImagesPipeline):
    #   需要headers的网站，再使用
    headers = {
        'User-Agent': '',
        'Referer': '',
    }

    def get_media_requests(self, item, info):
        for pic_url in item['pic_urls']:
            # 为每个url生成一个Request
            yield scrapy.Request(pic_url)
            # 需要请求头的时候，添加headers参数
            # yield scrapy.Request(pic_url, headers=self.headers)

    def file_path(self, request, response=None, info=None):
        # 重命名(包含后缀名)，若不重写这函数，图片名为哈希
        pic_path = request.url.split('/')[-1]
        return pic_path