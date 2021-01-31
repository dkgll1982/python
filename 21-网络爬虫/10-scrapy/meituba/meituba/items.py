# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeitubaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category = scrapy.Field()    #图片分类
    name = scrapy.Field()        #图片名称
    image_urls = scrapy.Field()    #图片链接地址
