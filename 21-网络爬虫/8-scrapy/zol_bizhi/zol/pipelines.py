# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy 

# ImagesPipeline中主要介绍2个函数。get_media_requests和item_completed
class GirlPic(ImagesPipeline):
    # 管道会得到图片的URL并从项目中下载。为了这么做，
    # 你需要重写 get_media_requests() 方法，并对各个图片URL返回一个Request:
    # 这些请求将被管道处理，当它们完成下载后，结果将以元素的元组列表形式传送到 item_completed() 方法:
    def get_media_requests(self, item, info):
        for image_url in item["image_urls"]:
            yield scrapy.Request(image_url, meta={"image_name": item["image_name"]})
            
    def file_path(self, request, response=None, info=None):
        '''自定义图片保存路径,以图片的url保存,重写前是图片的url经过MD5编码后存储'''
        file_name = request.meta["image_name"].strip().replace('\r\n\t\t', '')+'.jpg'
        file_name = file_name.replace('/', '-')
        return file_name
