# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy 

#ImagesPipeline中主要介绍2个函数。get_media_requests和item_completed
class GirlPic(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item["image_urls"]:
            yield scrapy.Request(image_url, meta={"image_name": item["image_name"]})

    def file_path(self, request, response=None, info=None):
        file_name = request.meta["image_name"].strip().replace('\r\n\t\t', '')+'.jpg'
        file_name = file_name.replace('/', '-')
        return file_name
