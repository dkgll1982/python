# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WeiyitukuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()       #图片标题
    name = scrapy.Field()       #图片名称
    img_url = scrapy.Field()    #图片地址
