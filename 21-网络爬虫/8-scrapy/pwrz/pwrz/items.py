# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PwrzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field() 
    title = scrapy.Field()
    author = scrapy.Field()
    vnum = scrapy.Field()
    cnum = scrapy.Field()
    time = scrapy.Field() 
    content = scrapy.Field()