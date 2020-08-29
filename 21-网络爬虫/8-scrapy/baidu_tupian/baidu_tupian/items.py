# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy 

class BaiduTupianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    word = scrapy.Field()           #关键词
    name = scrapy.Field()           #图片名称
    image_url = scrapy.Field()      #图片链接
    
