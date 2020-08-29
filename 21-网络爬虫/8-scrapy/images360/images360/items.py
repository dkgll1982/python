# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Images360Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = table = 'images'
    id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    thumb = scrapy.Field()    
    #图片链接
    image_urls = scrapy.Field()
    # 图片存储路径
    # image_paths = scrapy.Field()
