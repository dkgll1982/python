# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NetbianPicItem(scrapy.Item):
    # define the fields for your item here like:
    # 图片名称
    title = scrapy.Field()
    # 图片下载链接
    link = scrapy.Field()
    
